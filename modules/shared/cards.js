(() => {
  const config = window.CARDS_CONFIG || {};
  const cardEl = document.getElementById("card");
  const progressBadge = document.getElementById("progressBadge");
  const progressInfo = document.getElementById("progressInfo");
  const shuffleBtn = document.getElementById("shuffleBtn");
  const resetBtn = document.getElementById("resetBtn");
  const leftBtn = document.getElementById("leftBtn");
  const rightBtn = document.getElementById("rightBtn");
  const sideSelect = document.getElementById("sideSelect");
  const repeatLeftOnly = document.getElementById("repeatLeftOnly");
  const pageTitle = document.getElementById("pageTitle");
  const wordsLink = document.getElementById("wordsLink");
  const navLink = document.getElementById("navLink");

  if (pageTitle && config.title) pageTitle.textContent = config.title;
  if (wordsLink && config.wordsLink) wordsLink.href = config.wordsLink;
  if (navLink && config.navLink) navLink.href = config.navLink;

  const cookieName = config.storageKey
    ? `greek_cards_${config.storageKey}`
    : "greek_cards_generic";

  const state = {
    order: [],
    index: 0,
    status: {},
    side: "gr-ru",
    repeatLeftOnly: false,
  };

  let deck = [];
  let activeOrder = [];
  let isFlipped = false;
  let isDragging = false;
  let isAnimating = false;
  let activePointerId = null;
  let startX = 0;
  let startY = 0;
  let lastX = 0;
  let moved = false;

  function setCookie(name, value, days = 365) {
    const maxAge = days * 24 * 60 * 60;
    document.cookie = `${name}=${encodeURIComponent(value)}; max-age=${maxAge}; path=/`;
  }

  function getCookie(name) {
    const match = document.cookie.match(new RegExp(`(?:^|; )${name}=([^;]*)`));
    return match ? decodeURIComponent(match[1]) : null;
  }

  function deleteCookie(name) {
    document.cookie = `${name}=; max-age=0; path=/`;
  }

  function saveState() {
    setCookie(cookieName, JSON.stringify(state));
  }

  function loadState() {
    const saved = getCookie(cookieName);
    if (!saved) return;
    try {
      const data = JSON.parse(saved);
      if (data && typeof data === "object") {
        state.order = Array.isArray(data.order) ? data.order : [];
        state.index = Number.isInteger(data.index) ? data.index : 0;
        state.status = data.status || {};
        state.side = data.side === "ru-gr" ? "ru-gr" : "gr-ru";
        state.repeatLeftOnly = Boolean(data.repeatLeftOnly);
      }
    } catch (error) {
      deleteCookie(cookieName);
    }
  }

  function shuffle(array) {
    const result = [...array];
    for (let i = result.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [result[i], result[j]] = [result[j], result[i]];
    }
    return result;
  }

  function parseLines(text) {
    const lines = text.split(/\r?\n/);
    const cards = [];
    for (const line of lines) {
      const trimmed = line.trim();
      if (!trimmed.startsWith("-")) continue;
      const content = trimmed.replace(/^-+\s*/, "");
      const match = content.match(/\s+—\s+|\s+-\s+/);
      if (!match || match.index === undefined) continue;
      const front = content.slice(0, match.index).trim();
      const back = content.slice(match.index + match[0].length).trim();
      if (front && back) {
        cards.push({ front, back });
      }
    }
    return cards;
  }

  function updateActiveOrder() {
    if (state.repeatLeftOnly) {
      activeOrder = state.order.filter((idx) => state.status[idx] === "left");
    } else {
      activeOrder = [...state.order];
    }
    if (state.index >= activeOrder.length) {
      state.index = activeOrder.length;
    }
  }

  function updateProgress() {
    const total = activeOrder.length;
    const current = total === 0 ? 0 : Math.min(state.index + 1, total);
    const values = Object.values(state.status);
    const known = values.filter((value) => value === "right").length;
    const unknown = values.filter((value) => value === "left").length;
    progressBadge.textContent = `${current}/${total}`;
    progressInfo.innerHTML = `<span>Всего карточек: ${deck.length}</span><span>Помню: ${known} • Не помню: ${unknown}</span>`;
  }

  function renderCard() {
    updateActiveOrder();
    updateProgress();
    sideSelect.value = state.side;
    repeatLeftOnly.checked = state.repeatLeftOnly;
    isFlipped = false;
    cardEl.classList.remove("flipped");
    cardEl.classList.remove("swipe-left", "swipe-right", "drag-left", "drag-right");
    cardEl.style.transform = "";
    cardEl.style.opacity = "";

    if (deck.length === 0) {
      cardEl.textContent = "Карточки не найдены.";
      cardEl.classList.add("empty");
      leftBtn.disabled = true;
      rightBtn.disabled = true;
      return;
    }

    if (activeOrder.length === 0) {
      cardEl.textContent = "Нет карточек для повторения.";
      cardEl.classList.add("empty");
      leftBtn.disabled = true;
      rightBtn.disabled = true;
      return;
    }

    if (state.index >= activeOrder.length) {
      cardEl.textContent = "Урок завершен! Можно перемешать или повторить.";
      cardEl.classList.add("empty");
      leftBtn.disabled = true;
      rightBtn.disabled = true;
      return;
    }

    leftBtn.disabled = false;
    rightBtn.disabled = false;
    cardEl.classList.remove("empty");

    const card = deck[activeOrder[state.index]];
    const front = state.side === "gr-ru" ? card.front : card.back;
    cardEl.textContent = front;
  }

  function flipCard() {
    if (state.index >= activeOrder.length || isDragging || moved) return;
    const card = deck[activeOrder[state.index]];
    const front = state.side === "gr-ru" ? card.front : card.back;
    const back = state.side === "gr-ru" ? card.back : card.front;
    isFlipped = !isFlipped;
    cardEl.textContent = isFlipped ? back : front;
    cardEl.classList.toggle("flipped", isFlipped);
  }

  function moveCard(direction) {
    if (state.index >= activeOrder.length) return;
    const currentIndex = activeOrder[state.index];
    state.status[currentIndex] = direction;
    state.index += 1;
    saveState();
    renderCard();
  }

  function resetProgress() {
    state.order = deck.map((_, idx) => idx);
    state.index = 0;
    state.status = {};
    state.repeatLeftOnly = false;
    saveState();
    renderCard();
  }

  function animateSwipe(direction) {
    if (isAnimating || state.index >= activeOrder.length) return;
    isAnimating = true;
    cardEl.classList.remove("swipe-left", "swipe-right", "drag-left", "drag-right");
    cardEl.classList.add(direction === "right" ? "swipe-right" : "swipe-left");

    const onEnd = () => {
      cardEl.removeEventListener("transitionend", onEnd);
      cardEl.classList.remove("swipe-left", "swipe-right");
      cardEl.style.transform = "";
      cardEl.style.opacity = "";
      isAnimating = false;
      moveCard(direction);
    };

    cardEl.addEventListener("transitionend", onEnd);
  }

  function handlePointerDown(event) {
    if (state.index >= activeOrder.length) return;
    if (event.pointerType === "mouse" && event.button !== 0) return;
    if (activePointerId !== null) return;
    activePointerId = event.pointerId;
    startX = event.clientX;
    startY = event.clientY;
    lastX = startX;
    moved = false;
    isDragging = false;
    cardEl.setPointerCapture(event.pointerId);
    cardEl.classList.remove("drag-left", "drag-right");
  }

  function handlePointerMove(event) {
    if (state.index >= activeOrder.length) return;
    if (activePointerId === null || event.pointerId !== activePointerId) return;
    const dx = event.clientX - startX;
    const dy = event.clientY - startY;
    lastX = event.clientX;
    const threshold = 6;
    if (!isDragging && Math.abs(dx) > threshold && Math.abs(dx) > Math.abs(dy)) {
      isDragging = true;
    }
    if (!isDragging) return;
    moved = true;
    event.preventDefault();
    const rotate = dx / 18;
    const opacity = Math.max(0.2, 1 - Math.abs(dx) / 260);
    cardEl.classList.add("dragging");
    cardEl.classList.toggle("drag-right", dx > 0);
    cardEl.classList.toggle("drag-left", dx < 0);
    cardEl.style.transform = `translateX(${dx}px) rotate(${rotate}deg)`;
    cardEl.style.opacity = opacity;
  }

  function handlePointerUp(event) {
    if (activePointerId === null || event.pointerId !== activePointerId) return;
    cardEl.releasePointerCapture(event.pointerId);
    activePointerId = null;
    if (!isDragging) {
      isDragging = false;
      cardEl.classList.remove("dragging");
      cardEl.classList.remove("drag-left", "drag-right");
      return;
    }
    isDragging = false;
    cardEl.classList.remove("dragging");
    cardEl.classList.remove("drag-left", "drag-right");
    const dx = lastX - startX;
    const swipeThreshold = 80;
    if (Math.abs(dx) >= swipeThreshold) {
      animateSwipe(dx > 0 ? "right" : "left");
      return;
    }
    cardEl.style.transform = "";
    cardEl.style.opacity = "";
  }

  function initControls() {
    cardEl.addEventListener("click", flipCard);

    leftBtn.addEventListener("click", () => animateSwipe("left"));
    rightBtn.addEventListener("click", () => animateSwipe("right"));

    shuffleBtn.addEventListener("click", () => {
      state.order = shuffle(state.order);
      state.index = 0;
      saveState();
      renderCard();
    });

    resetBtn.addEventListener("click", () => {
      deleteCookie(cookieName);
      resetProgress();
    });

    sideSelect.addEventListener("change", () => {
      state.side = sideSelect.value;
      saveState();
      renderCard();
    });

    repeatLeftOnly.addEventListener("change", () => {
      state.repeatLeftOnly = repeatLeftOnly.checked;
      state.index = 0;
      saveState();
      renderCard();
    });

    cardEl.addEventListener("pointerdown", handlePointerDown);
    cardEl.addEventListener("pointermove", handlePointerMove);
    cardEl.addEventListener("pointerup", handlePointerUp);
    cardEl.addEventListener("pointercancel", handlePointerUp);
  }

  async function init() {
    try {
      const response = await fetch(config.source || "all.md");
      const text = await response.text();
      deck = parseLines(text);
    } catch (error) {
      deck = [];
    }

    loadState();

    if (!state.order.length || state.order.length !== deck.length) {
      state.order = deck.map((_, idx) => idx);
      state.index = 0;
    }

    initControls();
    renderCard();
  }

  init();
})();

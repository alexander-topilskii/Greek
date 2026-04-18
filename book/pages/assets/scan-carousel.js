/**
 * Minimal scan viewer for content_N.html: prev/next over raw/*.png with per-page links.
 * Expects <script type="application/json" id="scan-pages-data">[...]</script>
 * with items: { "n": number, "png": "raw/N.png", "md": "digitized/N.md" | null }
 */
(function () {
  var dataEl = document.getElementById("scan-pages-data");
  if (!dataEl) return;

  var pages;
  try {
    pages = JSON.parse(dataEl.textContent);
  } catch (e) {
    return;
  }
  if (!pages || !pages.length) return;

  var img = document.getElementById("scan-carousel-img");
  var cap = document.getElementById("scan-carousel-caption");
  var counter = document.getElementById("scan-carousel-counter");
  var prevBtn = document.getElementById("scan-carousel-prev");
  var nextBtn = document.getElementById("scan-carousel-next");
  var linkPng = document.getElementById("scan-link-png");
  var linkMd = document.getElementById("scan-link-md");
  var mdWrap = document.getElementById("scan-md-wrap");

  if (!img || !cap || !counter || !prevBtn || !nextBtn || !linkPng) return;

  var idx = 0;

  function show(i) {
    idx = ((i % pages.length) + pages.length) % pages.length;
    var p = pages[idx];
    img.src = p.png;
    img.alt = "Страница " + p.n;
    cap.textContent = "Стр. " + p.n;
    counter.textContent = idx + 1 + " / " + pages.length;
    linkPng.href = p.png;
    linkPng.textContent = p.n + ".png";
    if (p.md && linkMd && mdWrap) {
      linkMd.href = p.md;
      linkMd.textContent = p.n + ".md";
      mdWrap.hidden = false;
    } else if (mdWrap) {
      mdWrap.hidden = true;
    }
  }

  prevBtn.addEventListener("click", function () {
    show(idx - 1);
  });
  nextBtn.addEventListener("click", function () {
    show(idx + 1);
  });

  show(0);
})();

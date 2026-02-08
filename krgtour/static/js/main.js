(function () {
  const q = document.getElementById("q");
  const difficulty = document.getElementById("difficulty");
  const duration = document.getElementById("duration");
  const apply = document.getElementById("apply");
  const reset = document.getElementById("reset");
  const grid = document.getElementById("grid");
  const resultCount = document.getElementById("resultCount");

  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modalTitle");
  const modalText = document.getElementById("modalText");

  function normalize(s) {
    return (s || "").toString().toLowerCase().trim();
  }

  function filterCards() {
    const query = normalize(q.value);
    const diff = difficulty.value;
    const dur = duration.value;

    const cards = Array.from(grid.querySelectorAll(".route-card"));
    let visible = 0;

    cards.forEach((card) => {
      const title = card.dataset.title || "";
      const cDiff = card.dataset.difficulty || "";
      const cDur = card.dataset.duration || "";

      const okQuery = !query || normalize(title).includes(query);
      const okDiff = diff === "all" || cDiff === diff;
      const okDur = dur === "all" || cDur === dur || (dur === "3+ дня" && cDur.includes("3"));

      const show = okQuery && okDiff && okDur;
      card.style.display = show ? "" : "none";
      if (show) visible += 1;
    });

    resultCount.textContent = `Маршрутов: ${visible}`;
  }

  function openModal(title) {
    modalTitle.textContent = title;
    modalText.textContent =
      "Пока это моковая карточка. Дальше добавим описание, точки маршрута, карту и рекомендации ИИ.";
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
  }

  apply?.addEventListener("click", filterCards);
  reset?.addEventListener("click", () => {
    q.value = "";
    difficulty.value = "all";
    duration.value = "all";
    filterCards();
  });

  q?.addEventListener("keydown", (e) => {
    if (e.key === "Enter") filterCards();
  });

  grid?.addEventListener("click", (e) => {
    const btn = e.target.closest(".js-open");
    if (!btn) return;
    const card = btn.closest(".route-card");
    if (!card) return;
    openModal(card.dataset.title || "Маршрут");
  });

  modal?.addEventListener("click", (e) => {
    if (e.target.matches("[data-close]")) closeModal();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

  // Клик по популярным карточкам: подставляем запрос и фильтруем
  document.querySelectorAll(".mini-card").forEach((el) => {
    el.addEventListener("click", () => {
      q.value = el.dataset.jump || "";
      filterCards();
      document.getElementById("routes")?.scrollIntoView({ behavior: "smooth" });
    });
  });

  // Первичный подсчёт
  filterCards();
})();

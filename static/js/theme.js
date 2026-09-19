(function () {
  var KEY = "theme";
  var root = document.documentElement;

  function stored() {
    try { return localStorage.getItem(KEY); } catch (e) { return null; }
  }

  function preferred() {
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  function apply(theme) {
    root.setAttribute("data-bs-theme", theme);
    var isDark = theme === "dark";
    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.setAttribute("aria-pressed", String(isDark));
      btn.setAttribute("title", isDark ? "Mudar para o tema claro" : "Mudar para o tema escuro");
    });
  }

  // Executa no <head>, antes da pintura, para evitar o "flash" do tema errado.
  apply(stored() || preferred());

  document.addEventListener("DOMContentLoaded", function () {
    apply(root.getAttribute("data-bs-theme"));
    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var next = root.getAttribute("data-bs-theme") === "dark" ? "light" : "dark";
        try { localStorage.setItem(KEY, next); } catch (e) {}
        apply(next);
      });
    });
  });
})();

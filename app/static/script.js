// SAFELY SELECT ELEMENTS
const body = document.querySelector("body");
const modeToggle = document.querySelector(".mode-toggle");
const sidebar = document.querySelector("nav");
const sidebarToggle = document.querySelector(".sidebar-toggle");

// ------------------------------
// RESTORE SAVED THEME
// ------------------------------
let savedMode = localStorage.getItem("mode");
if (savedMode === "dark") {
    body.classList.add("dark");
}

// ------------------------------
// RESTORE SAVED SIDEBAR STATE
// ------------------------------
let savedSidebar = localStorage.getItem("status");
if (savedSidebar === "close") {
    if (sidebar) sidebar.classList.add("close");
}

// ------------------------------
// DARK MODE TOGGLE
// ------------------------------
if (modeToggle) {
    modeToggle.addEventListener("click", () => {
        body.classList.toggle("dark");

        if (body.classList.contains("dark")) {
            localStorage.setItem("mode", "dark");
        } else {
            localStorage.setItem("mode", "light");
        }
    });
}

// ------------------------------
// SIDEBAR OPEN/CLOSE TOGGLE
// ------------------------------
if (sidebarToggle && sidebar) {
    sidebarToggle.addEventListener("click", () => {
        sidebar.classList.toggle("close");

        if (sidebar.classList.contains("close")) {
            localStorage.setItem("status", "close");
        } else {
            localStorage.setItem("status", "open");
        }
    });
}

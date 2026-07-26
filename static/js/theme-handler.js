const themeButton$ = document.getElementById("theme-button");
        const body$ = document.body;

        function setInitialTheme() {
            const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
            const storedTheme = localStorage.getItem("theme");

            if (storedTheme === "dark") {
                body$.classList.add("dark-theme");
                themeButton$.textContent = "day";
                body$.setAttribute("data-bs-theme", "dark");
                return;
            } else if (storedTheme === "light") {
                body$.classList.remove("dark-theme");
                themeButton$.textContent = "night";
                body$.setAttribute("data-bs-theme", "light");
                return;
            }

            if (prefersDarkScheme) {
                body$.classList.add("dark-theme");
                themeButton$.textContent = "day";
                body$.setAttribute("data-bs-theme", "dark");
                return;
            }

            body$.classList.remove("dark-theme");
            themeButton$.textContent = "night";
            body$.setAttribute("data-bs-theme", "light");
        }

        setInitialTheme();

        themeButton$.addEventListener("click", () => {
            body$.classList.toggle("dark-theme");
            if (body$.classList.contains("dark-theme")) {
                themeButton$.textContent = "day";
                body$.setAttribute("data-bs-theme", "dark");
                localStorage.setItem("theme", "dark");
            } else {
                themeButton$.textContent = "night";
                body$.setAttribute("data-bs-theme", "light");
                localStorage.setItem("theme", "light");
            }
        });

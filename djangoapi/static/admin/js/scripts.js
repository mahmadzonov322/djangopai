// ===========================
// Navbar yuklash
// ===========================




// ===========================
// Chap Sidebar yuklash
// ===========================




// ===========================
// Register / Login / Logout
// ===========================

function loadAuth() {

    const auth = document.getElementById("authButtons");

    if (!auth) return;

    const registered = localStorage.getItem("registered");
    const loggedIn = localStorage.getItem("loggedIn");

    // Birinchi marta kirgan
    if (!registered) {

        auth.innerHTML = `
            <a href="register.html" class="contact-btn">
                Register
            </a>
        `;

    }

    // Register bo'lgan lekin login qilmagan
    else if (!loggedIn) {

        auth.innerHTML = `
            <a href="login.html" class="contact-btn">
                Login
            </a>
        `;

    }

    // Login qilgan
    else {

        auth.innerHTML = `
            <a href="#" class="contact-btn" id="logoutBtn">
                Logout
            </a>
        `;

        document.getElementById("logoutBtn").addEventListener("click", function (e) {

            e.preventDefault();

            localStorage.removeItem("loggedIn");

            location.reload();

        });

    }

}
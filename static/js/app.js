document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if (form) {

        form.addEventListener("submit", function () {

            showLoading();

        });

    }

});


function showLoading() {

    const overlay = document.createElement("div");

    overlay.id = "loadingOverlay";

    overlay.innerHTML = `

        <div class="loader-card">

            <div class="spinner"></div>

            <h2>Creating Your AI Video...</h2>

            <p>Please wait while ShortForge AI works its magic.</p>

            <div class="progress">

                <div class="progress-bar"></div>

            </div>

            <div id="statusText">

                Generating Script...

            </div>

        </div>

    `;

    document.body.appendChild(overlay);

    const steps = [

        "Generating Script...",

        "Splitting Scenes...",

        "Generating Images...",

        "Generating Voice...",

        "Rendering Video..."

    ];

    let index = 0;

    const status = document.getElementById("statusText");

    const interval = setInterval(() => {

        index++;

        if (index < steps.length) {

            status.innerText = steps[index];

        }

    }, 5000);

}


function copyScript() {

    const script = document.getElementById("script");

    navigator.clipboard.writeText(script.innerText);

    alert("✅ Script copied!");

}
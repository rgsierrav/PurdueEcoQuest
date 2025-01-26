const startButton = document.getElementById("start-button");
const eventSection = document.getElementById("event-section");
const eventTitle = document.getElementById("event-title");
const eventDescription = document.getElementById("event-description");
const choice1Button = document.getElementById("choice1-button");
const choice2Button = document.getElementById("choice2-button");
const healthDisplay = document.getElementById("health");
const happinessDisplay = document.getElementById("happiness");
const moneyDisplay = document.getElementById("money");
const academicsDisplay = document.getElementById("academics");
const ecoPointsDisplay = document.getElementById("ecopoints");

let stats = {};

// Start the game
startButton.addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:5000/start_game", {
        method: "POST",
    });
    const data = await response.json();

    stats = data.stats;
    updateStats();
    displayEvent(data.event);
});

// Handle choices
choice1Button.addEventListener("click", () => handleChoice("choice1"));
choice2Button.addEventListener("click", () => handleChoice("choice2"));

async function handleChoice(choice) {
    const response = await fetch("http://127.0.0.1:5000/make_choice", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ choice }),
    });
    const data = await response.json();

    stats = data.stats;
    updateStats();

    if (data.event) {
        displayEvent(data.event);
    } else {
        alert(data.summary); // End of the game
        location.reload();
    }
}

function updateStats() {
    healthDisplay.textContent = stats.health;
    happinessDisplay.textContent = stats.happiness;
    moneyDisplay.textContent = stats.money;
    academicsDisplay.textContent = stats.academics;
    ecoPointsDisplay.textContent = stats.ecopoints;
}

function displayEvent(event) {
    startButton.style.display = "none";
    eventSection.style.display = "block";
    eventTitle.textContent = `Week ${event.week}`;
    eventDescription.textContent = event.description;
    choice1Button.textContent = event.choice1;
    choice2Button.textContent = event.choice2;
}

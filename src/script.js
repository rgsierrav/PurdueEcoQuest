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

//current game stats
let stats = {}; 

// Start the game
startButton.addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:5000/start_game", {
        method: "POST",
    });
    const data = await response.json();

    // move-in stats
    stats = data.stats;
    updateStats();
    displayEvent(data.event);
});

// Handle "Choice 1"
choice1Button.addEventListener("click", () => handleChoice("/choice_1"));

// Handle "Choice 2"
choice2Button.addEventListener("click", () => handleChoice("/choice_2"));

// Fetch a new event
async function fetchNewEvent() {
    try {
        const response = await fetch("http://127.0.0.1:5000/new_event", {
            method: "POST",
        });
        if (!response.ok) throw new Error("Failed to fetch new event.");
        const data = await response.json();

        displayEvent(data.event); // Display the new event
    } catch (error) {
        console.error("Error fetching new event:", error);
        alert("An error occurred while fetching the new event. Please try again.");
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

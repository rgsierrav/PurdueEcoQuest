document.addEventListener("DOMContentLoaded", () => {
    const startButton = document.getElementById("start-button");
    const eventSection = document.getElementById("event-section");
    const choice1Button = document.getElementById("choice1-button");
    const choice2Button = document.getElementById("choice2-button");
    const stats = {
        health: document.getElementById("health"),
        happiness: document.getElementById("happiness"),
        money: document.getElementById("money"),
        academics: document.getElementById("academics"),
        ecopoints: document.getElementById("ecopoints"),
    };


    const eventTitle = document.getElementById("event-title");
    const eventDescription = document.getElementById("event-description");

    // Start Game
    startButton.addEventListener("click", () => {
        fetch("/start_game", { method: "POST" })
            .then((response) => response.json())
            .then((data) => {
                updateEvent(data);
                resetStats();
                eventSection.style.display = "block";
            })
            .catch((error) => console.error("Error starting game:", error));
    });


    // Handle Choice 1
    choice1Button.addEventListener("click", () => {
        fetch("/choice_1", { method: "POST" })
            .then((response) => response.json())
            .then((data) => {
                updateStats(data);
                getNewEvent();
            })
            .catch((error) => console.error("Error handling choice 1:", error));
    });

    // Handle Choice 2
    choice2Button.addEventListener("click", () => {
        fetch("/choice_2", { method: "POST" })
            .then((response) => response.json())
            .then((data) => {
                updateStats(data);
                getNewEvent();
            })
            .catch((error) => console.error("Error handling choice 2:", error));
    });

    // Fetch a new event
    function getNewEvent() {
        fetch("/new_event", { method: "POST" })
            .then((response) => response.json())
            .then((data) => {
                updateEvent(data);
            })
            .catch((error) => console.error("Error fetching new event:", error));
    }

    // Update Event Details
    function updateEvent(data) {
        eventTitle.textContent = data.Name || "Unknown Event";
        eventDescription.textContent = data.Description || "No description available.";
        choice1Button.textContent = data.Choice1 || "Option 1";
        choice2Button.textContent = data.Choice2 || "Option 2";
    }

    // Update Stats
    function updateStats(data) {
        stats.health.textContent = data.Health || 0;
        stats.happiness.textContent = data.Happiness || 0;
        stats.money.textContent = data.Money || 0;
        stats.academics.textContent = data.Academics || 0;
        stats.ecopoints.textContent = data.EcoPoints || 0;
    }

    // Reset Stats (to clear any previous values)
    function resetStats() {
        updateStats({
            Health: 90,
            Happiness: 80,
            Money: Math.floor(Math.random() * (50 - 20 + 1)) + 20, // Random between 20-50
            Academics: 50,
            EcoPoints: 0,
        });
    }
});

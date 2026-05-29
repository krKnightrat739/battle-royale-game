```javascript
const choices = ["Rock", "Paper", "Scissors", "Fire", "Water"];

const winRules = {
    Rock: ["Scissors", "Fire"],
    Paper: ["Rock", "Water"],
    Scissors: ["Paper", "Fire"],
    Fire: ["Paper", "Scissors"],
    Water: ["Rock", "Fire"]
};

let players = [];
let currentRound = [];
let winners = [];

let currentMatch = 0;

function createPlayerInputs() {

    const count = document.getElementById("playerCount").value;

    const container = document.getElementById("playerInputs");

    container.innerHTML = "";

    for (let i = 0; i < count; i++) {

        container.innerHTML += `
            <input class="player-input" type="text" id="player${i}" placeholder="Player ${i+1} Name">
        `;
    }

    container.innerHTML += `
        <button onclick="startTournament()">Begin Game</button>
    `;
}

function startTournament() {

    players = [];

    const count = document.getElementById("playerCount").value;

    for (let i = 0; i < count; i++) {

        const name = document.getElementById(`player${i}`).value;

        players.push(name || `Player ${i+1}`);
    }

    currentRound = [...players];

    shuffle(currentRound);

    showBracket();

    nextMatch();
}

function nextMatch() {

    if (currentRound.length === 1) {

        document.getElementById("matchArea").innerHTML = `
            <div class="winner">
                🏆 WINNER: ${currentRound[0]} <br><br>
                🎁 Prize: RayBan Meta Glass Gen 1
            </div>
        `;

        return;
    }

    if (currentMatch >= currentRound.length) {

        currentRound = [...winners];

        winners = [];

        currentMatch = 0;

        shuffle(currentRound);

        showBracket();
    }

    const p1 = currentRound[currentMatch];
    const p2 = currentRound[currentMatch + 1];

    document.getElementById("roundTitle").innerText =
        `🔥 ${p1} VS ${p2}`;

    let html = `
        <div class="match-card">

            <h2>${p1}</h2>

            <div class="choice-buttons">
    `;

    choices.forEach(choice => {

        html += `
            <button onclick="player2Choice('${choice}')">
                ${choice}
            </button>
        `;
    });

    html += `
            </div>

        </div>
    `;

    window.currentPlayers = [p1, p2];

    window.player1Selected = null;

    document.getElementById("matchArea").innerHTML = html;

    alert(`${p1}, select your move secretly`);
}

function player2Choice(choice1) {

    window.player1Selected = choice1;

    let html = `
        <div class="match-card">

            <h2>${window.currentPlayers[1]}</h2>

            <div class="choice-buttons">
    `;

    choices.forEach(choice => {

        html += `
            <button onclick="finishMatch('${choice}')">
                ${choice}
            </button>
        `;
    });

    html += `
            </div>

        </div>
    `;

    document.getElementById("matchArea").innerHTML = html;

    alert(`${window.currentPlayers[1]}, now choose secretly`);
}

function finishMatch(choice2) {

    const choice1 = window.player1Selected;

    const p1 = window.currentPlayers[0];
    const p2 = window.currentPlayers[1];

    let winner;

    if (choice1 === choice2) {

        alert("DRAW! Replay!");

        nextMatch();

        return;
    }

    if (winRules[choice1].includes(choice2)) {

        winner = p1;

    } else {

        winner = p2;
    }

    winners.push(winner);

    alert(`🏆 ${winner} wins this match!`);

    currentMatch += 2;

    nextMatch();
}

function showBracket() {

    let html = "";

    currentRound.forEach(player => {

        html += `<p>⚔️ ${player}</p>`;
    });

    document.getElementById("bracket").innerHTML = html;
}

function shuffle(array) {

    for (let i = array.length - 1; i > 0; i--) {

        const j = Math.floor(Math.random() * (i + 1));

        [array[i], array[j]] = [array[j], array[i]];
    }
}
```

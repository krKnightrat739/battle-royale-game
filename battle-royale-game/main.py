# Save this as: main.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# -----------------------------
# GAME RULES
# -----------------------------
choices = ["Rock", "Paper", "Scissors", "Fire", "Water"]

win_rules = {
    "Rock": ["Scissors", "Fire"],
    "Paper": ["Rock", "Water"],
    "Scissors": ["Paper", "Fire"],
    "Fire": ["Paper", "Scissors"],
    "Water": ["Rock", "Fire"]
}

players = []
current_round = []
winners = []

match_index = 0
round_number = 1

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("Battle Royale Tournament")
root.geometry("1200x700")
root.configure(bg="#111111")

title = tk.Label(
    root,
    text="BATTLE ROYALE TOURNAMENT",
    font=("Arial", 26, "bold"),
    fg="gold",
    bg="#111111"
)
title.pack(pady=15)

# -----------------------------
# FRAME SETUP
# -----------------------------
main_frame = tk.Frame(root, bg="#111111")
main_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(main_frame, bg="#1e1e1e", width=500)
left_frame.pack(side="left", fill="both", padx=10, pady=10)

right_frame = tk.Frame(main_frame, bg="#181818")
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# -----------------------------
# TOURNAMENT BRACKET UI
# -----------------------------
bracket_title = tk.Label(
    left_frame,
    text="TOURNAMENT BRACKET",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="#1e1e1e"
)
bracket_title.pack(pady=10)

bracket_text = tk.Text(
    left_frame,
    bg="#222222",
    fg="white",
    font=("Consolas", 12),
    width=45,
    height=30,
    bd=0
)
bracket_text.pack(padx=10, pady=10)

# -----------------------------
# MATCH UI
# -----------------------------
round_label = tk.Label(
    right_frame,
    text="ROUND 1",
    font=("Arial", 24, "bold"),
    fg="cyan",
    bg="#181818"
)
round_label.pack(pady=10)

match_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="#181818"
)
match_label.pack(pady=20)

status_label = tk.Label(
    right_frame,
    text="",
    font=("Arial", 14),
    fg="lightgreen",
    bg="#181818"
)
status_label.pack(pady=10)

player1_choice = tk.StringVar(value="Rock")
player2_choice = tk.StringVar(value="Rock")

# -----------------------------
# PLAYER INPUT AREA
# -----------------------------
players_frame = tk.Frame(right_frame, bg="#181818")
players_frame.pack(pady=10)

# Player 1
p1_frame = tk.Frame(players_frame, bg="#181818")
p1_frame.grid(row=0, column=0, padx=40)

p1_label = tk.Label(
    p1_frame,
    text="Player 1",
    font=("Arial", 18, "bold"),
    fg="orange",
    bg="#181818"
)
p1_label.pack()

for c in choices:
    tk.Radiobutton(
        p1_frame,
        text=c,
        variable=player1_choice,
        value=c,
        font=("Arial", 12),
        bg="#181818",
        fg="white",
        selectcolor="#333333"
    ).pack(anchor="w")

# Player 2
p2_frame = tk.Frame(players_frame, bg="#181818")
p2_frame.grid(row=0, column=1, padx=40)

p2_label = tk.Label(
    p2_frame,
    text="Player 2",
    font=("Arial", 18, "bold"),
    fg="orange",
    bg="#181818"
)
p2_label.pack()

for c in choices:
    tk.Radiobutton(
        p2_frame,
        text=c,
        variable=player2_choice,
        value=c,
        font=("Arial", 12),
        bg="#181818",
        fg="white",
        selectcolor="#333333"
    ).pack(anchor="w")

# -----------------------------
# GAME FUNCTIONS
# -----------------------------
def determine_winner(c1, c2):
    if c1 == c2:
        return None

    if c2 in win_rules[c1]:
        return 1
    else:
        return 2


def update_bracket():
    bracket_text.delete("1.0", tk.END)

    bracket_text.insert(tk.END, f"ROUND {round_number}\n")
    bracket_text.insert(tk.END, "=" * 30 + "\n\n")

    for i in range(0, len(current_round), 2):
        if i + 1 < len(current_round):
            bracket_text.insert(
                tk.END,
                f"{current_round[i]}  VS  {current_round[i+1]}\n"
            )

    bracket_text.insert(tk.END, "\n\nQUALIFIED PLAYERS:\n")
    bracket_text.insert(tk.END, "-" * 30 + "\n")

    for w in winners:
        bracket_text.insert(tk.END, f"✔ {w}\n")


def load_match():
    global match_index

    if match_index >= len(current_round):
        next_round()
        return

    p1 = current_round[match_index]
    p2 = current_round[match_index + 1]

    match_label.config(text=f"{p1}  VS  {p2}")
    p1_label.config(text=p1)
    p2_label.config(text=p2)

    update_bracket()


def submit_match():
    global match_index

    p1 = current_round[match_index]
    p2 = current_round[match_index + 1]

    c1 = player1_choice.get()
    c2 = player2_choice.get()

    winner = determine_winner(c1, c2)

    if winner is None:
        status_label.config(text="DRAW! Replay Match!")
        return

    if winner == 1:
        winners.append(p1)
        status_label.config(text=f"{p1} wins the match!")
    else:
        winners.append(p2)
        status_label.config(text=f"{p2} wins the match!")

    match_index += 2
    update_bracket()

    root.after(1500, load_match)


def next_round():
    global current_round, winners, match_index, round_number

    if len(winners) == 1:
        winner_screen(winners[0])
        return

    current_round = winners.copy()
    winners.clear()

    random.shuffle(current_round)

    if len(current_round) % 2 == 1:
        lucky = current_round.pop()
        winners.append(lucky)

    match_index = 0
    round_number += 1

    round_label.config(text=f"ROUND {round_number}")

    load_match()


def winner_screen(winner):
    messagebox.showinfo(
        "TOURNAMENT WINNER",
        f"🏆 WINNER: {winner}\n\n🎁 Prize: RayBan Meta Glass Gen 1"
    )

    root.destroy()


# -----------------------------
# START GAME
# -----------------------------
num_players = simpledialog.askinteger(
    "Players",
    "Enter number of players:"
)

if num_players is None or num_players < 2:
    messagebox.showerror("Error", "Minimum 2 players required!")
    root.destroy()

else:
    for i in range(num_players):
        name = simpledialog.askstring(
            "Player Name",
            f"Enter Player {i+1} Name:"
        )

        if not name:
            name = f"Player{i+1}"

        players.append(name)

    current_round = players.copy()

    random.shuffle(current_round)

    if len(current_round) % 2 == 1:
        lucky = current_round.pop()
        winners.append(lucky)

    load_match()

# -----------------------------
# BUTTON
# -----------------------------
submit_btn = tk.Button(
    right_frame,
    text="SUBMIT MATCH",
    font=("Arial", 18, "bold"),
    bg="gold",
    fg="black",
    padx=20,
    pady=10,
    command=submit_match
)
submit_btn.pack(pady=25)

root.mainloop()
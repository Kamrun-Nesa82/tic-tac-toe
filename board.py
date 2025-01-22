from tkinter import *

root = Tk()
root.geometry("800x850")  # Increased window size
root.title("Tic Tac Toe")

# Game state
turn = "X"

# Function to play (place "X" and "O" alternately on the board)
def play(event):
    global turn
    button = event.widget
    if button["text"] == " ":  # Only place if the cell is empty
        button["text"] = turn
        next_turn = "O" if turn == "X" else "X"  # Determine next turn
        turn_label.config(text=f"{next_turn}'s turn")  # Update turn label
        turn = next_turn  # Switch turn

# Function to restart the game
def restart_game():
    global turn
    turn = "X"  # Reset turn to X
    turn_label.config(text=f"{turn}'s turn")  # Reset turn label
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = " "  # Clear all buttons

# Frame for the boxed title
frame1 = Frame(root, bg="black", padx=10, pady=10)
frame1.pack(pady=10)
title_label = Label(frame1, text="Tic Tac Toe", font=("Arial", 20), bg="purple", relief=SOLID, borderwidth=2, padx=20, pady=10)
title_label.pack()

# Label to show the current turn (below the boxed title)
turn_label = Label(root, text=f"{turn}'s turn", font=("Arial", 20), fg="black")
turn_label.pack(pady=10)

# Frame for options (Single and Multiplayer Buttons)
frame2 = Frame(root)
frame2.pack(pady=10)

single_player_button = Button(frame2, text="Single Player", font=("Arial", 15), bg="lightblue", command=lambda: print("Single Player mode selected"))
single_player_button.grid(row=0, column=0, padx=10)

multiplayer_button = Button(frame2, text="Multiplayer", font=("Arial", 15), bg="lightgreen", command=lambda: print("Multiplayer mode selected"))
multiplayer_button.grid(row=0, column=1, padx=10)

# Frame for buttons (Tic Tac Toe board)
frame3 = Frame(root)
frame3.pack(pady=10)
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        # Larger button size for a bigger board
        buttons[r][c] = Button(frame3, text=" ", width=8, height=4, font=("Arial", 20), bg="lightblue", relief=RAISED, borderwidth=5)
        buttons[r][c].grid(row=r, column=c)
        buttons[r][c].bind("<Button-1>", play)

# Restart Button directly below the board
restart_button = Button(root, text="Restart Game", font=("Arial", 20), bg="lightcoral", command=restart_game)
restart_button.pack(pady=20)

root.mainloop()
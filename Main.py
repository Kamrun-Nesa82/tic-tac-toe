import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.geometry("1000x600")
root.title("Tic Tac Toe")

# Game variables
turn = "X"  # Player starts with 'X'
game_end = False
score_X = 0
score_O = 0
single_player = False  # Flag for single-player mode

# Function to update score
def update_score(winner):
    global score_X, score_O
    if winner == "X":
        score_X += 1
    elif winner == "O":
        score_O += 1
    score_label.config(text=f"X: {score_X}\nO: {score_O}")

# Function to play (place "X" or "O" on the board)
def play(event):
    global turn, game_end
    if game_end:
        return

    button = event.widget
    if button["text"] == " ":  # Ensure the button is empty
        button["text"] = turn
        if check_for_win(turn):
            result_label.config(text=f"{turn} wins the game!", bg="lightgreen")
            update_score(turn)
            game_end = True
        elif check_for_draw():
            result_label.config(text="It's a Draw!", bg="lightyellow")
            game_end = True
        else:
            turn = "O" if turn == "X" else "X"
            turn_label.config(text=f"{turn}'s turn")
            if single_player and turn == "O":
                root.after(500, ai_move)  # AI makes a move after a short delay

# AI for single-player mode using Minimax with Alpha-Beta Pruning
def ai_move():
    global turn, game_end
    if game_end:
        return

    best_score = -float('inf')
    best_move = None

    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] == " ":
                buttons[r][c]["text"] = "O"
                score = minimax(False, 4, -float('inf'), float('inf'))  # Depth-limited to 4
                buttons[r][c]["text"] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)

    if best_move:
        r, c = best_move
        buttons[r][c]["text"] = "O"
        if check_for_win("O"):
            result_label.config(text="O wins the game!", bg="lightgreen")
            update_score("O")
            game_end = True
        elif check_for_draw():
            result_label.config(text="It's a Draw!", bg="lightyellow")
            game_end = True
        else:
            turn = "X"
            turn_label.config(text=f"{turn}'s turn")

# Minimax function with Alpha-Beta Pruning
def minimax(is_maximizing, depth, alpha, beta):
    if check_for_win("O"):
        return 1  # O is the AI
    if check_for_win("X"):
        return -1  # X is the player
    if check_for_draw() or depth == 0:  # Limit depth to speed up calculations
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for r in range(3):
            for c in range(3):
                if buttons[r][c]["text"] == " ":
                    buttons[r][c]["text"] = "O"
                    eval = minimax(False, depth - 1, alpha, beta)
                    buttons[r][c]["text"] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:  # Prune
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for r in range(3):
            for c in range(3):
                if buttons[r][c]["text"] == " ":
                    buttons[r][c]["text"] = "X"
                    eval = minimax(True, depth - 1, alpha, beta)
                    buttons[r][c]["text"] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:  # Prune
                        break
        return min_eval

# Check for a win
def check_for_win(player):
    for r in range(3):
        if buttons[r][0]["text"] == buttons[r][1]["text"] == buttons[r][2]["text"] == player:
            return True
    for c in range(3):
        if buttons[0][c]["text"] == buttons[1][c]["text"] == buttons[2][c]["text"] == player:
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:
        return True
    return False

# Check for a draw
def check_for_draw():
    for r in range(3):
        for c in range(3):
            if buttons[r][c]["text"] == " ":
                return False
    return True

# Restart the game
def restart_game():
    global turn, game_end
    turn = "X"
    game_end = False
    turn_label.config(text=f"{turn}'s turn")
    result_label.config(text="", bg="lightgray")
    for r in range(3):
        for c in range(3):
            buttons[r][c]["text"] = " "

# Function to switch to multiplayer interface
def multiplayer_interface():
    global single_player
    single_player = False
    main_frame.pack_forget()  # Hide main menu
    game_frame.pack()  # Show multiplayer game interface
    restart_game()

# Function to switch to single-player interface
def singleplayer_interface():
    global single_player
    single_player = True
    main_frame.pack_forget()  # Hide main menu
    game_frame.pack()  # Show single-player game interface
    restart_game()

# Create frames
main_frame = tk.Frame(root)
main_frame.pack()

# Main menu title
menu_title = tk.Label(main_frame, text="Welcome to Tic Tac Toe", font=("Arial", 24), bg="purple", fg="white", padx=20, pady=10)
menu_title.pack(pady=20)

# Multiplayer button
multiplayer_button = tk.Button(main_frame, text="Multiplayer", font=("Arial", 18), command=multiplayer_interface, bg="lightblue", width=15)
multiplayer_button.pack(pady=10)

# Singleplayer button
singleplayer_button = tk.Button(main_frame, text="Single Player", font=("Arial", 18), command=singleplayer_interface, bg="lightgreen", width=15)
singleplayer_button.pack(pady=10)

# Quit button
quit_button = tk.Button(main_frame, text="Quit", font=("Arial", 18), command=root.quit, bg="lightcoral", width=15)
quit_button.pack(pady=10)

# Game interface frame
game_frame = tk.Frame(root)

# Left frame for game board
left_frame = tk.Frame(game_frame)
left_frame.pack(side=tk.LEFT, padx=10)

# Restart button
restart_button = tk.Button(left_frame, text="Restart", font=("Arial", 16), command=restart_game, bg="lightcoral")
restart_button.pack(pady=10)

# Turn label
turn_label = tk.Label(left_frame, text=f"{turn}'s turn", font=("Arial", 20), fg="black", bg="lightblue")
turn_label.pack(pady=5)

# Result label
result_label = tk.Label(left_frame, text="", font=("Arial", 20), fg="black", bg="lightgray", width=20)
result_label.pack(pady=5)

# Tic Tac Toe board
frame3 = tk.Frame(left_frame)
frame3.pack(pady=10)
buttons = [[None for _ in range(3)] for _ in range(3)]
for r in range(3):
    for c in range(3):
        buttons[r][c] = tk.Button(frame3, text=" ", width=8, height=2, font=("Arial", 20), bg="lightblue", relief="raised")
        buttons[r][c].grid(row=r, column=c)
        buttons[r][c].bind("<Button-1>", play)

# Back button
back_button = tk.Button(left_frame, text="Back to Menu", font=("Arial", 16), command=lambda: [game_frame.pack_forget(), main_frame.pack()], bg="lightblue")
back_button.pack(pady=10)

# Right frame for scoreboard
right_frame = tk.Frame(game_frame)
right_frame.pack(side=tk.RIGHT, padx=30)

score_title = tk.Label(right_frame, text="Scoreboard", font=("Arial", 20), bg="gold", width=15)
score_title.pack(pady=10)

score_label = tk.Label(right_frame, text=f"X: {score_X}\nO: {score_O}", font=("Arial", 20), bg="lightgray", width=15)
score_label.pack(pady=10)

# Start the main loop
root.mainloop()
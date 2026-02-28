import tkinter as tk
import random


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("500x450")
root.configure(bg="#f0f0f0")

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0


def play(user_choice):
    global user_score, computer_score
    
    computer_choice = random.choice(choices)
    
    user_choice_label.config(text=f"You chose: {user_choice}")
    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"Score → You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    user_choice_label.config(text="You chose: ")
    computer_choice_label.config(text="Computer chose: ")
    score_label.config(text="Score → You: 0 | Computer: 0")


title = tk.Label(root, text="Rock Paper Scissors Game", 
                 font=("Arial", 20, "bold"), bg="#f0f0f0")
title.pack(pady=15)


main_frame = tk.Frame(root, bg="#f0f0f0")
main_frame.pack()


left_frame = tk.Frame(main_frame, bg="white", bd=2, relief="ridge")
left_frame.grid(row=0, column=0, padx=20, pady=10)

tk.Label(left_frame, text="PLAYER", font=("Arial", 14, "bold"),
         bg="white").pack(pady=10)

tk.Button(left_frame, text="Rock", width=12,
          command=lambda: play("Rock")).pack(pady=5)

tk.Button(left_frame, text="Paper", width=12,
          command=lambda: play("Paper")).pack(pady=5)

tk.Button(left_frame, text="Scissors", width=12,
          command=lambda: play("Scissors")).pack(pady=5)

right_frame = tk.Frame(main_frame, bg="white", bd=2, relief="ridge")
right_frame.grid(row=0, column=1, padx=20, pady=10)

tk.Label(right_frame, text="COMPUTER", font=("Arial", 14, "bold"),
         bg="white").pack(pady=10)

computer_choice_label = tk.Label(right_frame, text="Computer chose: ",
                                 font=("Arial", 12), bg="white")
computer_choice_label.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"),
                        fg="blue", bg="#f0f0f0")
result_label.pack(pady=10)

user_choice_label = tk.Label(root, text="You chose: ",
                             font=("Arial", 12), bg="#f0f0f0")
user_choice_label.pack()


score_label = tk.Label(root, text="Score → You: 0 | Computer: 0",
                       font=("Arial", 12, "bold"), bg="#f0f0f0")
score_label.pack(pady=15)


reset_btn = tk.Button(root, text="Reset Game", width=15, bg="red", fg="white",
                      command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
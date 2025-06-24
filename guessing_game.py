import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")  # or "light"
ctk.set_default_color_theme("green") # options: "blue", "green", "dark-blue"

class GuessingGame(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Guessing Game")
        self.geometry("400x350")
        self.resizable(False, False)

        # Variables
        self.min_val = 1
        self.max_val = 100
        self.secret_number = None
        self.attempts = 0

        # Difficulty selection
        self.label_title = ctk.CTkLabel(self, text="Choose Difficulty:", font=("Helvetica", 16))
        self.label_title.pack(pady=(20, 5))

        self.difficulty_var = ctk.StringVar(value="hard")
        self.radio_easy = ctk.CTkRadioButton(self, text="Easy (1-10)", variable=self.difficulty_var, value="easy", command=self.set_difficulty)
        self.radio_easy.pack(pady=2)
        self.radio_medium = ctk.CTkRadioButton(self, text="Medium (1-50)", variable=self.difficulty_var, value="medium", command=self.set_difficulty)
        self.radio_medium.pack(pady=2)
        self.radio_hard = ctk.CTkRadioButton(self, text="Hard (1-100)", variable=self.difficulty_var, value="hard", command=self.set_difficulty)
        self.radio_hard.pack(pady=2)

        # Guess input
        self.label_prompt = ctk.CTkLabel(self, text="Enter your guess:")
        self.label_prompt.pack(pady=(15, 5))

        self.entry_guess = ctk.CTkEntry(self, width=120)
        self.entry_guess.pack()

        # Submit button
        self.button_submit = ctk.CTkButton(self, text="Submit Guess", command=self.check_guess)
        self.button_submit.pack(pady=10)

        # Feedback label
        self.label_feedback = ctk.CTkLabel(self, text="", font=("Helvetica", 14))
        self.label_feedback.pack(pady=5)

        # Attempts label
        self.label_attempts = ctk.CTkLabel(self, text="Attempts: 0")
        self.label_attempts.pack(pady=5)

        # Play Again button (disabled initially)
        self.button_play_again = ctk.CTkButton(self, text="Play Again", command=self.reset_game, state=ctk.DISABLED)
        self.button_play_again.pack(pady=10)

        self.set_difficulty()  # initialize the secret number

    def set_difficulty(self):
        diff = self.difficulty_var.get()
        if diff == "easy":
            self.min_val, self.max_val = 1, 10
        elif diff == "medium":
            self.min_val, self.max_val = 1, 50
        else:
            self.min_val, self.max_val = 1, 100

        self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(self.min_val, self.max_val)
        self.attempts = 0
        self.label_feedback.configure(text="")
        self.label_attempts.configure(text="Attempts: 0")
        self.entry_guess.delete(0, ctk.END)
        self.button_submit.configure(state=ctk.NORMAL)
        self.button_play_again.configure(state=ctk.DISABLED)
        self.label_prompt.configure(text=f"Enter your guess ({self.min_val}-{self.max_val}):")

    def check_guess(self):
        guess_str = self.entry_guess.get()
        try:
            guess = int(guess_str)
        except ValueError:
            self.label_feedback.configure(text="Please enter a valid whole number.")
            return

        if not (self.min_val <= guess <= self.max_val):
            self.label_feedback.configure(text=f"Guess must be between {self.min_val} and {self.max_val}.")
            return

        self.attempts += 1
        self.label_attempts.configure(text=f"Attempts: {self.attempts}")

        if guess < self.secret_number:
            self.label_feedback.configure(text="Too low!")
        elif guess > self.secret_number:
            self.label_feedback.configure(text="Too high!")
        else:
            self.label_feedback.configure(text=f"🎉 You guessed it in {self.attempts} attempts!")
            self.button_submit.configure(state=ctk.DISABLED)
            self.button_play_again.configure(state=ctk.NORMAL)

        self.entry_guess.delete(0, ctk.END)


if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()

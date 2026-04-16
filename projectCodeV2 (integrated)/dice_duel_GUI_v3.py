import tkinter as tk
from tkinter import ttk, messagebox
from dice_duel_logic import DiceDuelGame


class DiceDuelFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, background="black")
        self.pack(fill=tk.BOTH, expand=True)
        
        
        #Tkinter style to configure app appearance
        style = ttk.Style()
        style.theme_use("clam")
        
        # Frame style 
        style.configure("ArcadeFrame.TFrame",
                        background="black",
                        bordercolor="purple",
                        borderwidth=3,
                        relief="solid")
        
        # Label style 
        style.configure("ArcadeLabel.TLabel",
                        background="black",
                        foreground="Lime",
                        font=("Arial", 12, "bold"))
        
        # Title style 
        style.configure("ArcadeTitle.TLabel",
                        background="black",
                        foreground="Lime",
                        font=("Arial", 26, "bold"))
        
        # Button style 
        style.configure("ArcadeButton.TButton",
                        background="black",
                        foreground="Lime",
                        font=("Arial", 24, "bold"),
                        padding=1)
        # mapping allows change in appearance when cursor is hovering to make button "active"
        style.map("ArcadeButton.TButton",
                  background=[("active", "purple")])


        
        # game instance
        self.game = DiceDuelGame()

        # title frame and label
        title_frame = ttk.Frame(self, style="ArcadeFrame.TFrame", padding="10 10 10 10")
        title_frame.grid(column=0, row=0, columnspan=3)

        ttk.Label(title_frame, text="Welcome to Dice Duel!", style="ArcadeTitle.TLabel").grid(column=0, row=0)

        self.add_padding(title_frame)

        # player roll data frame
        self.player_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.player_frame.grid(column=0, row=1)

        ttk.Label(self.player_frame, text="Player Roll", style="ArcadeLabel.TLabel").grid(column=0, row=0)

        self.player_roll = tk.StringVar(value="##")
        ttk.Label(self.player_frame, textvariable=self.player_roll, style="ArcadeLabel.TLabel").grid(column=0, row=1)

        self.add_padding(self.player_frame)

        # versus frame
        self.vs_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.vs_frame.grid(column=1, row=1)

        ttk.Label(self.vs_frame, text="VS", style="ArcadeLabel.TLabel").grid(column=0, row=0)

        self.add_padding(self.vs_frame)

        # house roll data frame
        self.house_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.house_frame.grid(column=2, row=1)

        ttk.Label(self.house_frame, text="House Roll", style="ArcadeLabel.TLabel").grid(column=0, row=0)

        self.house_roll = tk.StringVar(value="##")
        ttk.Label(self.house_frame, textvariable=self.house_roll, style="ArcadeLabel.TLabel").grid(column=0, row=1)

        self.add_padding(self.house_frame)


        # round result data frame
        self.result_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.result_frame.grid(column=0, row=2, columnspan=3)

        self.round_result = tk.StringVar(value="Round Winning Result")
        ttk.Label(self.result_frame, textvariable=self.round_result, style="ArcadeLabel.TLabel").grid(column=0, row=0)

        self.add_padding(self.result_frame)

        # player scoreboard frame
        self.player_score_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.player_score_frame.grid(column=0, row=3)

        ttk.Label(self.player_score_frame, text="Player Score:", style="ArcadeLabel.TLabel").grid(column=0, row=0, sticky=tk.E)

        self.player_score = tk.StringVar(value="##")
        ttk.Label(self.player_score_frame, textvariable=self.player_score, style="ArcadeLabel.TLabel").grid(column=1, row=0, sticky=tk.W)

        self.add_padding(self.player_score_frame)


        # house scoreboard frame
        self.house_score_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.house_score_frame.grid(column=2, row=3)

        ttk.Label(self.house_score_frame,text="House Score:",style="ArcadeLabel.TLabel").grid(column=0, row=0, sticky=tk.E)

        self.house_score = tk.StringVar(value="##")
        ttk.Label(self.house_score_frame,textvariable=self.house_score,style="ArcadeLabel.TLabel").grid(column=1, row=0, sticky=tk.W)

        self.add_padding(self.house_score_frame)

        # total rounds played frame
        self.total_round_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.total_round_frame.grid(column=0, row=4, columnspan=3)

        ttk.Label(self.total_round_frame, text="Total Rounds Played:", style="ArcadeLabel.TLabel").grid(column=0, row=0, sticky=tk.E)

        self.total_round = tk.StringVar(value="##")
        ttk.Label(self.total_round_frame, textvariable=self.total_round, style="ArcadeLabel.TLabel").grid(column=1, row=0, sticky=tk.W)

        self.add_padding(self.total_round_frame)

        # roll die button frame & button
        self.button_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.button_frame.grid(column=0, row=5, columnspan=3)

        self.roll_button = ttk.Button(self.button_frame, text="Click to Roll", style="ArcadeButton.TButton",command=self.roll_die)
        self.roll_button.grid(column=0, row=0)


        self.reset_button = ttk.Button(self.button_frame, text="RESET GAME", style="ArcadeButton.TButton", command=self.reset_game)
        self.reset_button.grid(column=1, row=0, padx=5)

        self.add_padding(self.button_frame)

        # game rule frame
        self.game_rule_frame = ttk.Frame(self, padding="10 10 10 10", style="ArcadeFrame.TFrame")
        self.game_rule_frame.grid(column=0, row=6, columnspan=3)

        ttk.Label(self.game_rule_frame, text="RULES: First to win 10 rounds wins the game. Ties do not count.", style="ArcadeLabel.TLabel").grid(column=0, row=0)
       
        self.add_padding(self.game_rule_frame)
    
    

    # callback functions
    def roll_die(self):
        data = self.game.play_round()

        self.player_roll.set(str(data["player_roll"]))
        self.house_roll.set(str(data["house_roll"]))
        self.round_result.set(data["result"])
        self.player_score.set(str(data["player_score"]))
        self.house_score.set(str(data["house_score"]))
        self.total_round.set(str(data["rounds_played"]))

        winner = self.game.check_winner()
        if winner is not None:
            messagebox.showinfo("Game Over", f"{winner} wins the game!")
            self.roll_button.config(state="disabled")

    def reset_game(self):
        self.game.reset_game()

        self.player_roll.set("##")
        self.house_roll.set("##")
        self.round_result.set("Click the button to roll")
        self.player_score.set("0")
        self.house_score.set("0")
        self.total_round.set("0")
        self.roll_button.config(state="normal")

    def add_padding(self, frame):
        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dice Duel Game")
    DiceDuelFrame(root)
    root.mainloop()

# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 17:03:26 2026

@author: yayso
"""

import tkinter as tk
from tkinter import ttk


class DiceDuelFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding="10 10 10 10")
        self.pack(fill=tk.BOTH, expand=True)
          

        # title frame and label
        title_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=5, relief="solid")
        title_frame.grid(column=0, row=0, columnspan=3)
        ttk.Label(title_frame, text="Welcome to Dice Duel!", font=("Arial", 24, "bold")).grid(column=0, row=0)
        
        
        # add padding to title frame 
        self.add_padding(title_frame)
        
        
            
        # player roll data frame 
        self.player_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.player_frame.grid(column=0, row=1)
        self.player_roll_title = ttk.Label(self.player_frame, text="Player's Roll", font=("Arial", 12, "bold"))
        self.player_roll_title.grid(column=0, row=0)
        
        self.player_roll = tk.StringVar(value="##") # hashtag set as place holder for now
        self.player_roll_label = ttk.Label(self.player_frame, textvariable=self.player_roll, font=("Arial", 12))
        self.player_roll_label.grid(column=0, row=1)
        
        self.add_padding(self.player_frame)
        
        
        
        # versus frame 
        self.vs_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.vs_frame.grid(column=1, row=1)
        self.vs_label = ttk.Label(self.vs_frame, text="VS", font=("Arial", 16, "bold"))
        self.vs_label.grid(column=0, row=0)
        
        self.add_padding(self.vs_frame)
        
        
        
        # house roll data frame
        self.house_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.house_frame.grid(column=2, row=1)
        self.house_roll_title = ttk.Label(self.house_frame, text="House Roll", font=("Arial", 12, "bold"))
        self.house_roll_title.grid(column=0, row=0)
        
        self.house_roll = tk.StringVar(value="##") # hashtag set as place holder for now
        self.house_roll_label = ttk.Label(self.house_frame, textvariable=self.house_roll, font=("Arial", 12))
        self.house_roll_label.grid(column=0, row=1)
        
        self.add_padding(self.house_frame)
        
        
        
        # round result data frame
        self.result_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.result_frame.grid(column=0, row=2, columnspan=3)
        
        self.round_result = tk.StringVar(value = "Round Winning Result")
        self.round_result_label = ttk.Label(self.result_frame, textvariable=self.round_result, font=("Arial", 16, "bold"))
        self.round_result_label.grid(column=0, row=0)
        
        self.add_padding(self.result_frame)
        
        
        
        # player scoreboard frame
        self.player_score_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.player_score_frame.grid(column=0, row=3)
        
        self.player_score = tk.StringVar(value="##") # hashtag set as place holder for now
        self.player_score_text = ttk.Label(self.player_score_frame, text="Player Score:", font=("Arial", 14, "bold"))
        self.player_score_text.grid(column=0, row=0, sticky=tk.E)
        
        self.player_score_label = ttk.Label(self.player_score_frame, textvariable=self.player_score, font=("Arial", 14, "bold"))
        self.player_score_label.grid(column=1, row=0, sticky=tk.W)
        
        self.add_padding(self.player_score_frame)

        
        
        # house scoreboard frame
        self.house_score_frame = ttk.Frame(self, padding="10 10 10 10", borderwidth=2, relief="solid")
        self.house_score_frame.grid(column=2, row=3)
        
        self.house_score = tk.StringVar(value="##") # hashtag set as place holder for now
        self.house_score_text = ttk.Label(self.house_score_frame, text="House Score:", font=("Arial", 14, "bold"))
        self.house_score_text.grid(column=0, row=0, sticky=tk.E)
        
        self.house_score_label = ttk.Label(self.house_score_frame, textvariable=self.house_score, font=("Arial", 14, "bold"))
        self.house_score_label.grid(column=1, row=0, sticky=tk.W)
        
        self.add_padding(self.house_score_frame)
        
        
        
        # need to create a total rounds played frame to track overall rounds played 
        
        
        # need to create a button frame with one button to roll die (this is the action button)
            # will need to implement callback function to run game logic
        
        
        # need to create rules frame with label to state the rules of the game 
        
        
        
        
            
        
        
        
    # Created method to add padding to all componenets within the frame (still need to work on the padding)
    def add_padding(self, frame):
        for child in frame.winfo_children():
            child.grid_configure(padx=10, pady=10)
       


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Dice Duel Game")
    DiceDuelFrame(root)
    root.mainloop()


	
import random


class DiceDuelGame:
    def __init__(self):
        self.player_score = 0
        self.house_score = 0
        self.rounds_played = 0
        self.winning_score = 10

    def roll_die(self):
        return random.randint(1, 6)

    def play_round(self):
        player_roll = self.roll_die()
        house_roll = self.roll_die()

        result = ""

        if player_roll > house_roll:
            self.player_score += 1
            result = "Player wins the round"
        elif house_roll > player_roll:
            self.house_score += 1
            result = "House wins the round"
        else:
            result = "Tie - no points"

        self.rounds_played += 1

        return {
            "player_roll": player_roll,
            "house_roll": house_roll,
            "result": result,
            "player_score": self.player_score,
            "house_score": self.house_score,
            "rounds_played": self.rounds_played
        }

    def check_winner(self):
        if self.player_score >= self.winning_score:
            return "Player"
        elif self.house_score >= self.winning_score:
            return "House"
        return None

    def reset_game(self):
        self.player_score = 0
        self.house_score = 0
        self.rounds_played = 0






if __name__ == "__main__":
    game = DiceDuelGame()

    while True:
        input("Press Enter to roll...")

        data = game.play_round()

        print(f"Player rolled: {data['player_roll']}")
        print(f"House rolled: {data['house_roll']}")
        print(data["result"])
        print(f"Score -> Player: {data['player_score']} | House: {data['house_score']}")
        print("-" * 30)

        winner = game.check_winner()
        if winner:
            print(f"{winner} wins the game!")
            break

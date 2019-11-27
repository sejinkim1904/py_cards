class Turn:
    def __init__(self, guess, card):
        self.guess = guess
        self.card = card

    def correct(self):
        return self.guess == self.card.answer

    def feedback(self):
        if self.correct():
            return "Correct!"
        else:
            return "Incorrect!"

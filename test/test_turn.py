from lib.turn import Turn
from lib.card import Card

class TestTurn:
    card = Card("What is the capital of Alaska?", "Juneau", "Geography")
    turn = Turn("Juneau", card)

    def test_attributes(self):
        assert self.turn.card == self.card
        assert self.turn.guess == "Juneau"

    def test_correct_guess(self):
        turn = Turn("Denver", self.card)

        assert self.turn.correct() == True
        assert turn.correct() == False

    def test_feedback(self):
        turn = Turn("Denver", self.card)

        assert self.turn.feedback() == "Correct!"
        assert turn.feedback() == "Incorrect!"

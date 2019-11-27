from lib.turn import Turn
from lib.card import Card
from lib.deck import Deck
from lib.round import Round

class TestRound:
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)
    round = Round(deck)

    def test_attributes(self):
        assert self.round.deck == self.deck
        assert self.round.turns == []

    def test_current_card(self):
        assert self.round.current_card() == self.card_1

    def test_take_turn(self):
        turn_1 = self.round.take_turn("Juneau")

        assert turn_1.card == self.card_1
        assert turn_1.guess == "Juneau"
        assert turn_1.correct() == True
        assert self.round.turns == [turn_1]
        assert self.round.number_correct == 1
        assert self.round.current_card() == self.card_2

        turn_2 = self.round.take_turn("Venus")

        assert len(self.round.turns) == 2
        assert self.round.turns[-1].feedback() == "Incorrect!"
        assert self.round.number_correct == 1
        assert self.round.current_card() == self.card_3

    def test_number_correct_by_category(self):
        assert self.round.number_correct_by_category("Geography") == 1
        assert self.round.number_correct_by_category("STEM") == 0

    def test_percent_correct(self):
        assert self.round.percent_correct() == 50.0

    def test_percent_correct_by_category(self):
        assert self.round.percent_correct_by_category("Geography") == 100.0

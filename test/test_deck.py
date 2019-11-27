from lib.turn import Turn
from lib.card import Card
from lib.deck import Deck

class TestDeck:
    card_1 = Card("What is the capital of Alaska?", "Juneau", "Geography")
    card_2 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", "STEM")
    card_3 = Card("Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west", "STEM")
    cards = [card_1, card_2, card_3]
    deck = Deck(cards)

    def test_attributes(self):
        assert self.deck.cards == self.cards

    def test_deck_count(self):
        assert self.deck.count() == 3

    def test_cards_in_category(self):
        assert self.deck.cards_in_category("STEM") == [self.card_2, self.card_3]
        assert self.deck.cards_in_category("Geography") == [self.card_1]
        assert self.deck.cards_in_category("Pop Culture") == []

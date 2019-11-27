from lib.card import Card

class TestCard:
    def test_attributes(self):
        card = Card("What is the capital of Alaska?", "Juneau", "Geography")

        assert card.question == 'What is the capital of Alaska?'
        assert card.answer == 'Juneau'
        assert card.category == 'Geography'

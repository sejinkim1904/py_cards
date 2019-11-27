from lib.turn import Turn

class Round:
    def __init__(self, deck):
        self.deck = deck
        self.turns = []
        self.number_correct = 0

    def current_card(self):
        return self.deck.cards[0]

    def take_turn(self, guess):
        turn = Turn(guess, self.current_card())

        self.turns.append(turn)
        self.deck.cards.pop(0)

        if turn.correct():
            self.number_correct += 1

        return turn

    def number_correct_by_category(self, category):
        number_correct = 0

        for turn in self.turns:
            if turn.card.category == category and turn.correct():
                number_correct += 1

            return number_correct

    def percent_correct(self):
        return (self.number_correct / len(self.turns)) * 100

    def percent_correct_by_category(self, category):
        turns = 0

        for turn in self.turns:
            if turn.card.category == category:
                turns += 1

        return (self.number_correct_by_category(category) / turns) * 100

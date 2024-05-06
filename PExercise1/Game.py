import random


class NumberGuesser:

    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        self.attempts.append(number)
        number = int(number)
        if number == self.secret_number:
            return f'You won after {len(self.attempts)} attempts'
        elif number > self.secret_number:
            return 'Lower'
        elif number < self.secret_number:
            return 'Higher'

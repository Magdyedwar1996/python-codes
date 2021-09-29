import random as rnd
suits = ['hearts', 'clubs', 'spades', 'diamonds']
ranks = [str(r) for r in range(2, 11)]
ranks.extend(list('AKQJ'))
suit = rnd.choice(suits)
rank = rnd.choice(ranks)
card = f'{rank} of {suit}'

def draw_card():
    suit = rnd.choice(suits)
    rank = rnd.choice(ranks)
    card = f'{rank} of {suit}'
    return card
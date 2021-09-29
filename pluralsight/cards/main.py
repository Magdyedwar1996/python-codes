from card import draw_card

def draw_hand(num_cards):
    hand = [draw_card() for i in range(num_cards)]
    return hand

if __name__ == '__main__':
    poker_hand = draw_hand(5)
    print(poker_hand)
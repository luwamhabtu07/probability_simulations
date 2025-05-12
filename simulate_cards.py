import random
import matplotlib.pyplot as plt

def simulate_drawing_cards(n=20):
    deck = ['Red'] * 26 + ['Black'] * 26
    random.shuffle(deck)
    draws = random.sample(deck, n)
    red_count = draws.count('Red')
    black_count = n - red_count

    print(f"Red cards drawn: {red_count}")
    print(f"Black cards drawn: {black_count}")

    plt.bar(['Red', 'Black'], [red_count, black_count])
    plt.title("20 Cards Drawn from Deck")
    plt.ylabel("Count")
    plt.savefig("card_draw_plot.png")
    plt.show()

    return {'Red': red_count, 'Black': black_count}

if __name__ == "__main__":
    result = simulate_drawing_cards()
    print("\nResult:", result)

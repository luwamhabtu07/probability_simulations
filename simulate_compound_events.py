import random
import matplotlib.pyplot as plt

def simulate_two_coin_flips(n=50):
    both_heads = 0
    at_least_one_head = 0

    for _ in range(n):
        toss1 = random.choice(['H', 'T'])
        toss2 = random.choice(['H', 'T'])
        if toss1 == 'H' and toss2 == 'H':
            both_heads += 1
        if toss1 == 'H' or toss2 == 'H':
            at_least_one_head += 1

    print(f"Both Heads: {both_heads} times")
    print(f"At least One Head: {at_least_one_head} times")

    plt.bar(['Both Heads', 'At Least One Head'], [both_heads, at_least_one_head])
    plt.title("50 Two-Coin Flips")
    plt.ylabel("Frequency")
    plt.savefig("compound_events_plot.png")
    plt.show()

    return {'Both Heads': both_heads, 'At Least One Head': at_least_one_head}

if __name__ == "__main__":
    result = simulate_two_coin_flips()
    print("\nResult:", result)

import random
import matplotlib.pyplot as plt

def simulate_coin_tosses(n=100):
    results = {'Heads': 0, 'Tails': 0}
    for _ in range(n):
        toss = random.choice(['Heads', 'Tails'])
        results[toss] += 1

    print(f"Heads: {results['Heads']} times")
    print(f"Tails: {results['Tails']} times")

    plt.bar(results.keys(), results.values())
    plt.title("100 Coin Tosses")
    plt.ylabel("Count")
    plt.savefig("coin_toss_plot.png")
    plt.show()

    return results

if __name__ == "__main__":
    result = simulate_coin_tosses()
    print("\nResult:", result)

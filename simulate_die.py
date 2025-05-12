import random
import matplotlib.pyplot as plt

def simulate_die_rolls(n=60):
    outcomes = [0] * 6
    for _ in range(n):
        roll = random.randint(1, 6)
        outcomes[roll - 1] += 1

    for i in range(6):
        print(f"Face {i+1}: {outcomes[i]} times")

    plt.bar(range(1, 7), outcomes)
    plt.title("60 Die Rolls")
    plt.xlabel("Die Face")
    plt.ylabel("Frequency")
    plt.savefig("die_roll_plot.png")
    plt.show()

    return outcomes

if __name__ == "__main__":
    result = simulate_die_rolls()
    print("\nResult List:", result)

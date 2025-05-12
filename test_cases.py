from simulate_coin import simulate_coin_tosses
from simulate_die import simulate_die_rolls
from simulate_cards import simulate_drawing_cards
from simulate_compound_events import simulate_two_coin_flips

def run_all_tests():
    print("==== Test 1: Coin Tosses ====")
    result1 = simulate_coin_tosses(10)  # edge case
    result2 = simulate_coin_tosses(100) # normal
    print("Result (10):", result1)
    print("Result (100):", result2)

    print("\n==== Test 2: Die Rolls ====")
    result3 = simulate_die_rolls(6)    # edge: one of each face
    result4 = simulate_die_rolls(60)   # normal
    print("Result (6):", result3)
    print("Result (60):", result4)

    print("\n==== Test 3: Card Drawing ====")
    result5 = simulate_drawing_cards(2)    # edge
    result6 = simulate_drawing_cards(20)   # normal
    print("Result (2):", result5)
    print("Result (20):", result6)

    print("\n==== Test 4: Two-Coin Flips ====")
    result7 = simulate_two_coin_flips(2)   # edge
    result8 = simulate_two_coin_flips(50)  # normal
    print("Result (2):", result7)
    print("Result (50):", result8)

if __name__ == "__main__":
    run_all_tests()

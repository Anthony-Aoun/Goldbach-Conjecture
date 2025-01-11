import matplotlib.pyplot as plt
import numpy as np

def is_prime(x):
    """
    Check if a number is prime.
    Args:
        x (int): Number to check for primality.
    Returns:
        bool: True if prime, False otherwise.
    """
    if x < 2:
        return False
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def verify_goldbach(n):
    """
    Verify Goldbach's conjecture for a given even number.
    Args:
        n (int): Even integer > 2.
    Returns:
        bool: True if the conjecture holds, False otherwise.
    """
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            return True
    return False

def goldbach_combinations(n):
    """
    Count the number of prime pairs whose sum equals n.
    Args:
        n (int): Even integer > 2.
    Returns:
        int: Number of prime pairs.
    """
    count = 0
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            count += 1
    return count

def plot_goldbach_combinations(max_n):
    """
    Plot the number of Goldbach prime pairs for even numbers up to max_n.
    Args:
        max_n (int): Maximum even number to evaluate.
    """
    x = list(range(4, max_n + 1, 2))
    y = [goldbach_combinations(n) for n in x]

    plt.scatter(x, y)
    plt.xlabel('Even Number')
    plt.ylabel('Number of Prime Pairs')
    plt.title("Goldbach's Conjecture: Number of Prime Pairs")
    plt.grid(True)
    plt.show()

def plot_prime_gaps(max_n):
    """
    Plot prime numbers and their gaps up to max_n.
    Args:
        max_n (int): Maximum number to search for primes.
    """
    primes = []
    gaps = []
    prev_prime = None

    for n in range(2, max_n + 1):
        if is_prime(n):
            if prev_prime is not None:
                gaps.append(n - prev_prime)
            else:
                gaps.append(0)
            primes.append(n)
            prev_prime = n

    plt.plot(primes, gaps, marker='o', linestyle='-')
    plt.xlabel('Prime Numbers')
    plt.ylabel('Gap to Previous Prime')
    plt.title('Gaps Between Consecutive Prime Numbers')
    plt.grid(True)
    plt.show()

def goldbach_menu():
    """
    Menu-driven program to explore Goldbach's conjecture.
    """
    print("(1): Show prime pairs and their count for an even number > 2.")
    print("(2): Show counts of Goldbach combinations for even numbers up to a limit.")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        n = int(input("Enter an even number > 2: "))
        while n <= 2 or n % 2 != 0:
            print("Invalid input! Please enter an even number greater than 2.")
            n = int(input("Enter an even number > 2: "))
        print(f"Prime pairs that sum to {n}:")
        count = 0
        for i in range(2, n // 2 + 1):
            if is_prime(i) and is_prime(n - i):
                print(f"{i} + {n - i} = {n}")
                count += 1
        print(f"Total combinations: {count}")

    elif choice == 2:
        max_n = int(input("Enter the maximum even number (>2): "))
        while max_n <= 2 or max_n % 2 != 0:
            print("Invalid input! Please enter an even number greater than 2.")
            max_n = int(input("Enter the maximum even number (>2): "))
        for n in range(4, max_n + 1, 2):
            count = goldbach_combinations(n)
            print(f"Number of combinations for {n}: {count}")
            print('*' * count)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    goldbach_menu()
    # Uncomment below to visualize plots
    # plot_goldbach_combinations(2000)
    # plot_prime_gaps(10000)

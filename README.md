# Goldbach's Conjecture Exploration

## Description

This Python program explores **Goldbach's Conjecture**, which states that every even integer greater than 2 can be expressed as the sum of two prime numbers. The program provides:

- Verification of Goldbach's conjecture for a given even number.
- Counting and displaying all prime pairs that sum to an even number.
- Visualization of the number of prime pairs for even numbers up to a specified limit.
- Visualization of prime numbers and the gaps between consecutive primes.

## Requirements

- Python 3.x
- Libraries:
  - `matplotlib`
  - `numpy`

Install the required libraries using:
```bash
pip install matplotlib numpy
```

## Usage

Run the program using:
```bash
python goldbach_conjecture.py
```

### Menu Options

1. **Prime Pairs for a Given Even Number**
   - Input an even number > 2.
   - The program will display all pairs of prime numbers that sum to the given number and count how many such pairs exist.

2. **Prime Pair Counts for Even Numbers in a Range**
   - Input a maximum even number (>2).
   - The program will show the number of Goldbach combinations for every even number from 4 up to the input number.
   
### Visualization (Optional)

To visualize data, uncomment the relevant function calls at the end of the script:
```python
# plot_goldbach_combinations(2000)  # Plots Goldbach pairs up to 2000
# plot_prime_gaps(10000)            # Plots prime gaps up to 10000
```

## Functions Documentation

### 1. `is_prime(x)`
**Purpose:** Checks if a number `x` is prime.

**Args:**
- `x` (int): Number to check.

**Returns:**
- `True` if `x` is prime.
- `False` otherwise.

### 2. `verify_goldbach(n)`
**Purpose:** Verifies if the Goldbach conjecture holds for the even number `n`.

**Args:**
- `n` (int): Even number (>2).

**Returns:**
- `True` if there exists at least one pair of primes summing to `n`.
- `False` otherwise.

### 3. `goldbach_combinations(n)`
**Purpose:** Counts the number of unique prime pairs that sum up to `n`.

**Args:**
- `n` (int): Even number (>2).

**Returns:**
- `int`: Number of valid prime pairs.

### 4. `plot_goldbach_combinations(max_n)`
**Purpose:** Plots the number of prime pairs for all even numbers up to `max_n`.

**Args:**
- `max_n` (int): Maximum even number for analysis.

**Visualization:**
- Scatter plot showing the relationship between even numbers and their prime pair counts.

### 5. `plot_prime_gaps(max_n)`
**Purpose:** Plots consecutive prime numbers and their gaps up to `max_n`.

**Args:**
- `max_n` (int): Upper limit for prime generation.

**Visualization:**
- Line plot of primes vs. the gap to the previous prime.

### 6. `goldbach_menu()`
**Purpose:** Provides a menu-driven interface for user interaction.

**Usage:**
- Guides the user to explore Goldbach's conjecture with options for detailed results and visualization.

## Example

1. **Check Goldbach pairs for 28:**
```
Enter your choice (1 or 2): 1
Enter an even number > 2: 28

Prime pairs that sum to 28:
5 + 23 = 28
11 + 17 = 28
Total combinations: 2
```

2. **Goldbach counts up to 20:**
```
Enter your choice (1 or 2): 2
Enter the maximum even number (>2): 20

Number of combinations for 4: 1
*
Number of combinations for 6: 1
*
Number of combinations for 8: 1
*
...
Number of combinations for 20: 2
**
```

## License
This project is licensed under the MIT License.

## Author
© 2024 [Anthony Aoun](https://github.com/Anthony-Aoun). All rights reserved.

This project is open-source and free to use for educational purpouses only.




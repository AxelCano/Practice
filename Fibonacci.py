#Fibonacci series
"""
The goal is to replicate the fibonacci series.
In mathematics, the Fibonacci sequence is a sequence
in which each number is the sum of the two preceding ones.
"""
def fibonacci(n):
    fib_series = [0, 1]  # Initialize Fibonacci series with first two terms
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])  # Add the last two terms to get the next term
    return fib_series[:n]

# Example usage:
num_terms = 10  # Change this to generate Fibonacci series up to a different number of terms
fib_result = fibonacci(num_terms)
print("Fibonacci series up to", num_terms, "terms:", fib_result)

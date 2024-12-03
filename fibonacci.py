def fibonacci(n):
    """Fibonacci Sequence."""
    sequence = [0, 1]
    for i in range(2, n):
        next = sequence[-1] + sequence[-2]
        sequence.append(next)
    return sequence[:n]

# Printing sequence
n = int(input("Enter a leght of sequence: "))
print(fibonacci(n))
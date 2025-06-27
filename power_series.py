# Power series
def power_series_sum(x, terms=10):
    total = 0
    for n in range(terms):
        total += x ** n
    return total

# Example use
x = 0.5  # Try values between -1 and 1
terms = 20  # Number of terms to include in the sum

result = power_series_sum(x, terms)
print(f"Power series sum for x = {x} with {terms} terms: {result}")

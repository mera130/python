# Power series
def power_series_sum(x, terms=10):
    total = 0
    for n in range(terms):
        total += x ** n
    return total

# Example use
x = 0.5  
terms = 20  

result = power_series_sum(x, terms)
print(f"Power series sum for x = {x} with {terms} terms: {result}")

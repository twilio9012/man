class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Total value accumulated

    for item in items:
        if capacity > 0:
            if item.weight <= capacity:
                # If the item can fit in the knapsack, take it all
                capacity -= item.weight
                total_value += item.value
                print(f"Including full item with value {item.value} and weight {item.weight}")
            else:
                # Take the fraction of the remaining capacity
                fraction = capacity / item.weight
                total_value += item.value * fraction
                print(f"Including {fraction:.4f} of item with value {item.value} and weight {item.weight}")
                capacity = 0  # Knapsack is now full

    return total_value

# Example usage
if __name__ == "__main__":
    # Define the items with their values and weights
    items = [Item(60, 10), Item(100, 20), Item(120, 30)]
    capacity = 50  # Maximum capacity of the knapsack

    max_value = fractional_knapsack(capacity, items)

    print(f"Maximum value in the knapsack: {max_value:.2f}")

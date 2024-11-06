def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value that can be obtained
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the dp array
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                # Include the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude the item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Main function to get user input
if __name__ == "__main__":
    # Get the number of items from the user
    n = int(input("Enter the number of items: "))
    values = []
    weights = []

    # Get the values and weights for each item
    for i in range(n):
        value = int(input(f"Enter value for item {i + 1}: "))
        weight = int(input(f"Enter weight for item {i + 1}: "))
        values.append(value)
        weights.append(weight)

    # Get the capacity of the knapsack
    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value = knapsack(values, weights, capacity)

    print(f"Maximum value in the knapsack: {max_value}")

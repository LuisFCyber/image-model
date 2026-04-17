def calculate_statistics(numbers):
    """Compute total, average, maximum, and minimum values for a list of numbers."""
    if not numbers:
        raise ValueError("The list of numbers must not be empty.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


def main():
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(values)

    print("Total:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)


if __name__ == "__main__":
    main()
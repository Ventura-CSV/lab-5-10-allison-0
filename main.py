import random


def foldandswap(numbers):
    # Get length of the list
    lenlist = len(numbers)

    # Iterate through first half of the list
    for i in range(lenlist // 2):
        # Swap the element at index i with its opposite element
        numbers[i], numbers[lenlist - i - 1] = numbers[lenlist - i - 1], numbers[i]


def main():
    numbers = [2, 3, 0, 5, 4, 1, 6, 9, 8, 7]
    print(numbers)
    foldandswap(numbers)
    print(numbers)

    numbers = [random.randint(0, 10) for i in range(10)]
    print(numbers)
    foldandswap(numbers)
    print(numbers)


if __name__ == '__main__':
    main()

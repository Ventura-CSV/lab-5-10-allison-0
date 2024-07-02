import random


def foldandswap(numbers):
    # Get length of the list
    lenlist = len(numbers)

    # Iterate through first half of the list
    for i in range(lenlist // 2):


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


def sameBirthdayProbability(n):
    """Returns the probability that n people have the same birthday."""
    probability = 1.0
    for i in range(n):
        probability = probability * (365 - i) / 365
    probability = round(probability, 10)
    return 1 - probability


def main():
    print(sameBirthdayProbability(100))


if __name__ == '__main__':
    main()

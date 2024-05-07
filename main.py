import random

def average(numbers):

    numbersSum = 0

    if len(numbers) == 0:
        return None
    else:
        for element in numbers:
            numbersSum = numbersSum + element

    return numbersSum/len(numbers)




assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0

random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    # Shuffle the list
    random.shuffle(testData)
    # The average is independent by the order of the data
    assert average(testData) == 2
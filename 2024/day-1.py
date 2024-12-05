PATH = "2024/resources/day-1/dataset.txt"
# PATH = "2024/resources/day-1/dataset-test.txt"

def compareDistanceLists(array1, array2):
    sum = 0
    array1.sort()
    array2.sort()
    for i, elem in enumerate(array1):
        diff = abs(elem - array2[i])
        print(i, elem, array2[i], diff)
        sum += diff
    return sum


def loadData(path):
    with open(path, "r") as file:
        cols = [
            list(col)
            for col in zip(*(line.split() for line in file.read().splitlines()))
        ]
        return [
            [int(x) for x in cols[0]],
            [int(x) for x in cols[1]]
        ]


def init():
    columns = loadData(PATH)
    sum = compareDistanceLists(columns[0], columns[1])
    print("the sum is: ", sum)


init()

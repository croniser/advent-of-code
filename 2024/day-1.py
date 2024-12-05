PATH = "2024/resources/day-1/dataset.txt"
# PATH = "2024/resources/day-1/dataset-test.txt"
DEBUG = False

def compare_distance_lists(array1: list[int], array2: list[int]) -> int:
    aggregate = 0
    array1.sort()
    array2.sort()
    for i, elem in enumerate(array1):
        delta = abs(elem - array2[i])
        if DEBUG: print(i, elem, array2[i], diff)
        aggregate += delta
    return aggregate


def load_data(path):
    with open(path, "r") as file:
        cols = [
            list(col)
            for col in zip(*(line.split() for line in file.read().splitlines()))
        ]
        return [
            [int(x) for x in cols[0]],
            [int(x) for x in cols[1]]
        ]


def main() -> int:
    columns = load_data(PATH)
    return compare_distance_lists(columns[0], columns[1])


print("The answer is: ", main())

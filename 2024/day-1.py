locationArray1 = [3,4,2,1,3,3]
locationArray2 = [4,3,5,3,9,3]

def compareDistanceLists(array1, array2):
    sum = 0
    array1.sort()
    array2.sort()
    for i, elem in enumerate(array1):
        diff = abs(elem - array2[i])
        print(i, elem, array2[i], diff)
        sum += diff
    return sum

print("The sum of differences is: ", compareDistanceLists(locationArray1, locationArray2));
# https://adventofcode.com/2024/day/1/input
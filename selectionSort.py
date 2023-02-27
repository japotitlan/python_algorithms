values = [4,6,0,8,5,2,9,1,7,3]

def selectionSort(values):
    valuesLength = len(values)

    for position in range(valuesLength):
        minValueIndex = position

        for newPosition in range(minValueIndex + 1,valuesLength):
            if values[newPosition] < values[minValueIndex]:
                minValueIndex = newPosition
            
        tempValue = values[position]

        values[position] = values[minValueIndex]
        values[minValueIndex] = tempValue
    
    return values

print(selectionSort(values))
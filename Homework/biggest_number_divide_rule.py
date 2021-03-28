def divide_rule(array):
    middle=len(array)//2
    lhalf=max(array[:middle])
    rhalf=max(array[middle:])
    if lhalf>rhalf:
        return lhalf
    else:
        return rhalf

array=[1,9,10,2,3,4,5,6,7]
print(divide_rule(array))
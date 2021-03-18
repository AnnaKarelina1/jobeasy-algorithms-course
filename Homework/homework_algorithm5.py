# When given a list, the program should return a list of all the elements that are below the arithmetical mean
# of the original list.  The arithmetical mean is the sum of all elements divided by the number of elements.


def under_mean_list(old_list):
    mean_num = 0
    new_list = []
    sum_old_list = 0
    x = 0
    while x < len(old_list):
        for element in old_list:
            sum_old_list += element
            x += 1
        mean_num = sum_old_list/(len(old_list))
        print(mean_num)
    for item in old_list:
        if item <= mean_num:
            new_list.append(item)
    return new_list

# When given a list of elements find the two lowest elements. They can be equal to each other or different.

def lowest_element_list(numbers):
    low_1=numbers[0]
    low_2=numbers[0]
    for element in range(len(numbers)):
        if numbers[element]<low_1:
            low_1=numbers[element]
        if numbers[element]>low_1  and numbers[element]<low_2:
                low_2=numbers[element]
        if numbers.count(low_1)>1:
            low_2=low_1
    return low_1, low_2

list_number=[2,1,3,4,-1,0,5,-9,-9,-4]

print(lowest_element_list(list_number))
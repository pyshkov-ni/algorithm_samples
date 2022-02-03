def simple_search(list, item):
    # low and high keep track of which part of the list you'll search in.
    item = int(item)
    low = 0
    high = len(list) - 1

    # Until you reach the end of the list...
    while low <= high:
        # ... check the low element
        guess = list[low]
        # Found the item and stop.
        if guess == item:
            return print("It is", low + 1)
            break
        # The guess was too low.
        else:
            low += 1
    # Item doesn't exist
    return None


my_list = range(1, 101)

print(simple_search(my_list, input('Введите число\n')))

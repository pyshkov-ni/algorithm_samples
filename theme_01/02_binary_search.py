def binary_search(list, item):
    # low and high keep track of which part of the list you'll search in.
    item = int(item)
    low = 0
    high = len(list) - 1

    # While you haven't narrowed it down to one element ...
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = list[mid]
        # Found the item.
        if guess == item:
            return print("Position is", mid + 1)
        # The guess was too high.
        if guess > item:
            high = mid - 1
        # The guess was too low.
        else:
            low = mid + 1

    # Item doesn't exist
    return None


my_list = range(1, 101)

print(binary_search(my_list, input('Введите число\n')))

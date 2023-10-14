numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

empty_item_index = 4
sum_before_empty_item = sum(numbers[:empty_item_index])
sum_after_empty_item = sum(numbers[empty_item_index + 1:])
numbers_length = len(numbers)

arithmetic_mean = (sum_before_empty_item + sum_after_empty_item) / numbers_length
numbers[empty_item_index] = arithmetic_mean

print("Измененный список:", numbers)
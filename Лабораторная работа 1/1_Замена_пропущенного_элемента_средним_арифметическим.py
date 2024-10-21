numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
missing_value = numbers.index(None)
sum_of_values = sum(num for num in numbers if num is not None)
count_of_numbers = len(numbers)
average_value = sum_of_values/count_of_numbers
numbers[missing_value] = average_value
print("Измененный список:", numbers)

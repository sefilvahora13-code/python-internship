numbers = [10, 50, 30, 90, 70, 90, 40]

largest = None
second_largest = None

for num in numbers:

    if largest is None or num > largest:
        second_largest = largest
        largest = num

    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

print("Largest Number:", largest)
print("Second Largest Number:", second_largest)

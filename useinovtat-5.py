def high_and_low(line_of_numbers):
    numbers = []
    pointer_1, pointer_2 = 0, 0
    for i in range(len(line_of_numbers)):
        if line_of_numbers[i] == " ":
            numbers.append(int(line_of_numbers[pointer_1:pointer_2]))
            pointer_1 = i+1
        elif i == (len(line_of_numbers) - 1):
            numbers.append(int(line_of_numbers[pointer_1:]))
        pointer_2 += 1

    return f"{max(numbers)} {min(numbers)}"

def left_shift(binary, positions):
    result = (binary << positions) & 0xFF
    print("Original binary :", format(binary, '08b'))

    for i in range(positions):
        binary = (binary << 1) & 0xFF
        print("After shift", i + 1, ":", format(binary, '08b'))

    print("Final result    :", format(result, '08b'))
    print()


def right_shift(binary, positions):
    print("Original binary :", format(binary, '08b'))

    for i in range(positions):
        binary = binary >> 1
        print("After shift", i + 1, ":", format(binary, '08b'))

    print("Final result    :", format(binary, '08b'))
    print()


print("a) Logical left shift of 10110110 by 2 positions")
left_shift(int('10110110', 2), 2)

print("b) Logical right shift of 11010100 by 2 positions")
right_shift(int('11010100', 2), 2)

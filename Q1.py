def binary_add(a, b):
    result = a + b

    # Convert operands to 8-bit binary
    bin_a = format(a & 0xFF, '08b')
    bin_b = format(b & 0xFF, '08b')
    bin_result = format(result & 0xFF, '08b')

    print("First operand :", bin_a)
    print("Second operand:", bin_b)
    print("Binary result :", bin_result)
    print("Decimal result:", result)

    # Check overflow
    if result < -128 or result > 127:
        print("Overflow: Yes")
    else:
        print("Overflow: No")

    print()


print("a) (25) + (+18)")
binary_add(25, 18)

print("b) (-25) + (-18)")
binary_add(-25, -18)

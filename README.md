# Python Programs: Binary Arithmetic and Bit Shifts

## 1. Signed Binary Arithmetic Using 8-bit 2's Complement

### Aim
To develop a Python program to perform signed binary addition using 8-bit 2's complement representation.

### Operations
- (25) + (+18)
- (-25) + (-18)

### Results

| Expression | Binary Result | Decimal Result | Overflow |
|---|---|---:|---|
| 25 + 18 | `00101011` | 43 | No |
| -25 + (-18) | `11010101` | -43 | No |

### Description
The program converts signed decimal numbers into 8-bit 2's complement binary format, performs addition, displays the binary and decimal results, and checks for arithmetic overflow.

## 2. Logical Left Shift and Right Shift

### Aim
To develop a Python program to perform logical left and right shifts on 8-bit binary numbers.

### Operations
- Left shift `10110110` by 2 positions.
- Right shift `11010100` by 2 positions.

### Results

**a) Logical Left Shift**

- Original number: `10110110`
- After first shift: `01101100`
- After second shift: `11011000`
- Final result: `11011000`

**b) Logical Right Shift**

- Original number: `11010100`
- After first shift: `01101010`
- After second shift: `00110101`
- Final result: `00110101`

### Description
The program shifts binary bits left or right by two positions. Zeros are added to the right during a logical left shift and to the left during a logical right shift. The final results are displayed in 8-bit binary format.

## Conclusion
Both Python programs successfully perform binary arithmetic and logical shift operations and display the required results.

def print_formatted(number):
    
    width = len(bin(number)) - 2  
    for i in range(1, number + 1):
        # Decimal representation (already an integer)
        decimal_str = str(i)

        # Octal representation (remove '0o' prefix)
        octal_str = oct(i)[2:]

        # Hexadecimal representation (remove '0x' prefix and capitalize)
        hex_str = hex(i)[2:].upper()

        # Binary representation (remove '0b' prefix)
        binary_str = bin(i)[2:]

        # Each value is padded to 'width' characters.
        print(f"{decimal_str.rjust(width)} {octal_str.rjust(width)} {hex_str.rjust(width)} {binary_str.rjust(width)}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

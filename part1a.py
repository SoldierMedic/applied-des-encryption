import math

# Array to hold the 16 keys
round_keys = [''] * 16

# String to hold the plain text
pt = ""

# Function to convert a number in decimal to binary
def convertDecimalToBinary(decimal):
    binary = ""
    while decimal != 0:
        binary = ("1" if decimal % 2 != 0 else "0") + binary
        decimal //= 2
    while len(binary) < 4:
        binary = "0" + binary
    return binary

# Function to convert a number in binary to decimal
def convertBinaryToDecimal(binary):
    decimal = 0
    counter = 0
    size = len(binary)
    for i in range(size-1, -1, -1):
        if binary[i] == "1":
            decimal += int(math.pow(2, counter))
        counter += 1
    return decimal

# Function to compute xor between two strings
def Xor(a, b):
    result = ""
    size = len(b)
    for i in range(size):
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result

# Function to do a circular left shift by 1
def shift_left_once(key_chunk):
    shifted = key_chunk[1:] + key_chunk[0]
    return shifted

# Function to do a circular left shift by 2
def shift_left_twice(key_chunk):
    shifted = key_chunk
    for i in range(2):
        shifted = shifted[1:] + shifted[0]
    return shifted

#Function to generate the 16 keys
def generate_keys(key):
    # PC-1 permutation
    pc1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4,
    ]   
    # PC-2 permutation
    pc2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32,
    ]
    # 1. Compressing the key using the PC1 table
    perm_key = ''
    for i in range(56):
        perm_key += key[pc1[i]-1]

    # 2. Dividing the result into two equal halves
    left = perm_key[:28]
    right = perm_key[28:]

    # Generating 16 keys
    for i in range(16):
        # 3.1. For rounds 1, 2, 9, 16 the key_chunks are shifted by one.
        if i == 0 or i == 1 or i == 8 or i == 15:
            left = shift_left_once(left)
            right = shift_left_once(right)
        # 3.2. For other rounds, the key_chunks are shifted by two.
        else:
            left = shift_left_twice(left)
            right = shift_left_twice(right)

        # 4. The chunks are combined
        combined_key = left + right
        round_key = ''
        # 5. Finally, the PC2 table is used to transpose the key bits
        for j in range(48):
            round_key += combined_key[pc2[j]-1]
        round_keys[i] = round_key
        print("Key {}: {}".format(i+1, round_keys[i]))

def main():
    key = "1010101010111011000010010001100000100111001101101100110011011101"
    generate_keys(key)
  



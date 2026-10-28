def xor_divide(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i + j] = "0" if rem[i + j] == divisor[j] else "1"
    return "".join(rem[-(len(divisor) - 1):])

data = input("Enter data bits: ")
divisor = input("Enter divisor bits: ")

# Sender side
padded = data + "0" * (len(divisor) - 1)
print("Dividend (after appending 0's):", padded)
crc = xor_divide(padded, divisor)
codeword = data + crc
print("CRC remainder:", crc)
print("Transmitted code:", codeword)

# Receiver side
received = input("Enter received code: ")
if "1" in xor_divide(received, divisor):
    print("Error detected")
else:
    print("No Error")

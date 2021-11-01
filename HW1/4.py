number = int(input())

reverse_decimal = 0
reverse_binary = ''

# to reverse binary
while number > 0:
    tmp = number // 2
    bin_tmp = number % 2
    number = tmp
    reverse_binary += str(bin_tmp)
# reverse_bin to decimal
binary = reverse_binary[::-1]
bin_len = len(binary)
bin_base = 1
for i in range(bin_len):
    if binary[i] == '1':
        reverse_decimal += bin_base
    bin_base *= 2

print(reverse_decimal)    

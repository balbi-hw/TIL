# 10진수 2진수로 변환 함수
# def decimal_to_binary(n):
#     binary_number = ""

#     while n > 0:
#         remain = n % 2

#         binary_number = str(remain) + binary_number

#         n = n // 2

#     return binary_number

# print(decimal_to_binary(int(input())))

# 2진수 > 10진수 변환 필요
# 16진수도

# 10진수 > 16진수
# 17은 16진수라고 가정
def decimal_to_hexadecimal(n):
    hex_digits = "0123456789ABCDEFG"
    hexadecimal_number = ""

    while n > 0:
        
        remain = n % 16
        hexadecimal_number = hex_digits[remain] + hexadecimal_number
        
        n //= 16

    return hexadecimal_number

print(decimal_to_hexadecimal(255))

'''
10 > 2
10 > 16

2 > 10
16 > 10
이 되면

2 > 16 도 가능
'''


import string

alphabet = string.ascii_lowercase

# abcdefghijklmnopqrstuvwxyz

print(len(alphabet))

# print(alphabet.index('h'))

def encode(word='hellocoders', step=9):
    result = ''
    for letter in word:
        new_num = alphabet.index(letter) + step
        if new_num >= len(alphabet):
            new_num = new_num % 26
        result += alphabet[new_num]
    return result

def decode(word='qnuuxlxmnab', step=9):
    result = ''
    for letter in word:
        new_num = alphabet.index(letter) - step
        if new_num <= 0:
            new_num = new_num % 26
        result += alphabet[new_num]
    return result


print(encode())
print(decode())

print(encode('hello', 56))
print(decode('lipps', 56))



























# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#             'w', 'x', 'y', 'z']

# # direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# # text = input("Type your message:\n").lower()
# # shift = int(input("Type the shift number:\n"))


# def caesar(direction, text, shift_amount):
#     answer = ''
#     for letter in text:
#         curr_index = alphabet.index(letter)
#         if direction == 'encode':
#             new_index = curr_index + shift_amount
#         elif direction == 'decode':
#             new_index = curr_index - shift_amount
#         if 0 > new_index or new_index > 25:
#             new_index = new_index % 26
#         answer += alphabet[new_index]

#     return answer


# print()
# print(caesar('encode', 'hello', 56))
# print(caesar('decode', 'lipps', 56))
# print()
# print(caesar('encode', 'hellocoders', 9))
# print(caesar('decode', 'qnuuxlxmnab', 9))

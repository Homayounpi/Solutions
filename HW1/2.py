text = input("Enter your text: ")

# 1 :
# vowels = ['a', 'e', 'i', 'o', 'u']
# new_text = ''
# for char in text:
#     if char == ' ':
#         continue
#     elif char.lower() in vowels:
#         new_text += '.'
#     elif char.isupper():
#         new_text += char.lower()
#     elif char.islower():
#         new_text += char.upper()
# print(new_text)

# 2 :
# with builtin functions :
for char in text.replace(" ", ""):
    print("." if char.lower() in ['a', 'e', 'i', 'o', 'u'] else char.swapcase(), end="")

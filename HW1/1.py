n = int(input("Enter your number: "))

# 1 :
print(*('*' * _ for _ in range(1, n)), sep="\n")
print(*('*' * _ for _ in range(n, 0, -1)), sep="\n")

# 2 :
# print("\n".join("*" * _ for _ in range(1, n + 1)))
# print("\n".join("*" * _ for _ in range(n - 1, 0, -1)))

# 3 :
# for _ in range(1, n + 1):
#     print("*" * _)
# for _ in range(n - 1, 0, -1):
#     print("*" * _)

# a = []
# l = int(input())
# h = int(input())

# for i in range(l):
#     a += [input().split()]

# for i in range(h):
#     for b in range(l-1, 0, -1):
#         print(a[b][i], end=' ')
#     print(a[0][i])

a_string = "1 2 3"
print(a_string)
splited = a_string.split()
print(splited)
print(list(map(int, splited)))
print('---'.ljust(23, 'w'))

print(pow(10, 4, 2))
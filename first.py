import keyword

print("Hello")

print((2 + 1) * 2)

print(5 / 2)  # 2.5
print(5 // 2)  # 2 - integer division

print(3 % 2)  # returns the reminder 1
print("hello")  # okay

print((100 - 5 ** 3) / 5)  # -5
print(2 ** 2 + 9 // 2)  # 8

# all rational numbers expressed as fractions can be represented as float

print(type(6.9))  # float
print(int(6.999999999))  # type casting 6

print(2j / 2j)

y = 10
y -= 5.0
print(type(y))

x = 14
x += 1
print((x / 5) ** 2)

print(keyword.kwlist)
a, b = 1, 2
print(b // a)
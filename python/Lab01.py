# 2
print('# 2')
name = '수지'
weight = 56
age = 23

# 3
print('# 3')
x = 3
y = 5
z = 7
print(3*x)
print(3*x + y)
print((x+y)/7)
print((3*x + y)/(z+2))

# 4
print('# 4')
x, y = 4, 8
print(x, y)
x *= y
print(x, y)
x -= y
print(x, y)

# 5
print('# 5')
x = 3
print(x+7 == 10)

# 6
print('# 6')
a = (-32+95)*12/3
b = (3*4-((-27+67)/4))**8
c = (512+1968-432)/2**4+128
d = 256 == 2**8
e = 50 + 50 <= 10*10
f = 99 != 10**2-1
print(a, b, c, d, e, f)

# 7
print('# 7')
x = 2.5
y = -1.5
m = 18
n = 4
a = x + n * y - (x + n) * y
b = m/n + m%n
c = 5*x-n/5
d = 1-(1-(1-(1-(1-n))))
print(a, b, c, d)

# 8
print('# 8')
roomA = 2.5 * 3 / 27
roomB = 4 * 2 / 30
if roomA > roomB:
    print('A')
elif roomA == roomB:
    print('똑같')
else:
    print('B')

# 9
print('# 9')
b = True or False and 3 < 4 or not (5==7)
c = True or (3<5 and 6>=2)
d = 'B' > 'A'
# e = 7%4 + 3 -2 / 6 * int('Z')
# f = int('D') + 1 + int('M') %2/3
g = 5.0/3 +3/3
h = 53 % 21 < 45 /18
i = (4<6) or True and False or False and(2>3)
j = 7-(3+8*6+3) - (2 + 5*2)
k = True and False
print(b, c, d, f, e, g, h, i, j, k)

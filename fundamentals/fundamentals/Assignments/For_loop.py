for x in range(150):
    print(x)

for x in range(5,1000):
    if x%5 == 0:
        print(x)

for x in range(1,100):
    if x%5 == 0:
        print(x, "coding")
    if x%10 == 0:
        print(x, "coding dojo")

odd_num = 0
for x in range(50000):
    if x%2 != 0:
        odd_num += x
print(odd_num)

for num in range(2018, 0, -4):
    print(num)

lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum+1):
    if num%mult == 0:
        print(num)
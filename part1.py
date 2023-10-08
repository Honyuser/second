# 键值是唯一的，新键会覆盖旧键

d = {x:y for x in [1, 2, 3] for y in [2, 4, 6]}
print(d) 

def myfunc(name, times):
    for i in range(times):
        print(f"I love {name}.")
    return i

myfunc("Python", 3)

def div(x, y):
    if y == 0:
        print('除数不能为0!!')
    else:
        z = x / y
        print(z)
    return 0 
div(4, 2)

h = input("输入你的身高",  )
w = input("输入你的体重",  )
height = float(h)
weight = float(w)
BMI = weight / pow(height, 2)
if BMI < 18.5:
    print('过轻')
elif 18.5 < BMI <= 25:
    print('正常')
elif 25 < BMI <= 28:
    print('过重')
elif 28 < BMI <= 32:
    print('肥胖')
else: 
    print('dangerous')

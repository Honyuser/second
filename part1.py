# 键值是唯一的，新键会覆盖旧键
"""
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

k = 1
while k < 4:
    h = input("输入你的身高",  )
    w = input("输入你的体重",  )
    height = float(h)
    weight = float(w)
    BMI = weight / pow(height, 2)
    if BMI < 18.5:
        print('过轻')
    elif 18.5 < BMI <= 25:
        print('正常')
        break
    elif 25 < BMI <= 28:
        print('过重')
    elif 28 < BMI <= 32:
        print('肥胖')
    else: 
        print('dangerous')
k += 1



# use function which is in the Python

def myfunc(a, b, c):
    return ''.join((c, b, a))

print(myfunc('you', 'love', 'I'))

def div(*args):
    print('有{}个元素'.format(len(args)))
    print('The second element is', args[1])  # element 翻译为 "元素"
div('666', 'hold on!', 'excellent')

def fun(**dic):  # 两个 ** 表示创建字典,而 * 表示创建元组
    print(dic)

fun(a=8, b=6, c=5)



def myfunc(*args, x, y):
    print((*args, x, y))

myfunc('666','cheers!', x=5, y=8)  # In here, x and y need to give them real numbers
   


def funA():
    x =520
    def funB():
        y = 1314
        print("In funB y =", y)
    print("In funA x =", x)
    return funB

funA()()  # 通过连续调用两次()来实现在funA中调用funB的功能


def power(exp):
    def exp_of(num):
        return num ** exp
    return exp_of

square = power(2)
cuble = power(3)
print(square(3))
print(cuble(3))


# 闭包函数
def funa(): 
    x = 0
    y = 0
    def funb(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f'现在,x = {x},y = {y}')
    return funb

move = funa()
move(1,2)
move(-1,4)



import time

def myfunc(fun):
    print('开始运行程序...')
    star = time.time()  # time.time()添加一个时间戳
    fun()
    stop = time.time()
    print('程序运行结束...')
    print(f'程序运行总耗时{(stop-star):.2f} 秒')

def cx():
    time.sleep(2)  #是程序沉睡 2 秒
    print('Hello myPython world!')

myfunc(cx)



n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    else:
        print(n)


import time

def myfunc(fun):
    def call_myfunc():
        print('开始运行程序...')
        star = time.time()  # time.time()添加一个时间戳
        fun()
        stop = time.time()
        print('程序运行结束...')
        print(f'程序运行总耗时{(stop-star):.2f} 秒')
    return call_myfunc

    
@myfunc  # 装饰器，使程序应用一次便可自动实现全部功能
def cx():
    time.sleep(2)  #是程序沉睡 2 秒
    print('Hello myPython world!')

cx()

"""
cuble = lambda x : pow(x,3)
print(cuble(5))
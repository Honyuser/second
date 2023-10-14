"""
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


cuble = lambda x : x + x + x ** 2
print(cuble(2))


# 生成器的使用(use yield replace return),斐波那契数列的生成
def counter():
    num1, num2 = 0, 1 
    while True:
        yield num1
        num1, num2 = num2, num1+num2

fib = counter()  # counter()为一个生成器
for f in fib:
    if f > 25000:
        break
    else:
        print(f)


# 使用迭代来计算斐波那契数列
def fibiten(n):
    a = 1
    b = 1
    c = 1
    while n > 2:
        c = a + b  
        a = b
        b = c
        n -= 1
    return c
print(fibiten(12))

# 使用递归来计算斐波那契数列
def fibdg(n):
    if n == 1 or n == 2:
        return 1
    else:
        num = fibdg(n-1) + fibdg(n-2)
        return num
    
print(fibdg(12))

"""
"""
# 递归(函数调用自己)思想解决汉诺塔问题

def hnt(n, x, y, z):
    if n == 1:
        print(x, '--->', z)
    else:
        hnt(n-1, x, z, y)
        print(x, '--->', z)
        hnt(n-1, y, x, z)
n = int(input('请输入汉诺塔的层数: '))
hnt(n, 'A', 'B', 'C')
# 函数的类型注释  [ times(s:dict[str,int], n: int = 3) ->list: ]
def times(s:dict[str,int], n: int) ->list:
    '''
    This is a test.
    Don't worry!!
    '''
    return list(s.items()) * n

print(times({'A':1, 'B':2, 'C':3}, 3))

print(times.__doc__)  # 查看函数的文档
print(times.__annotations__)  # 查看注释的内容

i = input('content: ')
alpha = 0
space = 0
num = 0
for t in i:
    if t.isalpha():  # 字母判断： .isalpha
         alpha += 1  
    elif t.isspace():  # 空格判断： .isspace
         space += 1
    elif t.isdigit():  # 数字判断： .isdigit
         num += 1
print(f'字母:{alpha}, 空格:{space}, 数字:{num}')

import functools  # 导入functools模块

def add(x, y):
    return x + y 

f = functools.reduce(add,[1, 2, 3, 4, 5, 6])
print(f)

n = functools.partial(pow, exp=3)  # 偏函数 partial
print(n(3))

p = functools.reduce(lambda x, y: x * y,[1, 2, 3, 5, 6])
print(p)


# f = open("./Zhang.txt", "w")


import pickle

with open('data.pkl', 'rb') as f:
    x, y, z, s, l, d = pickle.load(f)
    print(x, y, z, s, l, d, sep='\n')



try:
    while True:
        for i in range(10):
            if i > 4:
                raise 
            print(i)
        print("6")
    print('666')
except:
    print('到这来.')

    

"""
"""
# 面向对象编程的三大要素：封装、继承、多态
class a:
     x = 520
     def A(self):
          print("Hello, I'm A~")
     
class b:
     x = 666
     y = 1314
     def B(self):  # 每一个类里面的函数都必须以 self 为初始变量
          print("Hello, I'm B!")

class c(a,b):  # 子类可以继承多个父类
     pass

z = c()  # 将类赋值给 z
print(z.x)
print(z.y)
z.A()
z.B()  # 函数调用不需要 print() 语句来打印

print(isinstance(z,b))  # 判断对象 z 是否属于类 b
print(issubclass(c,b))  # 判断类 c 是否为类 b 的子类
       
"""
# 组合
class Turtle:
    def say(self):
        print("不积跬步，无以至千里.")

class Cat:
    def say(self):
        print("喵喵喵~")

class Dog:
    def say(self):
        print("我只是一条修狗~~")

class Garden:
    t = Turtle()
    c = Cat()
    d = Dog()
    def say(self):  # self 将 g 绑定到自己身上
        self.t.say()
        self.c.say()
        self.d.say()

g = Garden()
g.say()

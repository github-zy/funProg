# 第一章 第一课

命令式编程(imperative programming)和函数式编程(functional programming)

命令式编程像是操作状态
```
car = create_car()
car.add_gas(10)
print(car.get_gas())
# 10
```

函数式编程像是操作函数

```
car = create_car()
car_with_gas = add_gas(car, 10)
gas = get_gas(car_with_gas)
print(gas)
# 10
```
# 第一章 第二课

python并不是最适合函数式编程的语言，因为It doesn't enforce **static typing**, **immutability**, or **pure functions**, and it lacks **tail call optimization**.

# 第一章 第三课

不变性(immutability)：FP偏好让数据不可变

元组(Tuples)和列表(Lists)：元组和列表都是有序集合，但是元组是不可变的

列表可变

```
ages: list[int] = [16, 21, 30]
ages.append(80)
# [16, 21, 30, 80]
```

元组不可变

```
ages: tuple[int, ...] = (16, 21, 30)
# (16, 21, 30)
more_ages: tuple[int, ...] = (80,)
# (80,)
all_ages: tuple[int, ...] = ages + more_ages
# (16, 21, 30, 80)
```

# 第一章 第四课

宣言式编程(Declarative Programing)：FP的目标是告诉计算机想要什么结果，而不是命令计算机每一步该干嘛

例如前端语言CSS就是宣言式编程

```
button {
  color: red;
}
```
# 第一章 第五课

FP就像数学一样，比如下面的数学语言

```
avg = Σx/N
```

如果是命令式编程
```
def get_average(nums: list[int]) -> float:
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
```

如果是FP

```
def get_average(nums: list[int]) -> float:
    return sum(nums) / len(nums)
```
作为一个优秀的FP程序员，代码应该禁止：

1. 使用循环
2. 修改任何变量（可以创造新的变量）

# 第一章 第六课

类(Class)和函数(Function)

如果不确定使用函数还是类，默认使用函数。

如果需要一些长时间存在的、有状态的、容易建模的、可以通过继承传递行为和数据结构的东西，可以考虑类，比如说

1. 电子游戏
2. 仿真
3. 图形用户界面

类将世界想象成分级对象的集合，对象通过将行为、数据和状态捆在一起彼此区分，就像棋盘上的棋子。

函数将世界想象成数据的转变，就像棋盘的上一步变为下一步。

# 第一章 第七课

Debug FP：对于FP比如下面的语句

```
def get_player_position(
    position: float, velocity: float, friction: float, gravity: float
) -> float:
    return calc_gravity(calc_friction(calc_move(position, velocity), friction), gravity)
```

一个debug的技巧就是将它们拆开

```
def get_player_position(
    position: float, velocity: float, friction: float, gravity: float
) -> float:
    moved = calc_move(position, velocity)
    slowed = calc_friction(moved, friction)
    final = calc_gravity(slowed, gravity)
    print("Given:")
    print(
        f"position: {position}, velocity: {velocity}, friction: {friction}, gravity: {gravity}"
    )
    print("Results:")
    print(f"moved: {moved}, slowed: {slowed}, final: {final}")
    return final
```

# 第一章 第八课

FP和OOP最大的区别在于FP没有继承的概念，因为继承带来可变类，与FP相冲突。FP中依然可以利用封装、抽象、多态的概念。

# 第一章 第九课

语句(Statement)和表达式(Expression)

语句就是被执行的动作，比如
```
n: int = 7  # Variable assignment statement


def greet(name: str) -> str:  # Function definition statement
    return f"Hello, {name}!"


if x > 10:  # `if` statement
    print(greet("Alice"))

for i in range(n):  # `for` loop statement
    print(i)
```

表达式是语句的子集，用来求值，例如
```
result: int = 2 + 2  # Arithmetic expression
length: int = len("hello")  # Function call expression
total_cost: float = len(items) * cost  # Multiple expressions combined into one
```

对于大多数语言（包括Python）来说，函数调用是一种表达式。

FP鼓励使用表达式，因为所有表达式可以组合计算，例如

```
print(sum([1, 2, 3, 4]) * 2)  # 20
```

而一些语句无法组合计算，例如
```
# This doesn't work!
print((
total = 0
for n in [1, 2, 3, 4]:
    total += n
) * 4)
```
# 第一章 第十课

三目运算符(Ternary)

语法如下：
```
value_a if condition else value_b
```

三目运算符将语句变为表达式，对于一些很复杂的条件逻辑，为了可读性，还是使用if/else语句比较好。

# 第二章 第一课

在Python中，函数就是值，可以将函数赋给一个变量，例如
```
from collections.abc import Callable


def add(x: int, y: int) -> int:
    return x + y


# assign the function to a new variable
# called `addition`. It behaves the same
# as the original `add` function
addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7
```

# 第二章 第二课

匿名函数就是没有名字的函数。在Python中，匿名函数被称作lambda函数，例如
```
lambda x: x + 1
```
lambda函数可以被赋值给变量，常用来代替小型的、简单的算式
```
get_age: Callable[[str], int | str] = lambda name: {
    "lane": 29,
    "hunter": 69,
    "allan": 17,
}.get(name, "not found")
print(get_age("lane"))
# 29
```

# 第二章 第三课

如果一种编程语言的函数可以被传递给参数、可以被函数返回、且可以被赋值给变量，那么就说这种编程语言支持第一类函数(First-class functions)

1. 第一类函数：被当作值来看待的函数
2. 高阶函数：接收函数参数或返回函数的函数
   
# 第二章 第四课

map在FP中是一种常被使用的高阶函数。

在Python中，内置map函数接收一个函数和可迭代对象(iterable)（通常是list）将函数应用在可迭代对象上然后返回另一个一个可迭代对象（iterator）

使用map可以避免使用循环和状态变量
```
from collections.abc import Iterator


def square(x: int) -> int:
    return x * x


nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: Iterator[int] = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
```
# 第二章 第五课

内置filter函数接受一个函数和一个可迭代对象（通常是list），将函数应用在个体上若函数返回值为真，则保留，最后返回保留的个体组成的可迭代对象。
```
def is_even(x: int) -> bool:
    return x % 2 == 0


numbers: list[int] = [1, 2, 3, 4, 5, 6]
evens: list[int] = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]
```
# 第二章 第六课

functools.reduce()接受一个函数和一个值的列表，然后依次计算，例子如下
```
# import functools from the standard library
import functools


def add(sum_so_far: int, x: int) -> int:
    return sum_so_far + x


numbers: list[int] = [1, 2, 3, 4]
total: int = functools.reduce(add, numbers)
print(total)
# 10
```

# 第二章 第八课

zip函数接受两个可迭代对象（通常是list），然后返回一个新的可迭代对象（一个元组的列表），见例子
```
a: list[int] = [1, 2, 3]
b: list[int] = [4, 5, 6]

c: list[tuple[int, int]] = list(zip(a, b))
print(c)
# [(1, 4), (2, 5), (3, 6)]
```
# 第三章 第一课

纯函数(pure function)有两个性质：

1. 给定相同的参数它们总是返回相同的值
2. 运行它们不会造成任何副作用

纯函数
```
def find_max(nums: list[int]) -> float:
    max_val: float = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val
```
非纯函数
```
# instead of returning a value
# this function modifies a global variable
global_max: float = float("-inf")


def find_max(nums: list[int]) -> None:
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num
```

# 第三章 第二课

纯函数不会执行任何I/O操作（比如说读文件，访问网络，或者写控制台）

# 第三章 第三课

引用(Reference)和值(Value)：当给函数传参时，有些是传引用，函数可以直接访问原始值；有些是传值，函数只可以访问原始值的副本，修改参数不会导致原值改变。

下列类型传引用：

1. 列表
2. 字典
3. 集合
   
下列类型传值：

1. 整数
2. 浮点数
3. 字符串
4. 布尔值
5. 元组

# 第三章 第五课

输入和输出的例子

1. 从硬盘读写文件
2. 访问网络
3. 从数据库读写数据
4. 在控制台打印
   
# 第三章 第七课

一个no-op就是一个没有作任何事情的运算。

如果一个函数没有返回任何东西，那么它要么造成了副作用，要么就是no-op

# 第三章 第八课

记忆化(Memoization)意识是将计算的结果缓存起来以便未来不需要再计算一次。

# 第三章 第九课

引用透明性(Referential transparency)意思是一个函数每一次可以被他的返回值来代表，意思是相同输入总是得到相同输出。对于引用透明的函数，例如纯函数，可以放心地使用记忆化。

记忆化是内存和速度的交易。

# 第四章 第一课

递归实际上就是函数调用自己。

递归函数的基本组成
1. 解决一个小问题
2. 递归
3. 基本情况（函数中不调用自己的部分）
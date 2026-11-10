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
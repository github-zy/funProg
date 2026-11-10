# 第一课

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
# 第二课

python并不是最适合函数式编程的语言，因为It doesn't enforce **static typing**, **immutability**, or **pure functions**, and it lacks **tail call optimization**.

# 第三课

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

# 第四课

宣言式编程(Declarative Programing)：FP的目标是告诉计算机想要什么结果，而不是命令计算机每一步该干嘛

例如前端语言CSS就是宣言式编程

```
button {
  color: red;
}
```


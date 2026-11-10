## 第一课

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

##第二课

python并不是最适合函数式编程的语言，因为It doesn't enforce **static typing**, **immutability**, or **pure functions**, and it lacks **tail call optimization**.
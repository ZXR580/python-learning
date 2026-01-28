def scope():
    global car1
    car1 = 1
    print("函数内部结果")
    print(car1,car2)
car1=10
car2=20
scope()
print("函数外部结果")
print(car1,car2)
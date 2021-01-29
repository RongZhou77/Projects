"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法， 改成【喵喵叫】
"""


# 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
class Animal():
    def __init__(self):
        self.name = "动物"
        self.colour = "black"
        self.age = 1
        self.sex = "雄性"

    def speak(self):
        print(f"{self.name}会叫")

    def run(self):
        print(f"{self.name}会跑")


# 创建子类【猫】，继承【动物类】
class Cat(Animal):
    # 重写父类的__init__方法，继承父类的属性
    def __init__(self):
        super().__init__()
        self.name = "猫"
        # 添加一个新的属性，毛发 = 短毛，
        self.hair = "short"

    # 添加一个新的方法， 会捉老鼠，
    def catch_mouse(self):
        print(f"{self.name}会捉老鼠")

    # 重写父类的【会叫】的方法，改成【喵喵叫】
    def speak(self):
        print(f"{self.name}会喵喵叫")


if __name__ == '__main__':
    MyAnimal = Animal()
    MyAnimal.run()
    MyAnimal.speak()
    print("动物里面我最喜欢猫")
    myCat = Cat()
    myCat.speak()
    myCat.run()
    print(f"{myCat.name}的毛发是：{myCat.hair}，颜色是{myCat.colour},年龄是{myCat.age}岁")

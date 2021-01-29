"""
一个回合制游戏，每个角色都有 hp 和 power，hp 代表血量，power 代表攻击力，hp 的初始值为 1000，power 的初始值为 200。
定义一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜
"""


class Game():
    def __init__(self):
        self.my_hp = 1000
        self.my_power = 200
        self.enemy_hp = 1000
        self.enemy_power = 180
        self.__hujia = 50

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.__hujia - self.enemy_power
            self.enemy_hp -= self.my_power
            print(f"我的血量：{self.my_hp} VS 对手的血量：{self.enemy_hp}")

            if self.my_hp <= 0:
                print("我输了")
                self.__rest(10)
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                self.__rest(10)
                break

    def __rest(self, time):
        print(f"我累了，我要休息{time}分钟")


if __name__ == '__main__':
    game = Game()
    game.fight()

"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять
Ниже пример использования
"""
from datetime import datetime


def instances_counter(cls):
    instances = 0
    saved_init = cls.__init__

    def decorated_init(self, *args, **kwargs):
        nonlocal instances
        saved_init(self, *args, **kwargs)
        instances += 1

    # *args is needed in order to let get_created_instances() and
    # reset_instances_counter() methods behave both like normal and static

    def get_created_instances(*args):
        return instances

    def reset_instances_counter(*args):
        nonlocal instances
        try:
            return instances
        finally:
            instances = 0

    cls.__init__ = decorated_init
    cls.get_created_instances = get_created_instances
    cls.reset_instances_counter = reset_instances_counter

    return cls


@instances_counter
class Homework:
    def __init__(self, text, deadline):
        self.text = text
        self.deadline = deadline
        self.created = datetime.now()

    def is_active(self):
        now = datetime.now()
        return False if now >= self.deadline else True


@instances_counter
class User:
    pass


if __name__ == "__main__":
    print(Homework.get_created_instances())  # 0
    hw, _, _ = Homework("123", 0), Homework("123", 0), Homework("123", 0)
    print(hw.get_created_instances())  # 3
    print(hw.reset_instances_counter())  # 3
    print(hw.get_created_instances())  # 0

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
    print(user.get_created_instances())  # 0

# from selenium import webdriver
#
# driver = webdriver.Chrome(executable_path="")


# class webdriver:
#
#     def __index__(self, path):
#         self.path = path
#
#     def Chrome(self):
#         return "Chrome"
#
#     def Firefox(self):
#         return "Firefox"
#
#
# browser = webdriver.Chrome("x")
# print(browser)

class People:
    def __init__(self, age, sex, height):
        self.age = age
        self.sex = sex
        self.height = height

    def jump(self):
        print("Прыгаю")

    def run(self):
        print("Бегу")

    def seat(self):
        print("Сажусь")


Alex = People(age=20, sex="M", height=182)
Alex.jump()
# Marina = Human(25, "Марина", "Продавец")

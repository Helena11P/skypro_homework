class User:
    first_name = "Имя"
    last_name = "Фамилия"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def sayName(self):
        print(f"Имя: {self.first_name}")

    def sayLastName(self):
        print(f"Фамилия: {self.last_name}")

    def sayUser(self):
        print(f"Имя и фамилия: {self.first_name} {self.last_name}")

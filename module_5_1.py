#  1. Создаем класс House.
class House:
    #  2. Вунтри класса House определяем метод __init__, в который передадаем название и кол-во этажей.
    def __init__(self, name, number_of_floors):
        #  3. Внутри метода __init__ создаем атрибуты объекта self.name и self.number_of_floors,
        #  присваиваем им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors

    #  4. Создаем метод go_to с параметром new_floor и записываем логику внутри него на основе описания задачи.
    def go_to(self, new_floor):
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')


#  5. Создаем объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
#  6. Вызоваем метод go_to у этого объекта с произвольным числом.
h1.go_to(5)
h2.go_to(10)

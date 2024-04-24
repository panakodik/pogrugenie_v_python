import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2

class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"

class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        try:
            if animal_type == 'Bird':
                return Bird(*args)
            elif animal_type == 'Fish':
                return Fish(*args)
            elif animal_type == 'Mammal':
                return Mammal(*args)
            else:
                raise ValueError('Недопустимый тип животного')
        except Exception as e:
            logging.error(f'Ошибка при создании животного: {e}')

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python script.py <тип_животного> <имя> <параметр>")
        sys.exit(1)

    animal_type = sys.argv[1]
    name = sys.argv[2]
    parameter = sys.argv[3]

    try:
        if animal_type not in ['Bird', 'Fish', 'Mammal']:
            raise ValueError('Недопустимый тип животного')
        
        if animal_type == 'Bird':
            animal = AnimalFactory.create_animal(animal_type, name, float(parameter))
            print(animal.wing_length())
        elif animal_type == 'Fish':
            animal = AnimalFactory.create_animal(animal_type, name, float(parameter))
            print(animal.depth())
        elif animal_type == 'Mammal':
            animal = AnimalFactory.create_animal(animal_type, name, float(parameter))
            print(animal.category())
    except ValueError as ve:
        logging.error(f'Ошибка: {ve}')
    except Exception as e:
        logging.error(f'Общая ошибка: {e}')
# Этот скрипт можно запускать из командной строки следующим образом:

# python script.py <тип_животного> <имя> <параметр>
# Где <тип_животного> может быть "Bird", "Fish" или "Mammal", <имя> это имя животного, а <параметр> это параметр, который соответствует типу животного (например, для птицы это размах крыльев, для рыбы - максимальная глубина, для млекопитающего - вес).

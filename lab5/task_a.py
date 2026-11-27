class RaceHorse:

    def __init__(self, name: str, speed: float, age: int, breed: str = "Чистокровна"):
    self.__name = name
    self.__breed = breed
    self.__place_in_race = None
    self.set_speed(speed)
    self.set_age(age)

def set_speed(self, speed: float):
    if speed <= 0:
        raise ValueError("Speed must be positive")
    self.__speed = speed

def set_age(self, age: int):
    if age <= 0:
        raise ValueError("Age must be positive")
    self.__age = age

    def __del__(self):
        print(f"[Log] Об'єкт коня '{self.__name}' видалено з пам'яті.")

    def get_name(self) -> str:
        return self.__name

    def get_speed(self) -> float:
        return self.__speed

    def get_age(self) -> int:
        return self.__age

    def get_breed(self) -> str:
        return self.__breed

    def get_place(self):
        return self.__place_in_race

    def set_speed(self, speed: float):
        if speed > 0:
            self.__speed = speed

    def set_age(self, age: int):
        if age > 0:
            self.__age = age

    def set_place(self, place: int):
        self.__place_in_race = place

    def show_info(self):
        place_str = (f"{self.__place_in_race} місце"
             if self.__place_in_race is not None else "ще не фінішував")
        print(f"Кінь: {self.__name} | Порода: {self.__breed} | Вік: {self.__age} р. | "
              f"Швидкість: {self.__speed} км/год | Результат: {place_str}")

class Race:
    def __init__(self, race_name: str):
        self.__race_name = race_name
        self.__participants = []

    def __del__(self):
        print(f"[Log] Перегони '{self.__race_name}' завершено, об'єкт видалено.")

    def add_horse(self, horse: RaceHorse):
        if 3 <= horse.get_age() <= 7:
            if any(h.get_name().lower() == horse.get_name().lower() for h in self.__participants):
    print(f"Кінь {horse.get_name()} вже зареєстрований!")
    return
            print(f"Кінь {horse.get_name()} (вік: {horse.get_age()}) успішно допущений до перегонів!")
        else:
            print(f"Відмова! Кінь {horse.get_name()} (вік: {horse.get_age()}) не підходить за віком (допускаються лише від 3 до 7 років).")

    def remove_horse(self, name: str):
        for horse in self.__participants:
            if horse.get_name().lower() == name.lower():
                self.__participants.remove(horse)
                print(f"Учасника {name} знято з перегонів.")
                return
        print(f"Учасника з ім'ям {name} не знайдено.")

    def sort_by_speed_and_assign_places(self):
        self.__participants.sort(key=lambda h: h.get_speed(), reverse=True)
        
        for index, horse in enumerate(self.__participants):
            if index < 3:
                horse.set_place(index + 1)
            else:
                horse.set_place(None)
        print("\nУчасників відсортовано за швидкістю, а першій трійці присвоєно призові місця.")

    def determine_winner_by_formula(self):
        if not self.__participants:
            print("Немає учасників для визначення переможця!")
            return None

        total_age = sum(h.get_age() for h in self.__participants)
        average_age = total_age / len(self.__participants)
        print(f"\nСередній вік учасників перегонів: {average_age:.2f} років.")

        best_horse = None
        best_score = -float('inf')

        for horse in self.__participants:
            age_diff = abs(horse.get_age() - average_age)
            score = horse.get_speed() - age_diff
            print(f"   -> {horse.get_name()}: швидкість {horse.get_speed()} - різниця віку {age_diff:.2f} = {score:.2f} балів")
            
            if score > best_score:
                best_score = score
                best_horse = horse

        print(f"Переможець за спеціальною формулою: {best_horse.get_name()} (результат: {best_score:.2f} балів)!")
        return best_horse

    def show_all_participants(self):
        print(f"\n--- Список учасників перегонів '{self.__race_name}' ---")
        if not self.__participants:
            print("Список порожній.")
        else:
            for horse in self.__participants:
                horse.show_info()
        class RaceHorse:
    """Represents a race horse with private attributes."""
    def __init__(...):

    derby = Race("Кубок Львова 2026")
    h1 = RaceHorse("Буцефал", 65.5, 5, "Арабська")
    h2 = RaceHorse("Вітер", 68.0, 4, "Англійська")
    h3 = RaceHorse("Грім", 62.0, 6, "Орловський рисак")
    h4 = RaceHorse("Малюк", 70.0, 2, "Поні")
    h5 = RaceHorse("Дідусь", 55.0, 10, "Ваговоз")
    h6 = RaceHorse("Блискавка", 67.5, 5, "Ахалтекінська")

    print("=== Етап 1: Реєстрація учасників ===")
    for horse in [h1, h2, h3, h4, h5, h6]:
        derby.add_horse(horse)

    derby.show_all_participants()

    print("=== Етап 2: Видалення одного учасника ===")
    derby.remove_horse("Грім")
    derby.show_all_participants()

    print("=== Етап 3: Сортування за швидкістю та розподіл місць ===")
    derby.sort_by_speed_and_assign_places()
    derby.show_all_participants()

    print("=== Етап 4: Визначення переможця за формулою ===")
    derby.determine_winner_by_formula()

    print("\n=== Завершення програми (спрацювання деструкторів) ===")

if __name__ == "__main__":
    main()
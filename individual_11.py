def main():
    people = []
    n = int(input("Введите количество людей: "))

    for i in range(n):
        print(f"Введите информацию о {i + 1}-м человеке:")
        person = input_person()
        people.append(person)

    people = sorted(people, key=lambda x: x['дата рождения'])

    print("\nИнформация о людях (сортировка по дате рождения):")
    for person in people:
        print_person(person)

    search_number = input("\nВведите номер телефона для поиска: ")
    found = False
    for person in people:
        if person['номер телефона'] == search_number:
            print("\nИнформация о человеке с введенным номером телефона:")
            print_person(person)
            found = True
            break

    if not found:
        print("\nЧеловек с таким номером телефона не найден.")


def input_person():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    birth_date = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
    day, month, year = map(int, birth_date.split('.'))
    return {"фамилия": last_name, "имя": first_name, "номер телефона": phone_number,
            "дата рождения": [day, month, year]}


def print_person(person):
    print(
        f"Фамилия: {person['фамилия']}, Имя: {person['имя']}, Номер телефона: {person['номер телефона']}, Дата рождения: {'.'.join(map(str, person['дата рождения']))}")

if __name__ == '__main__':
    main()
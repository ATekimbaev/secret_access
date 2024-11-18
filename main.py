def secret_access():
    """Программа проверки по секретному списку."""
    secret_list = {"Attila", "Zarya", "Starship", "Ilon", "Gooder"}
    while True:
        nickname = input("Введите свой ник: ")
        if nickname in secret_list:
            print(f"Ты – свой. Приветствую, любезный {nickname}!")
            break
        else:
            print("Тут ничего нет. Еще есть вопросы?")

def dialogue_program():
    """Диалоговая программа с пользователем."""
    print("Как вас зовут?")
    username = input()
    print(f"Здравствуйте {username}")
    print("Как дела?")
    mood = input().strip().lower()
    if mood == "хорошо":
        print("Я за вас рад")
    elif mood == "плохо":
        print("Сочувствую вам")
    else:
        print("Хорошо, что делитесь своими эмоциями!")

def reverse_dialogue_program():
    """Обратный порядок диалога с пользователем."""
    print("Как дела?")
    mood = input().strip().lower()
    if mood == "хорошо":
        print("Я за вас рад")
    elif mood == "плохо":
        print("Сочувствую вам")
    else:
        print("Хорошо, что делитесь своими эмоциями!")
    print("Как вас зовут?")
    username = input()
    print(f"Здравствуйте {username}")

def main():
    """Главная программа выбора."""
    print("Выберите, какую программу запустить:")
    print("1. Проверка по секретному списку")
    print("2. Диалоговая программа (прямой порядок)")
    print("3. Диалоговая программа (обратный порядок)")
    
    choice = input("Введите номер программы (1, 2, или 3): ").strip()
    
    if choice == "1":
        secret_access()
    elif choice == "2":
        dialogue_program()
    elif choice == "3":
        reverse_dialogue_program()
    else:
        print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

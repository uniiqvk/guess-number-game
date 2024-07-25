import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. У вас есть 10 попыток, чтобы угадать его.")

    while attempts_left > 0:
        try:
            user_guess = int(input(f"У вас осталось {attempts_left} попыток. Введите ваше предположение: "))
            if user_guess < 1 or user_guess > 100:
                print("Пожалуйста, введите число от 1 до 100.")
                continue
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        if user_guess < number_to_guess:
            print("Ваше число меньше загаданного.")
        elif user_guess > number_to_guess:
            print("Ваше число больше загаданного.")
        else:
            print("Поздравляем! Вы угадали число.")
            break
        
        attempts_left -= 1

    if attempts_left == 0:
        print(f"К сожалению, вы исчерпали все попытки. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    guess_number_game()

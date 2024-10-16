def get_player_choice():
    while True:
        player_choice = input("Выберите: камень (к), ножницы (н), бумага (б): ").strip().lower()
        if player_choice in ['к', 'н', 'б']:
            return player_choice
        else:
            print("Некорректный выбор. Попробуйте снова.")

def get_computer_choice():
    choices = ['к', 'н', 'б']
    if get_computer_choice.turns % 3 == 0:
        return choices[0]
    elif get_computer_choice.turns % 3 == 1:
        return choices[1]
    else:
        return choices[2]

get_computer_choice.turns = 0

def determine_winner(player_choice, computer_choice):
    print(f"Ваш выбор: {player_choice}")
    print(f"Выбор компьютера: {computer_choice}")

    if player_choice == computer_choice:
        print("Ничья!")
    elif (player_choice == 'к' and computer_choice == 'н') or \
         (player_choice == 'н' and computer_choice == 'б') or \
         (player_choice == 'б' and computer_choice == 'к'):
        print("Вы победили!")
    else:
        print("Компьютер победил!")

def play_game():
    print("Добро пожаловать в игру 'Камень-Ножницы-Бумага'!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        determine_winner(player_choice, computer_choice)
        get_computer_choice.turns += 1
        play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
        if play_again != 'да':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    play_game()

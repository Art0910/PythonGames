import random


class Game:
    def __init__(self):
        self.number = []
        self.user_number = []
        self.attempt = 0
        self._bulls_name = 'быки'
        self._cows_name = 'коровы'
        self.bulls_cows = {self._cows_name: set(), self._bulls_name: set()}

    def game_menu(self):
        """
        Запускает игру и управляет ее ходом
        """
        answer = input('Сыграем в "Быки и коровы"? (y/n): ')
        while True:
            if answer == 'y':
                self.start_game()
                answer = input('Еще разок"? (y/n): ')
            elif answer == 'n':
                print('До свидания!')
                break
            else:
                answer = input('Непонятная команда! Введи "y" для старта или "n" для выхода: ')

    def start_game(self):
        """
        Управляет одним коном игры
        """
        self.new_number()
        self.attempt = 0
        self.bulls_cows = {self._cows_name: set(), self._bulls_name: set()}

        print('Угадай 4-х значное число из неповторяющихся цифр! Удачи!')
        while True:
            self.attempt += 1
            self.get_user_number()
            if self.compare() == 'end':
                break

    def new_number(self):
        """
        Генерируем новой число, которое нужно угадать
        :return: number как список
        """
        nums = [str(i) for i in range(10)]
        self.number = []
        while len(self.number) < 4:
            random_num = random.randrange(len(nums))
            self.number.append(nums.pop(random_num))

    def get_user_number(self):
        """
        Ввод числа пользователем и обновление user_number
        """
        user_input = input('Введите число (4 знака): ')
        self.user_number = [i for i in user_input]

    def compare(self):
        """
        Сравнивает угадываемое число с числом, предложенным пользователем
        :return: 'end' если игра окончена
        """
        if ''.join(self.number) == ''.join(self.user_number):
            print('Победа! Вы справились за {} попыток'.format(self.attempt))
            return 'end'
        else:
            self.get_bulls_cows()
        self.print_results()

    def get_bulls_cows(self):
        """
        Определяет наличие быков и коров и обновляет словарь с быками и коровами
        """
        for n_pc, i_pc in enumerate(self.number):
            for n_usr, i_usr in enumerate(self.user_number):
                if i_pc == i_usr and n_pc == n_usr:  # определение быка
                    self.bulls_cows[self._bulls_name].add(i_usr)
                    if i_usr in self.bulls_cows[self._cows_name]:
                        self.bulls_cows[self._cows_name].remove(i_usr)
                    break
                elif i_pc == i_usr:  # определение коровы
                    self.bulls_cows[self._cows_name].add(i_usr)
                    break
                else:  # отсутствие совпадений
                    pass

    def print_results(self):
        """
        В красивом виде выводит число пользователя, набор быков и коров
        """
        cows = ', '.join(self.bulls_cows[self._cows_name]) if self.bulls_cows[self._cows_name] else '-'
        bulls = ', '.join(self.bulls_cows[self._bulls_name]) if self.bulls_cows[self._bulls_name] else '-'
        print('{} --> {}: {}; {}: {}'.format(''.join(self.user_number), self._cows_name, cows, self._bulls_name, bulls))


if __name__ == '__main__':
    my_game = Game()
    my_game.game_menu()

    # Ниже код для тестирования

    # my_game.new_number()
    # my_game.user_number = my_game.number
    # my_game.compare()
    # my_game.get_user_number()

    # my_game.number = ['1', '2', '3', '4']
    # my_game.user_number = ['5', '2', '6', '4']
    # my_game.get_bulls_cows()
    # my_game.print_results()



    # Сделать фичу - выбор длины числа
    # исправить баг с необнулением коров при переходе в быки
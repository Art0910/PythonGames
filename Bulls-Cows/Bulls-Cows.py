import random


class Game:
    def __init__(self):
        self.number = []
        self.user_number = []
        self.attempt = 0
        self._bulls_name = 'быки'
        self._cows_name = 'коровы'
        self.bulls_cows = {self._cows_name: [], self._bulls_name: []}

    def start_game(self):
        """
        Запускает игру
        :return:
        """
        pass

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
        print(self.user_number)

    def compare(self):
        """
        Сравнивает угадываемое число с числом, предложенным пользователем
        :return:
        """
        if ''.join(self.number) == ''.join(self.user_number):
            print('Победа! Вы справились за {} попыток'.format(self.attempt))
            return
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
                    self.bulls_cows[self._bulls_name].append(i_usr)
                    break
                elif i_pc == i_usr:  # определение коровы
                    self.bulls_cows[self._cows_name].append(i_usr)
                    break
                else:                # отсутствие совпадений
                    pass
        print(self.bulls_cows)

    def print_results(self):
        """
        В красивом виде выводит число пользователя, набор быков и коров
        """
        cows = ', '.join(self.bulls_cows[self._cows_name]) if self.bulls_cows[self._cows_name] else '-'
        bulls = ', '.join(self.bulls_cows[self._bulls_name]) if self.bulls_cows[self._bulls_name] else '-'
        print('{} --> {}: {}; {}: {}'.format(''.join(self.user_number), self._cows_name, cows, self._bulls_name, bulls))


if __name__ == '__main__':
    my_game = Game()
    my_game.start_game()

    # Ниже код для тестирования

    # my_game.new_number()
    # my_game.user_number = my_game.number
    # my_game.compare()
    # my_game.get_user_number()

    my_game.number = ['1', '2', '3', '4']
    my_game.user_number = ['5', '2', '6', '4']
    my_game.get_bulls_cows()
    my_game.print_results()



    # Сделать фичу - выбор длины числа
    # При старте игры обнулять все хранимые значения (number, user_number, attempts, bulls_cows)
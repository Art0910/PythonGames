import random


class Game:
    def __init__(self):
        self.number = []
        self.user_number = []
        self.attempt = 0
        self.bulls_cows = {}

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

    def compare(self):
        """
        Сравнивает угадываемое число с числом, предложенным пользователем
        :return:
        """
        if ''.join(self.number) == ''.join(self.user_number):
            print ('Победа! Вы справились за {} попыток'.format(self.attempt))
        else:
            self.get_bulls_cows()


    def get_bulls_cows(self):
        """
        Определяет наличие быков и коров и обновляет словарь с быками и коровами
        """
        pass


if __name__ == '__main__':
    my_game = Game()
    my_game.start_game()

    # Ниже код для тестирования

    my_game.new_number()
    my_game.user_number = my_game.number
    my_game.compare()
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
        :return:
        """
        pass

    def compare(self):
        """
        Сравнивает угадываемое число с числом, предложенным пользователем
        :return:
        """
        pass

    def _get_bulls_cows(self):
        """
        Определяет наличие быков и коров и обновляет словарь с быками и коровами
        """
        pass

if __name__ == '__main__':
    my_game = Game()
    my_game.start_game()
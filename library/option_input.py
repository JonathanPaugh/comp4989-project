class OptionInput:
    """
    Class that handles receiving user input from a list of options.
    """

    INVALID_INPUT_MESSAGE = 'Invalid Option'
    MENU_EXIT = ('Exit', lambda: True)

    def __init__(self, text: str, options: [], display_option: callable):
        self._text = text
        self._options = options
        self._display_option = display_option

    def get_input(self):
        """
        Gets an option from user input.

        :returns: The selected option.
        """
        self._display_options()

        selected = False
        user_input = None

        while not selected:
            try:
                user_input = int(input(F'{self._text}: ')) - 1
            except ValueError:
                user_input = -1

            if 0 <= user_input < len(self._options):
                selected = True
            else:
                print(self.INVALID_INPUT_MESSAGE)

        return self._options[user_input]

    def _display_options(self):
        """
        Displays the options.
        """
        for index in range(0, len(self._options)):
            print(f'{index + 1}. {self._display_option(self._options[index])}')

def run_menu(title, options):
    exit_menu = None
    while exit_menu is None:
        print(f'--- {title} ---')
        option_input = OptionInput('Select option', options, lambda option: option[0])
        _, option = option_input.get_input()
        exit_menu = option()

    return exit_menu

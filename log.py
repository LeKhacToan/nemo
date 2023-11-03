import colorama


class Log:
    def __init__(self):
        pass

    @classmethod
    def success(cls, mess):
        print(colorama.Fore.GREEN + mess + colorama.Fore.RESET)

    @classmethod
    def error(cls, mess):
        print(colorama.Fore.RED + mess + colorama.Fore.RESET)

    @classmethod
    def warning(cls, mess):
        print(colorama.Fore.YELLOW + mess + colorama.Fore.RESET)

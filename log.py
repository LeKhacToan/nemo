import colorama
import logging


class CustomFormatter(logging.Formatter):
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: colorama.Fore.CYAN + format + colorama.Fore.RESET,
        logging.INFO: colorama.Fore.GREEN + format + colorama.Fore.RESET,
        logging.WARNING: colorama.Fore.YELLOW + format + colorama.Fore.RESET,
        logging.ERROR: colorama.Fore.LIGHTRED_EX + format + colorama.Fore.RESET,
        logging.CRITICAL: colorama.Fore.RED + format + colorama.Fore.RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# set up logging to file - see previous section for more details
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="myapp.log",
    filemode="w",
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
console.setFormatter(CustomFormatter())
logging.getLogger("").addHandler(console)


class Log:
    def __init__(self):
        pass

    @classmethod
    def success(cls, mess):
        logging.info(mess)

    @classmethod
    def error(cls, mess):
        logging.error(mess)

    @classmethod
    def warning(cls, mess):
        logging.warning(mess)

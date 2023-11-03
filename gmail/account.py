import pathlib


class Account:
    def __init__(self, file="account.txt"):
        self.file = file

    def get_accounts(self):
        here = pathlib.Path(__file__).parent
        with open(here.joinpath(self.file)) as infile:
            list_account = list(set(map(str.strip, infile)))
            username = [account.split("@")[0] for account in list_account]
            valid_username = [a for a in username if len(a) >= 6 and len(a) <= 30]
            return valid_username

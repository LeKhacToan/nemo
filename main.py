from fire import Fire
from aiohttp import ClientSession
from gmail.gmail import GmailAccount


class Scaffold:
    """System scaffolding Top-level interface commands"""

    def __init__(self):
        pass

    @staticmethod
    async def gmail():
        async with ClientSession() as session:
            gmail = GmailAccount(session)
            await gmail.check_account("lkhactoan")


if __name__ == "__main__":
    Fire(Scaffold)

from fire import Fire
from aiohttp import ClientSession
import asyncio
import time

from gmail.gmail import GmailAccount
from gmail.account import Account
from log import Log


class Scaffold:
    """System scaffolding Top-level interface commands"""

    def __init__(self):
        pass

    @staticmethod
    def gmail():
        async def __gmail():
            start_time = time.time()

            accounts = Account().get_accounts()
            semaphore = asyncio.Semaphore(500)

            async with ClientSession() as session:
                gmail = GmailAccount(session, semaphore)
                is_success = await gmail.setup()
                if not is_success:
                    Log.warning("Cant setup project, need retry after 5 seconds")
                    return

                tasks = []
                for account in accounts:
                    tasks.append(asyncio.create_task(gmail.run(account)))
                await asyncio.gather(*tasks)

                time_difference = time.time() - start_time
                print(f"Scraping time: %.2f seconds." % time_difference)

        loop = asyncio.get_event_loop()
        loop.run_until_complete(__gmail())


if __name__ == "__main__":
    Fire(Scaffold)

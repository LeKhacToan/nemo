import re
import json

from .config import (
    SIGNUP_URL,
    SIGNUP_HEADER,
    VALIDATE_PERSONAL_URL,
    VALIDATE_PERSONAL_HEADER,
    USERNAME_AVAILABILITY_URL,
    USERNAME_AVAILABILITY_HEADER,
)
from log import Log
from proxy import Proxy


class GmailAccount:
    def __init__(self, session, semaphore, azt="", ae="", dsh="", tl=""):
        self.session = session
        self.semaphore = semaphore
        self.timeout = 5
        self.azt = azt
        self.ae = ae
        self.dsh = dsh
        self.tl = tl

    async def call_signup(self):
        url = SIGNUP_URL
        header = SIGNUP_HEADER
        is_success = False
        try:
            response = await self.session.get(
                url,
                headers=header,
                timeout=20,
                raise_for_status=True,
                proxy=Proxy.get_proxy(),
            )
            status_code = response.status
            res_data = await response.text()

            global_data = re.findall(
                r"window.WIZ_global_data = (.*?);</script>", res_data
            )
            format_str = global_data[0].replace('\\"', "")
            json_data = json.loads(format_str)

            self.ae = re.findall(r"&quot;,null,null,null,&quot;(.*?)&quot;", res_data)[
                0
            ]
            self.azt = json_data.get("OewCAd").split(",").pop()[:-1]
            self.dsh = json_data.get("Qzxixc")
            is_success = status_code == 200
        except Exception as e:
            Log.error(str(e))

        return is_success

    async def call_validate_personal(self):
        url = VALIDATE_PERSONAL_URL
        header = VALIDATE_PERSONAL_HEADER
        raw_data = f'continue=https://accounts.google.com/&dsh={self.dsh}&flowEntry=ServiceLogin&followup=https://accounts.google.com/&ifkv=AVQVeyxXhIn2uVhrnXzAymbHAW8ijA5r7aQqTBzTFPzp8QXPBbsRBVS2VlE84q_6bwehT_Hu9dYW&theme=glif&f.req=["{self.ae}","Toan","Le","Toan","Le"%2C0%2C1%2Cnull%2Cnull%2C%22web-glif-signup%22%2C0%2Cnull%2C1%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2C1%5D&azt={self.azt}&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C1%2C1%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A93%3A0&checkedDomains=youtube&pstMsg=1&'

        is_success = False
        try:
            response = await self.session.post(
                url,
                data=raw_data,
                headers=header,
                timeout=20,
                raise_for_status=True,
                proxy=Proxy.get_proxy(),
            )
            status_code = response.status
            res_data = await response.text()
            self.tl = re.findall(r"gf\.ttu\",null,\"(.*?)\"]", res_data)[0]
            is_success = status_code == 200
        except Exception as e:
            Log.error(str(e))

        return is_success

    async def call_username_availability(self, username: str):
        async with self.semaphore:
            url = USERNAME_AVAILABILITY_URL.format(self.tl)
            header = USERNAME_AVAILABILITY_HEADER
            raw_data = f"continue=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&dsh={self.dsh}&flowEntry=ServiceLogin&followup=https%3A%2F%2Faccounts.google.com%2Fb%2F0%2FAddMailService&ifkv=AVQVeyyf9q-bmuViM90CQymcrX8ivPqO4BAkyc_7NSpErWpdN34mvHk88n5d45AkoQZpe0K9EpzZ&theme=glif&f.req=%5B%22TL%3A{self.tl}%22%2C%22{username}%22%2C0%2C0%2C1%2Cnull%2C0%2C762%5D&azt={self.azt}&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22VN%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C1%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C1%2C1%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&checkConnection=youtube%3A192%3A0&checkedDomains=youtube&pstMsg=1&"
            is_success = False
            try:
                response = await self.session.post(
                    url,
                    data=raw_data,
                    headers=header,
                    timeout=60,
                    raise_for_status=True,
                    proxy=Proxy.get_proxy(),
                )
                status_code = response.status
                res_data = await response.text()
                failed = '"er",null,null,null,null,400'
                success = ["1", "5", "7"]
                code = re.findall(r"gf\.uar\",(.*?),\"TL", res_data)
                code = code[0] if code else None
                print(f"{username}: {code}")

                if failed in res_data:
                    return False, True
                if status_code == 200 and code in success:
                    is_success = True

            except Exception as e:
                print(e)
                return False, True

        return is_success, False

    async def setup(self) -> bool:
        is_success = await self.call_signup()
        if not is_success:
            return False

        validate_success = await self.call_validate_personal()
        if not validate_success:
            return False

        return True

    async def run(self, username):
        validate_username, retry = await self.call_username_availability(username)
        if retry:
            Log.warning(username)
        
        if validate_username:
            Log.success(username)
        else:
            Log.error(username)

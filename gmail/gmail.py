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


class GmailAccount:
    def __init__(self, session):
        self.session = session
        self.timeout = 5
        self.azt = ''
        self.ae = ''
        self.dsh = ''

    def validate_result(self, response) -> bool:
        pass

    async def call_signup(self):
        url = SIGNUP_URL
        header = SIGNUP_HEADER
        is_success = False
        try:
            response = await self.session.get(
                url,
                headers=header,
                timeout=self.timeout,
            )
            status_code = response.status
            res_data = await response.text()
            
            global_data = re.findall(
                r"window.WIZ_global_data = (.*?);</script>", res_data
            )
            format_str = global_data[0].replace("\\\"", "")
            json_data = json.loads(format_str)
            
            self.ae = json_data.get("thykhd")
            self.azt = json_data.get("OewCAd").split(',').pop()[:-1]
            self.dsh = json_data.get("Qzxixc")
            
            print(self.ae)
            print(self.azt)

            is_success = status_code == 200
        except Exception as e:
            print(str(e))

        return is_success

    async def call_validate_personal(self):
        url = VALIDATE_PERSONAL_URL
        header = VALIDATE_PERSONAL_HEADER
        data = {
            "continue": "https://mail.google.com/mail/u/0/&dsh=S-1357936412:1690047970143809&emr=1&flowEntry=ServiceLogin",
            "dsh": "S-1357936412:1690047970143809",
            "flowEntry": "ServiceLogin",
            "followup": "https://mail.google.com/mail/u/0/",
            "ifkv": "AeDOFXhCFmTSacmtS5Gfy8i8JiIMSGaHMtiOZMuhOOug5SJMJsIJQYdZVPEvR8s8z0fPzepEsJaG",
            "theme": "glif",
            "f.req": [
                self.ae,
                "Toan",
                "Le",
                "Toan",
                "Le",
                0,
                1,
                None,
                None,
                "web-glif-signup",
                0,
                None,
                1,
                [
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    [],
                ],
                1,
            ],
            "azt": self.azt,
            "cookiesDisabled": False,
            "deviceinfo": [
                None,
                None,
                None,
                [],
                None,
                "VN",
                None,
                None,
                None,
                "GlifWebSignIn",
                None,
                [
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    [],
                ],
                None,
                None,
                None,
                None,
                1,
                None,
                0,
                1,
                "",
                None,
                None,
                1,
                1,
            ],
            "gmscoreversion": "undefined",
            "flowName": "GlifWebSignIn",
            "checkConnection": "youtube:86:0",
            "checkedDomains": "youtube",
            "pstMsg": 1,
        }
        is_success = False
        try:
            response = await self.session.post(
                url, data=data, headers=header, timeout=self.timeout
            )
            status_code = response.status
            res_data = await response.text()
            print(status_code)
            print(res_data)
            is_success = status_code == 200
        except Exception as e:
            print(e)

        return is_success

    async def call_usernamea_vailability(self, tl: str, username: str):
        url = USERNAME_AVAILABILITY_URL.format(tl)
        header = USERNAME_AVAILABILITY_HEADER
        data = {
            "continue": "https://accounts.google.com/",
            "dsh": self.dsh,
            "flowEntry": "ServiceLogin",
            "followup": "https://accounts.google.com/",
            "ifkv": "AVQVeyw6J6WFYpq-qEm7_Z0aSnpETfpc7jiMyPQzWVigNEl3EDQpW3aOKWztqNdvIFKisVlxpP7_",
            "theme": "glif",
            "f.req": [f"TL:{tl}", username, 0, 0, 1, None, 0, 30481],
            "azt": self.azt,
            "cookiesDisabled": False,
            "deviceinfo": [
                None,
                None,
                None,
                [],
                None,
                "VN",
                None,
                None,
                None,
                "GlifWebSignIn",
                None,
                [
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    None,
                    [],
                    None,
                    None,
                    None,
                    None,
                    [],
                ],
                None,
                None,
                None,
                None,
                1,
                None,
                0,
                1,
                "",
                None,
                None,
                1,
                1,
            ],
            "gmscoreversion": "undefined",
            "flowName": "GlifWebSignIn",
            "checkConnection": "youtube:86:0",
            "checkedDomains": "youtube",
            "pstMsg": 1,
        }
        is_success = False

        return is_success

    async def check_account(self, username: str) -> bool:
        is_success = await self.call_signup()
        tl = await self.call_validate_personal()
        # res = await self.call_usernamea_vailability(tl, azt, username)
        # is_success = self.validate_result(res)

        return is_success

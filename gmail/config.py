SIGNUP_URL = (
    "https://accounts.google.com/signup/v2?flowName=GlifWebSignIn&flowEntry=SignUp"
)
SIGNUP_HEADER = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Pragma": "no-cache",
    "Accept": "*/*",
}

VALIDATE_PERSONAL_URL = "https://accounts.google.com/_/signup/validatepersonaldetails?hl=vi&_reqid=2780&rt=j"
VALIDATE_PERSONAL_HEADER = {
    "Accept": "*/*",
    "Accept-Language": "en-USen;q=0.9",
    "Content-Length": "1463",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Google-Accounts-Xsrf": "1",
    "Origin": "https://accounts.google.com",
    "Referer": "https://accounts.google.com/signup/v2/createaccount?biz=false&cc=VN&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S-1357936412%3A1690047970143809&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AeDOFXhCFmTSacmtS5Gfy8i8JiIMSGaHMtiOZMuhOOug5SJMJsIJQYdZVPEvR8s8z0fPzepEsJaG&osid=1&service=mail",
    "Sec-Ch-Ua": '"Not/A)Brand";v="99" "Brave";v="115" "Chromium";v="115"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": '"',
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Ch-Ua-Platform-Version": "15.0.0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "X-Same-Domain": "1",
    "Cookie": "NID=511=LMx5QAr8l1q9I_DURlv1f6GB6l7DU8aM02XKt-QdGb00len83AHv5mZgdzQs3QSAf49wrieDvrshyEcUf-oNowB3SvwUR1RScz-s90_on3ourasiVREdoCZiRtjtZXxf5lzZV5BtIm9lE3UPWPLje-IzwxA3a0pqrIn9DeI12nM; OTZ=7272549_28_28__28_; __Host-GAPS=1:T29VJEKRsh3Ozeild6v75kGDQJFurg:qKuYGiv287Hd5LQl",
}

USERNAME_AVAILABILITY_URL = (
    "https://accounts.google.com/_/signup/usernameavailability?hl=vi&TL={}&rt=j"
)
USERNAME_AVAILABILITY_HEADER = {
    "Accept": "*/*",
    "Accept-Language": "en-USen;q=0.9",
    "Content-Length": "1463",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Google-Accounts-Xsrf": "1",
    "Origin": "https://accounts.google.com",
    "Referer": "https://accounts.google.com/signup/v2/createaccount?biz=false&cc=VN&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S-1357936412%3A1690047970143809&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AeDOFXhCFmTSacmtS5Gfy8i8JiIMSGaHMtiOZMuhOOug5SJMJsIJQYdZVPEvR8s8z0fPzepEsJaG&osid=1&service=mail",
    "Sec-Ch-Ua": '"Not/A)Brand";v="99" "Brave";v="115" "Chromium";v="115"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": '""',
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "X-Same-Domain": "1",
    "Cookie": "__Host-GAPS=1:M3pXT--0QYt3qFYb7hPdW5j6m87ujg:i0eWVz3qFrUPnYrk",
}

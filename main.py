import os
from os import getenv
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from fake_headers import Headers
import random
from pprint import pprint

load_dotenv()
session = requests.Session()

# not successfully
# url_login = "https://ticket.pobeda.aero/websky/json/login"
# profile_url = "https://ticket.pobeda.aero/websky/#/private/profile"

url_login = "https://shop220.ru/index.php"
profile_url = "https://shop220.ru/?action=cabinet"

ua = UserAgent().random
# print(f"USER-AGENT:   {ua}")

header = {
    "user-agent": ua
}

# headers = Headers()
# header = headers.generate()

# data = {
# "login": getenv("POBEDA_LOGIN"),
# "password": getenv("POBEDA_PASSWORD")
# }

data = {
    "action": getenv("SHOP220_ACTION"),
    "keepoldcart": getenv("SHOP220_KEEPOLDCART"),
    "Username": getenv("SHOP220_LOGIN"),
    "Password": getenv("SHOP220_PASSWORD")
}


def main():
    response = session.post(url=url_login, data=data, headers=header)
    print(response.status_code)
    print(response.text)
    # print(response.json())


if __name__ == "__main__":
    main()

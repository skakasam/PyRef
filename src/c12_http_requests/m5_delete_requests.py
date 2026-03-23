"""Making DELETE Requests with Python Requests Library"""

import requests
from m1_api_config import BEARER_TOKEN, TIMEOUT, USER_RESOURCE
from termcolor import colored


def delete_user(id: int):
    """Create a new User"""
    headers = {
        "Authorization": BEARER_TOKEN,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    return requests.delete(
        f"{USER_RESOURCE}{id}",
        headers=headers,
        timeout=TIMEOUT,
    )


if __name__ == "__main__":
    try:
        response = delete_user(id=8153258)
        print(f"{colored('Status   :', 'magenta')} {response.status_code}")

        if response.ok:
            print(f"{colored('Success  :', 'green')} User deleted! {response.text}")
        else:
            print(f"{colored('Warning  :', 'yellow')} {response.text}")
    except requests.RequestException as ex:
        print(f"{colored('Failure  :', 'red')} {ex}")

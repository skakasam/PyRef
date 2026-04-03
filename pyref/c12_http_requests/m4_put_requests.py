"""Making PUT Requests with Python Requests Library"""

import requests
from m1_api_config import BEARER_TOKEN, TIMEOUT, USER_RESOURCE
from termcolor import colored


def update_user(
    *,
    id: int,
    name: str | None = None,
    email: str | None = None,
    gender: str | None = None,
    status: str | None = None,
):
    """Update an existing User"""
    headers = {
        "Authorization": BEARER_TOKEN,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    payload = {}
    if name:
        payload["name"] = name
    if email:
        payload["email"] = email
    if gender:
        payload["gender"] = gender
    if status:
        payload["status"] = status

    return requests.put(
        f"{USER_RESOURCE}{id}",
        headers=headers,
        data=payload,
        timeout=TIMEOUT,
    )


if __name__ == "__main__":
    try:
        response = update_user(id=8153258, email="emma.watson@example.io")
        print(f"{colored('Status   :', 'magenta')} {response.status_code}")

        if response.ok:
            print(f"{colored('Success  :', 'green')} User updated! {response.text}")
        else:
            print(f"{colored('Warning  :', 'yellow')} {response.text}")
    except requests.RequestException as ex:
        print(f"{colored('Failure  :', 'red')} {ex}")

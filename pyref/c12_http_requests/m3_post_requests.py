"""Making POST Requests with Python Requests Library"""

import requests
from m1_api_config import BEARER_TOKEN, TIMEOUT, USER_RESOURCE
from termcolor import colored


def create_user(name: str, email: str, gender: str, status: str):
    """Create a new User"""
    headers = {
        "Authorization": BEARER_TOKEN,
        "Content-Type": "application/json",
        # for form-encoding use "Content-Type": "application/x-www-form-urlencoded"
        "Accept": "application/json",
    }

    payload = {
        "name": name,
        "email": email,
        "gender": gender,
        "status": status,
    }

    return requests.post(
        USER_RESOURCE,
        headers=headers,
        json=payload,
        # for form-encoding use, data=payload
        timeout=TIMEOUT,
    )


if __name__ == "__main__":
    try:
        response = create_user("Emma Watson", "ewatson@example.io", "female", "active")
        print(f"{colored('Status   :', 'magenta')} {response.status_code}")

        if response.ok:
            user_id = response.json().get("id")
            print(f"{colored('Success  :', 'green')} User (ID={user_id}) created! {response.text}")
        else:
            print(f"{colored('Warning  :', 'yellow')} {response.text}")
    except requests.RequestException as ex:
        print(f"{colored('Failure  :', 'red')} {ex}")

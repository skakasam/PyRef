"""Making GET requests with the requests library."""

import requests
from m1_api_config import BEARER_TOKEN, RETRIES, TIMEOUT, USER_RESOURCE
from requests.exceptions import RequestException
from termcolor import colored


def get_users(*, id: int | None = None, page_no=1, per_page=5):
    """Get a list of users from the API."""
    if id:
        url = f"{USER_RESOURCE}/{id}"
        params = {}
    else:
        url = USER_RESOURCE
        params = {"page": page_no, "per_page": per_page}

    headers = {"Authorization": BEARER_TOKEN, "Accept": "application/json"}
    print(f"{url=}")
    return requests.get(
        url,
        headers=headers,  # HTTP headers
        params=params,  # Query parameters
        timeout=TIMEOUT,  # Timeout in seconds
    )


if __name__ == "__main__":
    for attempt in range(RETRIES):
        try:
            response = get_users(id=8153258)
            print(f"{colored('Status Code      :', 'blue')} {response.status_code}")
            print(f"{colored('Response Body    :', 'green')} {response.json()}")
            break
        except RequestException as ex:
            print(f"{colored('Exception Message:', 'red')} {ex}")
            continue
    else:
        print(colored("Max retries exceeded. Unable to retrieve users!", "red"))

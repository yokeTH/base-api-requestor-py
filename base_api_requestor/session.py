

import random
from httpx import Client
from typing import Optional, Dict, List
from os.path import exists


def create_session(headers: Optional[Dict], cookies: Optional[Dict]) -> Client:
    return Client(headers=headers, cookies=cookies)


def create_proxy_session(proxy: str, headers: Optional[Dict], cookies: Optional[Dict]) -> Client:
    return Client(headers=headers, cookies=cookies, proxy=proxy)


def copy_client_state(from_client: Client, to_client: Client):
    to_client.headers.update(from_client.headers)
    to_client.cookies.update(from_client.cookies)


def load_proxies(file_path: str = 'proxy_list.txt') -> List[str]:
    if not exists(file_path):
        return []

    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def get_random_proxy(proxies: List[str]) -> str:
    if len(proxies) == 0:
        raise Exception('length of proxies is 0 can\'t get random proxy')
    return random.choice(proxies)

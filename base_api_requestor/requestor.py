from .logger import logger
from .session import create_session, create_proxy_session, copy_client_state, load_proxies, get_random_proxy
from typing import Literal
import httpx


class Requestor:
    def __init__(self, headers={}, cookies={}) -> None:
        logger.debug('create new Requestor')
        self.proxy_list = load_proxies()
        self.client = create_session(headers=headers, cookies=cookies)

    def base_request(self, method: Literal['GET', 'OPTIONS', 'HEAD', 'POST', 'PUT', 'PATCH', 'DELETE'], url: str, use_proxy: bool, **kwargs) -> httpx.Response:
        if use_proxy:
            proxy = get_random_proxy(self.proxy_list)
            logger.debug(f'using proxy {proxy}')
            client = create_proxy_session(proxy, {}, {})
            logger.debug(f'copy state {self.client.headers} {
                         self.client.cookies}')
            copy_client_state(self.client, client)
        else:
            client = self.client

        response = client.request(method=method, url=url, **kwargs)
        logger.debug(f'response status code: {response.status_code}')
        logger.debug(f'response headers: {response.headers}')
        logger.debug(f'response cookies: {response.cookies}')
        logger.debug(f'response text: {response.text}')
        copy_client_state(client, self.client)

        return response

    def get(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'GET request to {url}')
        return self.base_request('GET', url, use_proxy, **kwargs)

    def post(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'POST request to {url}')
        return self.base_request('POST', url, use_proxy, **kwargs)

    def put(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'PUT request to {url}')
        return self.base_request('PUT', url, use_proxy, **kwargs)

    def delete(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'DELETE request to {url}')
        return self.base_request('DELETE', url, use_proxy, **kwargs)

    def patch(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'PATCH request to {url}')
        return self.base_request('PATCH', url, use_proxy, **kwargs)

    def head(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'HEAD request to {url}')
        return self.base_request('HEAD', url, use_proxy, **kwargs)

    def options(self, url: str, use_proxy: bool = False, **kwargs) -> httpx.Response:
        logger.debug(f'OPTIONS request to {url}')
        return self.base_request('OPTIONS', url, use_proxy, **kwargs)

import httpx


class BaseService:
    def __init__(self, api_key: str, server_prefix: str):
        self._api_key = api_key
        self._client: httpx.Client = httpx.Client(base_url=server_prefix, headers=
        {
            'x-api-key': self._api_key
        })


class AsyncBaseService:
    def __init__(self, api_key: str, server_prefix: str):
        self._api_key = api_key
        self._client: httpx.AsyncClient = httpx.AsyncClient(base_url=server_prefix, headers=
        {
            'x-api-key': self._api_key
        })

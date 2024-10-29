import httpx


class Client(httpx.Client):
    def __init__(self):
        super().__init__()

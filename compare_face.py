from services.recognition_service import RecognitionService


class CompareFace:
    def __init__(self, domain: str, port: int):
        self.recognition_service = None
        self._server_prefix = f'{domain}:{port}'

    def init_recognition_service(self, api_key):
        self.recognition_service: RecognitionService = RecognitionService(api_key, self._server_prefix)
        return self.recognition_service

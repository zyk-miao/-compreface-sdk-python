from services import RecognitionService, DetectionService, VerificationService


class CompareFace:
    def __init__(self, domain: str, port: int):
        self.recognition_service = None
        self.detect_service = None
        self.verify_service = None
        self._server_prefix = f'{domain}:{port}'

    def init_recognition_service(self, api_key)->RecognitionService:
        self.recognition_service: RecognitionService = RecognitionService(api_key, self._server_prefix)
        return self.recognition_service

    def init_detect_service(self, api_key)->DetectionService:
        self.detect_service: DetectionService = DetectionService(api_key, self._server_prefix)
        return self.detect_service

    def init_verify_service(self, api_key)->VerificationService:
        self.verify_service: VerificationService = VerificationService(api_key, self._server_prefix)
        return self.verify_service

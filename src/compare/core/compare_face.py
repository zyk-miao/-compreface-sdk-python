from ..services.detection_service import DetectionService, AsyncDetectionService
from ..services.verification_service import VerificationService, AsyncVerificationService
from ..services.recognition_service import RecognitionService, AsyncRecognitionService


class CompareFace:
    def __init__(self, domain: str, port: int):
        self.recognition_service = None
        self.detect_service = None
        self.verify_service = None
        self.async_recognition_service = None
        self.async_detect_service = None
        self.async_verify_service = None
        self._server_prefix = f'{domain}:{port}'

    def init_recognition_service(self, api_key) -> RecognitionService:
        self.recognition_service: RecognitionService = RecognitionService(api_key, self._server_prefix)
        return self.recognition_service

    def init_detect_service(self, api_key) -> DetectionService:
        self.detect_service: DetectionService = DetectionService(api_key, self._server_prefix)
        return self.detect_service

    def init_verify_service(self, api_key) -> VerificationService:
        self.verify_service: VerificationService = VerificationService(api_key, self._server_prefix)
        return self.verify_service

    def init_async_recognition_service(self, api_key) -> AsyncRecognitionService:
        self.async_recognition_service: AsyncRecognitionService = AsyncRecognitionService(api_key, self._server_prefix)
        return self.async_recognition_service

    def init_async_detect_service(self, api_key) -> AsyncDetectionService:
        self.async_detect_service: AsyncDetectionService = AsyncDetectionService(api_key, self._server_prefix)
        return self.async_detect_service

    def init_async_verify_service(self, api_key) -> AsyncVerificationService:
        self.async_verify_service: AsyncVerificationService = AsyncVerificationService(api_key, self._server_prefix)
        return self.async_verify_service

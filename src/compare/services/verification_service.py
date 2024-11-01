import aiofiles

from .base_service import BaseService, AsyncBaseService
from .server_api_list import VERIFY_URL


class VerificationService(BaseService):
    def __init__(self, api_key: str, server_prefix: str, ):
        super().__init__(api_key, server_prefix)

    def verify(self, source_image_path: str, target_image_path: str, limit: int = 0, threshold: float = None,
               face_plugins: str = None,
               status: bool = False):
        rv = self._client.post(f'{VERIFY_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, files={
            'source_image': open(source_image_path, 'rb'),
            'target_image': open(target_image_path, 'rb')
        })
        return rv.json()

    def verify_by_64(self, source_image_64: str, target_image_64: str, limit: int = 0, threshold: float = None,
                     face_plugins: str = None,
                     status: bool = False):
        rv = self._client.post(f'{VERIFY_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={
            'source_image': source_image_64,
            'target_image': target_image_64
        })
        return rv.json()


class AsyncVerificationService(AsyncBaseService):
    def __init__(self, api_key: str, server_prefix: str, ):
        super().__init__(api_key, server_prefix)

    async def verify(self, source_image_path: str, target_image_path: str, limit: int = 0, threshold: float = None,
                     face_plugins: str = None,
                     status: bool = False):
        source_image = await aiofiles.open(source_image_path, mode='rb')
        target_image = await aiofiles.open(target_image_path, mode='rb')
        source_content = await source_image.read()
        target_content = await target_image.read()
        rv = await self._client.post(f'{VERIFY_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, files={
            'source_image': (source_image.name, source_content),
            'target_image': (target_image.name, target_content)
        })
        return rv.json()

    async def verify_by_64(self, source_image_64: str, target_image_64: str, limit: int = 0, threshold: float = None,
                           face_plugins: str = None,
                           status: bool = False):
        rv = await self._client.post(f'{VERIFY_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={
            'source_image': source_image_64,
            'target_image': target_image_64
        })
        return rv.json()

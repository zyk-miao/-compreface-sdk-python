import os.path
import typing
import uuid

import aiofiles

from .base_service import BaseService, AsyncBaseService
from .server_api_list import SUBJECT_URL, FACE_URL, RECOGNIZE_URL


class RecognitionService(BaseService):
    def __init__(self, api_key: str, server_prefix: str):

        super().__init__(api_key, server_prefix)

    def add_a_subject(self, subject: str) -> dict:
        rv = self._client.post(f'{SUBJECT_URL}', json={
            'subject': subject
        })
        return rv.json()

    def rename_a_subject(self, subject: str, new_subject) -> dict:
        rv = self._client.put(f'{SUBJECT_URL}/{subject}', json={
            'subject': new_subject
        })
        return rv.json()

    def delete_a_subject(self, subject: str) -> dict:
        rv = self._client.delete(f'{SUBJECT_URL}/{subject}')
        return rv.json()

    def delete_all_subjects(self) -> dict:
        rv = self._client.delete(f'{SUBJECT_URL}')
        return rv.json()

    def list_all_subjects(self) -> dict:
        rv = self._client.get(f'{SUBJECT_URL}')
        return rv.json()

    def add_a_img(self, subject: str, img_path: str, threshold: float = None) -> dict:
        with open(img_path, 'rb') as f:
            rv = self._client.post(f'{FACE_URL}', params={
                'subject': subject,
                'threshold': threshold
            }, files={'file': f})
            return rv.json()

    def add_a_img_by_64(self, subject: str, img64: str, threshold: float = None) -> dict:
        rv = self._client.post(f'{FACE_URL}', params={
            'subject': subject,
            'threshold': threshold
        }, json={'file': img64})
        return rv.json()

    def list_saved_img_subject(self, page: int = 0, size: int = 10, subject: str = None) -> dict:
        params = {
            'page': page,
            'size': size,
        }
        if subject:
            params['subject'] = subject
        rv = self._client.get(f'{FACE_URL}', params=params)
        return rv.json()

    def delete_saved_img_by_subject(self, subject: str) -> dict:
        rv = self._client.delete(f'{FACE_URL}', params={
            'subject': subject
        })
        return rv.json()

    def delete_a_img(self, img_id: str) -> dict:
        rv = self._client.delete(f'{FACE_URL}/{img_id}')
        return rv.json()

    def delete_multiple_img(self, img: typing.List[str]) -> dict:
        rv = self._client.post(f'{FACE_URL}/delete', json=img)
        return rv.json()

    def direct_download_img(self, img_id: str, save_path: str = None) -> str:
        if not save_path:
            save_path = f'{uuid.uuid4()}.jpg'
        with open(save_path, 'wb') as f:
            rv = self._client.get(f'{self._client.base_url}/api/v1/static/{self._api_key}/images/{img_id}')
            f.write(rv.content)
            return os.path.abspath(save_path)

    def download_a_img(self, img_id: str, save_path: str = None) -> str:
        if not save_path:
            save_path = f'{uuid.uuid4()}.jpg'
        with open(save_path, 'wb') as f:
            rv = self._client.get(f'{FACE_URL}/{img_id}/img')
            f.write(rv.content)
            return os.path.abspath(save_path)

    def recognize(self, img_path: str, limit: int = 0, threshold: float = None, prediction_count: int = 1,
                  face_plugins: str = None, status: bool = False, detect_faces: bool = True) -> dict:
        with open(img_path, 'rb') as f:
            rv = self._client.post(f'{RECOGNIZE_URL}', params={
                'limit': limit,
                'threshold': threshold,
                'prediction_count': prediction_count,
                'face_plugins': face_plugins,
                'status': status,
                'detect_faces': detect_faces
            }, files={'file': f})
            return rv.json()

    def recognize_by_64(self, img64: str, limit: int = 0, threshold: float = None, prediction_count: int = 1,
                        face_plugins: str = None, status: bool = False, detect_faces: bool = True) -> dict:
        rv = self._client.post(f'{RECOGNIZE_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'prediction_count': prediction_count,
            'face_plugins': face_plugins,
            'status': status,
            'detect_faces': detect_faces
        }, json={'file': img64})
        return rv.json()

    def verify(self, img_path: str, img_id: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
               status: bool = False) -> dict:
        with open(img_path, 'rb') as f:
            rv = self._client.post(f'{FACE_URL}/{img_id}/verify', params={
                'limit': limit,
                'threshold': threshold,
                'face_plugins': face_plugins,
                'status': status,
            }, files={'file': f})
            return rv.json()

    def verify_by_64(self, img_64: str, img_id: str, limit: int = 0, threshold: float = None, face_plugins: str = None,
                     status: bool = False) -> dict:
        rv = self._client.post(f'{FACE_URL}/{img_id}/verify', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={'file': img_64})
        return rv.json()


class AsyncRecognitionService(AsyncBaseService):
    def __init__(self, api_key: str, server_prefix: str):

        super().__init__(api_key, server_prefix)

    async def add_a_subject(self, subject: str) -> dict:
        rv = await self._client.post(f'{SUBJECT_URL}', json={
            'subject': subject
        })
        return rv.json()

    async def rename_a_subject(self, subject: str, new_subject) -> dict:
        rv = await self._client.put(f'{SUBJECT_URL}/{subject}', json={
            'subject': new_subject
        })
        return rv.json()

    async def delete_a_subject(self, subject: str) -> dict:
        rv = await self._client.delete(f'{SUBJECT_URL}/{subject}')
        return rv.json()

    async def delete_all_subjects(self) -> dict:
        rv = await self._client.delete(f'{SUBJECT_URL}')
        return rv.json()

    async def list_all_subjects(self) -> dict:
        rv = await self._client.get(f'{SUBJECT_URL}')
        return rv.json()

    async def add_a_img(self, subject: str, img_path: str, threshold: float = None) -> dict:
        async with aiofiles.open(img_path, 'rb') as f:
            content = await f.read()
            rv = await self._client.post(f'{FACE_URL}', params={
                'subject': subject,
                'threshold': threshold
            }, files={'file': (f.name,content)})
            return rv.json()

    async def add_a_img_by_64(self, subject: str, img64: str, threshold: float = None) -> dict:
        rv = await self._client.post(f'{FACE_URL}', params={
            'subject': subject,
            'threshold': threshold
        }, json={'file': img64})
        return rv.json()

    async def list_saved_img_subject(self, page: int = 0, size: int = 10, subject: str = None) -> dict:
        params = {
            'page': page,
            'size': size,
        }
        if subject:
            params['subject'] = subject
        rv = await self._client.get(f'{FACE_URL}', params=params)
        return rv.json()

    async def delete_saved_img_by_subject(self, subject: str) -> dict:
        rv = await self._client.delete(f'{FACE_URL}', params={
            'subject': subject
        })
        return rv.json()

    async def delete_a_img(self, img_id: str) -> dict:
        rv = await self._client.delete(f'{FACE_URL}/{img_id}')
        return rv.json()

    async def delete_multiple_img(self, img: typing.List[str]) -> dict:
        rv = await self._client.post(f'{FACE_URL}/delete', json=img)
        return rv.json()

    async def direct_download_img(self, img_id: str, save_path: str = None) -> str:
        if not save_path:
            save_path = f'{uuid.uuid4()}.jpg'
        async with aiofiles.open(save_path, 'wb') as f:
            rv = await self._client.get(f'{self._client.base_url}/api/v1/static/{self._api_key}/images/{img_id}')
            await f.write(rv.content)
            return os.path.abspath(save_path)

    async def download_a_img(self, img_id: str, save_path: str = None) -> str:
        if not save_path:
            save_path = f'{uuid.uuid4()}.jpg'
        async with aiofiles.open(save_path, 'wb') as f:
            rv = await self._client.get(f'{FACE_URL}/{img_id}/img')
            await f.write(rv.content)
            return os.path.abspath(save_path)

    async def recognize(self, img_path: str, limit: int = 0, threshold: float = None, prediction_count: int = 1,
                        face_plugins: str = None, status: bool = False, detect_faces: bool = True) -> dict:
        async with aiofiles.open(img_path, 'rb') as f:
            content=await f.read()
            rv = await self._client.post(f'{RECOGNIZE_URL}', params={
                'limit': limit,
                'threshold': threshold,
                'prediction_count': prediction_count,
                'face_plugins': face_plugins,
                'status': status,
                'detect_faces': detect_faces
            }, files={'file': (f.name, content)})
            return rv.json()

    async def recognize_by_64(self, img64: str, limit: int = 0, threshold: float = None, prediction_count: int = 1,
                              face_plugins: str = None, status: bool = False, detect_faces: bool = True) -> dict:
        rv = await self._client.post(f'{RECOGNIZE_URL}', params={
            'limit': limit,
            'threshold': threshold,
            'prediction_count': prediction_count,
            'face_plugins': face_plugins,
            'status': status,
            'detect_faces': detect_faces
        }, json={'file': img64})
        return rv.json()

    async def verify(self, img_path: str, img_id: str, limit: int = 0, threshold: float = None,
                     face_plugins: str = None,
                     status: bool = False) -> dict:
        async with aiofiles.open(img_path, 'rb') as f:
            content=await f.read()
            rv = await self._client.post(f'{FACE_URL}/{img_id}/verify', params={
                'limit': limit,
                'threshold': threshold,
                'face_plugins': face_plugins,
                'status': status,
            }, files={'file': (f.name,content)})
            return rv.json()

    async def verify_by_64(self, img_64: str, img_id: str, limit: int = 0, threshold: float = None,
                           face_plugins: str = None,
                           status: bool = False) -> dict:
        rv = await self._client.post(f'{FACE_URL}/{img_id}/verify', params={
            'limit': limit,
            'threshold': threshold,
            'face_plugins': face_plugins,
            'status': status,
        }, json={'file': img_64})
        return rv.json()

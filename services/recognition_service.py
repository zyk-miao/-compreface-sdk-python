import typing

import httpx
from distributed.utils_test import client

from sever_list.recognition import SUBJECT_URL, FACE_URL


class RecognitionService:
    def __init__(self, api_key: str, server_prefix: str):
        self._api_key = api_key
        self._client: httpx.Client = httpx.Client(base_url=server_prefix, headers=
        {
            'x-api-key': self._api_key
        })

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

    def list_all_subjects(self):
        rv = self._client.get(f'{SUBJECT_URL}')
        return rv.json()

    def add_a_img(self, subject: str, img_path: str, threshold: float = None) -> dict:
        with open(img_path, 'rb') as f:
            rv = self._client.post(f'{FACE_URL}', params={
                'subject': subject,
                'threshold': threshold
            }, files={'file': f})
            return rv.json()

    def list_saved_img_subject(self, page: int = None, size: int = None, subject: str = None) -> dict:
        rv = self._client.get(f'{FACE_URL}', params={
            'page': page,
            'size': size,
            'subject': subject
        })
        return rv.json()

    def delete_saved_img_by_subject(self, subject: str = None):
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

    def direct_download_img(self, img_id: str) -> bytes:
        rv = self._client.get(f'{self._client.base_url}/api/v1/static/{self._api_key}/images/{img_id}')
        return rv.content

from abc import ABC, abstractmethod
from typing import Any
from schemas.dataclass.http import HttpResponse
from custom_types.http_types import Headers, Params, Data

class AbstractHttpClient(ABC):
    @abstractmethod
    async def get(self, url: str, params: Params, headers: Headers) -> HttpResponse:
        """
        Отправляет GET запрос
        Args:
            url (str): URL запроса
            params (Params): Query параметры запроса. По умолчанию None.
            headers (Headers): Заголовки запроса. По умолчанию None.

        Returns:
            HttpResponse: Объект ответа от сервера.

        """
        ...
    @abstractmethod
    async def post(self,  url: str, data: Data, headers: Headers) -> HttpResponse:
        """
        Отправляет POST запрос
        Args:
            url (str): URL запроса
            data (Data): Тело запроса в формате (JSON). По умолчанию None.
            headers (Headers): Заголовки запроса .По умолчанию None.
            Returns:
            HttpResponse: Объект ответа от сервера.
        """
        ...

import httpx
from httpx import AsyncClient
from typing import Any

from schemas.dataclass.http import HttpResponse
from enums.http import HttpMethodEnum
from custom_types.http_types import Headers, Params, Data
from .abrstract_http_client import AbstractHttpClient
import json

class AsyncHttpxClient(AbstractHttpClient):
    def __init__(
        self,
        client: AsyncClient
    ) -> None:
        """

        Args:
            client (AsyncClient): объект типа httpx.AsyncClient

        Returns:
              None
        """
        self._client = client

    async def request(self, url: str, method: HttpMethodEnum, **kwargs) -> HttpResponse:
        """
        Метод для выполнения запросов
        Args:
            url (str): URL запроса
            method (HttpMethodEnum): тип http запроса

        Returns:
            HttpResponse: Объект ответа от сервера

        """
        try:
            result = await self._client.request(url=url, method=method, **kwargs)

            try:
                json_data = json.loads(await result.json())
            except (ValueError, UnicodeError):
                print("Ошибка декодирования json")
                json_data = None

            return HttpResponse(
                status_code=result.status_code,
                json_data=json_data,
                headers=result.headers,
                text=result.text.encode("utf-8")
            )
        except httpx.RequestError as e:
            print(f"Произошла ошибка при выполнении запроса: {e.args}: {e.__class__}")
            raise
        except httpx.TimeoutException as e:
            print(f"Ошибка ожидания ответа")
            raise
        except Exception as e:
            print(f"Неизвестная ошибка: : {e.__class__}")
            raise

    async def get(self, url: str, params: Params=None, headers: Headers=None) -> HttpResponse:
        return await self.request(url=url, method=HttpMethodEnum.GET, params=params, headers=headers)

    async def post(self, url: str, data: Data = None, headers: Headers = None) -> HttpResponse:
        return await self.request(url=url, method=HttpMethodEnum.POST,json=data, headers=headers)

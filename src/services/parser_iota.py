from infrastructure.http.async_httpx_client import AsyncHttpxClient
from httpx import AsyncClient
from bs4 import BeautifulSoup
from models.models import CountryModel, CityModel
from urllib.parse import urlparse, parse_qs
class ParserIATA:
    def __init__(self):
        self._client = AsyncHttpxClient(
            client=AsyncClient(
                base_url="http://betravel.ru"
            )
        )


    async def run(self):
        urls = await self.get_urls()

    async def get_urls(self) -> list[str]:
        response = await self._client.get("/iata-country-list.php")
        soup = BeautifulSoup(response.text)
        urls = [
            href
            for country in soup.find_all("td",class_="CountryList")
            for url in country.find_all("a")
            if (href:=url.get("href")) and parse_qs(urlparse(href).query)
        ]
        return urls
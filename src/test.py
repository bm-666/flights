import asyncio

from httpx import  Response
BASE_URL = "https://api.travelpayouts.com/aviasales/v3/"
prices_for_dates = "/prices_for_dates"
from datetime import datetime

from services.parser_iota import ParserIATA
async def main():
    parser = ParserIATA()
    await parser.run()
asyncio.run(main())
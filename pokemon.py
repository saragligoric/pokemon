import aiohttp
import asyncio
from typing import List

pokemon_urls = ['https://pokeapi.co/api/v2/pokemon/151', 'https://pokeapi.co/api/v2/pokemon/152',
                'https://pokeapi.co/api/v2/pokemon/153']
results = []


async def get_pokemon(url_names: List[str]):
    async with aiohttp.ClientSession() as session:
        for url in url_names:
            async with session.get(url) as resp:
                results.append(await resp.json())


async def main():
    await get_pokemon(pokemon_urls)
    for result in results:
        print(result['name'])


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import aiohttp
from aiohttp import ClientSession
from util import parse_str_matrx, spiral_matrix_in_counterclock, error_handler

async def get_matrix(url: str):
    async with ClientSession() as session:
        try:
            async with session.get(url) as response:
                response = await response.read()
                response = response.decode()
                
                try:
                    parsed_matrix = parse_str_matrx(response)
                except ValueError as err:
                    return error_handler(response)
                else:
                    spiral_matrix = spiral_matrix_in_counterclock(parsed_matrix)
                    
                return spiral_matrix

        except aiohttp.ClientConnectorError as e:
            return 0 
        except aiohttp.ServerConnectionError as e:
            raise Exception('Server connection error: {}'.format(str(e)))
        except aiohttp.ServerTimeoutError as e:
            raise Exception('Server timeout error: {}'.format(str(e)))
        except aiohttp.ClientError as e: 
            raise Exception('Unexpected error: {}'.format(str(e)))
        except aiohttp.ClientResponseError as e:
            raise Exception('Error getting response from server: {}'.format(str(e)))

def test_get_matrix():
    SOURCE_URL = 'https://f003.backblazeb2.com/file/am-avito/matri.txt'

    TRAVERSAL = [
        10, 50, 90, 130,
        140, 150, 160, 120,
        80, 40, 30, 20,
        60, 100, 110, 70,
    ]

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(get_matrix(SOURCE_URL))
    assert result == TRAVERSAL

test_get_matrix()
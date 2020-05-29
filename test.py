import unittest
from app import * 
import aiohttp
import asyncio

class RequestTest(unittest.TestCase):

    def test(self):
        SOURCE_URL = 'https://f003.backblazeb2.com/file/am-avito/matrix.txt'
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(get_matrix(SOURCE_URL))
        self.assertRaises(Exception, result)



if __name__ == '__main__': 
    unittest.main()
from random import choice

class Codec:

    def __init__(self):
        self.charset = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.urls = {}

    def get_key(self):
        return ''.join(choice(self.charset) for _ in range(7))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = self.get_key()
        while key in self.urls:
            key = self.get_key()
        
        self.urls[key] = longUrl
        return 'http://leetcode_535.com/' + key

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        idx = shortUrl.rindex("/")
        key = shortUrl[idx+1:]
        return self.urls[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
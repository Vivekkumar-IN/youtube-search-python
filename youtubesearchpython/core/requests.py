import os

import httpx

from youtubesearchpython.core.constants import userAgent


class RequestCore:
    def __init__(self):
        self.url = None
        self.data = None
        self.timeout = 2
        self.proxy = {}

        http_proxy = os.environ.get("HTTP_PROXY")
        if http_proxy:
            self.proxy["http://"] = httpx.ProxyTransport(proxy_url=http_proxy)
        https_proxy = os.environ.get("HTTPS_PROXY")
        if https_proxy:
            self.proxy["https://"] = httpx.ProxyTransport(proxy_url=https_proxy)

    def syncPostRequest(self) -> httpx.Response:
        with httpx.Client(mounts=self.proxy) as client:
            r = client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )
            return r

    async def asyncPostRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(mounts=self.proxy) as client:
            r = await client.post(
                self.url,
                headers={"User-Agent": userAgent},
                json=self.data,
                timeout=self.timeout,
            )
            return r

    def syncGetRequest(self) -> httpx.Response:
        with httpx.Client(mounts=self.proxy) as client:
            r = client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )
            return r

    async def asyncGetRequest(self) -> httpx.Response:
        async with httpx.AsyncClient(mounts=self.proxy) as client:
            r = await client.get(
                self.url,
                headers={"User-Agent": userAgent},
                timeout=self.timeout,
                cookies={"CONSENT": "YES+1"},
            )
            return r

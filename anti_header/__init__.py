# encoding: utf-8
import json
import string
import time
import hashlib

from random import sample, randint, choice
from urllib.parse import urlsplit

from anti_useragent import UserAgent
from anti_header.exceptions import UserAgentError, NotFoundParamError, UnSupportMethodError
from anti_header.headers import Headers
from anti_header.utils import logging


class UsageHeader(object):
    _INSTANCE = None

    def __new__(cls, *args, **kwargs):
        """
        singer instance if set dry param is True then destory current instance and create a new instance
        :param dry: True|False
        :return cls
        """
        if not cls._INSTANCE:
            cls._INSTANCE = super().__new__(cls)
        if kwargs.get('dry', False) is True:
            return super().__new__(cls)
        return cls._INSTANCE

    def __init__(self, url: str = None,
                 rand_header: dict = None,
                 must_header: dict = None,
                 default_header: dict = None,
                 logger=False, **kwargs):
        assert isinstance(logger, bool), "logger param must bool type"
        self.logger = logging.get_logger('anti_header') if logger else None
        self._headers: Headers = Headers({})
        self.url: str = url or "https://www.google.com/"
        self.headers_must: list = self.set_headers_must(must_header or {})
        self.headers_param: list = self.set_header_rand(rand_header or {})
        if kwargs.get('dry') is not None:
            del kwargs['dry']
        if default_header:
            self._headers.update(default_header)
        self._ua = UserAgent(**kwargs)

    def __getitem__(self, rule: str):
        return self.__getattr__(rule)

    def __getattr__(self, rule: str):
        if rule == 'random':
            self.headers_must.append(self.user_agent())
            return getattr(self, "process")()
        elif rule == 'base':
            for param in self.headers_must:
                self._headers.update(param)
            self._headers.update(self.user_agent())
            return self._headers
        else:
            raise UnSupportMethodError

    def set_headers_must(self, header: dict) -> list:
        _header_must = [
            {''.join(sample(string.ascii_lowercase, 5)): ''.join(sample(string.ascii_lowercase, 6))},
            {'referer': self.url},
        ]
        _header_must.extend([{key: value} for key, value in header.items()])
        return _header_must

    def set_header_rand(self, header: dict) -> list:
        parse_url = urlsplit(self.url)
        _header_params = [
            {'accept': '*/*'},
            {'accept-type': 'utf-8'},
            {'accept-encoding': 'gzip, deflate'},
            # {'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8'},
            {'authority': parse_url.netloc},
            {'cache-control': choice(['max-age=0', 'no-cache'])},
            {'cache-type': 'any'},
            {'content-from': 'google'},
            {'connection': 'keep-alive'},
            # {"content-type": "application/x-www-form-urlencoded"},

            {'cookie': self._md_hex},

            {'DNT': '1'},
            {'Host': parse_url.netloc},
            {'Origin': self.url},
            {'Origin-content': 'false'},
            {'referer-rec': 'ture'},
            {'pragma': 'no-cache'},
            {'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"'},
            {'sec-ch-ua-mobile': '?0'},
            {'sec-ch-ua-platform': '"Windows"'},
            {'sec-fetch-site': 'same-origin'},
            {'sec-fetch-mode': 'navigate'},
            {'sec-fetch-user': '?1'},
            {'sec-fetch-dest': 'document'},
            {'TE': 'Trailers'},
            {'upgrade-type': 'none'},
            {'upgrade-insecure-requests': '1'},
            {'X-Forwarded-For': '1'}
        ]
        _header_params.extend([{key: value} for key, value in header.items()])
        return _header_params

    @property
    def _md_hex(self) -> str:
        _m = hashlib.md5()
        _m.update(''.join(sample(string.ascii_lowercase, 5)).encode())
        _m_hex = _m.hexdigest()
        return f'Hd_ert_{_m_hex}={time.time()}; Hd_ervt_{_m_hex}={time.time()}'

    def user_agent(self) -> dict:
        try:
            _ua = self._ua.random
        except UserAgentError:
            _ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' \
                  ' (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
        return {"User-Agent": _ua}

    def process(self) -> dict:
        new_header_params = sample(self.headers_param, randint(0, len(self.headers_param)))
        for param in new_header_params + self.headers_must:
            self._headers.update(param)
        if self.logger is not None:
            self.logger.debug('[Headers]: {}', str(self._headers.to_unicode_dict()))
        return self._headers


Header = UsageHeader
__version__ = '0.0.3'

VERSION = __version__


__all__ = [
    Header,
    UsageHeader,
    VERSION
]

import json
from typing import Dict, Any
from urllib.request import urlopen

class ip:
    def __init__(self, ip_address: str):
        self.ip = ip_address
        res=urlopen(f'http://ipinfo.io/{self.ip}/json')
        self.res = json.load(res)

    @property
    def location(self) -> str:
        return self.res.get('loc')

    @property
    def org(self) -> str:
        return self.res.get('org')

    @property
    def city(self) -> str:
        return self.res.get('city')

    @property
    def country(self) -> str:
        return self.res.get('country')

    @property
    def region(self) -> str:
        return self.res.get('region')

    @property
    def timezone(self) -> str:
        return self.res.get('timezone')

    @property
    def postal(self) -> str:
        return self.res.get('postal')

    @property
    def hostname(self) -> str:
        return self.res.get('hostname')

    def get_all_info(self) -> Dict[str, Any]:
        data = {"ip" : {self.ip}, "hostname" : self.hostname, "city" : self.city, "region" : self.region, "country" : self.country, "location" : self.location, "organization" : self.org, "Post" : self.postal, "timezone" : self.timezone}
        return data

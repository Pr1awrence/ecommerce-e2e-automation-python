from requests import Session


class BaseAPI:
    DEFAULT_HEADERS = {
        "Charset": "UTF-8",
        "accept": "*/*",
    }

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = Session()
        self.session.headers.update(self.DEFAULT_HEADERS)

    def _request(self, method, url, raise_for_status=True, **kwargs):
        full_url = f"{self.base_url}{url}"

        response = self.session.request(method, full_url, **kwargs)

        if raise_for_status:
            response.raise_for_status()
        return response

    def get(self, url, **kwargs):
        return self._request("GET", url, **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self._request("POST", url, data=data, json=json, **kwargs)

    def put(self, url, data=None, json=None, **kwargs):
        return self._request("PUT", url, data=data, json=json, **kwargs)

    def delete(self, url, **kwargs):
        return self._request("DELETE", url, **kwargs)

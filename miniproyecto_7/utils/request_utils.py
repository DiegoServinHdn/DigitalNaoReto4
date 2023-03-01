import requests
from requests.exceptions import HTTPError, RequestException
from responses import Response


class RequestUtilsException(Exception):
    pass


class RequestUtils:
    @staticmethod
    def call_get_request(url: str, **kwargs) -> Response:
        """
        Makes a GET request to an URL

        Raises:
            RequestUtils: Request Errors

        Returns:
            Response: Request response
        """
        try:
            response = requests.get(url, kwargs)
            response.raise_for_status()
        except (HTTPError, RequestException) as e:
            print("Failed to make request")
            raise RequestUtilsException(e) from e

        return response

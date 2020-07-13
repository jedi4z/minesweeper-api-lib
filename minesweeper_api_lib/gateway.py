import requests
from requests import Response
from urllib.parse import urljoin

from minesweeper_api_lib.constants import PRODUCTION_ENV_KEY, STAGE_ENV_KEY, PRODUCTION_URL, STAGE_URL
from minesweeper_api_lib.models.user import User


class MinesweeperAPILib:
    def __init__(self, environment=STAGE_ENV_KEY):
        self._session = requests.Session()
        self._base_url = STAGE_URL

        if environment == PRODUCTION_ENV_KEY:
            self._base_url = PRODUCTION_URL

    def _build_url(self, path):
        return urljoin(self._base_url, path)

    def ping(self) -> Response:
        """ Calls the /v1/ping endpoint """
        url = self._build_url('/v1/ping')
        return self._session.get(url)

    def register_user(self, user: User) -> Response:
        """
        Creates a new user

        :param user: User to be registered
        :return: response
        """
        url = self._build_url('/v1/users/register')
        return self._session.post(url=url, json=user.__dict__)

    def authenticate_user(self, user: User) -> Response:
        """
        Authenticates a user

        :param user: user to be authenticated
        :return: response
        """
        url = self._build_url('/v1/users/auth')
        return self._session.post(url=url, json=user.__dict__)

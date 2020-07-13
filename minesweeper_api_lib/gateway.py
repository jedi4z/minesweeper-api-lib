from urllib.parse import urljoin

import requests
from requests import Response

from minesweeper_api_lib.constants import (
    PRODUCTION_ENV_KEY,
    STAGE_ENV_KEY,
    PRODUCTION_URL,
    STAGE_URL,
    AUTHORIZATION_HEADER_KEY,
)
from minesweeper_api_lib.models.game import Game
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
        :return: Response
        """
        url = self._build_url('/v1/users/register')
        return self._session.post(url=url, json=user.__dict__)

    def authenticate_user(self, user: User) -> Response:
        """
        Authenticates a user

        :param user: user to be authenticated
        :return: Response
        """
        url = self._build_url('/v1/users/auth')
        return self._session.post(url=url, json=user.__dict__)

    def create_game(self, access_token: str, game: Game) -> Response:
        """
        Creates a new Game

        :param access_token: The access token to be authenticated
        :param game: Game object to be created
        :return: Response
        """
        url = self._build_url('/v1/games')
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.post(url=url, headers=headers, json=game.__dict__)

    def retrieve_game(self, access_token: str, game_id: int) -> Response:
        """
        Retrieves a Game

        :param access_token: The access token to be authenticated
        :param game_id: The game id to retrieve
        :return: Response
        """
        url = self._build_url(f'/v1/games/{game_id}')
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.get(url=url, headers=headers)

    def list_games(self, access_token: str) -> Response:
        """
        Gets a list of Games

        :param access_token: The access token to be authenticated
        :return: Response
        """
        url = self._build_url(f'/v1/games')
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.get(url=url, headers=headers)

    def hold_game(self, access_token: str, game_id: int) -> Response:
        """
        Changes the status of a Game to OnHold

        :param access_token: The access token to be authenticated
        :param game_id: The game id to hold
        :return: Response
        """
        url = self._build_url(f'/v1/games/{game_id}/hold')
        print(url)
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.post(url=url, headers=headers)

    def resume_game(self, access_token: str, game_id: int) -> Response:
        """
        Changes the status of a Game to Playing

        :param access_token: The access token to be authenticated
        :param game_id: The game id to resume
        :return: Response
        """
        url = self._build_url(f'/v1/games/{game_id}/resume')
        print(url)
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.post(url=url, headers=headers)

    def uncover_cell(self, access_token: str, game_id: int, cell_id: int) -> Response:
        """
        Uncovers a cell of the Game grid

        :param access_token: The access token to be authenticated
        :param game_id: The Game id
        :param cell_id: The Cell id to be uncover
        :return: Response
        """
        url = self._build_url(f'/v1/games/{game_id}/uncover/{cell_id}')
        print(url)
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.post(url=url, headers=headers)

    def flag_cell(self, access_token: str, game_id: int, cell_id: int) -> Response:
        """
        Flags a cell of the Game grid

        :param access_token: The access token to be authenticated
        :param game_id: The Game id
        :param cell_id: The Cell id to be flagged
        :return: Response
        """
        url = self._build_url(f'/v1/games/{game_id}/flag/{cell_id}')
        print(url)
        headers = {AUTHORIZATION_HEADER_KEY: f'Bearer {access_token}'}
        return self._session.post(url=url, headers=headers)

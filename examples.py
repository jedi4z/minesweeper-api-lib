from minesweeper_api_lib.constants import PRODUCTION_ENV_KEY
from minesweeper_api_lib.gateway import MinesweeperAPILib
from minesweeper_api_lib.models.game import Game
from minesweeper_api_lib.models.user import User

gateway = MinesweeperAPILib(PRODUCTION_ENV_KEY)
res = gateway.ping()
json_res = res.json()
print(json_res)

new_user = User(email='jesus.diaz@gmail.com', password='demo')
res2 = gateway.register_user(new_user)
json_res2 = res2.json()
print(json_res2)

user_auth = User(email='jesus.diaz@gmail.com', password='demo')
res3 = gateway.authenticate_user(user_auth)
json_res3 = res3.json()
print(json_res3)

access_token = json_res3['access_token']

new_game = Game(number_of_rows=3, number_of_cols=3, number_of_mines=3)
res4 = gateway.create_game(access_token, new_game)
json_res4 = res4.json()
print(json_res4)

res5 = gateway.retrieve_game(access_token, json_res4['id'])
json_res5 = res5.json()
print(json_res5)

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
new_game = Game(number_of_rows=15, number_of_cols=15, number_of_mines=20)
res4 = gateway.create_game(access_token, new_game)
print(res4.json())

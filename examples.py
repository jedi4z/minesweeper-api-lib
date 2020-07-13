from minesweeper_api_lib.constants import PRODUCTION_ENV_KEY
from minesweeper_api_lib.gateway import MinesweeperAPILib
from minesweeper_api_lib.models.user import User

gateway = MinesweeperAPILib(PRODUCTION_ENV_KEY)
res = gateway.ping()
print(res.json())

new_user = User(email='jesus.diaz@gmail.com', password='demo')
res2 = gateway.register_user(new_user)
print(res2.json())

user_auth = User(email='jesus.diaz@gmail.com', password='demo')
res3 = gateway.authenticate_user(user_auth)
print(res3.json())

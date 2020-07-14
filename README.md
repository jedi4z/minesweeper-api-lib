# Minesweeper-API-lib
This library allows you to interact with Minesweeper-API

# Usage
For more examples see [`examples.py`](https://github.com/jedi4z/minesweeper-api-lib/blob/master/examples.py)

```python
from minesweeper_api_lib.constants import PRODUCTION_ENV_KEY
from minesweeper_api_lib.gateway import MinesweeperAPILib
from minesweeper_api_lib.models.game import Game
from minesweeper_api_lib.models.user import User

# Creating gateway object
gateway = MinesweeperAPILib(PRODUCTION_ENV_KEY)

# Getting an access token
user_auth = User(email='jesus.diaz@gmail.com', password='demo')
auth_response = gateway.authenticate_user(user_auth)
access_token = auth_response.json()['access_token']

# Creating a new Game
new_game = Game(number_of_rows=3, number_of_cols=3, number_of_mines=3)
game_response = gateway.create_game(access_token, new_game)
print(game_response)
```

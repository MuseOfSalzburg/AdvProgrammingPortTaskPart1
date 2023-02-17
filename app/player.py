

class Player:
    def __init__(self, uid: str, player_name: str):
        self._uid = uid
        self._player_name = player_name

    @property
    def uid(self):
        return self._uid

    @property
    def player_name(self):
        return self._player_name

    def __str__(self):
        return f"Player name: {self._player_name} \n Player ID: {self._uid}"

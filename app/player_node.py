from player import Player


class PlayerNode:
    def __init__(self, player: Player):
        self._player = player
        self._next = None
        self._prev = None

    @property
    def say_player(self):
        return self._player

    @property
    def next_node(self):
        return self._next

    @next_node.setter
    def next_node(self, next):
        self._next = next

    @property
    def prev_node(self):
        return self._prev

    @prev_node.setter
    def prev_node(self, prev):
        self._prev = prev

    @property
    def key(self):
        return self._player.uid

    def __str__(self):
        return f"Player Name: {self._player.player_name}" \
               f"Player ID: {self._player.uid}" \
               f"Previous Node: {self._prev}" \
               f"Next Node: {self._next}"

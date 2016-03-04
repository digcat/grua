# global state
from singleton import Singleton


@Singleton
class Global:
    def __init__(self):
        self._state = {}

    def set(self, key, val):
        self._state[key] = val

    def get(self, key):
        return self._state[key]

G = Global.Instance()

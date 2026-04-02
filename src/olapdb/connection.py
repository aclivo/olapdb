from __future__ import annotations
from .cursor import Cursor
import pep249

def connect() -> Connection:
    return Connection()

class Connection(pep249.TransactionlessConnection):
    def cursor(self: pep249.TransactionlessConnection) -> pep249.cursor.CursorType:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

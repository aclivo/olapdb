from __future__ import annotations

import pep249

from typing import Sequence, Type, Any, Dict, Tuple


def connect() -> Connection:
    return Connection()


class Connection(pep249.TransactionlessConnection):
    def cursor(self: pep249.TransactionlessConnection) -> Cursor:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError


class Cursor(pep249.Cursor):
    def setinputsizes(self: Cursor, sizes: Sequence[int | Type | None]) -> None:
        raise NotImplementedError

    def setoutputsize(self: Cursor, size: int, column: int | None) -> None:
        raise NotImplementedError

    def execute(
        self: Cursor,
        operation: str,
        parameters: Sequence[Any] | Dict[str | int, Any] | None = None,
    ) -> Cursor:
        raise NotImplementedError

    def executemany(
        self: Cursor,
        operation: str,
        seq_of_parameters: Sequence[Sequence[Any] | Dict[str | int, Any]],
    ) -> Cursor:
        raise NotImplementedError

    def callproc(
        self: Cursor, procname: str, parameters: Sequence[Any] | None = None
    ) -> Sequence[Any] | None:
        raise NotImplementedError

    @property
    def description(
        self: Cursor,
    ) -> (
        Sequence[
            Tuple[
                str, type, int | None, int | None, int | None, int | None, bool | None
            ]
        ]
        | None
    ):
        raise NotImplementedError

    @property
    def rowcount(self: Cursor) -> int:
        raise NotImplementedError

    def fetchone(self: Cursor) -> Sequence[Any] | Dict[str, Any] | None:
        raise NotImplementedError

    def fetchall(self: Cursor) -> Sequence[Sequence[Any] | Dict[str, Any]]:
        raise NotImplementedError

    def nextset(self: Cursor) -> bool | None:
        raise NotImplementedError

    def close(self) -> None:
        raise NotImplementedError

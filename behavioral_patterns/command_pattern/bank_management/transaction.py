from typing import Protocol


class Transaction(Protocol):
    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass

    def redo(self) -> None:
        pass

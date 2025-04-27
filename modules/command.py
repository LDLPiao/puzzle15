from abc import ABC, abstractmethod

class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver

    @abstractmethod
    def execute(self) -> None:
        pass


class MoveUp(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('up')


class MoveDown(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('down')


class MoveLeft(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('left')


class MoveRight(Command):
    def __init__(self, receiver):
        super().__init__(receiver)

    def execute(self) -> None:
        self.receiver.move('right')
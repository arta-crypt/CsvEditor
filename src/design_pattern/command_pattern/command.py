from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        raise NotImplementedError()

    @abstractmethod
    def unexecute(self):
        raise NotImplementedError()


class CompositeCommand(Command):
    def __init__(self) -> None:
        self.commands: list[Command] = []

    def append_command(self, cmd):
        self.commands.append(cmd)

    def execute(self):
        for cmd in self.commands:
            cmd.execute()

    def unexecute(self):
        for cmd in reversed(self.commands):
            cmd.unexecute()

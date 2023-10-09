import os
import shutil
from design_pattern.command_pattern.command import Command
from design_pattern.command_pattern.command import CompositeCommand


class Receiver:
    def __init__(self) -> None:
        self.text = '!!!Test!!!'


class DeleteCommand(Command):
    def __init__(self, path, receiver: Receiver) -> None:
        self.path = path
        self.contents = None
        self.receiver = receiver

    def execute(self):
        with open(self.path, 'r') as f:
            self.contents = f.read()
        os.remove(self.path)
        self.receiver.text = self.contents

    def unexecute(self):
        if self.contents is not None:
            with open(self.path, 'w') as f:
                f.write(self.contents)


class CopyCommand(Command):
    def __init__(self, path_from, path_to, receiver: Receiver) -> None:
        self.path_from = path_from
        self.path_to = path_to
        self.receiver = receiver

    def execute(self):
        shutil.copyfile(src=self.path_from,
                        dst=self.path_to)

    def unexecute(self):
        os.remove(self.path_to)


def print_folder(path1, path2) -> None:
    print('folder1: ', os.listdir(path1))
    print('folder2: ', os.listdir(path2))


def main() -> None:
    receiver = Receiver()
    print(receiver.text)

    foldername1 = "__temp1"
    foldername2 = "__temp2"
    print("step1: do nothing")
    print_folder(path1=foldername1, path2=foldername2)
    command_mv = CompositeCommand()
    command_mv.append_command(CopyCommand('__temp1/hello1.txt',
                                          '__temp2/hello1.txt',
                                          receiver=receiver))
    command_mv.append_command(DeleteCommand('__temp1/hello1.txt',
                                            receiver=receiver))

    print('step2: do move')
    command_mv.execute()
    print_folder(path1=foldername1, path2=foldername2)

    print('step3: undo move')
    command_mv.unexecute()
    print_folder(path1=foldername1, path2=foldername2)

    print(receiver.text)


if __name__ == '__main__':
    main()

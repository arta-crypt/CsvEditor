from abc import ABCMeta, abstractmethod
from . import subject


class Observer(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def update(self, subject: 'subject.Subject') -> None:
        raise NotImplementedError()


def main():
    pass


if __name__ == '__main__':
    main()

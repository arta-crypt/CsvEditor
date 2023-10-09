from abc import ABCMeta, abstractmethod
from . import observer


class Subject(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.__observers: list['observer.Observer'] = []

    def attach(self, observer: 'observer.Observer') -> None:
        self.__observers.append(observer)

    def detach(self, observer: 'observer.Observer') -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for o in self.__observers:
            o.update(self)


def main():
    pass


if __name__ == '__main__':
    main()

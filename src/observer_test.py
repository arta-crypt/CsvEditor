from design_pattern.observer_pattern.observer import Observer
from design_pattern.observer_pattern.subject import Subject
import random


class ConcreateSubjectRandomNumber(Subject):
    def __init__(self) -> None:
        super(ConcreateSubjectRandomNumber, self).__init__()
        self.number: int = 0
        self.flag: bool = False

    def get_number(self) -> int:
        return self.number

    def execute(self) -> None:
        for _ in range(20):
            self.number: int = random.randint(0, 49)
            self.notify()


class DegitObserver(Observer):
    def update(self,
               subject: ConcreateSubjectRandomNumber) -> None:
        print(f'DigitObserver: {subject.get_number()}')


class GraphObserver(Observer):
    def update(self,
               subject: ConcreateSubjectRandomNumber) -> None:
        count: int = subject.get_number()
        print('*'*count)


def main() -> None:
    generator_subject: ConcreateSubjectRandomNumber \
        = ConcreateSubjectRandomNumber()
    degit_observer: DegitObserver = DegitObserver()
    graph_observer: GraphObserver = GraphObserver()
    generator_subject.attach(degit_observer)
    generator_subject.attach(graph_observer)
    generator_subject.execute()


if __name__ == '__main__':
    main()

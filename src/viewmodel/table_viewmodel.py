import pandas as pd
from design_pattern.observer_pattern.subject import Subject
from design_pattern.observer_pattern.observer import Observer
from model.data_model import DataSubject
from . import window_viewmodel


class DataOvserverForTableViewModel(Observer):
    def __init__(self, master: 'DataObserverAndSubjectForTableViewModel') -> None:
        self.master = master

    def update(self, subject: DataSubject) -> None:
        self.master.subject.data = subject.data
        self.master.subject.notify()


class DataSubjectForTableViewModel(Subject):
    def __init__(self, data: pd.DataFrame) -> None:
        super().__init__()
        self.data = data


class DataObserverAndSubjectForTableViewModel:
    def __init__(self, data: pd.DataFrame = None) -> None:
        self.subject = DataSubjectForTableViewModel(data=data)
        self.observer = DataOvserverForTableViewModel(master=self)


class TableViewModel:
    def __init__(self,
                 root_viewmodel: 'window_viewmodel.WindowViewModel') -> None:
        self._root_viewmodel = root_viewmodel
        self._data_model = root_viewmodel.data_model
        self.data_observer_and_subject = DataObserverAndSubjectForTableViewModel()
        # init settings
        self.init_settings()

    def init_settings(self) -> None:
        self._data_model.get_data_subject().attach(
            self.data_observer_and_subject.observer)

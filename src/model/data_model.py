import pandas as pd
from design_pattern.observer_pattern.subject import Subject


class DataSubject(Subject):
    def __init__(self, data: pd.DataFrame = None) -> None:
        super().__init__()
        self.data = data


class DataModel():
    def __init__(self, data: pd.DataFrame = None) -> None:
        self._data = DataSubject()

    @property
    def data(self) -> pd.DataFrame:
        return self._data.data

    @data.setter
    def data(self, value: pd.DataFrame) -> None:
        self._data.data = value
        print(self._data.data)
        self._data.notify()

    def get_data_subject(self) -> DataSubject:
        return self._data

import pandas as pd
from . import window_viewmodel
from design_pattern.command_pattern.command import Command
from design_pattern.observer_pattern.subject import Subject
from model.data_model import DataModel


class SetDataCommand(Command):
    def __init__(self,
                 data: pd.DataFrame,
                 receiver: DataModel) -> None:
        self.data = data
        self.receiver = receiver

    def execute(self):
        self.receiver.data = self.data

    def unexecute(self):
        pass


class FileControlViewModel(Subject):
    def __init__(self, root_viewmodel: 'window_viewmodel.WindowViewModel') -> None:
        self._root_viewmodel = root_viewmodel
        self._data_model = self._root_viewmodel.data_model

    def set_data(self, data: pd.DataFrame) -> None:
        SetDataCommand(data=data, receiver=self._data_model).execute()

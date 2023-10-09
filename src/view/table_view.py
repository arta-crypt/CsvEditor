import tkinter as tk
from tkinter import ttk
from viewmodel.table_viewmodel import TableViewModel
from viewmodel.table_viewmodel import DataSubjectForTableViewModel
from design_pattern.observer_pattern.observer import Observer


class DataOvserverForTableView(Observer):
    def __init__(self, master: 'TableFrame') -> None:
        self.master = master

    def update(self, subject: DataSubjectForTableViewModel) -> None:
        print(subject.data)


class TableFrame(ttk.LabelFrame):
    def __init__(self,
                 master,
                 text: str,
                 viewmodel: TableViewModel) -> None:
        super().__init__(master=master, text=text)
        self._viewmodel = viewmodel
        self._data_observer = DataOvserverForTableView(master=self)
        self.create_widget()
        self.init_settings()

    def create_widget(self) -> None:
        pass

    def init_settings(self) -> None:
        self._viewmodel.data_observer_and_subject.subject.attach(
            self._data_observer)

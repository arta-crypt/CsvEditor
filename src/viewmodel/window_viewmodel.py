from view import window_view
from model.data_model import DataModel
from .file_control_viewmodel import FileControlViewModel
from .table_viewmodel import TableViewModel


class WindowViewModel:
    def __init__(self, title: str, geometry: str) -> None:
        # init model
        self.data_model = DataModel()
        # init viewmodel
        self.file_control_viewmodel = FileControlViewModel(root_viewmodel=self)
        self.table_viewmodel = TableViewModel(root_viewmodel=self)
        # init view
        self.view = window_view.WindowView(title=title,
                                           geometry=geometry,
                                           viewmodel=self)

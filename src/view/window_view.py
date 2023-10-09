import tkinter as tk
from tkinter import ttk
from viewmodel import window_viewmodel
from .scrollbar_frame import ScrollBarFrame
from .file_control_view import FileControlFrame
from .table_view import TableFrame


class WindowView(tk.Tk):
    FILE_CONTROL_FRAME_TEXT = 'Table'
    PROPERTY_FRAME_TEXT = 'Property'

    def __init__(self,
                 title: str,
                 geometry: str,
                 viewmodel: 'window_viewmodel.WindowViewModel') -> None:
        super().__init__()
        self.init_setting(title=title, geometry=geometry)
        self._viewmodel = viewmodel
        self.creage_widget()

    def init_setting(self, title: str, geometry: str) -> None:
        self.title(title)
        self.geometry(geometry)

    def creage_widget(self) -> None:
        parent_frame = ttk.Frame(master=self, borderwidth=10)
        file_control_frame = FileControlFrame(master=parent_frame,
                                              viewmodel=self._viewmodel.file_control_viewmodel)
        table_frame = TableFrame(master=parent_frame,
                                 text=WindowView.FILE_CONTROL_FRAME_TEXT,
                                 viewmodel=self._viewmodel.table_viewmodel)
        property_frame = PropertyFrame(master=parent_frame,
                                       text=WindowView.PROPERTY_FRAME_TEXT)
        # Pack
        file_control_frame.pack(side=tk.TOP)
        table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        property_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        parent_frame.pack()


class PropertyFrame(ttk.LabelFrame):
    def __init__(self, master, text) -> None:
        super().__init__(master=master, text=text)
        self.create_widget()

    def create_widget(self) -> None:
        scrollbar_frame = ScrollBarFrame(master=self,
                                         has_x_scrollbar=True,
                                         has_y_scrollbar=True)


def main():
    pass


if __name__ == '__main__':
    main()

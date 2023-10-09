import tkinter as tk
from tkinter import ttk


class ScrollBarFrame(ttk.Frame):
    """スクロールバー付Frameクラス
        ※bind時の注意
            selfのConfigure, self.canvasのConfigureは
            既にbindしているので、
            外部でバインドする場合add=Trueオプションを指定する

    Args:
        ttk (_type_): _description_
    """

    SELF_BORDER_WIDTH = 10

    def __init__(self,
                 master,
                 has_x_scrollbar=False,
                 has_y_scrollbar=False) -> None:
        self.parent_canvas = tk.Canvas(master=master)
        super().__init__(master=self.parent_canvas)
        self.__create_widget(has_x_scrollbar=has_x_scrollbar,
                             has_y_scrollbar=has_y_scrollbar)

    def __create_widget(self,
                        has_x_scrollbar=False,
                        has_y_scrollbar=False):
        # Vertical Scrollbar
        if has_y_scrollbar:
            y_scrollbar = ttk.Scrollbar(master=self.parent_canvas,
                                        orient=tk.VERTICAL,
                                        command=self.parent_canvas.yview)
            self.parent_canvas.configure(yscrollcommand=y_scrollbar.set)
            y_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # Horizontal Scrollbar
        if has_x_scrollbar:
            x_scrollbar = ttk.Scrollbar(master=self.parent_canvas,
                                        orient=tk.HORIZONTAL,
                                        command=self.parent_canvas.xview)
            self.parent_canvas.configure(xscrollcommand=x_scrollbar.set)
            x_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        # canvas pack
        self.parent_canvas.pack(side=tk.LEFT,
                                fill=tk.BOTH,
                                expand=True)
        # frame set on canvas
        self.parent_canvas.create_window(0, 0,
                                         anchor=tk.NW,
                                         window=self)
        self.parent_canvas.configure(
            scrollregion=self.parent_canvas.bbox(tk.ALL))
        # bind
        self.bind('<Configure>', self.__on_frame_configure)

    def __on_frame_configure(self, event=None) -> None:
        """canvasを親に持つframeでサイズ変更があった場合に
            canvasのscrollregionを更新する
            これでスクロールバーが動作する
            frameの<configure>シーケンスとbindして使う

        Args:
            event (_type_, optional): _description_. Defaults to None.
        """
        if event:
            if type(event.widget.master) == tk.Canvas:
                canvas = event.widget.master
                # canvas.configure(
                #     scrollregion=canvas.bbox(tk.ALL))
                canvas.configure(scrollregion=(canvas.bbox(tk.ALL)[0]-10,
                                               canvas.bbox(tk.ALL)[1]-10,
                                               canvas.bbox(tk.ALL)[2]+30,
                                               canvas.bbox(tk.ALL)[3]+30))


def __create_test_widget(master: tk.Tk):
    parent_frame = ttk.LabelFrame(master=master,
                                  relief=tk.RAISED,
                                  text='Test')
    main_frame = ScrollBarFrame(master=parent_frame,
                                has_x_scrollbar=True,
                                has_y_scrollbar=True)
    for i in range(100):
        label = ttk.Label(master=main_frame, text='Test'*100)
        label.pack(side=tk.TOP)
    parent_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def main():
    window = tk.Tk()
    window.title('title')
    window.geometry('400x200')
    __create_test_widget(master=window)
    window.mainloop()


if __name__ == '__main__':
    main()

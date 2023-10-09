from viewmodel.window_viewmodel import WindowViewModel


def main():
    title = 'Csv Editor'
    geomerty = '1200x500'
    app = WindowViewModel(title=title, geometry=geomerty)
    app.view.mainloop()


if __name__ == '__main__':
    main()

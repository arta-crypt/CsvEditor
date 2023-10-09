import sys
from cx_Freeze import setup, Executable

copyDependentFiles = True
silent = True
base = None

# if sys.platform == "win32":
#     base = "Win32GUI"


packages = []
includes = []
excludes = []

# exe にしたい python ファイル
my_exe = Executable(script='main.py',
                    base=base,
                    target_name='csv_editor.exe')

setup(
    name='Csv Editor',
    version='0.1',
    description="My Csv Editor!",
    options={'build_exe': {'includes': includes,
                           'excludes': excludes,
                           'packages': packages}},
    executables=[my_exe]
)

from cx_Freeze import setup, Executable

# Определите зависимости вашего приложения
build_exe_options = {
    "packages": ["kivy"],
    "excludes": ["tkinter"],
    "include_files": ["C:/Users/User/Desktop/Все скрипты/Портфолио/"]
}

setup(
    name="Мой портфолио",
    version="0.1",
    description="Your application description",
    options={"build_exe": build_exe_options},
    executables=[Executable("testing.py", base=None)],
)

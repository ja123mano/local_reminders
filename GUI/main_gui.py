import customtkinter
import tkinter
import pathlib
import tkcalendar

from ReminderDisplayFrame import ReminderDisplayFrame
from ReminderInfoFrame import ReminderInfoFrame
from Reminder import Reminder
from WarningWindow import WarningWindow

class App(customtkinter.CTk):
    WIDTH: int = 1300
    HEIGHT: int = 500
    RIGHT_FRAME_HEADERS: int = 2
    REM_ID: int = 0
    SOUNDS_FOLDER: pathlib.Path = pathlib.Path.joinpath(pathlib.Path.cwd(), "Sounds")

    def __init__(self) -> None:
        super().__init__()

        self.title("Reminders")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")
        self.CREATED_REMINDERS = dict()

        # =================================== Frames ===================================

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, minsize=400)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ReminderInfoFrame(self)
        self.left_frame.grid(row=0, column=0, padx=(6,3), pady=(6,2), sticky="nswe")

        self.create_reminder_button = customtkinter.CTkButton(self, text="Create reminder", font=self.NORMAL_FONT, command=self.create_reminder)
        self.create_reminder_button.grid(row=1, column=0, padx=10, pady=(2,6), sticky="nswe")

        self.right_frame = ReminderDisplayFrame(self)
        self.right_frame.grid(row=0, column=1, rowspan=2, padx=(3,6), pady=6, sticky="nswe")

    def get_geometry_info(self) -> tuple[int, int, int, int]:
        self.update_idletasks()
        w_geometry = self.winfo_geometry()
        w_geometry = w_geometry.split("+")
        temp = w_geometry[0].split("x")
        w_geometry[0] = temp[0]
        w_geometry.insert(1, temp[1])
        
        for i, info in enumerate(w_geometry):
            w_geometry[i] = int(info)
        
        return tuple(w_geometry)

    def create_reminder(self) -> None:
        remind_info: tuple[bool, str] = self.left_frame.validate_main_data()

        if not remind_info[0]:
            warning_sound: str = str(pathlib.Path.joinpath(App.SOUNDS_FOLDER, "Warning_window.mp3"))
            WarningWindow(self.get_geometry_info(), "Missing information", remind_info[1], sound=warning_sound)
            return None

        reminder_data: list[str] = self.left_frame.get_reminder_data()
        self.CREATED_REMINDERS[App.REM_ID] = Reminder(reminder_data, self.right_frame)

        reminder = self.CREATED_REMINDERS[App.REM_ID]
        reminder.select_checkbox.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=0, padx=10, sticky="e")
        reminder.reminder_name.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=1, sticky="we")
        reminder.reminder_desc.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=2, sticky="we")
        reminder.reminder_link.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=3, sticky="we")
        reminder.reminder_date.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=4, sticky="we")
        reminder.reminder_days.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=5, sticky="we")
        reminder.reminder_repetitions.grid(row=App.RIGHT_FRAME_HEADERS+App.REM_ID+1, column=6, sticky="we")
        
        App.REM_ID += 1
        return None


if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()
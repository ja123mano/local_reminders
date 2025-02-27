import customtkinter
import tkinter
import pathlib
import pickle
import datetime

from ReminderDisplayFrame import ReminderDisplayFrame
from ReminderInfoFrame import ReminderInfoFrame
from Reminder import Reminder
from WarningWindow import WarningWindow

class App(customtkinter.CTk):
    # TODO Create documentation for this entire class and its functions

    WIDTH: int = 1300
    HEIGHT: int = 500
    RIGHT_FRAME_HEADERS: int = 2
    REM_ID: int = 0
    SOUNDS_FOLDER: pathlib.Path = pathlib.Path.joinpath(pathlib.Path.cwd(), "Sounds")
    WARNING_SOUND: str = str(pathlib.Path.joinpath(SOUNDS_FOLDER, "Warning_window.mp3"))

    def __init__(self) -> None:
        super().__init__()

        self.title("Reminders")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")
        self.CREATED_REMINDERS = dict()

        # =================================== Frames ===================================

        self.grid_columnconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, minsize=400)
        self.grid_rowconfigure(0, weight=1)

        self.left_frame = ReminderInfoFrame(self)
        self.left_frame.grid(row=0, column=0, padx=(6,3), pady=(6,2), sticky="nswe")

        self.create_reminder_button = customtkinter.CTkButton(self, text="Create reminder", font=self.NORMAL_FONT, command=self.create_reminder)
        self.create_reminder_button.grid(row=1, column=0, padx=(6,3), pady=(2,6), sticky="nswe")

        self.right_frame = ReminderDisplayFrame(self)
        self.right_frame.grid(row=0, column=1, columnspan=2, padx=(3,6), pady=(6,2), sticky="nswe")

        self.save_reminder_button = customtkinter.CTkButton(self, text="Save reminders", font=self.NORMAL_FONT, command=self.save_reminders)
        self.save_reminder_button.grid(row=1, column=1, padx=3, pady=(2,6), sticky="nswe")

        self.delete_reminder_button = customtkinter.CTkButton(self, text="Delete reminders", font=self.NORMAL_FONT, command=self.delete_reminders)
        self.delete_reminder_button.grid(row=1, column=2, padx=(3,6), pady=(2,6), sticky="nswe")

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

    def create_reminder(self) -> int:
        remind_info: tuple[bool, str] = self.left_frame.validate_main_data()

        if not remind_info[0]:
            WarningWindow(self.get_geometry_info(), "Missing information", remind_info[1], sound=App.WARNING_SOUND)
            return -1

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
        return 0
    
    def save_reminders(self) -> int:
        if len(self.CREATED_REMINDERS) == 0:
            warning_message: str = "No reminders to be saved.\nPlease create at least 1 reminder before saving."
            WarningWindow(self.get_geometry_info(), "Missing reminders", warning_message, sound=App.WARNING_SOUND)
            return -1
        
        saving_reminders: dict[str] = dict()
        today: datetime.datetime = datetime.date.today().strftime(r"%d_%m_%Y")
        pickle_file_name: str = f"reminder {today}.pickl"

        for rem in self.CREATED_REMINDERS.keys():
            reminder: Reminder = self.CREATED_REMINDERS[rem]
            rem_id: int = rem
            saving_reminders[rem_id] = reminder.get_reminder_details()

        with open(rf"Saved_reminders\{pickle_file_name}", "wb") as pickle_file:
            pickle.dump(saving_reminders, pickle_file)

        return 0
    
    def delete_reminders(self) -> None:
        return None


if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()
import customtkinter
import tkinter

class ReminderInfoFrame(customtkinter.CTkFrame):
    """
    Class inheriting functionality from the CTkFrame widget from customtkinter.
    
    Encapsulates the ability to enter the reminder information and important
    functions to retrieve the correct information for the reminder.

    Attributes
    ----------
    reminder_name_var (tkinter.StringVar): Name of the reminder.
    reminder_desc_var (tkinter.StringVar): Description of the reminder.
    reminder_date_var (tkinter.StringVar): Date of the reminder.
    reminder_link_var (tkinter.StringVar): Link of the reminder.
    reminder_repeat_time_var (tkinter.StringVar): Days to wait to repeat the reminder. 
    reminder_end_repeat_time_var (tkinter.StringVar): Limit of repetitions of the reminder.
    TITLE_FONT (customtkinter_CTkFont): Font used in the object's title.
    SUBTITLE_FONT (customtkinter_CTkFont): Font used in the object's subtitles.
    NORMAL_FONT (customtkinter_CTkFont): Font used in the object's label spaces.

    The rest of the attributes are customtkinter widgets used for the user to enter
    the reminder information accordingly.
    """

    def __init__(self, master, corner_radius = 8):
        """
        Initializes the frame object. This is only called once at the start of the program
        to display the frame the user will be using to enter the reminder information.

        Parameters
        ----------
        master : customtkinter.CTk
            Tells the object who the parent window will be (in this case, the main window)
            so the object displays in the correct place.
        corner_radius : int = 8
            Used to round the frame's corners. A higher number means the corners will be
            rounder. A smaller number means the corners will be squarer.
        """

        # ===================================  ===================================

        super().__init__(master, corner_radius=corner_radius)

        # =================================== Object variables ===================================

        self.reminder_name_var = tkinter.StringVar()
        self.reminder_desc_var = tkinter.StringVar()
        self.reminder_date_var = tkinter.StringVar()
        self.reminder_link_var = tkinter.StringVar()
        self.reminder_repeat_time_var = tkinter.StringVar()
        self.reminder_end_repeat_time_var = tkinter.StringVar()
        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        # =================================== Object widgets ===================================

        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(9, weight=1)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder info", font=self.TITLE_FONT)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=4, pady=(10, 2), sticky="we")

        self.name_label = customtkinter.CTkLabel(self, text="Name", font=self.SUBTITLE_FONT)
        self.name_label.grid(row=1, column=0, padx=10, pady=2, sticky="w")
        self.name_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_name_var, fg_color="grey10")
        self.name_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.desc_label = customtkinter.CTkLabel(self, text="Description", font=self.SUBTITLE_FONT)
        self.desc_label.grid(row=2, column=0, padx=10, pady=2, sticky="w")
        self.desc_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_desc_var, fg_color="grey10")
        self.desc_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.date_label = customtkinter.CTkLabel(self, text="Date", font=self.SUBTITLE_FONT)
        self.date_label.grid(row=3, column=0, padx=10, pady=2, sticky="w")
        self.date_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_date_var, fg_color="grey10")
        self.date_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.link_label = customtkinter.CTkLabel(self, text="Link", font=self.SUBTITLE_FONT)
        self.link_label.grid(row=4, column=0, padx=10, pady=2, sticky="w")
        self.link_entry = customtkinter.CTkEntry(self, textvariable=self.reminder_link_var, fg_color="grey10")
        self.link_entry.grid(row=4, column=1, columnspan=2, padx=10, pady=2, sticky="we")

        self.repeat_label = customtkinter.CTkLabel(self, text="Repeat?", font=self.SUBTITLE_FONT)
        self.repeat_label.grid(row=5, column=0, padx=10, pady=(50,2), sticky="w")
        self.repeat_checkbox = customtkinter.CTkCheckBox(self, text="", command=self.toggle_repeat)
        self.repeat_checkbox.grid(row=5, column=1, padx=10, pady=(50,2), sticky="we")

        self.repeat_every_label = customtkinter.CTkLabel(self, text="Repeat every", font=self.SUBTITLE_FONT)
        self.repeat_every_label.grid(row=6, column=0, padx=10, pady=2, sticky="w")
        self.repeat_entry_num = customtkinter.CTkEntry(self, textvariable=self.reminder_repeat_time_var, state="disabled")
        self.repeat_entry_num.grid(row=6, column=1, padx=10, pady=2, sticky="we")
        self.repeat_time_label = customtkinter.CTkLabel(self, text="days", font=self.NORMAL_FONT)
        self.repeat_time_label.grid(row=6, column=2, padx=10, pady=2, sticky="w")

        self.end_repeat_label = customtkinter.CTkLabel(self, text="End repeat", font=self.SUBTITLE_FONT)
        self.end_repeat_label.grid(row=7, column=0, padx=10, pady=2, sticky="w")
        self.end_repeat_checkbox = customtkinter.CTkCheckBox(self, text="", command=self.toggle_end_repeat, state="disabled")
        self.end_repeat_checkbox.grid(row=7, column=1, padx=10, pady=2, sticky="we")

        self.end_after_label = customtkinter.CTkLabel(self, text="End after", font=self.SUBTITLE_FONT)
        self.end_after_label.grid(row=8, column=0, padx=10, pady=2, sticky="w")
        self.end_after_entry_num = customtkinter.CTkEntry(self, textvariable=self.reminder_end_repeat_time_var, state="disabled")
        self.end_after_entry_num.grid(row=8, column=1, padx=10, pady=2, sticky="we")
        self.end_after_time_label = customtkinter.CTkLabel(self, text="repetitions", font=self.NORMAL_FONT)
        self.end_after_time_label.grid(row=8, column=2, padx=10, pady=2, sticky="w")

    def toggle_repeat(self) -> None:
        """
        Called every time the user clics the 'Repeat?' checkbox to
        enable or disable the repeat/end repeat options of the reminder.
        """

        if self.repeat_checkbox.get():
            self.repeat_entry_num.configure(state="normal")
            self.end_repeat_checkbox.configure(state="normal")
        else:
            self.repeat_entry_num.configure(state="disabled")
            self.end_repeat_checkbox.configure(state="disabled")

        self.toggle_end_repeat()

    def toggle_end_repeat(self) -> None:
        """
        Called every time the toggle_repeat function is called or
        the 'end repeat' checkbox is clicked. Used to enable/disable the
        end repeat option of the reminder.
        """

        if self.repeat_checkbox.get() and self.end_repeat_checkbox.get():
            self.end_after_entry_num.configure(state="normal")
        else:
            self.end_after_entry_num.configure(state="disabled")

    def get_reminder_data(self) -> list[str]:
        """
        Returns a list of the information of the reminder.

        Returns
        -------
        list[str]
            A list containing the information of the reminder.
        """
        
        data: list[str] = list()
        data.append(self.reminder_name_var.get())
        data.append(self.reminder_desc_var.get())
        data.append(self.reminder_date_var.get())
        data.append(self.reminder_link_var.get())
        data.append(self.repeat_checkbox.get())
        data.append(self.reminder_repeat_time_var.get())
        data.append(self.end_repeat_checkbox.get())
        data.append(self.reminder_end_repeat_time_var.get())
        return data

    def validate_main_data(self) -> tuple[bool, str]:
        """
        Validates that the reminder information entered by the user
        is correct.

        Returns
        -------
        tuple[bool, str]
            Tuple containing a flag [0] wheter the information is correct or not
            and a string [1] that contains a message of the incorrect information
            entered by the user. 
            
            The string is meant to be displayed by an object of type WarningWindow,
            using the string as the w_msg attribute of the object initializacion call.
        """

        validate_flag: int = True
        warning_msg: str = "Please set a valid:"

        if self.reminder_name_var.get() == "":
            validate_flag = False
            warning_msg += "\n- Name for the reminder"
        
        if self.reminder_desc_var.get() == "":
            validate_flag = False
            warning_msg += "\n- Description for the reminder"
        
        if self.reminder_date_var.get() == "":
            validate_flag = False
            warning_msg += "\n- Date for the reminder"
        
        if self.repeat_checkbox.get():
            try:
                repeat_time_int = int(self.reminder_repeat_time_var.get())
                if repeat_time_int < 1: raise Exception
            except:
                validate_flag = False
                warning_msg += "\n- Number of days for repetition"
            
            if self.end_repeat_checkbox.get():
                try:
                    end_repeat_time_int = int(self.reminder_end_repeat_time_var.get())
                    if end_repeat_time_int < 1: raise Exception
                except:
                    validate_flag = False
                    warning_msg += "\n- Number of repetitions"
        
        return (validate_flag, warning_msg)


class ReminderDisplayFrame(customtkinter.CTkFrame):
    def __init__(self, master, corner_radius = 8):
        super().__init__(master,corner_radius=corner_radius)

        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        self.grid_columnconfigure((1,2,3,4), weight=1)
        self.grid_columnconfigure((1,2,3,4,5,6), minsize=100)

        self.title_label = customtkinter.CTkLabel(self, text="Reminder display frame", font=self.TITLE_FONT)
        self.title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=(10,2), sticky="we")

        self.select_label = customtkinter.CTkLabel(self, text="Select", font=self.SUBTITLE_FONT)
        self.select_label.grid(row=1, column=0, padx=10, pady=2, sticky="we")

        self.name_label = customtkinter.CTkLabel(self, text="Name", font=self.SUBTITLE_FONT)
        self.name_label.grid(row=1, column=1, padx=10, pady=2, sticky="we")

        self.description_label = customtkinter.CTkLabel(self, text="Description", font=self.SUBTITLE_FONT)
        self.description_label.grid(row=1, column=2, padx=10, pady=2, sticky="we")

        self.link_label = customtkinter.CTkLabel(self, text="Link", font=self.SUBTITLE_FONT)
        self.link_label.grid(row=1, column=3, padx=10, pady=2, sticky="we")

        self.date_label = customtkinter.CTkLabel(self, text="Next remind", font=self.SUBTITLE_FONT)
        self.date_label.grid(row=1, column=4, padx=10, pady=2, sticky="we")

        self.constancy_label = customtkinter.CTkLabel(self, text="Remind every", font=self.SUBTITLE_FONT)
        self.constancy_label.grid(row=1, column=5, padx=10, pady=2, sticky="we")

        self.repeat_label = customtkinter.CTkLabel(self, text="# of repeats", font=self.SUBTITLE_FONT)
        self.repeat_label.grid(row=1, column=6, padx=10, pady=2, sticky="we")


class Reminder():
    def __init__(self, reminder_data: list[str], master_frame: customtkinter.CTkFrame, text_font: customtkinter.CTkFont):
        name: str = reminder_data[0]
        description: str = reminder_data[1]
        date: str = reminder_data[2]
        link: str = reminder_data[3]
        days: str = "NA"
        repetitions: str = "None"

        if link == "": link = "NA"
        if reminder_data[4]:
            days: int = f"{reminder_data[5]} day(s)"
            if reminder_data[6]: repetitions: int = reminder_data[7]
            else: repetitions = "Infinite"

        self.select_checkbox = customtkinter.CTkCheckBox(master=master_frame, width=35, text="")
        self.reminder_name = customtkinter.CTkLabel(master=master_frame, text=name, font=text_font)
        self.reminder_desc = customtkinter.CTkLabel(master=master_frame, text=description, font=text_font)
        self.reminder_link = customtkinter.CTkLabel(master=master_frame, text=link, font=text_font)
        self.reminder_date = customtkinter.CTkLabel(master=master_frame, text=date, font=text_font)
        self.reminder_days = customtkinter.CTkLabel(master=master_frame, text=days, font=text_font)
        self.reminder_repetitions = customtkinter.CTkLabel(master=master_frame, text=repetitions, font=text_font)

        return None


class WarningWindow(customtkinter.CTkToplevel):
    def __init__(self, main_geometry: tuple, w_title = "Warning", w_msg: str = "Something happened", w_width = 350, w_height = 150):
        super().__init__()

        self.title(w_title)
        self.geometry(f"{w_width}x{w_height}")
        self.minsize(w_width, w_height)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.w_label = customtkinter.CTkLabel(self, text=w_msg, font=customtkinter.CTkFont("console", 15, "normal"))
        self.w_label.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.center(main_geometry)
        self.attributes('-topmost', True)

    def center(self, main_geometry) -> None:
        self.update_idletasks()
        x = main_geometry[2] + main_geometry[0]//3
        y = main_geometry[3] + main_geometry[1]//3
        self.geometry(f"+{x}+{y}")


class App(customtkinter.CTk):
    WIDTH: int = 1300
    HEIGHT: int = 500
    RIGHT_FRAME_HEADERS: int = 2
    REM_ROWS: int = 0 + RIGHT_FRAME_HEADERS
    REM_ID: int = 0

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
            WarningWindow(self.get_geometry_info(), "Missing information", remind_info[1])
            return None

        reminder_data: list[str] = self.left_frame.get_reminder_data()
        self.CREATED_REMINDERS[App.REM_ID] = Reminder(reminder_data, self.right_frame, self.NORMAL_FONT)
        App.REM_ID += 1

        for i in range(len(self.CREATED_REMINDERS)):
            reminder = self.CREATED_REMINDERS[i]

            reminder.select_checkbox.grid(row=App.REM_ROWS+i, column=0, padx=10, sticky="e")
            reminder.reminder_name.grid(row=App.REM_ROWS+i, column=1, sticky="we")
            reminder.reminder_desc.grid(row=App.REM_ROWS+i, column=2, sticky="we")
            reminder.reminder_link.grid(row=App.REM_ROWS+i, column=3, sticky="we")
            reminder.reminder_date.grid(row=App.REM_ROWS+i, column=4, sticky="we")
            reminder.reminder_days.grid(row=App.REM_ROWS+i, column=5, sticky="we")
            reminder.reminder_repetitions.grid(row=App.REM_ROWS+i, column=6, sticky="we")
        
        App.REM_ROWS += 1
        print(self.CREATED_REMINDERS)
        return None


if __name__ == "__main__":
    new_window: App = App()

    new_window.mainloop()
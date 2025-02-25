import tkinter
import customtkinter
import tkcalendar

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
    TITLE_FONT (customtkinter.CTkFont): Font used in the object's title.
    SUBTITLE_FONT (customtkinter.CTkFont): Font used in the object's subtitles.
    NORMAL_FONT (customtkinter.CTkFont): Font used in the object's label spaces.

    The rest of the attributes are customtkinter widgets used for the user to enter
    the reminder information accordingly.
    """

    def __init__(self, master, corner_radius = 8):
        """
        Initializes a frame object. This is only called once at the start of the program
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

        # =================================== Super class call ===================================

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
        self.date_dateEntry = tkcalendar.DateEntry(self, background="midnight blue", foreground="white", borderwidth=2)
        self.date_dateEntry.grid(row=3, column=1, columnspan=2, padx=10, pady=2, sticky="we")

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

    def get_date(self) -> None:
        """
        Grabs the date from the Date Entry widget and sets it into the
        reminder_date_var variable 
        """

        self.reminder_date_var.set(self.date_dateEntry.get_date())

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
        
        self.get_date()
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
        
        if validate_flag: warning_msg = None

        return (validate_flag, warning_msg)

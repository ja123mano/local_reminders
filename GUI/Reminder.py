import tkinter
import customtkinter

class Reminder():
    """
    This class represents a reminder, with the data the user entered in the
    ReminderInfoFrame object. This class helps encapsulate the data needed for the
    reminder to exist.

    Attributes
    ----------
    All the attributes of the class are customtkinter widgets, filled with the
    information obtained from the ReminderInfoFrame object.
    """

    def __init__(self, reminder_data: list[str], master_frame: customtkinter.CTkFrame) -> None:
        """
        Initializes a reminder object. This object will contain all the info
        that the ReminderInfoFrame object has when pressing the 'Create reminder'
        button in the main window.

        Parameters
        ----------
        reminder_data : list[str]
            A list with the reminder info at the moment the Reminder object is
            created.
        master_frame: customtkinter.CTkFrame
            The parent object where this Reminder object will be displayed.
        """

        name: str = reminder_data[0]
        description: str = reminder_data[1]
        date: str = reminder_data[2]
        link: str = reminder_data[3]
        days: str = "NA"
        repetitions: str = "None"
        text_font: customtkinter.CTkFont = customtkinter.CTkFont("console", 15, "normal")

        if link == "": link = "NA"
        if reminder_data[4]:
            days = f"{reminder_data[5]} day(s)"
            if reminder_data[6]: repetitions = str(reminder_data[7])
            else: repetitions = "Infinite"

        self.select_checkbox = customtkinter.CTkCheckBox(master=master_frame, width=35, text="")
        self.reminder_name = customtkinter.CTkLabel(master=master_frame, text=name, font=text_font)
        self.reminder_desc = customtkinter.CTkLabel(master=master_frame, text=description, font=text_font)
        self.reminder_link = customtkinter.CTkLabel(master=master_frame, text=link, font=text_font)
        self.reminder_date = customtkinter.CTkLabel(master=master_frame, text=date, font=text_font)
        self.reminder_days = customtkinter.CTkLabel(master=master_frame, text=days, font=text_font)
        self.reminder_repetitions = customtkinter.CTkLabel(master=master_frame, text=repetitions, font=text_font)

        return None

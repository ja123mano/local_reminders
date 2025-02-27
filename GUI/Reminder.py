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

        self.name: str = reminder_data[0]
        self.description: str = reminder_data[1]
        self.date: str = reminder_data[2]
        self.link: str = reminder_data[3]
        self.days: str = "NA"
        self.repetitions: str = "None"
        text_font: customtkinter.CTkFont = customtkinter.CTkFont("console", 15, "normal")

        if self.link == "": self.link = "NA"
        if reminder_data[4]:
            self.days = f"{reminder_data[5]} day(s)"
            if reminder_data[6]: self.repetitions = str(reminder_data[7])
            else: self.repetitions = "Infinite"

        self.select_checkbox = customtkinter.CTkCheckBox(master=master_frame, width=35, text="")
        self.reminder_name = customtkinter.CTkLabel(master=master_frame, text=self.name, font=text_font)
        self.reminder_desc = customtkinter.CTkLabel(master=master_frame, text=self.description, font=text_font)
        self.reminder_link = customtkinter.CTkLabel(master=master_frame, text=self.link, font=text_font)
        self.reminder_date = customtkinter.CTkLabel(master=master_frame, text=self.date, font=text_font)
        self.reminder_days = customtkinter.CTkLabel(master=master_frame, text=self.days, font=text_font)
        self.reminder_repetitions = customtkinter.CTkLabel(master=master_frame, text=self.repetitions, font=text_font)

        return None
    
    def get_reminder_details(self) -> dict[str]:
        # TODO Update documentations for the function and the class

        reminder_details: dict[str] = dict()

        reminder_details["checkbox"] = self.select_checkbox.get()
        reminder_details["name"] = self.name
        reminder_details["description"] = self.description
        reminder_details["date"] = self.date
        reminder_details["link"] = self.link
        reminder_details["days"] = self.days
        reminder_details["reps"] = self.repetitions
        
        return reminder_details

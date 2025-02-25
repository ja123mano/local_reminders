import tkinter
import customtkinter

class ReminderDisplayFrame(customtkinter.CTkFrame):
    """
    Class inheriting functionality from the CTkFrame widget from customtkinter.
    
    This class is used to display the created reminders.

    Attributes
    ----------
    TITLE_FONT (customtkinter.CTkFont): Font used in the object's title.
    SUBTITLE_FONT (customtkinter.CTkFont): Font used in the object's subtitles.
    NORMAL_FONT (customtkinter.CTkFont): Font used in the object's label spaces.

    The rest of the attributes are customtkinter widgets used for the user to enter
    the reminder information accordingly.
    """
    
    def __init__(self, master, corner_radius = 8):
        """
        Initializes a frame object. This is only called once at the start of the program
        to place a frame where the reminders will be displayed for the user to see with
        the information they entered.

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

        super().__init__(master,corner_radius=corner_radius)

        # =================================== Object variables ===================================

        self.TITLE_FONT = customtkinter.CTkFont("console", 20, "bold")
        self.SUBTITLE_FONT = customtkinter.CTkFont("console", 15, "bold")
        self.NORMAL_FONT = customtkinter.CTkFont("console", 15, "normal")

        # =================================== Object widgets ===================================

        self.grid_columnconfigure((1,2,3), weight=1)
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

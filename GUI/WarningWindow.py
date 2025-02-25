import tkinter
import customtkinter
import pathlib
from playsound import playsound

class WarningWindow(customtkinter.CTkToplevel):
    """
    Class inheriting functionality from the CTkTopLevel widget from customtkinter.
    
    This class is used to display a variety of warning messages.

    Attributes
    ----------
    All the attributes of the class are attributes of the super class and a level
    widget to display the warning message.
    """

    def __init__(self, main_geometry: tuple[int, int, int, int], w_title: str = "Warning", w_msg: str = "Something happened", w_width: int = 350, w_height: int = 150, sound: pathlib.Path = None):
        """
        Initializes a top level object used to display a message when something happens.
        This is the way the main window communicates with the user when something needs
        his attention.

        Parameters
        ----------
        main_geometry : tuple[int, int, int, int]
            Tuple that contains the geometry dimensions and displacement of the main
            window. This information is used to display the warning window near the
            center of the main window.
        w_title : str = "Warning"
            The title of the warning window.
        w_msg : str = "Something happened"
            The message the warning window will display.
        w_width : int = 350
            The width of the warning window.
        w_height : int = 150
            The height of the warning window.
        """

        # =================================== Super class call ===================================

        super().__init__()

        # =================================== Object configuration ===================================

        self.title(w_title)
        self.geometry(f"{w_width}x{w_height}")
        self.minsize(w_width, w_height)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.w_label = customtkinter.CTkLabel(self, text=w_msg, font=customtkinter.CTkFont("console", 15, "normal"))
        self.w_label.grid(row=0, column=0, padx=10, pady=10, sticky="nswe")

        self.center(main_geometry)
        self.attributes('-topmost', True)
        if sound: playsound(sound, False)

    def center(self, main_geometry: tuple[int, int, int, int]) -> None:
        """
        Function used to center the warning window within the main window.
        This is done so the warning message does not goes unoticed.

        Parameters
        ----------
        main_geometry : tuple[int, int, int, int]
            Tuple that contains the geometry dimensions and displacement of the main
            window.
        """

        self.update_idletasks()
        x = main_geometry[2] + main_geometry[0]//3
        y = main_geometry[3] + main_geometry[1]//3
        self.geometry(f"+{x}+{y}")


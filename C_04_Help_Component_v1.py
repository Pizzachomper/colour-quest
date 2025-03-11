from tkinter import *
from functools import partial  # To prevent unwanted windows

# Classes start here
class StartGame:
    """
    Initial Game Interface
    """
    def __init__(self):
        """
        Colour quest GUI
        """

        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()
        
        # Create play button
        self.play_button = Button(self.entry_area_frame, font=("Arial", "16", "bold"),
                                    fg="#FFFFFF", bg="#0057D8", text="Play", width=10,
                                    command=self.check_rounds)
        self.play_button.grid(row=0, column=1, padx=20, pady=20)

    def check_rounds(self):
        """
        Checks user have entered 1 or more rounds
        """

        # Retrieve temperature to be converted
        rounds_wanted = 5
        self.to_play(rounds_wanted)

    def to_play(self, num_rounds):
        """
        Invokes Game GUI and takes across number of rounds to be played
        """
        Play(num_rounds)
        # Hide root window (hide rounds choice window)
        root.withdraw()

class Play:
    """
    Interface for playing the Colour Quest Game
    """

    def __init__(self, how_many):
        self.play_box = Toplevel()

        self.game_frame = Frame(self.play_box)
        self.game_frame.grid(padx=10, pady=10)

        self.heading_label = Label(self.game_frame, text="Colour Quest", font=("Arial", "14", "bold")
                                   padx=5, pady=5)
        self.heading_label.grid(row=0)

        self.hints_button = Button(self.game_frame, font=("Arial", "14", "bold"),
                                   text="Hints", width=15, fg="#FFFFFF",
                                   bg="#FF8000", padx=10, pady=10, command=self.to_hints)
        self.hints_button.grid(row=1)

    def to_hints(self):
        """
        Displays hints for playing game
        :return:
        """
        DisplayHints(self)

class DisplayHints:

    def __init__(self, partner):
        
        # setup dialouge box and background colour
        background = "#ffe6cc"
        self.hint_box = Toplevel()

        # disable hint button
        partner.to_hint_button.config(state=DISABLED)

        # If users press cross at top, closes hint box and releases hint button
        self.hint_frame.protocol('WM_DELETE_WINDOW',
                               partial(self.close_hint, partner)) 

        self.hint_frame = Frame(self.hint_frame, width=300,
                                height=200)
        self.hint_frame.grid()

        self.hint_heading_label = Label(self.hint_frame,
                                        text= "Hint / Info",
                                        font=("Arial", "14", "bold"))
        self.hint_heading_label.grid(row=0)

        hint_text = "To use the program, simply enter the temperature you wish to convert to either Celsisus or Fahrenheit \n"\
                    "Note that -273C and -459F, if you try to convert a temperature lower than these values, you will get an error message\n"\
                    "To see your calculation history and export it as a text file, please click the 'History / Export' button." 

        self.hint_text_label = Label(self.hint_frame,
                                     text=hint_text, wraplength=350,
                                     justify="left")
        self.hint_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.hint_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", 
                                     command=partial(self.close_hint, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on everything except the buttons
        recolour_list = [self.hint_frame, self.hint_heading_label,
                         self.hint_text_label]
        
        for item in recolour_list:
            item.config(bg=background)

    def close_hint(self, partner):
        partner.to_hint_button.config(state=NORMAL)
        self.hint_frame.destroy()



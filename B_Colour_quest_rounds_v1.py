from tkinter import *
from functools import partial  # To prevent unwanted windows

class StartGame:
    def __init__(self):
            """
            Colour quest GUI
            """

            self.temp_frame = Frame(padx=10, pady=10)
            self.temp_frame.grid()

            self.to_help_button = Button(self.temp_frame,
                                        text="Help / Info",
                                        bg="#CC6600",
                                        fg="#FFFFFF",
                                        font=("Arial", "14", "bold"), width=12,
                                        command=self.to_help)
            
            self.to_help_button.grid(row=1, padx=5, pady=5)

    def to_help(self):
        """
        Opens help dialogue box and disables help button (So users don't create multible boxes)
        """
        DisplayHelp(self)

class DisplayHelp:

    def __init__(self, partner):
        
        # setup dialouge box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at top, closes help and releases help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner)) 

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "In each round you will be invited to choose a colour.\n"\
                    "Your goal is to beat the target score and win the round (and keep your points)\n"\
                    "To begin, please choose how many rounds you'd like to play" 

        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "14", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF", 
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # List and loop to set background colour on everything except the buttons
        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]
        
        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Colour Quest")
    StartGame()
    root.mainloop()

number = input(int)

if number >= 1:
      print("You have chosen to play one round")

else:
     print("<error> Please enter an whole number more than 0")
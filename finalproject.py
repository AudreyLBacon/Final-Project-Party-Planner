
from Tkinter import *
import tkMessageBox
from partycalc import *

#partycalc.Class.
root = Tk()

class Application(Frame): # Create a class called 'Application' (Which inherits from the 'Frame' class)



	def __init__(self, master=None): # How to initialize the class, when created using Application()
		Frame.__init__(self, master)	# Initialize using Frame's __init__ function
		self.parent = master			# Set the parent variable to the optional value master
		
	def make_color(self):
		 self.configure(background = 'orchid1') #Too ugly, don't use.


	def suggestion(self):#addded for suggestion botton pop-up
   		self.tkMessageBox.showinfo( "Party Planner", "text stuff")#addded for suggestion


   	def get_meal_type(self):
   		selection = "Your meal will be ", str(self.meal_selection.get())
   		print selection

   	def get_location_type(self):
   		selection = "Your event will be held ", str(self.location_selection.get())
   		print selection

   	def get_service_type(self): 
   		selection = "Your Food Presentation Will Be ", str(self.service_selection.get())
   		print selection

   	def get_shape_type(self):# used in conditional
   		selection = "Your type of table will be" , str(self.shape_selection.get())
   		print selection


	def get_round_size_type(self):#used in conditional
		selection = "size" , int(self.round_size_selection.get())
   		print selection


	def get_rectangle_size_type(self):#used in conditional
		selection = "You selected the option", int(self.rectangle_size_selection.get())
   		print selection

	def get_seating_space_type(self):#used in conditional
		selection = "Your seating space choice is", str(self.seating_space_selection.get())
		print selection
   		
	def get_seating_share_type(self):#used in conditional
		selection = "Your seating preferance is", str(self.seating_share_selection.get())
		print selection

	    # make the next two functions print on another page what is requested(menu and seating chart), no need to print answer	
	def get_arrangement_sug_type(self):
		selection = "", str(self.arrangement_selection.get())
		print selection
	def get_menu_sug_type(self):
		selection = "", str(self.menu_selection.get())
		print selection
   	

	def create_widgets(self):
	    #GUI hellish repetition
	    # button - text- entry  

		self.meal_selection = StringVar()
		self.location_selection = StringVar()
		self.suggestion = StringVar()
		self.service_selection = StringVar()
		self.shape_selection = StringVar()
		self.round_size_selection = StringVar()		
		self.rectangle_size_selection = StringVar()
		self.seating_space_selection = StringVar()
		self.seating_share_selection = StringVar()
		self.arrangement_selection = StringVar()
		self.menu_selection = StringVar()
		self.color_scheme = StringVar()

		self.event_occasion = StringVar()
		self.event_guests = StringVar()
		self.event_time = StringVar()


		# Array of dictionaries, setting up radio buttons with labels.
		# Each entry in the array is a dictionary with a "label" and "options"
		# The "options" entry in the dictionary is an array with each radio button option.
		questions = [
			{'label': "Enter the Event Occasion", 'variable': self.event_occasion},
			{'label': "Enter the Number of Guests Expected", 'variable': self.event_guests},
			{'label': "Event Start and Finish Time", 'variable': self.event_time},

			{'label': "Choose Meal", 
				'options': ["Breakfast", "Brunch", "Lunch", "Dinner"], 
				'variable': self.meal_selection, 
				'command': self.get_meal_type
			},
			{'label': "Choose Location", 
				'options': ["Indoors", "Outdoors"], 
				'variable': self.location_selection, 
				'command': self.get_location_type
			},
			{'label': "Choose Service", 
				'options': ["Food to Table", "Buffet"], 
				'variable': self.service_selection, 
				'command': self.get_location_type
			},
			{'label': "Table Type", 
				'options': ["Round", "Rectangle"], 
				'variable': self.shape_selection, 
				'command': self.get_shape_type
			},
			{'label': "Round sizes", 
				'options': ["45", "60", "72"], 
				'variable': self.round_size_selection, 
				'command': self.get_shape_type
			},
			{'label': "Round sizes", 
				'options': ["45", "60", "72"], 
				'variable': self.shape_selection, 
				'command': self.get_round_size_type
			},
			{'label': "Rectangle sizes", 
				'options': ["72", "96", "120"], 
				'variable': self.rectangle_size_selection, 
				'command': self.get_rectangle_size_type
			},
			{'label': "Choose Seating Space", 
				'options': ["Max", "Spacious"], 
				'variable': self.seating_space_selection, 
				'command': self.get_seating_space_type
			},
			{'label': "Will guests sit together or require private tables?", 
				'options': ["Share", "Private"], 
				'variable': self.seating_share_selection, 
				'command': self.get_seating_share_type
			},
			{'label': "Would You Like Table Arrangment Suggestions?", 
				'options': ["Yes", "No"], 
				'variable': self.arrangement_selection, 
				'command': self.get_arrangement_sug_type
			},
			{'label': "What is your color scheme?",
				'variable': self.color_scheme
			},
			{'label': "Would You Like Menu Suggestions?", 
				'options': ["Yes", "No"], 
				'variable': self.menu_selection, 
				'command': self.get_menu_sug_type
			},
		]
		
		grid_row = 6

		for entry in questions:
			grid_row += 1 # Move down a row, then create the label
			Label(self, text=entry['label']).grid(row = grid_row, column = 0, columnspan = 3, sticky = W)
			grid_row += 1 # Move down a row and put the options.
			grid_column = 1 # Options start on column 1
			# If the dictionary has 'options', it's a radio button
			if 'options' in entry:
				for option in entry['options']:
					#First create the radio button
					btn = Radiobutton(self, text=option, value = option, variable = entry['variable'], command=entry['command'])
					# Then place the radio button on the grid
					btn.grid(row = grid_row, column = grid_column, sticky = W) 
					# If this is the first option, make it the default.
					if grid_column == 1:
						btn.select() 
					# Finally, move to the next column so we're ready for the next option
					grid_column += 1 
			# Otherwise, if the dictionary has no 'options', it's an Entry
			else: 
				Entry(self, textvariable = entry['variable']).grid(row = grid_row, column = grid_column, columnspan = 2, sticky = W)

		self.submit_button = Button(self, text ="Print Report", bg = "pink", command = self.reveal)
		self.submit_button.grid(row = grid_row + 1, column = 0, sticky = W)



	def reveal(self):
		#display based on what you input in input box, and shown in the other section - create later
		content = self.password.get()

		if content == "password":
			message = "Its stupid now"
		else:
			message = "blew it"

		self.text.delete(0.0,END) #delates input after done with it
		self.text.insert(0.0, message)

	def __init__(self,master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()		
		#self.configure(background = 'orchid1')#backround nightmare


def main():
	
	root.title("Party Planner")	
	root.geometry("575x768")# sets size of window
	root.configure(background = 'orchid1')
	app = Application(root)
	
	root.mainloop() #Tkinter loop that runs all the time to make graphic stay up
	

if __name__ == '__main__':
    main()
 	
'''
	def create_widgets():
		self.button1 = Button(self,text = "yes") #one way to make buttons
		self.button.grid()

		self.button2 = Button(self)
		self.button2.grid()
		self.button2 configure(text = "no")		#second way

		self.button3 = Button(self)				#third way
		self.button3.grid()      
    def __init__(self, master):

        # creates a label
        var_lbl_message = StringVar(master)  # Special Tkinter Variable for label text
        var_lbl_message.set("Party Planner")
        lbl_message = Label(master, textvariable=var_lbl_message)
        lbl_message.pack()

        # creates a text entry box
        entry_message = Entry(master)
        entry_message.insert(0, "text")
        entry_message.pack()

        # creates a button
        # command= sets the function to be called when the button is clicked.
        btn_ok = Button(master, text='Ok',command=lambda: var_lbl_message.set(entry_message.get()))
        btn_ok.pack()


# main function where an instance of the GUI is created
def main():
    root_widget = Tk()                    # creates a widget window which will hold all other widgets.
    root_widget.geometry("1050x768")       # sets the size of the window
    root_widget.title("Demo Input Text")  # set the title of the window
    app = AppMain(root_widget)            # creates an instance of AppMain which has all the other widgets
                                          # which will show up on the root_widget
    root_widget.mainloop()                # make the widget window run continuously

# if running file directly
# allow option to import file and call main() from another file
if __name__ == '__main__':
    main()
'''


	
'''
	def calculate(self):# calculates numbers for reports

	'''
 
# Future feature functions to expand on listed below:
# report include buffet servers or not
# report include waiters and waitress qty
# report include kitchen workers qty
# create food class 
# method to pick menu which then translates and prints shopping list on report
# method to add menus and recipe in dictionary from class,and print info as desired in report
# food method to calculate portions /qty of food to purchase/ per number of people from food class and party class or decide if both classes should be one class
# creat shopping list print out from food class and menu picked
# create function food helpers/ employees/ volunteers tracker: direct to google virtual sign up and live communications.
# create final print out which displays tables and chairs and side tables pattern, and  color, text of what is needed , time factors for set up and menue- three pages one final visual of set up and on page for menue and one instructional
# create method for food class enter your own menu
# future rewrite in html css and javascript

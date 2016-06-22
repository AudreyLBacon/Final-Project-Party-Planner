
from Tkinter import *
import tkMessageBox
from partycalc import *
import tkFont

#partycalc.Class.     
root = Tk()

class Application(Frame): # Create a class called 'Application' (Which inherits from the 'Frame' class)#frame is a Tkinter thing for layout that holds everything

	def __init__(self, master=None): # How to initialize the class, when created using Application()
		Frame.__init__(self, master)	# Initialize using Frame's __init__ function
		self.parent = master			# Set the parent variable to the optional value master


	def make_color(self):
		self.configure(background = 'orchid1') 


	def suggestion(self): # Expand later -add suggestion botton pop-up 
   		self.tkMessageBox.showinfo( "Party Planner", "text stuff")#addded for suggestion



   	def	calculate(self):
   		# Step One: Take the input from the GUI and put it into the party calculator.

   		party_calculator = None # Create an empty variable for use later. "None" means it's nothing yet.
   		if self.shape_selection.get() == "Round":  # Get if they picked "Round" or "Rectangle" from the GUI
   			# If they picked round, create a calculator from the PartyCalc class using the round size.
   			party_calculator = PartyCalc(self.num_guests,"Round",self.round_size_selection.get(),self.seating_space_selection.get())
   		else:
   			# If they picked rectangle, create a calculator using the rectangle size.
   			party_calculator = PartyCalc(self.num_guests,"Rectangle",self.rectangle_size_selection.get(),self.seating_space_selection.get())

   		# Step Two: This moves the input from the gui questions into the report window.
   		# This part only handles the questions that don't require math to answer.
   		text = "Occasion: " + self.event_occasion.get() + "\n"
   		# Plus-equals is short for: text = text + "More text". Start with what's already there, then add more.
   		text += "Meal: " + self.meal_selection.get() + "\n" 
   		text += "Location: " + self.location_selection.get() + "\n" 
   		text += "Service: " + self.service_selection.get() + "\n"
   		text += "Hours: " + self.event_time.get() + "\n"

   		# Find out which shape, so we know which size to print.
   		if self.shape_selection.get() == "Round":
   			text += "Table Type: " + self.round_size_selection.get() + " " + self.shape_selection.get() + "\n"
   		else:
   			text += "Table Type: " + self.rectangle_size_selection.get() + " " + self.shape_selection.get() + "\n"

   		text += "Private Tables: " + self.seating_share_selection.get() + "\n"
   		text += "Seating: " + self.seating_space_selection.get() + "\n"
		text += "Color Scheme: " + self.color_scheme.get() + "\n"
   		text += "Menu set up instructions included: " + self.menu_selection.get() + "\n"
   		text += "Table arrangement instructions included: " + self.arrangement_selection.get() + "\n"
   		
		# Last Step: Calls the calculate() method on the PartyCalc class.
   		text += party_calculator.calculate()  # Calculate
   		self.label_output.configure(text = text)  # Send the text to the report Label on the gui.

   	# This method reads the number of guests from the GUI and then saves it as an Integer.
	def validate_guests(self):
		try: # Try to make it an int...
			self.num_guests = int(self.event_guests.get())
		except ValueError: # But if it crashes, just use 0.
			self.num_guests = 0
		# After the user types a number of guests, call calculate() method to recalculate.
		self.calculate()
		return True
		
	# This code disables the round sizes when the user picks rectangle, and vice versa.
   	def get_shape_type(self):
   		if self.shape_selection.get() == "Round":
   			for item in self.survey_elements[8]:
   				print item
   				item.configure(state = "disabled")
   			for item in self.survey_elements[7]:
   				item.configure(state = "normal")
   		else:
   			for item in self.survey_elements[7]:
   				item.configure(state = "disabled")
   			for item in self.survey_elements[8]:
   				item.configure(state = "normal")
   		self.calculate()

   	# This function creates the GUI widgets.
	def create_widgets(self):
		self.num_guests = 0
		self.grid()
		# Step One: Divide the screen into two halfs and color them. 
		self.survey_frame = Frame(self, bg = "orchid1")  # This frame has the survey questions
		self.survey_frame.grid(row=0,column=0, sticky = N+W+S) # Tells the GUI where on the screen to show the survey section
		
		self.result_frame = Frame(self, bg = "orchid1") # Thhidis frame has the results.
		self.result_frame.grid(row=0,column=1) # Tells the GUI where on the screen to show the results

		# StringVar is a class used by Tkinter to store strings for the GUI.
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

		# List of dictionaries, setting up radio buttons with labels.
		# Each entry in the list is a dictionary with a "label" and "options"
		# The "options" entry in the dictionary is a list with each radio button option.
		questions = [
			{'label': "Enter the Event Occasion", 'variable': self.event_occasion},
			{'label': "Enter the Number of Guests Expected", 'variable': self.event_guests, 'command': self.validate_guests},
			{'label': "Event Start and Finish Time", 'variable': self.event_time},
			{'label': "Choose Meal", 
				'options': ["Breakfast", "Brunch", "Lunch", "Dinner"], 
				'variable': self.meal_selection, 
				'command': self.calculate
			},
			{'label': "Choose Location", 
				'options': ["Indoors", "Outdoors"], 
				'variable': self.location_selection, 
				'command': self.calculate
			},
			{'label': "Choose Service", 
				'options': ["Food to Table", "Buffet"], 
				'variable': self.service_selection, 
				'command': self.calculate
			},
			{'label': "Table Type", 
				'options': ["Round", "Rectangle"], 
				'variable': self.shape_selection, 
				'command': self.get_shape_type
			},
			{'label': "Round sizes", 
				'options': ["48", "60", "72"], 
				'variable': self.round_size_selection, 
				'command': self.get_shape_type
			},
			{'label': "Rectangle sizes", 
				'options': ["6ft", "8ft", ], 
				'variable': self.rectangle_size_selection, 
				'command': self.get_shape_type
			},
			{'label': "Choose Seating Space", 
				'options': ["Max", "Spacious"], 
				'variable': self.seating_space_selection, 
				'command': self.calculate
			},
			{'label': "Will guests sit together or require private tables?", 
				'options': ["Share", "Private"], 
				'variable': self.seating_share_selection, 
				'command': self.calculate
			},
			{'label': "Table Arrangment instruction included?", 
				'options': ["Yes", "No"], 
				'variable': self.arrangement_selection, 
				'command': self.calculate
			},
			{'label': "What is the color scheme?",
				'variable': self.color_scheme,
				'command': self.calculate
			},
			{'label': "Menu set up instructions included?", 
				'options': ["Yes", "No"], 
				'variable': self.menu_selection, 
				'command': self.calculate
			},
		]
		
		grid_row = 0

		self.survey_elements = []

		# This section creates the gui.
		for entry in questions: # for loop
			survey_array = []
			grid_row += 1 # Move down a row, then create the label
			
			lbl = Label(self.survey_frame,background = 'orchid1', text=entry['label'])
			lbl.grid(row = grid_row, column = 0, columnspan = 3, sticky = W)
			survey_array.append(lbl)
			grid_row += 1 # Move down a row and put the options.
			grid_column = 1 # Options start on column 1
			# If the dictionary has 'options', it's a radio button

			if 'options' in entry:
				for option in entry['options']:
					#First create the radio button
					btn = Radiobutton(self.survey_frame, text=option, value = option, background = 'orchid1', variable = entry['variable'], command=entry['command'])
					survey_array.append(btn)
	
					# Then place the radio button on the grid
					btn.grid(row = grid_row, column = grid_column, sticky = W) 
					# If this is the first option, make it the default.
					if grid_column == 1:
						btn.select() # This WAS how I made a line default
					# Finally, move to the next column so we're ready for the next option
					grid_column += 1 
			# Otherwise, if the dictionary has no 'options', it's an Entry
			else: 
				if 'command' in entry:
					ent = Entry(self.survey_frame, textvariable = entry['variable'], validatecommand = entry['command'], validate = 'focus')
					ent.grid(row = grid_row, column = grid_column, columnspan = 2, sticky = W)
				else:
					ent = Entry(self.survey_frame, textvariable = entry['variable'])
					ent.grid(row = grid_row, column = grid_column, columnspan = 2, sticky = W)

			#Store references in list.
			self.survey_elements.append(survey_array)

		# Now that the questions are set up, add a button for printing the report.


		self.submit_button = Button(self.survey_frame, text ="Print Report", bg = "pink", command = self.reveal)
		self.submit_button.grid(row = grid_row + 1, column = 0, sticky = W)

		label_font = tkFont.Font(family='Arial', size=18)# block for report
		self.label_output = Label(self.result_frame, font=label_font, text="Please fill out your choices so that we can calculate the result.")
		self.label_output.grid(row = 2, column = 5, sticky = E)

	def reveal(self):
		#display based on what you input in input box, and shown in the other section - create later
		content = self.password.get()

		if content == "password":
			message = "Its stupid now"
		else:
			message = "blew it"

		self.text.delete(0.0,END) #delates input after done with it
		self.text.insert(0.0, message)

	#When the application object is created, run the create_widgets function.
	def __init__(self,master):
		Frame.__init__(self, master)
		self.grid()
		self.create_widgets()		
		#self.configure(background = 'orchid1')#backround nightmare


#This is the main function, which creates our application object
def main():
	root.title("Party Planner")	# set the title of the window
	root.geometry("1024x768")# sets size of window
	root.configure(background = 'orchid1')
	app = Application(root)# creates an instance of AppMain which has all the other widgets
                                          # which will show up on the root_widget

	app.configure(background = 'orchid1')
	
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

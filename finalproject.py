

'''
	def create_widgets():
		self.button1 = Button(self,text = "yes") #one way to make buttons
		self.button.grid()

		self.button2 = Button(self)
		self.button2.grid()
		self.button2 configure(text = "no")		#second way

		self.button3 = Button(self)				#third way
		self.button3.grid()
		self.button3["text"] = "submit"

		
'''


from Tkinter import *
import tkMessageBox
root = Tk()

class Application(Frame): # Create a class called 'Application' (Which inherits from the 'Frame' class)

#fra

	def __init__(self, master=None): # How to initialize the class, when created using Application()
		Frame.__init__(self, master)	# Initialize using Frame's __init__ function
		self.parent = master			# Set the parent variable to the optional value master
		
	def make_color(self):
		 self.configure(background = 'orchid1') #Too ugly, don't use.


	def suggestion(self):#addded for suggestion botton pop-up
   		self.tkMessageBox.showinfo( "Party Planner", "text stuff")#addded for suggestion


   	def get_meal_type(self):
   		selection = "you selected the option", str(self.meal_selection.get())
   		print selection

   	def get_location_type(self):
   		selection = "you selected the option", str(self.location_selection.get())
   		print selection

   	def get_service_type(self): 
   		selection = "you selected the option", str(self.servive_selection.get())
   		print selection

   	def get_shape_type(self):
   		selection = "you selected the option" , str(self.shape_selection.get())
   		print selection


	def get_round_size_type(self):
		selection = "you selected the option" , int(self.round_size_selection.get())
   		print selection


	def get_rectangle_size_type(self):
		selection = "you selected the option", int(self.rectangle_size_selection.get())
   		print selection

	def get_seating_space_type(self):
		selection = "you selected the option", str(self.seating_space_selection.get())
		print selection
   		
	def get_seating_share_type(self):
		selection = "you selected the option", str(self.seating_share_selection.get())
		print selection
	def get_arrangement_sug_type(self):
		selection = "you selected the option", str(self.arrangement_selection.get())
		print selection
	def get_menu_sug_type(self):
		selection = "you selected the option", str(self.menu_selection.get())
		print selection
	


   	

	def create_widgets(self):
	#GUI hellish repetition
	# button - text- entry  -(password :code to display to another box ----find out how)

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





		self.instruction = Label(self, text = "Enter the Party Occasion")
		self.instruction.grid(row = 1, column = 0, columnspan = 2, sticky = W)
		
		self.password = Entry(self)
		self.password.grid(row = 2, column = 1, sticky = W)

		self.instruction = Label(self, text = "Enter the Number of Guests Expected")
		self.instruction.grid(row = 4, column = 0, columnspan = 2, sticky = W)
		
		self.password = Entry(self)
		self.password.grid(row = 5, column = 1, sticky = W)

		self.instruction = Label(self, text = "Choose Meal")
		self.instruction.grid(row = 7, column = 0, columnspan = 2, sticky = W)
		
		self.breakfast_button = Radiobutton(self, text = "Breakfast",fg = "orchid1",variable = self.meal_selection, value = "Breakfast" , command = self.get_meal_type )
		self.breakfast_button.grid(row = 8, column = 1,columnspan = 2, sticky = E)
		self.lunch_button = Radiobutton(self, text = "Lunch",variable = self.meal_selection, value = "lunch" , command = self.get_meal_type)
		self.lunch_button.grid(row = 8, column = 1,columnspan = 1, sticky = W)
		self.dinner_button = Radiobutton(self, text = "Dinner",variable = self.meal_selection, value = "dinner" , command = self.get_meal_type)
		self.dinner_button.grid(row = 8, column = 7, columnspan = 2, sticky = W)
		self.Brunch_button = Radiobutton(self, text = "Brunch",variable = self.meal_selection, value = "brunch" , command = self.get_meal_type)
		self.Brunch_button.grid(row = 8, column = 10, columnspan = 12, sticky = W)

		self.instruction = Label(self, text = "Input Start and Finish Time")
		self.instruction.grid(row = 10, column = 0, columnspan = 2, sticky = W)
		
		self.password = Entry(self)
		self.password.grid(row = 11, column = 1, sticky = W)

		self.instruction = Label(self, text = "Choose Location")
		self.instruction.grid(row = 13, column = 0, columnspan = 2, sticky = W)
		
		self.outdoor_button = Radiobutton(self, text = "Outdoor",variable = self.location_selection, value = "outdoor", command = self.get_location_type)
		self.outdoor_button.grid(row = 14, column = 1,columnspan = 2, sticky = W)
		self.indoor_button = Radiobutton(self, text = "Indoor",variable = self.location_selection, value = "indoor", command = self.get_location_type)
	 	self.indoor_button.grid(row = 14, column = 1,columnspan = 2, sticky = E)
		
		self.submit_button = Button(self, text = "suggestion", command = self.suggestion)#try to add s button
		self.submit_button.grid(row = 14, column = 1,columnspan = 3, sticky = W)# s button position
		self.instruction = Label(self, text = "Choose Service")
		self.instruction.grid(row = 16, column = 0, columnspan = 2, sticky = W)
		
		self.served_button= Radiobutton(self, text = "Food Served to Table",variable = self.service_selection, value = "food to table", command = self.get_service_type )
		self.served_button.grid(row = 14, column = 1,columnspan = 1, sticky = E)
		self.submit_button.grid(row = 17, column = 1,columnspan = 2, sticky = W)
		self.buffet_button = Radiobutton(self, text =" Buffet Style",variable = self.service_selection, value = "buffet style" , command = self.get_service_type)
		self.buffet_button.grid(row = 17, column = 1,columnspan = 1, sticky = E)

		self.instruction = Label(self, text = "Choose Table Type")
		self.instruction.grid(row = 19, column = 0, columnspan = 2, sticky = W)
		
		self.round_button = Radiobutton(self, text ="Round",variable =  self.shape_selection, value = "round" , command = self.get_shape_type )
		self.round_button.grid(row = 20, column = 1,columnspan = 2, sticky = W)
		self.rectangle_button = Radiobutton(self, text ="Rectangle",variable = self.shape_selection, value = "rectangle" ,command = self.get_shape_type)
		self.rectangle_button.grid(row = 20, column = 1,columnspan = 1, sticky = E)


		self.instruction = Label(self, text = "Choose Round Table Size")
		self.instruction.grid(row = 22, column = 0, columnspan = 2, sticky = W)

		self.fortyfive_button = Radiobutton(self, text = '45"    ',variable = self.round_size_selection, value = "45", command = self.get_round_size_type  )
		self.fortyfive_button.grid(row = 23, column = 1,columnspan = 2, sticky = W)
		self.sixty_button = Radiobutton(self, text = '   60"     ' ,variable = self.round_size_selection, value = "60", command = self.get_round_size_type  )
		self.sixty_button.grid(row = 23, column = 1,columnspan = 1, sticky = E)
		self.seventy_two_button = Radiobutton(self, text = '72"',variable = self.round_size_selection , value ="72",command = self.get_round_size_type )
		self.seventy_two_button.grid(row = 23, column = 7, columnspan = 2, sticky = W)


		self.instruction = Label(self, text = "Choose Rectangle Size")
		self.instruction.grid(row = 25, column = 0, columnspan = 2, sticky = W)

		self.six_button = Radiobutton(self, text = "6'     ",variable = self.rectangle_size_selection, value = 6 , command = self.get_rectangle_size_type)
		self.six_button.grid(row = 26, column = 1,columnspan = 2, sticky = W)
		self.seven_button = Radiobutton(self, text = "   7'",variable = self.rectangle_size_selection, value = 7, command = self.get_rectangle_size_type )
		self.seven_button.grid(row = 26, column = 1,columnspan = 1, sticky = E)
		self.eight_button = Radiobutton(self, text = "8'  ",variable = self.rectangle_size_selection, value =  8 , command = self.get_rectangle_size_type )
		self.eight_button.grid(row = 26, column = 7, columnspan = 2, sticky = W)




		self.instruction = Label(self, text = "Choose Seating Space")
		self.instruction.grid(row = 28, column = 0, columnspan = 2, sticky = W)
		self.max_button = Radiobutton(self, text = "Max",variable = self.seating_space_selection, value = "max", command = self.get_seating_space_type )
		self.max_button.grid(row = 29, column = 1,columnspan = 1, sticky = E)
		self.spacious_button = Radiobutton(self, text = "Spacious Seating",variable = self.seating_space_selection, value = "spacious seating"  , command = self.get_seating_space_type)
		self.spacious_button.grid(row = 29, column = 1,columnspan = 1, sticky = W)
		



		self.instruction = Label(self, text = "Will Guests Share Tables?")
		self.instruction.grid(row = 31, column = 0, columnspan = 2, sticky = W)
		self.yes_button = Radiobutton(self, text = "Yes",variable = self.seating_share_selection, value = "yes", command = self.get_seating_share_type )
		self.yes_button.grid(row = 32, column = 1,columnspan = 2, sticky = W)
		self.no_button = Radiobutton(self, text = "No",variable = self.seating_share_selection, value = "no", command = self.get_seating_share_type )
		self.no_button.grid(row = 32, column = 1,columnspan = 1, sticky = E)		

		self.instruction = Label(self, text = "Would You Like Table Arrangment Suggestions?")
		self.instruction.grid(row = 34, column = 0, columnspan = 2, sticky = W)
		self.yes2_button = Radiobutton(self, text = "Yes",variable = self.arrangement_selection, value = "yes", command = self.get_arrangement_sug_type )
		self.yes2_button.grid(row = 35, column = 1,columnspan = 2, sticky = W)
		self.no_button = Radiobutton(self, text = "No",variable = self.arrangement_selection, value = "no" , command = self.get_arrangement_sug_type )
		self.no_button.grid(row = 35, column = 1,columnspan = 1, sticky = E)

		self.instruction = Label(self, text = "Input Your Two Major Color Theme")
		self.instruction.grid(row = 37, column = 0, columnspan = 2, sticky = W)
		self.password = Entry(self)
		self.password.grid(row = 38, column = 1, sticky = W)

		self.instruction = Label(self, text = "Would You Like Menu Suggestions?")
		self.instruction.grid(row = 40, column = 0, columnspan = 2, sticky = W)

		self.yes3_button = Radiobutton(self, text = "Yes",variable = self.menu_selection, value = "yes", command = self.get_menu_sug_type )
		self.yes3_button.grid(row = 41, column = 1,columnspan = 2, sticky = W)
		self.no3_button = Radiobutton(self, text = "No",variable = self.menu_selection, value = "no", command = self.get_menu_sug_type )
		self.no3_button.grid(row = 41, column = 1,columnspan = 1, sticky = E)

		self.submit_button = Button(self, text ="Print Report", bg = "pink", command = self.reveal)
		self.submit_button.grid(row = 44, column = 0, sticky = W)

		self.text = Text(self, width = 35, height = 5, wrap = WORD)
		self.text.grid(row = 45, column = 0, columnspan = 2, sticky = W)


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
		#self.configure(background = 'orchid1')backround nightmare


def main():
	
	root.title("Party Planner")	
	root.geometry("1024x768")# sets size of window
	root.configure(background = 'orchid1')
	app = Application(root)
	
	root.mainloop()
	
				#(backround = "pink")
	

	

if __name__ == '__main__':
    main()

#class Food(object):#make later
 	

'''
	      
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
 

		


# report include buffet servers or not
# report include waiters and waitress qty
# report include kitchen workers qty

# create food class

 

#method to pick menu which then translates and prints shopping list on report


#method to add menus and recipe in dictionary from class? and print menu (not recipie) in report


'''


# food method to calculate portions /qty of food to purchase/ per number of people from food class and party class or decide if both classes should be one class

# creat shopping list print out from food class and menu picked

# create function food helpers/ employees/ volunteers tracker: direct to google virtual sign up and live communications.

# create final print out which displays tables and chairs and side tables pattern, and  color, text of what is needed , time factors for set up and menue- three pages one final visual of set up and on page for menue and one instructional

# create method for food class enter your own menu

'''
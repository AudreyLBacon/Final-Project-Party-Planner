import math
 #create calculater method: calculates number of chairs, table, and tables needed based on guest number and ssome of the suggestions and print reports.
	
    
class PartyCalc(object):   #find out how to connect the answers/button into here from finalproject.py
	def __init__(self, guests, tableshape, tablesize, seating):
		self.tablesize = tablesize
		self.new_chair_qty = 0
		self.total_tables = 0 
		self.tableshape = tableshape        
		self.guests = int(guests)
		self.seating = seating
		self.table_pattern = 0
		self.tables = 0

		'''
			elif self.tableshape == "combination" : 
			rectangle_combo_qty_tables = raw_input(" How many rectangle tables?")
			round_combo_qty_tables = raw_input("How many round tables ") #button input integers
			
			total_combo_tables = rectangle_combo_qty_tables + round_combo_qty_tables
			combo_chairs_total = rectangle_combo_qty_tables / 6 + round_combo_qty_tables
			if self.tablesize  == 60 and  self.seating == "Max" and self.tableshape == "Combination":
					print " total tables needed are ", total_combo_tables, "with", reqtangle_combo_qty, "reqtangle tables and", round_combo_qty, "round tables and."
			elif self.tablesize == 72:
					print " total tables needed are ", total_combo_tables, "with", reqtangle_combo_qty, "reqtangle tables and ", round_combo_qty, "round tables and .", (round_combo_qty * 8 ) +  6 
		'''
		

	def calculate(self):
		new_chair_qty = 10

		if  self.tablesize == "72" and self.seating == "Max" or self.tablesize == "8ft":
			new_chair_qty = 10 
			total_tables = int(math.ceil(self.guests / 10.0))
		
		elif self.tablesize == "60" and self.seating != "Max" or self.tablesize == "48" and self.seating == "Max":
			new_chair_qty = 6 
			total_tables = int(math.ceil(self.guests / 6.0))
		elif self.tablesize == "72" and self.seating != "Max" or self.tablesize == "60" and self.seating == "Max" or self.tablesize == "6ft":
			new_chair_qty = 8 
			total_tables = int(math.ceil(self.guests / 8.0))
		elif self.tablesize == "48" and self.seating != "Max":
			new_chair_qty = 4
			total_tables = int(math.ceil(self.guests / 4.0))
		else:
			return "Somethings wrong here!"

		textvar = "Expected Guests: " + str(self.guests) + "\n"
		textvar += "Total tables needed is " + str(total_tables) + "\n" 
		textvar += "Total chairs needed is " + str(new_chair_qty * total_tables) + " with " +  str(new_chair_qty) + " chairs per table\n"
		textvar += "You will have " + str((new_chair_qty * total_tables) - self.guests) + " extra table spaces and chairs."
		
		return textvar
        
	def	pattern_and_color(self):#generate sample configs of pattern and color in report.
	 # info taken from  def questions  and def calc functions and using variables from class
	# put in a pattern selected or pre selected and add colors to table and centerpiece#	
		if self.table_pattern == "Yes" and self.tables == "Round" and self.serving_style == "Buffet":
			print self.pattern_1
		elif self.table_pattern == "Yes" and self.tables == "Rectangle" and self.serving_style == "Buffet":
			print self.pattern_2
		elif self.table_pattern == "Yes" and self.tables == "Combination" and serving_style == "Buffet":
			print self.pattern_3
		elif self.table_pattern == "Yes" and self.tables == "Round" and self.serving_style == "Non Buffet":
			print self.pattern_4

	def ask_questions(self):   # below is before button GUI conversion
		#The answers below will be buttons- redo answers for buttons

		# put all answers in a Party class 

		print ("Welcome to Party Planner. Please answer the questions. If you do not know the answer type 'd' for I don't know. ")
		self.occasion = raw_input ("What is the party occasion? " )
		print self.occasion
		self.guests = int(raw_input("How many guests are coming? " )) # use in table method
		print self.guests
		self.meal_time = raw_input("Will this be a Breakfast, Brunch, Lunch or Dinner?" ).title()
		print self.meal_time
		self.start_finish = raw_input (" What is the desired start and finish time?" )
		print self.start_finish
		self.where = raw_input("Will this be indoors or outdoors? ").title() 
		#bring to more questions if outside is picked(tents needed, weather)# use in method Table ?
		print self.where
		self.serving_style = raw_input ("Will this be a buffet style? type 'bs' style? type  or buffet style non self serve? type ").title() # use in table method
		print self.serving_style
		# page 2 report add 8 rectangles for buffet style and dessert /drink stations
		self.tableshape = raw_input ("What shape of tables will you be using for dining? all r=round, rec= rectangle, comb = combination, d = don't know please suggest" ).title() # use in table method	
		print self.tables
		#If answer is combo then Ask:
		#print raw_input "how many rectangles and how many rounds?"#new calculation goes to calc def and prints combine calc on page 2 report
		self.group_seating = raw_input ("Will guests have private table seating or shared table seating?")
		print  self.group_seating
		self.tablesize = int(raw_input('Would you like 60" or 72" size round tables? Enter size or zero for suggestions ' )) # use in table method
		print self.tablesize
		self.seating = raw_input("Do you prefer max seating per table ? or more spacious seating at tables ?" ).title() 
		# use in table method
		print self.seating
		self.color_scheme = raw_input ("What two colors will be your dominant color scheme ? " ).title() # use in table method
		print self.color_scheme
		# then print on page 3 end report :pattern and color of tables
		self.food_suggest = raw_input ("Would you like food suggestions?" ).title()
		# bring to food menue samples or print in page three , calc in food function
		print self.food_suggest
		# then go to food sugesstion page or print food sugestion menu's
		self.table_pattern = raw_input("Would you like seating arrangement suggestions?" ).title()# bring to patterns for seating people
		print self.table_pattern
		#then print on page 4 end report
		self.helpers = int(raw_input("How many people will be helping you?"))#if they know store, if not redirect page to number of people needed per number of guests
		# report qty needed on page 2 reprt

# Main code, runs only when the file is executed from the terminal, not imported.
if __name__ == '__main__':
	pc = PartyCalc(0,0,0,0)
	pc.ask_questions() #calling the method ask_questions
	pc.calculate() # calling the method calculate
	pc.pattern_and_color() # 
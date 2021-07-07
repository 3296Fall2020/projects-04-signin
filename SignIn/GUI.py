# This is the code for the GUI. Copy/Paste into Python editor.
# Written by Madison Stock - Application Development Intern July-August 2019
# Last updated August 14, 2019

#testing

import datetime
from tkinter import *
from tkinter import messagebox

after_id = None

# Function to set focus 
def focus1(event): 
	# set focus on the name_field box 
	name_field.focus_set() 

# Function for clearing the 
# contents of text entry boxes 
def clear(): 
	
	# clear the content of text entry box  
	name_field.delete('0', END) 
	name_field.insert(0, "OpenNet Username (ex. LastnameF)")
	office_field.delete('0', END)
	office_field.insert(0, 'Office Symbol (ex. FSI/SAIT)')
	
	#reset drop-down menus to default
	tkvar.set("-- Choose Activity --")
	tkvar2.set("-- Choose Purpose --")


def insert(): 
	
# if user does not fill any entry 
# then print error message 
	if (name_field.get() == "OpenNet Username (ex. LastnameF)" or
		name_field.get() == "" or
		office_field.get() == "Office Symbol (ex. FSI/SAIT)" or
		office_field.get() == "" or
		(tkvar.get() == "-- Choose Activity --" and
		tkvar2.get() == "-- Choose Purpose --")): 
		
		messagebox.showerror("Error", "Please Enter Valid Information")

	else: 

#when user fills out information, the data.txt file is opened
		f = open("data.txt", "a+")
		#print('Success, file Opened')

#method for getting current date and time
		date = datetime.datetime.now().strftime("%m-%d-%y %H:%M")

#On submission, the user is prompted to verify if the info they entered is correct
		msg = messagebox.askyesno('Just Checking...', 'Is this information correct?')
		
		if msg == True:

#if the user clicked 'Yes' the data is written into the data.txt document, the file is closed
#cursor is reset to the name field and all drop-down menus are reset to default for the next user
			f.write(date + ' ')
			f.write(name_field.get() + ' ')
			f.write(office_field.get() + ' ')
			f.write(tkvar.get() + ' ')
			f.write(tkvar2.get() + '\n')
			f.close()
			clear()
			name_field.focus_set() 

	
			#print ("Wrote the Stuff")

		else:
#if the user clicked no, the information is cleared and reset
			clear()
			#print("Did not Write the Stuff")

def on_click_clear_name(event):
	name_field.delete('0', END)

def on_click_clear_office(event):
	office_field.delete('0', END)

def session_end():
    clear()

def reset_timer(event=None):
    global after_id
    if after_id is not None:
        root.after_cancel(after_id)
    after_id = root.after(45000, session_end)
	

if __name__ == "__main__": 
	

	# create a GUI window 
	root = Tk() 
	
	reset_timer()


	# set the background colour of GUI window 
	frame = Frame(root, bd=2, relief=SUNKEN)
	frame.grid_rowconfigure(0, weight=1)
	frame.grid_columnconfigure(0, weight=10)
	root.configure(background='light blue') 
	

# set the title of GUI window 
	root.title("Welcome to the Sandbox!") 

# set the configuration (size) of GUI window 
	#root.geometry("1800x1200")
	width, height = root.winfo_screenwidth(), root.winfo_screenheight()
	root.geometry('%dx%d+0+0' % (width,height))


# create label names 
	heading = Label(root, text="Welcome to the SAIT Sandbox!", bg="light blue", font = 'Courier 60 bold', fg='steel blue', justify = CENTER) 
	
	under_text = Label(root, text="tap or click to sign in below", bg = 'light blue', font = "TrebuchetMS 22", fg= 'snow4', justify = CENTER)
	

# grid method is used for placing 
# the LABEL widgets at respective positions 
# in table like structure

	heading.grid(row=0, column=2)

	under_text.grid(row=1, column=2)

	root.grid_rowconfigure(0, minsize= 150)
	root.grid_rowconfigure(2, minsize=110)
	root.grid_rowconfigure(3, minsize=110)
	root.grid_rowconfigure(4, minsize=110)
	root.grid_rowconfigure(5, minsize=110)
	root.grid_rowconfigure(6, minsize = 100)

	root.grid_columnconfigure(2, weight=2)

# create a text entry box 
# for typing the information 
name_field = Entry(root)
office_field = Entry(root)

name_field.bind('<Button-1>', on_click_clear_name)
office_field.bind('<Button-1>', on_click_clear_office)

name_field.insert(0, "OpenNet Username (ex. LastnameF)")
office_field.insert(0, "Office Symbol (ex. FSI/SAIT)")

name_field.config(fg = 'steel blue', font = 'TrebuchetMS 18', justify = CENTER)
office_field.config(fg = 'steel blue', font = 'TrebuchetMS 18', justify = CENTER)

root.bind_all("<Key>", reset_timer)
root.bind_all("<ButtonRelease>", reset_timer)

root.title("AYOO Sandbox")

# creating drop-down menu
#tkvar and tkvar2 store the user input
tkvar = StringVar(root)
tkvar2 = StringVar(root)

actChoices = {'Meeting', 'EX-Work', 'Consultation', 'SAIT-DIN', 'Web/Video-Conference', 'Workshop'}
tkvar.set('-- Choose Activity --') #sets default option

purpChoices = {'Ed-Tech', 'Curriculum', 'SAIT-Operations', 'Solutions', 'Tour/Visit', 'Professional-Development'}
tkvar2.set('-- Choose Purpose --')

#configures drop-down menus (popupMenu), the box you actually see
popupMenu = OptionMenu(root, tkvar, *actChoices)
popupMenu.configure(background = "steel blue", activebackground = 'white', fg = 'white', font = 'Bodoni 20 bold', justify = CENTER)
popupMenu["menu"].config(bg='steel blue', font = 'TrebuchetMS 18 bold', fg = 'white', relief = FLAT)

popupMenu2 = OptionMenu(root, tkvar2, *purpChoices)
popupMenu2.configure(background = "steel blue", activebackground = 'white', fg = 'white', font = 'Bodoni 20 bold', justify = CENTER)
popupMenu2["menu"].config(bg='steel blue', font = 'TrebuchetMS 18 bold', fg = 'white', relief = FLAT)


def change_dropdown(*args):
 
	tkvar.trace('w', change_dropdown)
	tkvar2.trace('w', change_dropdown) 

# grid method is used for placing 
# the INPUT widgets at respective positions 
# in table like structure
name_field.grid(row=2, column=2, ipadx="120", ipady='12') 
office_field.grid(row=3, column=2, ipadx="120", ipady='12' )
popupMenu.grid(row=4, column=2, ipadx="105", ipady='12')
popupMenu2.grid(row=5, column=2, ipadx="105", ipady='12')  

 
submit = Button(root, text="Submit", fg="black", font = 'Bodoni 12 bold', activebackground = 'gold',
							bg="white", command=insert) 
submit.grid(row=6, column=2)

clear_button = Button(root, text="Reset", fg = "black", font = 'Bodoni 12 bold', bg = 'white', command = clear)
clear_button.grid(row= 7, column=2)


	# start the GUI 
root.mainloop() 
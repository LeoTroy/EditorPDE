#!/usr/bin/python
# -*- coding: utf-8 -*-


from tkinter import *
from tkinter.filedialog import *
from customText import *
 
class Application(Frame):
 
    def __init__(self, master=None):


    	 # ----------------------- GENERAL INFORMATION --------------------------

        Frame.__init__(self, master, background="grey")

        self.path = ""


        # ---------------------------- BARRE DE MENU ----------------------------

        self.barre_menu = Menu(self.master)
 
        # --- Menu File
        self.file = Menu(self.barre_menu, tearoff=0)
        self.barre_menu.add_cascade(label="File",menu=self.file)

        
        self.file.add_command(label="New File", command=self.newFile) # -------- New File        
        self.file.add_command(label="Open File", command=self.openFile) # ------ Open File       
        self.file.add_command(label="Save", command=self.save)  # -------------- Save
        self.file.add_command(label="Exit", command=self.exit) # --------------- Exit
 
        # --- Afficher le menu
        self.master.config(menu=self.barre_menu)

        # ------------------------------------------------------------------------

        self.numView = Text(self.master, width=3, state='disabled')
        self.numView.tag_configure('center', justify='center') 
        self.numView.grid(row=0, column=0)

        self.input_canvas = CustomText(self.master, bg="gray18", fg="white", insertbackground="white")
        self.input_canvas.grid(row=0, column=1)

        self.input_canvas.tag_config("class", foreground="red")
        self.input_canvas.tag_config("type", foreground="orange2")
        self.input_canvas.tag_config("cond", foreground="dark slate blue")

        self.writeNumRow()


    # ----------------------------------------------------------------------------

    # -------------------------------- NEW FILE ----------------------------------
 
    def newFile(self) : 
    	self.input_canvas.delete("1.0", "end")


    # --------------------------------- OPEN FILE ---------------------------------
 
    def openFile(self) : 

    	file_name = askopenfilename(filetypes=[("Text files", "*.pde")])
    	self.path = file_name

    	file = open(file_name, "r")
    	self.input_canvas.delete("1.0", "end")
    	self.input_canvas.insert("1.0", file.read())
    	file.close()

    	self.updateColor() ;


    # -------------------------------- SAVE FILE ----------------------------------

    def save(self) : 

    	if self.path == "" :
    		self.path = asksaveasfilename() + ".pde"

    	total_text = self.input_canvas.get("1.0", "end-1c")

    	file = open(self.path, "w+")
    	file.write(total_text)
    	file.close()

    # ------------------------------ EXIT PROGRAM ---------------------------------

    def exit(self): 

    	self.master.destroy()

    def updateColor(self) :

    	self.input_canvas.highlight_pattern("class", "class")
    	self.input_canvas.highlight_pattern("public", "class")
    	self.input_canvas.highlight_pattern("new", "class")
    	self.input_canvas.highlight_pattern("super", "class")
    	self.input_canvas.highlight_pattern("return", "class")
    	self.input_canvas.highlight_pattern("this", "class")
    	self.input_canvas.highlight_pattern("void", "class")
    	self.input_canvas.highlight_pattern("private", "class")

    	self.input_canvas.highlight_pattern("int", "type")
    	self.input_canvas.highlight_pattern("float", "type")
    	self.input_canvas.highlight_pattern("string", "type")
    	self.input_canvas.highlight_pattern("boolean", "type")

    	self.input_canvas.highlight_pattern("if", "cond")
    	self.input_canvas.highlight_pattern("for", "cond")
    	self.input_canvas.highlight_pattern("while", "cond")
    	self.input_canvas.highlight_pattern("else", "cond")

    def countInd(self) :

    	text = self.input_canvas.get("1.0", INSERT)
    	count = 0 ;

    	for i in range(len(text)) :
    		if text[i] == '{' :
    			count += 1
    		elif text[i] == '}' :
    			count -= 1

    	return count


    def writeNumRow(self) :

    	numRow = self.input_canvas.index('end').split('.')[0]

    	chaine = ""
    	for i in range(int(numRow)) :
    		chaine += str(i) + '\n'
    	
    	self.numView.configure(state='normal')
    	self.numView.delete("1.0", "end")
    	self.numView.insert("1.0", chaine)
    	self.numView.configure(state='disabled')

    	self.numView.tag_add('center', 1.0, 'end') 





 
 	# ----------------------------------------------------------------------------



# --------------------------------------------------------------------------------
# ---------------------------------- PROGRAM -------------------------------------
# --------------------------------------------------------------------------------


def key(event):
    app.updateColor()


def tab(arg):
    app.input_canvas.insert(INSERT, " " * 4)
    return 'break'

def entry(arg):
	count = app.countInd()
	app.input_canvas.insert(INSERT, "\n" + " " * 4 * count)
	app.writeNumRow()
	return 'break'

def backspace(arg):
	app.writeNumRow()


root = Tk()
app = Application(root)

app.input_canvas.bind("<Key>", key)
app.input_canvas.bind("<Tab>", tab)
app.input_canvas.bind("<Return>", entry)
app.input_canvas.bind("<BackSpace>", backspace)

root.mainloop()

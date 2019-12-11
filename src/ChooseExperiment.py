# Interface Imports
import tkinter
from tkinter import *
from tkinter import font
from tkinter import LEFT, RIGHT, BOTTOM, TOP, NONE
from tkinter import messagebox, filedialog, StringVar
from tkinter.font import Font

# Protocol, Plots and utils imports
import datetime
import os
import random
import re
import utils
from MyCommons import *
import utils

class ChooseExperiment:

	def __init__(self, master, prev_sc, main_bg):
		# 1. Initilising GUI Components
		# a. screen and log components
		self.master = master
		self.main_bg = main_bg
		self.main_bg.destroy()
		sw, sh = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

		# b. log components
		self.start_log = 		"---------------------------------\n" + \
								"| LOG CHOOSE EXP SCREEN         |\n" + \
								"---------------------------------"
		self.start1_txt = 		"| Experiment 1 Button Pressed   |"
		self.start2_txt = 		"| Experiment 2 Button Pressed   |"
		self.start3_txt = 		"| Experiment 3 Button Pressed   |"
		self.back_txt = 		"| Back Button Pressed           |"
		print(self.start_log)

		# b. setting background
		from utils import set_bg
		set_bg(self.master,self.main_bg,'bg/choose.png')

		# 2. Buttons Functions
		# a. Experiment 1
		self.exp1_button = \
			self.create_button('EXPERIMENTO 1',self.exp1_click,sw/2,2*sh/6)

		# b. Experiment 2
		self.exp2_button = \
			self.create_button('EXPERIMENTO 2',self.exp2_click,sw/2,3*sh/6)

		# c. Experiment 3
		self.exp3_button = \
			self.create_button('EXPERIMENTO 3',self.exp3_click,sw/2,4*sh/6)

		# d. Back Button
		self.back_button = \
			self.create_button('VOLTAR',self.back_button_click,sw/2,5*sh/6,18)
			
	def create_label_entry(self,label_text,x,y):
		# 1. Creating Entry Label
		label = tkinter.Label(self.master, bg="#%02x%02x%02x" % (255, 255, 255),justify='left',\
			fg = 'black', text=label_text, font=Font(family='Helvetica', size=20))
		label.place(x=x,y=y,anchor='center')

		# 2. Creating the Entry
		entry = tkinter.Entry(self.master, fg = 'black', font = Font(family='Helvetica', size=20),\
									 bg = "#%02x%02x%02x" % (255, 255, 255), insertbackground = 'black',\
									 highlightcolor = "#%02x%02x%02x" % (180,180,180), highlightbackground= "#%02x%02x%02x" % (50,50,50),\
									  bd=0, width = 33, justify='center')
		entry.place(x = x, y = y+50,anchor='center')

		# 3. Returning
		return label,entry

	def create_button(self,text,func,x,y,size=36):
		button = Button(self.master, text = text,\
			font = Font(family='Helvetica', size=size, weight='bold'),\
			fg = 'white', bg = "#%02x%02x%02x" % (30, 30, 30), \
			anchor = 'center', compound = 'center', 
			command = func,
			highlightthickness = 0, 
			bd = 0, padx=0, pady=0, height=2, width=16)
		button.place(x = x, y = y, anchor= 'center')
		return button

	def exp1_click(self):
		print(self.start1_txt)
		self.destroyWidgets()

		self.experiment = 1
		from ChooseStage import ChooseStage
		ChooseStage(self.master,self,self.main_bg)

	def exp2_click(self):
		print(self.start2_txt)
		self.destroyWidgets()

		self.experiment = 2
		from ChooseStage import ChooseStage
		ChooseStage(self.master,self,self.main_bg)

	def exp3_click(self):
		print(self.start3_txt)
		self.destroyWidgets()

		self.experiment = 3
		from ChooseStage import ChooseStage
		ChooseStage(self.master,self,self.main_bg)

	def back_button_click(self):
		print(self.back_txt)

		self.destroyWidgets()

		from Menu import Menu
		Menu(self.master,self,self.main_bg)

	def ableButtons(self):
		self.exp1_button.configure(state="normal")
		self.exp2_button.configure(state="normal")
		self.exp3_button.configure(state="normal")
		self.back_button.configure(state="normal")

	def disableButtons(self):
		self.exp1_button.configure(state="disabled")
		self.exp2_button.configure(state="disabled")
		self.exp3_button.configure(state="disabled")
		self.back_button.configure(state="disabled")

	def destroyWidgets(self):
		self.exp1_button.destroy()
		self.exp2_button.destroy()
		self.exp3_button.destroy()
		self.back_button.destroy()
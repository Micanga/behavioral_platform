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

class ChooseStage:

	def __init__(self, master, prev_sc, main_bg):
		# 1. Initilising GUI Components
		# a. screen and log components
		self.master = master
		self.main_bg = main_bg
		self.main_bg.destroy()
		sw, sh = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

		# b. log components
		self.start_log = 		"---------------------------------\n" + \
								"| LOG CHOOSE SCREEN             |\n" + \
								"---------------------------------"
		self.start1_txt = 		"| Stage 1 Button Pressed        |"
		self.start2_txt = 		"| Stage 2 Button Pressed        |"
		self.start3_txt = 		"| Stage 3 Button Pressed        |"
		self.start4_txt = 		"| Stage 4 Button Pressed        |"
		self.back_txt = 		"| Back Button Pressed           |"
		print(self.start_log)

		# b. setting background
		from utils import set_bg
		set_bg(self.master,self.main_bg,'bg/choose.png')

		# 2. Buttons Functions
		# a. Nickname
		self.experiment = prev_sc.experiment
		self.nickname_label, self.nickname_entry = \
			self.create_label_entry('Digite seu apelido para o experimento '+\
				str(self.experiment)+':',sw/2,sh/8)

		# b. Experiment 1
		self.exp1_button = \
			self.create_button('FASE 1',self.exp1_click,2*sw/6,sh/2 - 100)

		# c. Experiment 2
		self.exp2_button = \
			self.create_button('FASE 2',self.exp2_click,4*sw/6,sh/2 - 100)

		# d. Experiment 3
		self.exp3_button = \
			self.create_button('FASE 3',self.exp3_click,2*sw/6,sh/2 + 100)

		# e. Experiment 4
		self.exp4_button = \
			self.create_button('FASE 4',self.exp4_click,4*sw/6,sh/2 + 100)

		# f. Back Button
		self.back_button = \
			self.create_button('VOLTAR',self.back_button_click,sw/2,5*sh/6,18)

		# 2. Starting screen variables
		self.init_vars(prev_sc)

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
			bd = 0, padx=0, pady=0, height=2, width=13)
		button.place(x = x, y = y, anchor= 'center')
		return button

	def exp1_click(self):
		# a. verifying nickname
		print(self.start1_txt)
		if not self.nicknameCheck():
			return None

		# b. calculating the start time
		print("| Calculating the start time... |")
		self.start_time = datetime.datetime.now()
		print("| -- calculated start time...   |\n|",self.start_time)
		self.nickname = self.nickname_entry.get()
		utils.write_rheader(self.nickname,self.start_time)

		self.destroyWidgets()

		from IntroStage1 import IntroStage1
		IntroStage1(self.master,self,self.main_bg)

	def exp2_click(self):
		# a. verifying nickname
		print(self.start2_txt)
		if not self.nicknameCheck():
			return None

		# b. calculating the start time
		print("| Calculating the start time... |")
		self.start_time = datetime.datetime.now()
		print("| -- calculated start time...   |\n|",self.start_time)
		self.nickname = self.nickname_entry.get()
		utils.write_rheader(self.nickname,self.start_time)

		self.destroyWidgets()

		from Play2 import Play2
		Play2(self.master,self,self.main_bg)

	def exp3_click(self):
		# a. verifying nickname
		print(self.start3_txt)
		if not self.nicknameCheck():
			return None

		# b. calculating the start time
		print("| Calculating the start time... |")
		self.start_time = datetime.datetime.now()
		print("| -- calculated start time...   |\n|",self.start_time)
		self.nickname = self.nickname_entry.get()
		utils.write_rheader(self.nickname,self.start_time)

		self.destroyWidgets()

		from IntroStage3 import IntroStage3
		IntroStage3(self.master,self,self.main_bg)

	def exp4_click(self):
		# a. verifying nickname
		print(self.start4_txt)
		if not self.nicknameCheck():
			return None

		# b. calculating the start time
		print("| Calculating the start time... |")
		self.start_time = datetime.datetime.now()
		print("| -- calculated start time...   |\n|",self.start_time)
		self.nickname = self.nickname_entry.get()
		utils.write_rheader(self.nickname,self.start_time)
		
		self.destroyWidgets()

		from IntroStage4 import IntroStage4
		self.stages = utils.shuffleStages()
		IntroStage4(self.master,self,self.main_bg)

	def back_button_click(self):
		print(self.back_txt)

		self.destroyWidgets()

		from ChooseExperiment import ChooseExperiment
		ChooseExperiment(self.master,self,self.main_bg)

	def nicknameCheck(self):
		if re.match("^$",self.nickname_entry.get()) is not None:
			self.disableButtons()
			myPopUp(self,'Você precisa de um Apelido!\nPor favor, digite um apelido para você!')
			return False
		if re.match("^[a-zA-Z0-9]+$",self.nickname_entry.get()) is None:
			self.disableButtons()
			myPopUp(self,'Seu Apelido não pode conter espaços\nou caracteres especiais!\nPor favor, digite um apelido válido!')
			return False
		return True

	def init_vars(self,prev_sc):
		# 1. Initializing variables
		# a. loading the settings
		print("| Loading settings...           |")
		self.settings = utils.load_settings()
		print("| -- loaded settings...         |\n|",self.settings)

		# b. starting necessary variables
		print("| Loading experiment variable...|")
		self.experiment = prev_sc.experiment

		# c. intializing round variables
		print("| Loading round variables       |")
		self.clicks = ''
		self.points = tkinter.StringVar()
		self.points.set(0)
		self.repeat = 0
		self.reinforcement = []

		# d. game variables
		print("| Loading game variables...     |")
		self.combinations = ['EEEE','EEED','EEDE','EDEE',\
		'DEEE','EEDD','EDDE','DDEE','DEED','DEDE','EDED','DDDE',\
		'DDED','DEDD','EDDD','DDDD']
		self.frequency = {'EEEE':1,'EEED':1,'EEDE':1,'EDEE':1,\
		'DEEE':1,'EEDD':1,'EDDE':1,'DDEE':1,'DEED':1,'DEDE':1,'EDED':1,'DDDE':1,\
		'DDED':1,'DEDD':1,'EDDD':1,'DDDD':1}
		self.total_frequency = {'EEEE':1,'EEED':1,'EEDE':1,'EDEE':1,\
		'DEEE':1,'EEDD':1,'EDDE':1,'DDEE':1,'DEED':1,'DEDE':1,'EDED':1,'DDDE':1,\
		'DDED':1,'DEDD':1,'EDDD':1,'DDDD':1}
		self.memo_accuracy = 0
		self.memo_reinforced = []
		self.saved_order = []
		self.stages = []

		# e. result variables
		print("| Loading result variables...   |")
		self.results = []
		self.result_set = set()
		self.blocks = []

	def ableButtons(self):
		self.nickname_entry.configure(state="normal")
		self.exp1_button.configure(state="normal")
		self.exp2_button.configure(state="normal")
		self.exp3_button.configure(state="normal")
		self.exp4_button.configure(state="normal")
		self.back_button.configure(state="normal")

	def disableButtons(self):
		self.nickname_entry.configure(state="disabled")
		self.exp1_button.configure(state="disabled")
		self.exp2_button.configure(state="disabled")
		self.exp3_button.configure(state="disabled")
		self.exp4_button.configure(state="disabled")
		self.back_button.configure(state="disabled")

	def destroyWidgets(self):
		self.nickname_label.destroy()
		self.nickname_entry.destroy()
		self.exp1_button.destroy()
		self.exp2_button.destroy()
		self.exp3_button.destroy()
		self.exp4_button.destroy()
		self.back_button.destroy()
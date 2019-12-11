# Interface Imports
import tkinter
from tkinter import *
from tkinter import font
from tkinter import LEFT, RIGHT, BOTTOM, TOP, NONE
from tkinter import messagebox, filedialog, StringVar
from tkinter.font import Font
import tkinter.scrolledtext as scrolledtext

# Protocol, Plots and utils imports
import datetime
import os
import utils

class IntroStage2:

	def __init__(self, master, prev_sc, main_bg):
		# 1. Initilising GUI Components
		self.update_screen(master,main_bg)
		self.update_variables(prev_sc)
		
		self.start_log = 		"---------------------------------\n" + \
								"| LOG STAGE 2 START SCREEN      |\n" + \
								"---------------------------------"
		self.start_txt = 		"| Start Action Button Pressed   |"
		self.exit_txt = 		"| Exit Button Pressed           |"
		print(self.start_log)

		# 2. Setting the Screen Components
		self.title = tkinter.Label(master, bg='white',\
									 fg = 'black', text='FASE 2', font=Font(family='Helvetica', size=30, weight='bold'))
		self.title.place(x=self.sw/2,y=2*self.sh/10,anchor='center')

		# a. Start Button
		self.start_button = Button(master, anchor = 'center', compound = 'center', 
									text = 'JOGAR',font = Font(family='Helvetica', size=28, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.start_button_click,
									highlightthickness = 0,
									bd = 0, padx=0,pady=0,height=2,width=13)
		self.start_button.place(x = self.sw/2, y = 8*self.sh/10, anchor= 'center')

		# b. Stage 1 Text
		text = utils.load_text(2)
		self.text_display = scrolledtext.ScrolledText(master, fg = 'black', font = Font(family='Helvetica', size=18),\
									 bg = "#%02x%02x%02x" % (255, 255, 255), insertbackground = 'black',\
									 highlightcolor = "#%02x%02x%02x" % (180,180,180), highlightbackground= "#%02x%02x%02x" % (50,50,50),\
									  bd=0, width =47, height=10, padx=10, pady=10, wrap='word')
		self.text_display.insert('insert',text)
		self.text_display.configure(state='disabled')
		self.text_display.place(x=self.sw/2,y=self.sh/2,anchor='center')
		
	def update_screen(self,master,main_bg):
		self.master = master
		self.main_bg = main_bg
		self.main_bg.destroy()
		self.main_bg = tkinter.Label(master, bg= "#%02x%02x%02x" % (255,255,255))
		self.main_bg.place(x=0,y=0,relwidth=1,relheight=1)
		self.sw, self.sh = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

	def update_variables(self,prev_sc):
		self.prev_sc = prev_sc

		# a. experiment variables
		self.experiment = prev_sc.experiment
		self.settings = prev_sc.settings
		self.nickname = prev_sc.nickname
		self.start_time = prev_sc.start_time
		self.round_start_time = datetime.datetime.now()
		self.block_start_time = datetime.datetime.now()

		# b. round variables
		self.clicks = ''
		self.points = tkinter.StringVar()
		self.points.set(0)
		self.repeat = 0
		self.reinforcement = []

		# c. game variables
		self.combinations = ['EEEE','EEED','EEDE','EDEE',\
		'DEEE','EEDD','EDDE','DDEE','DEED','DEDE','EDED','DDDE',\
		'DDED','DEDD','EDDD','DDDD']
		self.frequency = {'EEEE':1,'EEED':1,'EEDE':1,'EDEE':1,\
		'DEEE':1,'EEDD':1,'EDDE':1,'DDEE':1,'DEED':1,'DEDE':1,'EDED':1,'DDDE':1,\
		'DDED':1,'DEDD':1,'EDDD':1,'DDDD':1}
		self.total_frequency = prev_sc.total_frequency
		self.memo_accuracy = prev_sc.memo_accuracy
		self.memo_reinforced = prev_sc.memo_reinforced
		self.saved_order = prev_sc.saved_order
		self.stages = prev_sc.stages

		# d. result variables
		self.results = []
		self.result_set = set()
		self.blocks = prev_sc.blocks

	def start_button_click(self):
		print(self.start_txt)

		self.destroyWidgets()

		# e. starting the game
		from Play2 import Play2
		self.points.set(int(self.prev_sc.points.get()))
		Play2(self.master,self,self.main_bg)

	def destroyWidgets(self):
		self.title.destroy()
		self.start_button.destroy()
		self.text_display.destroy()
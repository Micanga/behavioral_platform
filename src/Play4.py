# Interface Imports
import tkinter
from tkinter import *
from tkinter import font
from tkinter import LEFT, RIGHT, BOTTOM, TOP, NONE
from tkinter import messagebox, filedialog, StringVar
from tkinter.font import Font

# Protocol, Plots and utils imports
from copy import deepcopy
import datetime
import numpy as np
import os
import random
import time

from MyCommons import *
import utils

class Play4:

	def __init__(self, master, prev_sc, main_bg):
		# 1. Initializing the necessary varaibles
		self.update_screen(master,main_bg)
		self.update_variables(prev_sc)
		
		self.points.set(int(prev_sc.points.get()))
		self.global_points = tkinter.StringVar()
		self.global_points.set(int(prev_sc.global_points.get()))

		# b. log text
		self.start_log = 		"---------------------------------\n" + \
								"| LOG STAGE 4 PLAY SCREEN       |\n" + \
								"---------------------------------"
		print(self.start_log)
		print('| Stages order ('+str(len(self.blocks)+1)+')',self.stages)

		# 2. Redirecting
		self.ableMouse()
		if len(self.stages) == 0:
			self.finish()
		elif self.stages[0] == 2:
			self.stages.pop(0)
			from Play4blue import Play4blue
			Play4blue(self.master,self,self.main_bg)
		elif self.stages[0] == 3:
			self.stages.pop(0)
			from Play4red import Play4red
			Play4red(self.master,self,self.main_bg)
		elif self.stages[0] == 4:
			self.stages.pop(0)
			from Play4yellow import Play4yellow
			Play4yellow(self.master,self,self.main_bg)

	def ableMouse(self):
		self.master.configure(cursor='')
		self.reset_mouse_position()

	def reset_mouse_position(self):
		self.master.event_generate('<Motion>', warp=True, x=self.sw/2, y=self.sh/2)

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

	def finish(self):
		myReturnMenuPopUp(self,'Fim do Experimento! Você acumulou' +\
			str(int(self.points.get())+int(self.global_points.get())) +\
			'pontos!\nPor favor, contacte o pesquisador e informe o fim da tarefa.\n Obrigado pela sua participação!')


	def ableButtons(self):	
		return None
		
	def goMenu(self):
		from Menu import Menu
		Menu(self.master,self,self.main_bg)
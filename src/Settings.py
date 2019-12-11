# Interface Imports
import tkinter
from tkinter import *
from tkinter import font
from tkinter import LEFT, RIGHT, BOTTOM, TOP, NONE
from tkinter import messagebox, filedialog, StringVar
from tkinter.font import Font

# Utils Imports
import datetime
import os
import re
import time
from MyCommons import *
import utils

class Settings:

	def __init__(self, master, prev_sc, main_bg):
		# 1. Initilising GUI Components
		# a. screen and log components
		self.master = master
		self.main_bg = main_bg
		self.main_bg.destroy()
		sw, sh = self.master.winfo_screenwidth(), self.master.winfo_screenheight()

		self.start_log = 		"---------------------------------\n" + \
								"| LOG SETTINGS SCREEN           |\n" + \
								"---------------------------------"
		self.default_txt = 		"| -- default settings openned   | "
		self.saved_txt = 		"| -- saved settings openned     | "
		self.disabled_txt = 	"| -- disabling the buttons      |"
		self.abled_txt = 		"| -- enabling the buttons       |"
		self.destroy_txt = 		"| -- destroying the screen      |"
		self.edit1_txt = 		"| Edit Stage 1 Button Pressed   |"
		self.edit2_txt = 		"| Edit Stage 2 Button Pressed   |"
		self.edit3_txt = 		"| Edit Stage 3 Button Pressed   |"
		self.edit4_txt = 		"| Edit Stage 4 Button Pressed   |"
		self.left_txt = 		"| Left Button Pressed           |"
		self.right_txt = 		"| Right Button Pressed          |"
		self.back_txt = 		"| Back Action Button Pressed    |"
		self.save_txt =		 	"| Save Action Button Pressed    |"
		print(self.start_log)

		# b. setting background
		from utils import set_bg
		set_bg(self.master,self.main_bg,'bg/settings.png')

		# c. title and settings background
		self.settings_bg = tkinter.Frame(self.master,width=int(4*sw/5),height=int(4*sh/5),bg="#%02x%02x%02x" % (220, 220, 220))
		self.settings_bg.pack_propagate(0) # Stops child widgets of label_frame from resizing it
		self.settings_bg.place(x=sw/10,y=sh/10)

		self.settings_label = tkinter.Label(master, bg="#%02x%02x%02x" % (220, 220, 220),\
									 fg = 'black', text='CONFIGURAÇÕES:',\
									 font=Font(family='Helvetica', size=24, weight='bold'))
		self.settings_label.place(x=sw/10,y=sh/10)

		# 3. Loading the previous settings and images
		self.previous_settings = utils.load_settings()
		self.left_image, self.right_image, left_txt, right_txt  = utils.load_images(1)
		self.joker_image, joker_lt, joker_rt = utils.load_joker()

		# 4. Setting GUI Active Components
		# a. max time entry 
		self.max_time_label, self.max_time_entry = \
		 self.create_label_entry('Tempo Máximo (minutos):','max_time',\
		 	sw/9, 1.75*sh/10)

		# b. iri entry
		self.iri_label, self.iri_entry = \
		 self.create_label_entry('IRI (segundos):','iri',\
		 	sw/9, 2.25*sh/10 +20)

		# c. reinforce screen
		self.screen_label, self.screen_entry = \
		 self.create_label_entry('ITI (segundos):','iti',\
		 	sw/9, 2.75*sh/10 +40)

		# d. stability entry
		self.stability_label, self.stability_entry = \
		 self.create_label_entry('Estabilidade na Taxa de Resposta (%):','stability',\
		 	sw/9, 3.75*sh/10 + 60)

		# e. preinf entry
		self.preinf_label, self.preinf_entry = \
		 self.create_label_entry('Proporção de Reforço Miníma (%):','preinf',\
		 	sw/9, 4.25*sh/10 + 80)

		# f. threshold entry
		self.threshold_label, self.threshold_entry = \
		 self.create_label_entry('Limiar (%):','threshold',\
		 	sw/9, 4.75*sh/10 +100)

		# g. U
		self.u_label, self.u_entry = \
		 self.create_label_entry('Índice U Máximo (%):','u_threshold',\
		 	sw/9, 5.25*sh/10 +120)
		  
		# h. Min. blocks
		self.block_label1, self.block_entry1 = \
		 self.create_label_entry('Min. de Blocos (Fase 1):','blocks1',\
		 	sw/9 +400, 1.75*sh/10)

		self.block_label2, self.block_entry2 = \
		 self.create_label_entry('Min. de Blocos (Fase 2):','blocks2',
		 	sw/9 +400, 2.25*sh/10 +20)

		self.block_label3, self.block_entry3 = \
		 self.create_label_entry('Min. de Blocos (Fase 3):','blocks3',\
		 	sw/9 +400, 2.75*sh/10 +40)

		# i. Points
		self.points_label, self.points_entry = \
		 self.create_label_entry('Pontos por Acerto:','points',\
		 	sw/9 +400, 3.25*sh/10 +60)

		# i. Points
		self.min_memo_label, self.min_memo_entry = \
		 self.create_label_entry('Acurácia MTS (blocos consec.):','min_memo',\
		 	sw/9 +700, 1.75*sh/10)

		# 6. Setting Buttons
		# a. Stages Text
		self.stage_label = tkinter.Label(master, bg="#%02x%02x%02x" % (220, 220, 220),\
									 fg = 'black', text='Introdução verbal:', font=Font(family='Helvetica', size=12))
		self.stage_label.place(x=sw/9 +400,y=4.25*sh/10 +60)
		self.stage1_button = Button(master, anchor = 'center', compound = 'center', 
									text= 'FASE 1',font = Font(family='Helvetica', size=12),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.stage1_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=1,width=8)
		self.stage1_button.place(x=sw/9 +550, y=4.25*sh/10 +60)


		self.stage2_button = Button(master, anchor = 'center', compound = 'center', 
									text= 'FASE 2',font = Font(family='Helvetica', size=12),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.stage2_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=1,width=8)
		self.stage2_button.place(x=sw/9 +650, y=4.25*sh/10 +60)

		self.stage3_button = Button(master, anchor = 'center', compound = 'center', 
									text= 'FASE 3',font = Font(family='Helvetica', size=12),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.stage3_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=1,width=8)
		self.stage3_button.place(x=sw/9 +750, y=4.25*sh/10 +60)


		self.stage4_button = Button(master, anchor = 'center', compound = 'center', 
									text= 'FASE 4',font = Font(family='Helvetica', size=12),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.stage4_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=1,width=8)
		self.stage4_button.place(x=sw/9 +850, y=4.25*sh/10 +60)

		# b. left image
		self.left_label = tkinter.Label(master, bg="#%02x%02x%02x" % (220, 220, 220),\
									 fg = 'black', text='Imagem ESQUERDA:', font=Font(family='Helvetica', size=14))
		self.left_label.place(x=sw/9 +400,y=4.75*sh/10 +60)#,anchor='center')
		self.left_button = Button(master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.left_button_click,
									highlightthickness = 0, image=self.left_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.left_button.image = self.left_image
		self.left_button.place(x=sw/9 +435, y=4.75*sh/10 +90)#, anchor='center')

		# c. right image
		self.right_label = tkinter.Label(master, bg="#%02x%02x%02x" % (220, 220, 220),\
									 fg = 'black', text='Imagem DIREITA:', font=Font(family='Helvetica', size=14))
		self.right_label.place(x=sw/9 +600,y=4.75*sh/10 +60)#,anchor='center')
		self.right_button = Button(master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.right_button_click,
									highlightthickness = 0, image=self.right_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.right_button.image = self.right_image
		self.right_button.place(x=sw/9 +635,y=4.75*sh/10 +90)#, anchor='center')

		# c. joker image
		self.joker_label = tkinter.Label(master, bg="#%02x%02x%02x" % (220, 220, 220),\
									 fg = 'black', text='Imagem CORINGA:', font=Font(family='Helvetica', size=14))
		self.joker_label.place(x=sw/9 +770,y=4.75*sh/10 +60)#,anchor='center')
		self.joker_button = Button(master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.joker_button_click,
									highlightthickness = 0, image=self.joker_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.joker_button.image = self.joker_image
		self.joker_button.place(x=sw/9 +805,y=4.75*sh/10 +90)#, anchor='center')

		# e. Back Button
		self.back_button = Button(master, anchor = 'center', compound = 'center', 
									text = 'VOLTAR',font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.back_button_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=2,width=13)
		self.back_button.place(x = sw/10, y = 8*sh/10)

		# f. Save Button
		self.save_button = Button(master, anchor = 'center', compound = 'center', 
									text = 'SALVAR',font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.save_button_click,
									highlightthickness = 0, 
									bd = 0, padx=0,pady=0,height=2,width=13)
		self.save_button.place(x = 9*sw/10, y = 8*sh/10,anchor='ne')

	def create_label_entry(self,label_text,entry_idx,x,y):
		# 1. Creating Entry Label
		label = tkinter.Label(self.master, bg="#%02x%02x%02x" % (220, 220, 220),justify='left',\
			fg = 'black', text=label_text, font=Font(family='Helvetica', size=12))
		label.place(x=x,y=y)

		# 2. Creating the Entry
		entry = tkinter.Entry(self.master, fg = 'black', font = Font(family='Helvetica', size=14),\
									 bg = "#%02x%02x%02x" % (255, 255, 255), insertbackground = 'black',\
									 highlightcolor = "#%02x%02x%02x" % (180,180,180), highlightbackground= "#%02x%02x%02x" % (50,50,50),\
									  bd=0, width = 10)
		entry.insert(0,self.previous_settings[entry_idx])
		entry.place(x = x, y = y+24)

		# 3. Returning
		return label,entry

	def stage1_click(self):
		print(self.edit1_txt)
		self.disableButtons()
		myTextBox(self,'Texto para Fase 1',1)

	def stage2_click(self):
		print(self.edit2_txt)
		self.disableButtons()
		myTextBox(self,'Texto para Fase 2',2)

	def stage3_click(self):
		print(self.edit3_txt)
		self.disableButtons()
		myTextBox(self,'Texto para Fase 3',3)

	def stage4_click(self):
		print(self.edit4_txt)
		self.disableButtons()
		myTextBox(self,'Texto para Fase 4',4)

	def left_button_click(self):
		print(self.left_txt)
		self.change_left_image()

	def change_left_image(self):
		filename = filedialog.askopenfilenames(initialdir = ".",title = "Select image",
			filetypes = [("PNG files","*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg"),("All files","*")])
		
		if not filename:
			return None

		filename = filename[0]

		from PIL import Image
		self.left_image = Image.open(filename)
		self.left_image = self.left_image.resize((80, 80), Image.ANTIALIAS)

		t = datetime.datetime.now()
		self.left_image.save('local/left/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		time.sleep(1)

		self.left_button.destroy()
		self.left_image = tkinter.PhotoImage(file='local/left/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		self.left_button = Button(self.master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.left_button_click,
									highlightthickness = 0, image=self.left_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.left_button.image = self.left_image
		self.left_button.place(x=sw/9 +435, y=4.75*sh/10 +90)#, anchor='center')

	def right_button_click(self):
		print(self.right_txt)
		self.change_right_image()

	def change_right_image(self):
		filename = filedialog.askopenfilenames(initialdir = ".",title = "Select image",
			filetypes = [("PNG files","*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg"),("All files","*")])
		
		if not filename	:
			return None

		filename = filename[0]

		from PIL import Image
		self.right_image = Image.open(filename)
		self.right_image = self.right_image.resize((80, 80), Image.ANTIALIAS)

		t = datetime.datetime.now()
		self.right_image.save('local/right/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		time.sleep(1)

		self.right_button.destroy()
		self.right_image = tkinter.PhotoImage(file='local/right/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		self.right_button = Button(self.master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.right_button_click,
									highlightthickness = 0, image=self.right_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.right_button.image = self.right_image
		self.right_button.place(x=sw/9 +635,y=4.75*sh/10 +90)#, anchor='center')

	def joker_button_click(self):
		self.change_joker_image()

	def change_joker_image(self):
		filename = filedialog.askopenfilenames(initialdir = ".",title = "Select image",
			filetypes = [("PNG files","*.png"),("JPEG files","*.jpeg"),("JPG files","*.jpg"),("All files","*")])
		
		if not filename	:
			return None

		filename = filename[0]

		from PIL import Image
		self.joker_image = Image.open(filename)
		self.joker_image = self.joker_image.resize((80, 80), Image.ANTIALIAS)

		t = datetime.datetime.now()
		self.joker_image.save('local/joker/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		time.sleep(1)

		self.joker_button.destroy()
		self.joker_image = tkinter.PhotoImage(file='local/joker/'+t.strftime("%Y%m%d_%H%M%S")+".png")
		self.joker_button = Button(self.master, anchor = 'center', compound = 'center', 
									font = Font(family='Helvetica', size=18, weight='bold'),
									bg = "#%02x%02x%02x" % (30, 30, 30), fg = 'white',
									command = self.joker_button_click,
									highlightthickness = 0, image=self.joker_image,
									bd = 0, padx=0,pady=0,height=80,width=80)
		self.joker_button.image = self.joker_image
		self.joker_button.place(x=sw/9 +805,y=4.75*sh/10 +90)#, anchor='center')

	def back_button_click(self):
		print(self.back_txt)

		self.destroyWidgets()

		from Menu import Menu
		Menu(self.master,self,self.main_bg)

	def save_button_click(self):
		print(self.save_txt)

		# 1. Checking the entries
		if not self.intCheck(self.max_time_entry.get(),'Tempo Máximo','90'):
			return None
		elif not self.floatCheck(self.iri_entry.get(),'IRI','0.5'):
			return None
		elif not self.floatCheck(self.stability_entry.get(),'Estabilidade','0.2','1'):
			return None
		elif not self.floatCheck(self.threshold_entry.get(),'Limiar','0.2','1'):
			return None
		elif not self.floatCheck(self.preinf_entry.get(),'Acurácia','1.0','1'):
			return None
		elif not self.floatCheck(self.screen_entry.get(),'ITI','1.5'):
			return None
		elif not self.intCheck(self.block_entry1.get(),'número Mínimo de Blocos (Fase 1)','10'):
			return None
		elif not self.intCheck(self.block_entry2.get(),'número Mínimo de Blocos (Fase 2)','10'):
			return None
		elif not self.intCheck(self.block_entry3.get(),'número Mínimo de Blocos (Fase 3)','15'):
			return None
		elif not self.intCheck(self.points_entry.get(),'Pontos por Acerto','10'):
			return None
		elif not self.floatCheck(self.u_entry.get(),'Limiar U','1.0','1'):
			return None
		if not self.intCheck(self.min_memo_entry.get(),'Mínimo de Acertos em Memória','80'):
			return None

		# 2. Saving Settings
		time = datetime.datetime.now()
		save_file = open('local/settings/'+time.strftime("%Y%m%d_%H%M%S")+".csv","w")
		save_file.write('max_time,'+self.max_time_entry.get()+"\n")
		save_file.write('iri,'+self.iri_entry.get()+"\n")
		save_file.write('stability,'+self.stability_entry.get()+"\n")
		save_file.write('threshold,'+self.threshold_entry.get()+"\n")
		save_file.write('preinf,'+self.preinf_entry.get()+"\n")
		save_file.write('iti,'+self.screen_entry.get()+"\n")
		save_file.write('blocks1,'+self.block_entry1.get()+"\n")
		save_file.write('blocks2,'+self.block_entry2.get()+"\n")
		save_file.write('blocks3,'+self.block_entry3.get()+"\n")
		save_file.write('points,'+self.points_entry.get()+"\n")
		save_file.write('u_threshold,'+self.u_entry.get()+"\n")
		save_file.write('min_memo,'+self.min_memo_entry.get()+"\n")
		save_file.close()

		# 3. Destroying screen
		self.destroyWidgets()

		# 4. Returning to Menu
		from Menu import Menu
		Menu(self.master,self,self.main_bg)

	def intCheck(self,value,name,eg='10'):
		if re.match("^$",value) is not None:
			self.disableButtons()
			myPopUp(self,'Valor para '+name+' Vazio!\nPor favor, informe um valor válido.')
			return False
		if re.match("^\d+$",value) is None:
			self.disableButtons()
			myPopUp(self,'Valor para '+name+' Inválido!\nPor favor, entre com um valor decimal válido.\nExemplo: '+eg)
			return False
		return True

	def floatCheck(self,value,name,eg='0.5',max_value=99999):
		if re.match("^$",value) is not None:
			self.disableButtons()
			myPopUp(self,'Valor para '+name+' Vazio!\nPor favor, informe um valor válido.')
			return False
		if re.match("^\d*[.]{0,1}\d*$",value) is None:
			self.disableButtons()
			myPopUp(self,'Valor para '+name+' Inválido!\nPor favor, entre com um valor decimal válido.\nExemplo: '+str(eg))
			return False
		if float(value) > float(max_value): 
			self.disableButtons()
			myPopUp(self,'Valor para '+name+' Inválido!\nPor favor, entre com um valor entre 0 e '+str(max_value)+'.')
			return False
		return True

	def ableButtons(self):
		print(self.abled_txt)
		self.max_time_entry.configure(state="normal")
		self.iri_entry.configure(state="normal")
		self.stability_entry.configure(state="normal")
		self.threshold_entry.configure(state="normal")
		self.preinf_entry.configure(state="normal")
		self.screen_entry.configure(state="normal")
		self.block_entry1.configure(state="normal")
		self.block_entry2.configure(state="normal")
		self.block_entry3.configure(state="normal")
		self.points_entry.configure(state="normal")
		self.u_entry.configure(state="normal")
		self.min_memo_entry.configure(state="normal")
		self.stage1_button.configure(state="normal")
		self.stage2_button.configure(state="normal")
		self.stage3_button.configure(state="normal")
		self.stage4_button.configure(state="normal")
		self.left_button.configure(state="normal")
		self.right_button.configure(state="normal")
		self.joker_button.configure(state="normal")
		self.back_button.configure(state="normal")
		self.save_button.configure(state="normal")

	def disableButtons(self):
		print(self.disabled_txt)
		self.max_time_entry.configure(state="disabled")
		self.iri_entry.configure(state="disabled")
		self.stability_entry.configure(state="disabled")
		self.threshold_entry.configure(state="disabled")
		self.preinf_entry.configure(state="disabled")
		self.screen_entry.configure(state="disabled")
		self.block_entry1.configure(state="disabled")
		self.block_entry2.configure(state="disabled")
		self.block_entry3.configure(state="disabled")
		self.points_entry.configure(state="disabled")
		self.u_entry.configure(state="disabled")
		self.min_memo_entry.configure(state="disabled")
		self.stage1_button.configure(state="disabled")
		self.stage2_button.configure(state="disabled")
		self.stage3_button.configure(state="disabled")
		self.stage4_button.configure(state="disabled")
		self.left_button.configure(state="disabled")
		self.right_button.configure(state="disabled")
		self.joker_button.configure(state="disabled")
		self.back_button.configure(state="disabled")
		self.save_button.configure(state="disabled")

	def destroyWidgets(self):
		print(self.destroy_txt)
		self.settings_bg.destroy()
		self.settings_label.destroy() 

		self.max_time_label.destroy() # a
		self.max_time_entry.destroy()
		self.iri_label.destroy() # b
		self.iri_entry.destroy()
		self.stability_label.destroy() # c
		self.stability_entry.destroy()
		self.threshold_label.destroy() # d
		self.threshold_entry.destroy()
		self.preinf_label.destroy() # e
		self.preinf_entry.destroy()
		self.block_entry1.destroy() # f
		self.block_label1.destroy()
		self.block_entry2.destroy()
		self.block_label2.destroy()
		self.block_entry3.destroy()
		self.block_label3.destroy()
		self.points_label.destroy() #g
		self.points_entry.destroy()
		self.u_label.destroy() #h
		self.u_entry.destroy()
		self.min_memo_label.destroy() # i
		self.min_memo_entry.destroy

		self.stage_label.destroy()
		self.stage1_button.destroy()
		self.stage3_button.destroy()

		self.left_label.destroy()
		self.left_button.destroy()
		self.right_label.destroy()
		self.right_button.destroy()
		self.joker_label.destroy()
		self.joker_button.destroy()

		self.back_button.destroy()
		self.save_button.destroy()
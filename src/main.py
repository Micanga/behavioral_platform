# tkinter Imports
import tkinter
from tkinter import *

import os

# Main
if __name__ == "__main__":
	# 1. Starting root
	root = tkinter.Tk()

	# 2. Setting the commom features
	# a. window settings
	root.title('Plataforma de Experimento')
	root.resizable(width = False,height = False)
	root.configure(background='white')
	#root.iconbitmap('@logo.xmb')

	# b. setting full
	sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
	wc, hc = 0, 0
	pad = 0

	root.geometry('%dx%d+%d+%d' % (sw-pad,sh-pad,wc,hc))
	root.protocol("WM_DELETE_WINDOW", sys.exit)
	root.focus_set()  # <-- move focus to this widget
	root.bind("<Escape>", lambda e: root.quit())
	root.attributes('-fullscreen', True)

	# c. grid settings
	root.grid_rowconfigure(0,pad=0)
	root.grid_columnconfigure(0,pad=0)
	root.grid_rowconfigure(1,pad=0)

	root.grid_columnconfigure(1,pad=0)
	main_bg = None

	# 3. Verifying the not default directories integrity
	if not os.path.isdir('./results'):
		os.mkdir('./results')

	if not os.path.isdir('./local/imgseq'):
		os.mkdir('./local/imgseq')

	if not os.path.isdir('./local/joker'):
		os.mkdir('./local/joker')

	if not os.path.isdir('./local/right'):
		os.mkdir('./local/right')

	if not os.path.isdir('./local/left'):
		os.mkdir('./local/left')

	if not os.path.isdir('./local/settings'):
		os.mkdir('./local/settings')

	if not os.path.isdir('./local/texts'):
		os.mkdir('./local/texts')

	if not os.path.isdir('./local/texts/stage1'):
		os.mkdir('./local/texts/stage1')

	if not os.path.isdir('./local/texts/stage2'):
		os.mkdir('./local/texts/stage2')

	if not os.path.isdir('./local/texts/stage3'):
		os.mkdir('./local/texts/stage3')

	if not os.path.isdir('./local/texts/stage4'):
		os.mkdir('./local/texts/stage4')

	# 4. Starting app
	# a. resizing the background image
	from PIL import Image, ImageTk
	image = Image.open('bg/main.png')
	img_copy = image.copy()

	bg_image = ImageTk.PhotoImage(image)
	background = tkinter.Label(root, image=bg_image)
	background.place(x=0,y=0,relwidth=1,relheight=1,anchor='center')

	image = img_copy.resize((sw, sh), Image.ANTIALIAS)
	bg_image = ImageTk.PhotoImage(image)
	background.configure(image = bg_image)

	# b. running the menu screen
	from Menu import Menu
	Menu(root,None,background)
	root.mainloop()

	# 5. That's all folks :) ... 
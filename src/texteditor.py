#!/usr/bin/env python3
# coding: utf-8
import os,sys
import tkinter as tk
import tkinter.font as font

root = tk.Tk()
print(font.families())
my_font = font.Font(root,family="渦筆",size="64",weight="normal") # fc-list, wight=normal|bold

edit = tk.Text(root, wrap=tk.WORD, font=my_font) # wrap=NONE|CHAR|WORD
edit.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
edit.focus_set()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.title("メモ帳")
#root.iconbitmap(default="*.png")
icon_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'icon.png')
imgicon = tk.PhotoImage(file=icon_path ,master=root)
root.tk.call('wm', 'iconphoto', root._w, imgicon)  
root.geometry("600x480")
root.mainloop()


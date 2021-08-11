#!/usr/bin/env python
# coding: utf-8

# In[64]:


import tkinter as tk
import os;
import glob
import stat
import sys
import shutil


root= tk.Tk()
root.geometry('350x200')
root.title("Clean PC")
files = glob.glob('C:/Users/c4m3lion/AppData/Local/Temp/*')
def clean ():  
    os.system("taskkill /f /im explorer.exe");
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
            print('PermissionError do change')
            os.chmod(f, stat.S_IWRITE)
            try:
                shutil.rmtree(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
    
    label1 = tk.Label(root, text= 'AYE PC cleaned succesfully', fg='green', font=('helvetica', 12, 'bold'))
    label1.after(5000, label1.destroy)
    label1.pack()
def openExplorer():
    os.system('start explorer.exe');
    
    label1 = tk.Label(root, text= 'Explorere restored', fg='green', font=('helvetica', 12, 'bold'))
    label1.after(5000, label1.destroy)
    label1.pack()

tk.Button(root, text="Clean", command=clean).pack()
tk.Button(root, text="Open Explorer", command=openExplorer).pack()

root.mainloop()


# In[60]:





# In[ ]:





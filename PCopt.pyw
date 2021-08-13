#!/usr/bin/env python
# coding: utf-8

# In[11]:


import tkinter as tk
import os;
import glob
import stat
import sys
import shutil


root= tk.Tk()
root.geometry('600x300');
root.configure(background='black');
root.title("Clean PC")

def debugger(txt):
    label1 = tk.Label(root, text= txt, fg='green', font=('helvetica', 12, 'bold'))
    label1.after(5000, label1.destroy)
    label1.pack()

def clean ():  
    files = glob.glob('C:/Users/c4m3lion/AppData/Local/Temp/*')
    os.system("taskkill /f /im explorer.exe");#kill exploreer exe it save memory
    for f in files:
        try:
            os.remove(f) #try to remove file
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
            print('PermissionError do change')
            os.chmod(f, stat.S_IWRITE) # Ihave no idea
            try:
                shutil.rmtree(f) #try to remove folder
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
    debugger('AYE PC cleaned succesfully');

#open explorer.exe
def openExplorer():
    os.system('start explorer.exe');
    debugger('Explorere restored');
      

#delete edge
def deleteEdge():
    url = "C:/Program Files (x86)/Microsoft/Edge/Application/";
    files = glob.glob(url+'*');
    for f in files:
        if(f[len(f)-1] >='0' and f[len(f)-1] <='9'):
            f+="\Installer";
            debugger("edge found on this directory: ");
            debugger(f);
            if len(os.listdir(f) ) == 0:
                debugger("bu edge is uninstalled already!");
            else:    
                debugger("Uninstalling!!!")
                
                os.chdir(f);
                os.system('start cmd /k setup --uninstall --force-uninstall --system-level')
            
            
            
    
tk.Button(root, text="Clean", command=clean).pack()
tk.Button(root, text="Open Explorer", command=openExplorer).pack()
tk.Button(root, text="Delete Edge", command=deleteEdge).pack()

root.mainloop()


# In[60]:





# In[ ]:





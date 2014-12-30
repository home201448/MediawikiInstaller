# File: Mediawiki.py
import os
import tkMessageBox
from Tkinter import *

# Creating the Root Window
root = Tk()
root.title("GUI Tool for Mediawiki Installation and Configuration")
root.geometry("700x200")


# The About Box
def about():	
	tkMessageBox.showinfo("Mediawiki Installer","Graphical User Interface for \nMediawiki Installation and Configuration\n\nDeveloped by : Ashwin Tumma, 2011\n\nLicense: GPLv2");

def configMediawiki():
	print "Configuring Mediawiki" 
	callConfigScript="bash configScript.sh " 
	returnConfig=os.system(callConfigScript)
	if returnConfig==0:
		tkMessageBox.showinfo("Mediawiki Configuration","Configured Mediawiki Successfully");
	else:
		tkMessageBox.showerror("Mediawiki Configuration","Mediawiki Configuration failed. Check /var/log/messages for further details");
		
# Starting Mediawiki
def startApache():
	callStartScript="bash startApache.sh"
	returnStart=os.system(callStartScript)
	if returnStart==0:
		tkMessageBox.showinfo("Apache Running Status","Apache Web Server Start Successfully. Point your browser to \n http://localhost/mediawiki/index.php\n to go to home page of Mediawiki") 
	else:
		tkMessageBox.showerror("Apache Running Status","Apache Web Server Start failed. Check /var/log/messages for further details");

# Installing Mediawiki
def install():
        print "Downloading and Installing Mediawiki"
	passing="bash install.sh "
	a=os.system(passing)
	if a==0:
		tkMessageBox.showinfo("Mediawiki Installation","Installed Mediawiki Successfully");
	else:
		tkMessageBox.showerror("Mediawiki Installation","Mediawiki Installation failed. Check /var/log/messages for further details");


# Main Window and its components
menubar = Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Close", command=root.quit)

menubar.add_cascade(label="File",menu=filemenu)

helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label="About...",command=about)

menubar.add_cascade(label="Help",menu=helpmenu)
 


w=Label(root,text="Graphical User Interface Tool for \nInstalling and Configuring Mediawiki: \nWebsite Engine for Collaborative work and Wiki Software", font=("Helvetica",14),justify=CENTER)

w.pack()

installButton = Button(root, text="Install Mediawiki", command=install,width=15)
installButton.pack(side=LEFT)


configureButton=Button(root, text="Setting Up Mediawiki Server", command=configMediawiki, width=25)
configureButton.pack(side=LEFT)

startButton=Button(root, text="Restart Apache Web Server", command=startApache, width=20)
startButton.pack(side=LEFT)



button = Button(root, text="Quit", command=root.quit, justify=CENTER, width=15)
button.pack(side=LEFT)


root.config(menu=menubar)
root.mainloop()


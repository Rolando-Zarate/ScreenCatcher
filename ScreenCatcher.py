import tkinter
import pyautogui
import os
import time
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
class Application:
    def __init__(self):
        self.formatDict = {"PNG - Portable Network Graphics":".png","JPG - Joint Photographic Experts Group":".png","BMP - Microsoft Windows Bitmap":".bmp"}
        self.root = tkinter.Tk()
        self.root.geometry("313x155")
        self.root.resizable(False,False)
        self.root.title("ScreenCatcher")
        self.loadBar()
        self.loadUi()
        self.loadIcon()
        self.root.mainloop()
    def loadIcon(self):
        try:
            self.root.iconbitmap("img/favicon.ico")
        except FileNotFoundError:
            messagebox.showwarning(title="Warning", message="The icon of the application was not founded in the app folder, see if in this directory the carpet 'img' exists or have the file 'favicon.ico', Using Tk default icon")
    def screenCatch(self,name,folder,formatIndex):
        if folder != "" and name != "":
            try: 
                checker = os.path.exists(folder)
                if checker == True:
                    self.root.iconify()
                    time.sleep(0.3)
                    image = pyautogui.screenshot()
                    image.save(folder+name+self.formatDict[formatIndex])
                    seeImage = messagebox.askyesno(title="Screenshot success",message="Image "+folder+name+" saved with no errors, Do you want to see it?")
                    if seeImage == True:
                        try:
                            os.startfile(folder+name+self.formatDict[formatIndex],"open")
                        except:
                            messagebox.showinfo(title="Oops",message="Image not founded")
                    else:
                        pass
                else:
                    messagebox.showinfo(title="Error",message="Folder doesn't exist or bad use of slashes.")
            except FileNotFoundError:
                messagebox.showinfo(title="Oops",message="Folder doesn't exist or bad use of slashes.")
            except PermissionError:
                messagebox.showinfo(title="Error",message="Permission denied")
            except KeyError:
                messagebox.showinfo(title="Oops",message="Select a format")
            except Exception as error:
                messagebox.showinfo(title="Error",message="Unknown error with name: "+'"'+str(error)+'"'+", contact via email with 'rolandoctm@gmail.com'")

        else:
            messagebox.showinfo(title="Oops",message="Invalid folder or image name!")
    def aboutMessage(self):
        messagebox.showinfo(title="About ScreenCatcher",message="ScreenCatcher is a free and open source screenshot taker for Microsoft Windows. Apache License v2.")
    def imageLoader(self):
        image = filedialog.askopenfilename(title="Open a image or capture",initialdir="/",filetypes=(("PNG Image","*.png"),("JPG Image","*.jpg"),("Microsoft Windows Bitmap Image","* .bmp"),))
        try: 
            os.startfile(image,"open")
        except:
            messagebox.showinfo(title="Oops",message="Image not founded")
    def folderNameChanger(self,folderEntry): 
        folder = filedialog.askdirectory(initialdir="/Users/Public/Pictures/")
        if folder == "":
            messagebox.showinfo(title="Oops",message="Enter a folder please")
        else:
            folderEntry.delete(0,tkinter.END)
            folderEntry.insert(0,folder+"/")
    def loadBar(self):
        self.menuBar = tkinter.Menu(self.root)
        self.root.config(menu=self.menuBar)
        self.seeImages = tkinter.Menu(self.menuBar,tearoff=False)
        self.about = tkinter.Menu(self.menuBar,tearoff=False)
        self.seeImages.add_command(label="See images...",command=self.imageLoader)
        self.about.add_command(label="About ScreenCatcher",command=self.aboutMessage)
        self.menuBar.add_cascade(label="Images",menu=self.seeImages)
        self.menuBar.add_cascade(label="About",menu=self.about)
    def loadUi(self):
        self.fileEntry = ttk.Entry(self.root)
        self.fileEntry.place(x=10,y=10,width=205,height=25)
        self.fileButton = ttk.Button(self.root,command=lambda:self.folderNameChanger(self.fileEntry),text="Select folder")
        self.fileButton.place(x=226,y=9)
        self.nameEntry = ttk.Entry(self.root)
        self.nameEntry.insert(0,"ScreenCatcher Capture")
        self.nameEntry.place(x=10,y=48,width=205,height=25)
        self.captureFormat = ttk.Combobox(self.root)
        self.captureFormat.place(x=10,y=86,width=205,height=25)
        self.captureFormat["value"] = ["PNG - Portable Network Graphics","JPG - Joint Photographic Experts Group","BMP - Microsoft Windows Bitmap"]
        self.screenShotButton = ttk.Button(self.root,command=lambda:self.screenCatch(self.nameEntry.get(),self.fileEntry.get(),self.captureFormat.get()),text="Screenshot")
        self.screenShotButton.place(x=9,y=120)
        self.typeLabel = ttk.Label(self.root,text="Image Type")
        self.typeLabel.place(x=227,y=90)
        self.nameLabel = ttk.Label(self.root,text="Image Name")
        self.nameLabel.place(x=227,y=50)
if __name__ == "__main__":
    Application()

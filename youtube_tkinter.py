from tkinter import *
from pytube import YouTube
#author:- BalamithranS
from tkinter import messagebox as mbox
global i
global name
global res

i = 0
root = Tk()
root.title("YOUTUBE DOWNLOADER")
my_label_1 = Label(root, text="WELCOME TO YOUTUBE DOWNLOADER", fg="red")
my_label_1.grid(column=0, row=0)


# Fields for entering name and filename
my_label = Label(root, text="ENTER THE LINK:")
my_label.grid(column=0, row=1)
box=Entry(root, width=60, borderwidth=3)
box.grid(column=1, row=1,  padx=10, pady=10)

my_name = Label(root,text="ENTER THE FILENAME:")
my_name.grid(column=0,row=2)
box_name=Entry(root,width=60, borderwidth=3)
box_name.grid(column=1, row=2,  padx=10, pady=10)


def fun():
    global i
    global name
    global res
    i = i+1


    ''' # without try and except
    path = "F:/"
    yt = YouTube(str(box.get()))
    yt.streams.first().download(output_path=path, filename=str(box_name.get()))
    '''
    try:
        path = "F:/"
        yt = YouTube(str(box.get()))
        yt.streams.first().download(output_path=path, filename=str(box_name.get()))
    except:
        onError()
        return
    print(i,"sucessful")
    res = "VIDEO TITLE:" + str(yt.title)
    my_title = Label(root, text=res)
    my_title.grid(column=0, row=4)
    res = "VIDEO VIEWS:" + str(yt.views)
    my_views = Label(root, text=res)
    my_views.grid(column=0, row=5)
    res = "VIDEO LENGTH:" + str(yt.length)
    my_length = Label(root, text=res)
    my_length.grid(column=0, row=6)
    res = "VIDEO DESCRIPTION:" + str(yt.description)
    my_description = Label(root, text=res)
    my_description.grid(column=0, row=7)
    res = "VIDEO RATING:" + str(yt.rating)
    my_rating = Label(root, text=res)
    my_rating.grid(column=0, row=8)
    onInfo()


downloader = Button(root, text="Download", bg="red",command=fun)
downloader.grid(column=1,row=3)


def onInfo():
    mbox.showinfo("Information", "Download completed")
    root.destroy()

def onError():
        mbox.showerror("Error", "wrong link try link")
        

#author:- BalamithranS
root.mainloop()

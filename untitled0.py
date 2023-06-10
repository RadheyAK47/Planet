from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()

root.title("planet encyclopedia")
root.geometry("1500x1500")
root.configure(bg="light green")

Mercury=ImageTk.PhotoImage(Image.open("mercury.jpg"))
Venus=ImageTk.PhotoImage(Image.open("venus.jpg"))
Earth=ImageTk.PhotoImage(Image.open("earth.jpg"))
Mars=ImageTk.PhotoImage(Image.open("mars.png"))

planet=Label(root,text="select planet name")
planet.place(relx=0.3,rely=0.1,anchor=CENTER)

list=["Mercury","Venus","Earth","Mars"]
selectedVal=StringVar()
dropdown=ttk.Combobox(root,values=list,textvariable=selectedVal)
dropdown.place(relx=0.7,rely=0.1,anchor=CENTER)

planet_name=Label(root,font=("courier",18,"bold"))
planet_name.place(relx=0.5,rely=0.4,anchor=CENTER)

planet_image=Label(root)
planet_image.place(relx=0.5,rely=0.7,anchor=CENTER)

planet_info=Label(root,font=("castellar",11))
planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)

def planetInfo():
    print("planet information")
    planet=selectedVal.get()
    if planet=="Mercury":
        planet_name["text"]="Mercury"
        planet_image["image"]=Mercury
        planet_info["text"]="Mercury is the smallest planet in our solar system.It is just a little bigger than Earth's Moon"
    elif planet=="Venus":
        planet_name["text"]="Venus"
        planet_image["image"]=Venus
        planet_info["text"]="Venus is the brightest object in the sky after the sun and the moon,it sometimes looks like a bright star in the morning or evening sky"
    elif planet=="Earth" :
        planet_name["text"]="Earth"
        planet_image["image"]=Earth
        planet_info["text"]="Earth is the only place in  the known universe confirmed to host life and it's the only one known for sure to have liquid water on it's surface"
    else :
        planet_name["text"]="Mars"
        planet_image["image"]=Mars
        planet_info["text"]="Mars is a dusty, cold, desert world with a very thin atmosphere."
    
btn=Button(root,text="show planet info",command=planetInfo)
btn.place(relx=0.5,rely=0.2,anchor=CENTER)

root.mainloop()


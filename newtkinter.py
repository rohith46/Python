import tkinter
root=tkinter.Tk()
root.title("The KML Generator")
label=tkinter.Label(root,text="This program generates KML files")
label.pack()
browserButton=tkinter.Button(root,text="Browse")
browserButton.pack()
kmlButton=tkinter.Button(root,text="Generate KML")
kmlButton.pack()
root.mainloop()
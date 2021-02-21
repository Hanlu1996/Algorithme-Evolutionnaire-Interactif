import tkinter as tk

from PIL import ImageTk, Image


class Initface():
    def __init__(self, master, png):
        # store id of selected images
        self.select_id = []

        self.master = master
        self.initface = tk.Frame(self.master, width=600, height=1000)

        # parameters
        self.png = png
        self.create_or_not = True

        self.info_label1 = tk.Label(self.initface,
                                    text="\nChoose your favorite 4 picture!!!\nPlease CLICK button OK after selection\n",
                                    justify='left', wraplength=280)
        self.info_label1.grid(row=1, column=1, columnspan=3)

        # picture 1 and RadioButton 1
        self.photo1 = Image.open(self.png[0])
        self.photo1 = self.photo1.resize((200, 150))
        self.photo1 = ImageTk.PhotoImage(self.photo1, master=self.master)
        self.img_label1 = tk.Label(self.initface, image=self.photo1)
        self.img_label1.grid(row=2, column=1)
        self.option1 = tk.Checkbutton(self.initface, text="picture 1", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(0))
        self.option1.grid(row=3, column=1)

        # picture 2 and RadioButton 2
        self.photo2 = Image.open(self.png[1])
        self.photo2 = self.photo2.resize((200, 150))
        self.photo2 = ImageTk.PhotoImage(self.photo2, master=self.master)
        self.img_label2 = tk.Label(self.initface, image=self.photo2)
        self.img_label2.grid(row=2, column=2)
        self.option2 = tk.Checkbutton(self.initface, text="picture 2", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(1))
        self.option2.grid(row=3, column=2)

        # picture 3 and RadioButton 3
        self.photo3 = Image.open(self.png[2])
        self.photo3 = self.photo3.resize((200, 150))
        self.photo3 = ImageTk.PhotoImage(self.photo3, master=self.master)
        self.img_label3 = tk.Label(self.initface, image=self.photo3)
        self.img_label3.grid(row=2, column=3)
        self.option3 = tk.Checkbutton(self.initface, text="picture 3", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(2))
        self.option3.grid(row=3, column=3)

        # picture 4 and RadioButton 4
        self.photo4 = Image.open(self.png[3])
        self.photo4 = self.photo4.resize((200, 150))
        self.photo4 = ImageTk.PhotoImage(self.photo4, master=self.master)
        self.img_label4 = tk.Label(self.initface, image=self.photo4)
        self.img_label4.grid(row=4, column=1)
        self.option4 = tk.Checkbutton(self.initface, text="picture 4", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(3))
        self.option4.grid(row=5, column=1)

        # picture 5 and RadioButton 5
        self.photo5 = Image.open(self.png[4])
        self.photo5 = self.photo5.resize((200, 150))
        self.photo5 = ImageTk.PhotoImage(self.photo5, master=self.master)
        self.img_label5 = tk.Label(self.initface, image=self.photo5)
        self.img_label5.grid(row=4, column=2)
        self.option5 = tk.Checkbutton(self.initface, text="picture 5", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(4))
        self.option5.grid(row=5, column=2)

        # picture 6 and RadioButton 6
        self.photo6 = Image.open(self.png[5])
        self.photo6 = self.photo6.resize((200, 150))
        self.photo6 = ImageTk.PhotoImage(self.photo6, master=self.master)
        self.img_label6 = tk.Label(self.initface, image=self.photo6)
        self.img_label6.grid(row=4, column=3)
        self.option6 = tk.Checkbutton(self.initface, text="picture 6", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(5))
        self.option6.grid(row=5, column=3)

        # picture 7 and RadioButton 7
        self.photo7 = Image.open(self.png[6])
        self.photo7 = self.photo7.resize((200, 150))
        self.photo7 = ImageTk.PhotoImage(self.photo7, master=self.master)
        self.img_label7 = tk.Label(self.initface, image=self.photo7)
        self.img_label7.grid(row=6, column=1)
        self.option7 = tk.Checkbutton(self.initface, text="picture 7", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(6))
        self.option7.grid(row=7, column=1)

        # picture 8 and RadioButton 8
        self.photo8 = Image.open(self.png[7])
        self.photo8 = self.photo8.resize((200, 150))
        self.photo8 = ImageTk.PhotoImage(self.photo8, master=self.master)
        self.img_label8 = tk.Label(self.initface, image=self.photo8)
        self.img_label8.grid(row=6, column=2)
        self.option8 = tk.Checkbutton(self.initface, text="picture 8", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(7))
        self.option8.grid(row=7, column=2)

        # picture 9 and RadioButton 9
        self.photo9 = Image.open(self.png[8])
        self.photo9 = self.photo9.resize((200, 150))
        self.photo9 = ImageTk.PhotoImage(self.photo9, master=self.master)
        self.img_label9 = tk.Label(self.initface, image=self.photo9)
        self.img_label9.grid(row=6, column=3)
        self.option9 = tk.Checkbutton(self.initface, text="picture 9", variable=tk.IntVar(),
                                      command=lambda: self.selectImage(8))
        self.option9.grid(row=7, column=3)

        # Button "OK" make sure the selection
        self.buttonOK = tk.Button(self.initface, text="    OK   ", bd=10, bg='blue', command=lambda: self.getId())
        self.buttonOK.grid(row=8, column=3, columnspan=1)

        # info label of option
        self.info_label2 = tk.Label(self.initface, text="\nGeneration 1\n", justify='left', wraplength=280)
        self.info_label2.grid(row=9, column=1, columnspan=3)

        self.initface.pack()

    # User clicks on image to select， we use this method to know the id of image
    def selectImage(self, id):
        self.select_id.append(id)

    # Return all images id which user selected
    def getId(self):
        print(self.select_id)
        return self.select_id

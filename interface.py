import tkinter as tk
import tkinter.messagebox
import matplotlib

from diffusionAlgo import diffAlgo


class Initface():
    def __init__(self, master, png, rgb):
        self.master = master
        self.initface = tk.Frame(self.master, width=600, height=1000)


        # parameters
        self.rgb = rgb
        self.png = png
        self.create_or_not = True
        self.option = -1
        self.algo = diffAlgo(rgb[0], rgb[1], rgb[2])

        self.create_or_not = True
        self.option = -1
        self.info_label1 = tk.Label(self.initface,
                                    text="\nChoose your favorite picture!!!\nPlease CLICK button OK after selection\n",
                                    justify='left', wraplength=280)
        self.info_label1.grid(row=1, column=1, columnspan=3)

        # option of image
        self.option = tk.IntVar()

        # picture 1 and RadioButton 1
        self.photo1 = tk.PhotoImage(file=self.png[0])
        self.img_label1 = tk.Label(self.initface, image=self.photo1)
        self.img_label1.grid(row=2, column=1)
        self.option1 = tk.Radiobutton(self.initface, text="picture 1", variable=self.option, value=1)
        self.option1.grid(row=3, column=1)

        # self.labelframe.pack()

        # picture 2 and RadioButton 2
        self.photo2 = tk.PhotoImage(file=self.png[1])
        self.img_label2 = tk.Label(self.initface, image=self.photo2)
        self.img_label2.grid(row=2, column=2)
        self.option2 = tk.Radiobutton(self.initface, text="picture 2", variable=self.option, value=2)
        self.option2.grid(row=3, column=2)

        # picture 3 and RadioButton 3
        self.photo3 = tk.PhotoImage(file=self.png[2])
        self.img_label3 = tk.Label(self.initface, image=self.photo3)
        self.img_label3.grid(row=2, column=3)
        self.option3 = tk.Radiobutton(self.initface, text="picture 3", variable=self.option, value=3)
        self.option3.grid(row=3, column=3)

        # picture 4 and RadioButton 4
        self.photo4 = tk.PhotoImage(file=self.png[3])
        self.img_label4 = tk.Label(self.initface, image=self.photo4)
        self.img_label4.grid(row=4, column=1)
        self.option4 = tk.Radiobutton(self.initface, text="picture 4", variable=self.option, value=4)
        self.option4.grid(row=5, column=1)

        # picture 5 and RadioButton 5
        self.photo5 = tk.PhotoImage(file=self.png[4])
        self.img_label5 = tk.Label(self.initface, image=self.photo5)
        self.img_label5.grid(row=4, column=2)
        self.option5 = tk.Radiobutton(self.initface, text="picture 5", variable=self.option, value=5)
        self.option5.grid(row=5, column=2)

        # picture 6 and RadioButton 6
        self.photo6 = tk.PhotoImage(file=self.png[4])
        self.img_label6 = tk.Label(self.initface, image=self.photo6)
        self.img_label6.grid(row=4, column=3)
        self.option6 = tk.Radiobutton(self.initface, text="picture 6", variable=self.option, value=6)
        self.option6.grid(row=5, column=3)

        # picture 7 and RadioButton 7
        self.photo7 = tk.PhotoImage(file=self.png[6])
        self.img_label7 = tk.Label(self.initface, image=self.photo7)
        self.img_label7.grid(row=6, column=1)
        self.option7 = tk.Radiobutton(self.initface, text="picture 7", variable=self.option, value=7)
        self.option7.grid(row=7, column=1)

        # picture 8 and RadioButton 8
        self.photo8 = tk.PhotoImage(file=self.png[7])
        self.img_label8 = tk.Label(self.initface, image=self.photo8)
        self.img_label8.grid(row=6, column=2)
        self.option8 = tk.Radiobutton(self.initface, text="picture 8", variable=self.option, value=8)
        self.option8.grid(row=7, column=2)

        # picture 9 and RadioButton 9
        self.photo9 = tk.PhotoImage(file=self.png[8])
        self.img_label9 = tk.Label(self.initface, image=self.photo9)
        self.img_label9.grid(row=6, column=3)
        self.option9 = tk.Radiobutton(self.initface, text="picture 9", variable=self.option, value=9)
        self.option9.grid(row=7, column=3)

        # Button "OK" make sure the selection
        self.buttonOK = tk.Button(self.initface, text="    OK   ", bd=10, bg='blue', command=self.select_img)
        self.buttonOK.grid(row=8, column=3, columnspan=1)

        # info label of option
        self.info_label2 = tk.Label(self.initface, justify='left', wraplength=280)
        self.info_label2.grid(row=9, column=1, columnspan=3)

        # info label of recreating image
        self.info_label3 = tk.Label(self.initface,
                                    text=" If there are NO your favorite picture, INPUT Color variable (0-255) and CLICK button \'CREATE\' to generate your picture.",
                                    justify='left', wraplength=280)
        self.info_label3.grid(row=10, column=1, columnspan=3)

        # create new image by rgb
        self.labelRED = tk.Label(self.initface, justify='left', text="RED : ").grid(row=11, column=1)
        self.inputRED = tk.Entry(self.initface, justify='right')
        self.inputRED.grid(row=12, column=1)

        self.labelGREEN = tk.Label(self.initface, justify='left', text="GREEN : ").grid(row=11, column=2)
        self.inputGREEN = tk.Entry(self.initface, justify='right')
        self.inputGREEN.grid(row=12, column=2)

        self.labelBLUE = tk.Label(self.initface, justify='left', text="BLUE : ").grid(row=11, column=3)
        self.inputBLUE = tk.Entry(self.initface, justify='right')
        self.inputBLUE.grid(row=12, column=3)

        # Button "CREATE" to create new image
        self.buttonCREATE = tk.Button(self.initface, text="    CREATE\t", bd=10, bg='blue',
                                      command=self.create_new_image)
        self.buttonCREATE.grid(row=13, column=3)

        self.initface.pack()

        # # set up window
        # self.root.mainloop()

    def select_img(self):
        if self.option.get() == 0:
            tk.messagebox.showinfo(title='Information', message="Please choose your favorite!")
        else:
            selstr = "You selected the picture " + str(self.option.get()) + " as your favorite."
            tk.messagebox.showinfo(title='Information', message=selstr)

    def create_new_image(self):
        try:
            r = int(self.inputRED.get())
            g = int(self.inputGREEN.get())
            b = int(self.inputBLUE.get())
            if r < 0 or r > 255 or g < 0 or g > 255 or g < 0 or g > 255:
                tk.messagebox.showwarning(title='ERROR', message="Please input an integer between 0 to 255")
            else:
                self.rgb = [r, g, b]
                # self.algo.rgb = [r,g,b]
                # self.algo.completed_algo()
                self.initface.destroy()
                questionFrame(self.master, self.png, self.rgb)

        except ValueError:
            # Handle the exception
            tk.messagebox.showwarning(title='ERROR', message="Please input an integer between 0 to 255")



class questionFrame():
    def __init__(self, master, png, rgb):
        self.master = master
        self.questionFrame = tk.Frame(self.master, width=400, height=400)

        self.rgb = rgb
        self.png = png
        self.choose = True
        self.algo = diffAlgo(self.rgb[0], self.rgb[1], self.rgb[2])
        self.label1 = tk.Label(self.questionFrame, text="Your new color is here, do you agree with it ? ")
        self.label1.grid(row=1, column=2)
        self.color = matplotlib.colors.to_hex((float(self.rgb[0]/255), float(self.rgb[1]/255), float(self.rgb[2]/255)))
        self.label3 = tk.Label(self.questionFrame, text="         ", bg=self.color)
        self.label3.grid(row=2, column=2)
        self.buttonYES = tk.Button(self.questionFrame, text="YES, Let's go!", command=self.yes)
        self.buttonYES.grid(row=4, column=1)
        self.buttonNO = tk.Button(self.questionFrame, text="No, change again", command=self.no)
        self.buttonNO.grid(row=4, column=2)

        self.questionFrame.pack()



    def yes(self):
        self.algo.completed_algo()
        self.choose = True
        self.questionFrame.destroy()
        Initface(self.master, self.algo.filename, self.rgb)

    def no(self):
        self.choose = False
        tk.messagebox.showinfo(title='Information', message="Come back to re-input your color")
        self.questionFrame.destroy()
        whitecolor = [255, 255, 255]
        Initface(self.master, self.png, whitecolor)
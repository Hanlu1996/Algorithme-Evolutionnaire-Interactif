from interface import Initface
from interface import questionFrame
from diffusionAlgo import diffAlgo

import tkinter as tk


class basedesk():
    def __init__(self, master, pngs, rgbs):
        self.root = master
        self.root.config()
        self.root.title('Base page')
        self.root.geometry('630x1100')
        self.root.resizable(width=True, height=True)
        self.rgb = rgbs
        self.png = pngs
        Initface(self.root, self.png, self.rgb)
        # questionFrame(self.root, self.png, self.rgb)


if __name__ == '__main__':

    root = tk.Tk()
    png = ["pic/view.png"]
    R = [1,3,5,7,9,11,13,15]
    for i in R :
        str = "pic/view_after_" + (i).__str__() + ".png"
        png.append(str)
    rgb=[255,255,255]
    # intefrace = Interface(png=png, rgb=rgb)
    basedesk(root, pngs=png, rgbs=rgb)
    root.mainloop()


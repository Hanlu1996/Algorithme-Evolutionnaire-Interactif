import random
import tkinter as tk
import time

from AlgoEvolution import AlgoEvolu
from interface import Initface
from turing import ReactionDiffusion



def geneticContinue(array, N_GENERATIONS):
    arr = array
    # for _ in range(N_GENERATIONS):
    init_window = tk.Tk()
    png = ["pic/test0.png"]
    for i in range(9):
        str = "pic/test" + (i + 1).__str__() + ".png"
        png.append(str)
    window = Initface(init_window, png=png)

    algo = AlgoEvolu()
    parents = algo.select(arr, window.getId())
    print('parents: ', parents)
    children = algo.crossover(parents)
    children = algo.mutate(children)
    parents.append(children)
    for i in range(len(parents)):
        reactiondiffusion2 = ReactionDiffusion(parents[i], 200, i)
        reactiondiffusion2.generateimage()
        arr[i] = reactiondiffusion2.getAttribute()
    if N_GENERATIONS != 0:
        N_GENERATIONS -= 1
        geneticContinue(arr,N_GENERATIONS)
    init_window.mainloop()


if __name__ == '__main__':

    arr = [[0] * 7 for i in range(9)]
    for i in range(9):
        reactiondiffusion = ReactionDiffusion(random.random(), random.random(), random.randint(1, 9),
                                              random.randint(1, 50), random.random(), random.randint(50, 500),
                                              random.random(), 200, i)
        reactiondiffusion.generateimage()
        arr[i] = reactiondiffusion.getAttribute()

    print(arr)
    init_window = tk.Tk()
    png = ["pic/test0.png"]
    for i in range(9):
        str = "pic/test" + (i + 1).__str__() + ".png"
        png.append(str)
    window = Initface(init_window, png=png)
    if window.getFlag() == 0:
        geneticContinue(arr,10)
    init_window.mainloop()

import random
import tkinter as tk

from AlgoEvolution import AlgoEvolu
from interface import Initface
from turing import ReactionDiffusion

N_GENERATIONS = 10

if __name__ == '__main__':

    arr = [[0] * 7 for i in range(9)]
    for i in range(9):
        reactiondiffusion = ReactionDiffusion(random.random(), random.random(), random.randint(1, 9),
                                              random.randint(1, 50), random.random(), random.randint(50, 500),
                                              random.random(), 200, i)
        reactiondiffusion.generateimage()
        arr[i] = reactiondiffusion.getAttribute()

    print(arr)

    for _ in range(N_GENERATIONS):
        init_window = tk.Tk()
        png = ["pic/test0.png"]
        for i in range(9):
            str = "pic/test" + (i + 1).__str__() + ".png"
            png.append(str)
        window = Initface(init_window, png=png)
        init_window.mainloop()
        # id = window.getId()
        # print(id)
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

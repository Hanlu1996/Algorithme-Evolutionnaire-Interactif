import random

import numpy as np


class AlgoEvolu(object):

    # Get the parameters of all selected images
    def select(self, parents, id):
        selected_parents = []
        for i in id:
            selected_parents.append(parents[i])
        return selected_parents

    # Randomly select two parents to generate new children
    def crossover(self, parents):
        children = []
        for i in range(5):
            a = random.sample(parents, 2)
            print(a)
            parent1 = a[0]
            parent2 = a[1]
            x = random.random()
            child = [0, 0, 0, 0, 0, 0, 0]
            for j in range(7):
                child[j] = x * abs(parent1[j] - parent2[j])
            children.append(child)
        print('children:', children)

        return children

    # Random mutation of the child's genes
    def mutate(self, children):
        children_mutate = []
        for i in range(5):
            j = random.randint(0, 6)
            children[i][j] = children[i][j] + np.random.normal(loc=0, scale=1.0, size=None)
            children_mutate.append(children[i])

        return children_mutate

# if __name__ == '__main__':
#     algo = AlgoEvolu()
# algo.select([[1,2,3,4,5],[2,3,1,6,8],[1,5,9,3,4]],[0,2])
# algo.crossover([[1, 2, 3, 4], [2, 3, 5, 7], [3, 7, 8, 9], [9, 9, 7, 5]])
# algo.mutate([[1, 2, 3, 4], [2, 3, 5, 7], [3, 7, 8, 9], [9, 9, 7, 5], [3.3, 6.8, 5, 9]])

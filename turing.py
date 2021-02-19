import numpy as np
import matplotlib.pyplot as plt
import random


class ReactionDiffusion(object):

    def __init__(self, tauxrea, tauxrei, vitessedia, vitessedii, tauxreso, seuilact, size):
        self.tauxReactionA = tauxrea
        self.tauxReactionI = tauxrei
        self.vitesseDiffusionA = vitessedia
        self.vitesseDiffusionI = vitessedii
        self.tauxResorption = tauxreso
        self.seuilActivation = seuilact
        self.size = size
        self.A = [[0] * self.size for i in range(self.size)]
        self.I = [[0] * self.size for i in range(self.size)]
        self.X = [[0] * self.size for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.A[i][j] = random.random() * 100
                self.I[i][j] = random.random() * 100
                self.X[i][j] = [255, 165, 0]

    def reagir(self):
        for i in range(self.size):
            for j in range(self.size):
                ancien_i = self.I[i][j]
                self.I[i][j] = self.I[i][j] + (self.tauxReactionI * self.A[i][j] * self.A[i][j])
                self.A[i][j] = self.A[i][j] + (self.tauxReactionA * self.A[i][j] * self.A[i][j] / ancien_i)

    def diffusion(self):
        taux_diffusion = 0.1
        up = -1
        down = -1
        left = -1
        right = -1
        while self.vitesseDiffusionA > 0:
            for i in range(self.size):
                for j in range(self.size):
                    if i == 0:
                        up = self.size - 1
                    if i == self.size - 1:
                        down = 0
                    if j == 0:
                        left = self.size - 1
                    if j == self.size - 1:
                        right = 0
                    if up == -1:
                        up = i - 1
                    if down == -1:
                        down = i + 1
                    if left == -1:
                        left = j - 1
                    if right == -1:
                        right = j + 1
                    temp = self.A[i][j] * 0.1 / 8
                    self.A[i][left] = self.A[i][left] + temp
                    self.A[i][right] = self.A[i][right] + temp
                    self.A[up][j] = self.A[up][j] + temp
                    self.A[down][j] = self.A[down][j] + temp
                    self.A[up][j] = self.A[up][j] - temp
                    self.A[up][left] = self.A[up][left] + temp
                    self.A[up][right] = self.A[up][right] + temp
                    self.A[down][left] = self.A[down][left] + temp
                    self.A[down][right] = self.A[down][right] + temp
                    up = -1
                    down = -1
                    left = -1
                    right = -1
            self.vitesseDiffusionA = self.vitesseDiffusionA - 1

        while self.vitesseDiffusionI > 0:
            for i in range(self.size):
                for j in range(self.size):
                    if i == 0:
                        up = self.size - 1
                    if i == self.size - 1:
                        down = 0
                    if j == 0:
                        left = self.size - 1
                    if j == self.size - 1:
                        right = 0
                    if up == -1:
                        up = i - 1
                    if down == -1:
                        down = i + 1
                    if left == -1:
                        left = j - 1
                    if right == -1:
                        right = j + 1
                    temp = self.I[i][j] * taux_diffusion / 8
                    self.I[i][left] = self.I[i][left] + temp
                    self.I[i][right] = self.I[i][right] + temp
                    self.I[up][j] = self.I[up][j] + temp
                    self.I[down][j] = self.I[down][j] + temp
                    self.I[up][j] = self.I[up][j] - temp
                    self.I[up][left] = self.I[up][left] + temp
                    self.I[up][right] = self.I[up][right] + temp
                    self.I[down][left] = self.I[down][left] + temp
                    self.I[down][right] = self.I[down][right] + temp
                    up = -1
                    down = -1
                    left = -1
                    right = -1
            self.vitesseDiffusionI = self.vitesseDiffusionI - 1

    def resorber(self):
        for i in range(self.size):
            for j in range(self.size):
                self.A[i][j] = self.A[i][j] * (1 - self.tauxResorption)
                self.I[i][j] = self.I[i][j] * (1 - self.tauxResorption)

    def seiller(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.seuilActivation < self.A[i][j]:
                    self.X[i][j] = [139, 69, 19]
                else:
                    self.X[i][j] = [255, 165, 0]
            # self.setCouleur()

    def setCouleur(self):
        plt.imshow(self.X)
        plt.title("Plot 2D array")
        plt.show()


if __name__ == '__main__':
    reactiondiffusion = ReactionDiffusion(0.04, 0.0002, 4, 25, 0.06, 122, 500)
    reactiondiffusion.reagir()
    reactiondiffusion.diffusion()
    reactiondiffusion.resorber()
    reactiondiffusion.seiller()
    reactiondiffusion.setCouleur()


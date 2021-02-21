import matplotlib.pyplot as plt
import random


class ReactionDiffusion(object):

    def __init__(self, tauxrea, tauxrei, vitessedia, vitessedii, tauxreso, seuilact, tauxdiffu, size, id):
        self.tauxReactionA = tauxrea
        self.tauxReactionI = tauxrei
        self.vitesseDiffusionA = vitessedia
        self.p = vitessedia
        self.q = vitessedii
        self.vitesseDiffusionI = vitessedii
        self.tauxResorption = tauxreso
        self.seuilActivation = seuilact
        self.tauxDiffusion = tauxdiffu
        self.size = size
        self.id = id
        self.A = [[0] * self.size for i in range(self.size)]
        self.I = [[0] * self.size for i in range(self.size)]
        self.X = [[0] * self.size for i in range(self.size)]
        for i in range(self.size):
            for j in range(self.size):
                self.A[i][j] = random.random() * 100
                self.I[i][j] = random.random() * 100
                self.X[i][j] = [255, 165, 0]

    def getAttribute(self):
        a = [self.tauxReactionA, self.tauxReactionI, self.p, self.q,
             self.tauxResorption, self.seuilActivation, self.tauxDiffusion]
        return a

    def reagir(self):
        for i in range(self.size):
            for j in range(self.size):
                ancien_i = self.I[i][j]
                self.I[i][j] = self.I[i][j] + (self.tauxReactionI * self.A[i][j] * self.A[i][j])
                self.A[i][j] = self.A[i][j] + (self.tauxReactionA * self.A[i][j] * self.A[i][j] / ancien_i)

    def diffusion(self):
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
                    temp = self.I[i][j] * self.tauxDiffusion / 8
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

    def generateimage(self):
        self.reagir()
        self.diffusion()
        self.resorber()
        self.seiller()
        plt.axis('off')
        plt.gca().set_position([0, 0, 1, 1])
        plt.imshow(self.X)
        filename = 'pic/test' + str(self.id) + '.png'
        plt.savefig(filename)

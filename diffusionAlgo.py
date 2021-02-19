import random

from PIL import Image

HEIGHT = 100
WIDTH = 100


class OnePatch:
    def __init__(self, a, i, r, g, b):
        self.a = a
        self.i = i
        self.r = r
        self.g = g
        self.b = b


class diffAlgo():
    def __init__(self,r,g,b):
        self.patches = []
        self.filename = []
        self.rgb = [r,g,b]

    def clean_all(self):
        print("clean all")

    def initialisation(self, patches, red, green, blue):
        # start up
        global taux_reaction_a
        global taux_reaction_i
        global vitesse_diffusion_a
        global vitesse_diffusion_i
        global taux_resorption
        global seuil_activation
        # to set up
        self.clean_all()
        # for ele in patches:
        for w in range(WIDTH):
            line = []
            for h in range(HEIGHT):
                r = red
                g = green
                b = blue
                a = random.randint(1, 100)
                i = random.randint(1, 100)
                line.append(OnePatch(a, i, r, g, b))
            patches.append(line)

        taux_reaction_a = 0.04
        taux_reaction_i = 0.0002
        vitesse_diffusion_a = 4
        vitesse_diffusion_i = 25
        taux_resorption = 0.06
        seuil_activation = 122
        print("init")
        return patches

    def reagir(self, patches):
        for line in patches:
            for ele in line:
                ancien_i = ele.i
                ele.i = ele.i + taux_reaction_i * pow(ele.a, 2)
                ele.a = ele.a + taux_reaction_a * pow(ele.a, 2) / ancien_i
        print("reagir")
        return patches

    def diffuser(self, patches, width, height):
        taux_diffusion = 0.1

        for w in range(WIDTH):
            for h in range(HEIGHT):
                left = w - 1
                right = w + 1
                up = h - 1
                down = h + 1
                a = patches[w][h].a * (taux_diffusion)
                i = patches[w][h].i * (taux_diffusion)
                # ()
                # *********************************** a ***********************************
                for a_ir in range(vitesse_diffusion_a):
                    if left >= 0:
                        patches[left][h].a += a * (1 / 8)
                        if up >= 0:
                            patches[left][up].a += a * (1 / 8)
                            patches[w][up].a += a * (1 / 8)
                        if down < HEIGHT:
                            patches[left][down].a += a * (1 / 8)
                            patches[w][down].a += a * (1 / 8)
                    if right < WIDTH:
                        patches[right][h].a += a * (1 / 8)
                        if up >= 0:
                            patches[right][up].a += a * (1 / 8)
                        if down < HEIGHT:
                            patches[right][down].a += a * (1 / 8)
                # *********************************** i ***********************************
                for i_ir in range(vitesse_diffusion_i):
                    if left >= 0:
                        patches[left][h].i += i * (1 / 8)
                        if up >= 0:
                            patches[left][up].i += i * (1 / 8)
                            patches[w][up].i += i * (1 / 8)
                        if down < HEIGHT:
                            patches[left][down].i += i * (1 / 8)
                            patches[w][down].i += i * (1 / 8)
                    if right < WIDTH:
                        patches[right][h].i += i * (1 / 8)
                        if up >= 0:
                            patches[right][up].i += i * (1 / 8)
                        if down < HEIGHT:
                            patches[right][down].i += i * (1 / 8)
        print("diffusion")
        return patches

    def diffusion_image(self, filename, patches, width, height, num):
        im = Image.open(filename, "r")
        rgb_im = im.convert('RGB')

        for w in range(width):
            for h in range(height):
                r, g, b = rgb_im.getpixel((w, h))
                patches[w][h].r = r
                patches[w][h].g = g
                patches[w][h].b = b

        patches = self.resorber(self.diffuser(self.reagir(patches), WIDTH, HEIGHT))

        # seuillage
        image_after = Image.new('RGB', (WIDTH, HEIGHT))
        for w in range(width):
            for h in range(height):
                if patches[w][h].a > seuil_activation:
                    patches[w][h].r = self.random_color(patches[w][h].r)
                    patches[w][h].g = self.random_color(patches[w][h].g)
                else:
                    patches[w][h].r = self.random_color(patches[w][h].r)
                    patches[w][h].g = self.random_color(patches[w][h].g)
                pixTuple = (patches[w][h].r, patches[w][h].g, patches[w][h].b, 0)
                image_after.putpixel((w, h), pixTuple)
        name = "mypic/myview_after_" + str(num) + ".png"
        self.filename.append(name)
        image_after.save(self.filename[num])
        return name

    def resorber(self, patches):
        for line in patches:
            for ele in line:
                ele.a = ele.a * (1 - taux_resorption)
                ele.i = ele.i * (1 - taux_resorption)
        print("resorber")
        return patches

    def seuillage(self, patches):
        for line in patches:
            for ele in line:
                if ele.a > seuil_activation:
                    # brown rgb (150,75,0)
                    xx = min(ele.r, ele.g, ele.b)
                    cg = random.randint(60,100)
                    if xx == ele.r:
                        ele.r = self.color_change(xx, cg)
                    elif xx == ele.g:
                        ele.g = self.color_change(xx, cg)
                    elif xx == ele.b:
                        ele.b = self.color_change(xx, cg)
        print("seuillage")
        return patches

    def color_change(self, cx, niv):
        if cx < 128:
            ncx = cx + niv
            return ncx
        else:
            ncx = cx - niv
            return ncx

    def random_color(self, cg):
        a = random.randint(1, 3)
        if a == 1:
            return cg
        elif a == 2:
            niv = 10 * random.randint(1, 5)
            res = self.color_change(cg, niv)
            return res
        elif a == 3:
            niv = 20 * random.randint(1, 5)
            res = self.color_change(cg, niv)
            return res

    def completed_algo(self):

        # initialization
        patches = self.initialisation(self.patches, self.rgb[0], self.rgb[1], self.rgb[2])
        # reagir
        # diffuser
        # resorber
        # seuiller
        newpatches = self.seuillage(self.resorber(self.diffuser(self.reagir(self.patches), WIDTH, HEIGHT)))
        # tick
        # track

        new_image = Image.new('RGB', (WIDTH, HEIGHT))

        for y in range(WIDTH):
            for x in range(HEIGHT):
                r = newpatches[y][x].r
                g = newpatches[y][x].g
                b = newpatches[y][x].b
                pixTuple = (r, g, b, 0)
                new_image.putpixel((y, x), pixTuple)
        self.filename.append("mypic/myview.png")
        new_image.save(self.filename[0])  # or another format
        files = []
        for i in range(15):
            name = self.diffusion_image(self.filename[i], newpatches, WIDTH, HEIGHT, i+1)
            files.append(name)
        R = [0, 2, 4, 6, 8, 10, 12, 14]
        for i in R:
            self.filename.append(files[i])


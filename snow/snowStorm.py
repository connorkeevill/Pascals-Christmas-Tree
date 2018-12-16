from snow.snowFlake import snowFlake
import random
import threading
import time

class snowStorm():
    def __init__(self):
        self.snowFlakes = []

        for i in range(5):
            self.generateSnowFlake()

        snowFall = threading.Thread(target=self.makeSnow)
        snowFall.setDaemon(True)
        snowFall.start()

        cleanStorm = threading.Thread(target=self.removeOldSnow)
        cleanStorm.setDaemon(True)
        cleanStorm.start()


    def makeSnow(self):
        while True:
            self.generateSnowFlake()
            time.sleep(1 / 100)

    def removeOldSnow(self):
        while True:
            for flake in self.snowFlakes:
                if flake.Ypos > 700:
                    self.snowFlakes.remove(flake)

            time.sleep(2)

    def generateSnowFlake(self):
        flake = snowFlake(random.randint(1, 3), random.randint(1, 700))
        self.snowFlakes.append(flake)

    def fall(self):
        for flake in self.snowFlakes:
            flake.fall()

    def draw(self, display):
        for flake in self.snowFlakes:
            flake.draw(display)
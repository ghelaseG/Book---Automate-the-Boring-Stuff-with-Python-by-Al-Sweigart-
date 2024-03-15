import zombiedice

class MyZombie:
    def _init_(self,name):
        self.name = name

    def turn(self,gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombieShotGun2:
    def _init_(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        shotGun = 0
        while diceRollResults is not None:
            shotGun += diceRollResults['shotgun']

            if shotGun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

class MyZombieRandom1:
    def _init_(self, name):
        self.name = name

    def turn(self, gameState):

        diceRollResults = zombiedice.roll()
        while diceRollResults and random.randint(0, 1) == 0:
            diceRollResults = zombiedice.roll()

class MyZombie1to4ThenShotGun:
    def _init_(self, name):
        self.name = name

    def turn(self, gameState):
        runRec = 4;
        diceRollResults = zombiedice.roll()
        shotGun = 0
        while diceRollResults is not None and runRec > 0:
            shotGun += diceRollResults['shotgun']
            runRec -= runRec
            if shotGun < 2:
                diceRollResults = zombiedice.roll()
            else:
                break

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name ='Stop at 2 Shotguns', minShotguns = 2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name ='Stop at 1 Shotgun', minShotguns = 1),
    MyZombieShotGun2(name ='ShotGunPro'),
    MyZombieRandom1(name ='RandomPro'),
    MyZombie1to4ThenShotGun(name ='PreMinded'),
    MyZombie1to4ThenShotGun(name ='MoreShotGuns')
)
zombiedice.runWebGui(zombies=zombies, numGames=1000)

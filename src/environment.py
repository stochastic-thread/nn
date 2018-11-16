import os
os.system("python3.7 prims.py")

class Environment:
    def runSimulation(self, sideEffects=None):
        integers = lambda startInt, lastInt: list(range(startInt, lastInt))
        sideEffects(integers(0, 100))

def main():
    sideEffects = lambda l: [print(item) for item in l]
    Environment().runSimulation(sideEffects=sideEffects)

if __name__=="__main__":
    main()

from random import randint

class Clock:
    def __init__(self, offset: float = 0, skew:float = 1) -> None:
        self.time = offset
        self.skew = skew

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"{self.time}"
    
    def get_time(self, passed_ticks: int) -> float:
        self.time = self.skew * passed_ticks + self.time
        return self.time
    
    def scramble_time(self) -> None:
        #Scramble skew rate from 0.95-1.05
        self.skew = 1 + randint(-5,5)/100
        #Scramble offset from -2 to 2 seconds
        self.time = self.time + randint(-2,2)

if __name__ == "__main__":
    #Test code for current class
    exampleClock = Clock(0, 1)
    print(exampleClock)

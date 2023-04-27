from random import randint

class Clock:
    def __init__(self, offset: float = 0, skew:float = 1) -> None:
        self.time = offset
        self.skew = skew

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"{self.time}"
    
    def get_time(self, systemTick: int) -> float:
        self.time = self.skew * systemTick + self.time
        return self.time
    
    def scramlbe_time(self):
        #Scramble skew rate from 0.9-1.1
        self.skew = 1 + randint(-10,10)/10
        #Scramble offset from -10 to 10 seconds
        self.time = self.time + randint(-10,10)

    def set_system_time(self, systemTick: int) -> None:
        self.time = systemTick
        self.skew = 1

if __name__ == "__main__":
    exampleClock = Clock(0, 1)
    print(exampleClock)

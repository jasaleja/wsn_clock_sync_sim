class Clock:
    def __init__(self, offset: float = 0, skew:float = 1) -> None:
        self.offset = offset
        self.skew = skew
    
    def getTime(self, systemTick) -> float:
        time = systemTick - self.offset
        return time
    
    def setSystemTime(self) -> None:
        self.offset = 0
        self.skew = 1

if __name__ == "__main__":
    exampleClock = Clock(0, 1)
    print(exampleClock)

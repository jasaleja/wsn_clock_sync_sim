"""Mode for class Clock."""

class Clock:
    """Class for mathematical representation of a clock."""
    def __init__(self, offset: float = 0, skew:float = 1) -> None:
        self.time = offset
        # Unknow to the user and should not be edited once set
        self.natural_skew = skew
        # Known to the user
        self.compensation_skew = 1

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.time}"

    def pass_time(self, passed_ticks: int) -> float:
        """Advance the clock by the amount of passed ticks."""
        self.time = (self.natural_skew/self.compensation_skew) * passed_ticks + self.time
        return self.time

    def scramble_time(self, skew: float, offset: float) -> None:
        """Introduce an error in the skew rate and offset."""
        #Scramble skew rate
        self.natural_skew = 1 + skew
        #Scramble offset
        self.time = self.time + offset

if __name__ == "__main__":
    # Test code for class Clock
    exampleClock = Clock(0, 1)
    print(exampleClock)

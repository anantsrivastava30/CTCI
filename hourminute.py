from sympy.physics.quantum.circuitplot import np

class clock:
    'base class for clock'
    hour = 0
    minute = 0

    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def display_time(self):
        print("Hour : ", self.hour, ", Minute: ", self.minute)

    @staticmethod
    def clock_type():
        print("Sonata")

    def find_angle(self):
        a1 = self.minute / 60 * 360
        a2 = (self.hour % 12) / 12 * 360 + a1/12
        angle = abs(a1 - a2)
        return angle


def main():
    c1 = clock(9, 38)
    c1.display_time()
    print("Angle between minute and hour hand : ", c1.find_angle())
    c1.clock_type()
    print(ord(" "))
    a = np.array([])
    print(a)
    print(min([1,2,3,-3]))

if __name__ == "__main__":
    main()

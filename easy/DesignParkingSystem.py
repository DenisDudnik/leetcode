# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.places = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.places[carType] == 0:
            return False
        self.places[carType] -= 1
        return True


if __name__ == "__main__":
    obj = ParkingSystem(1, 1, 0)

    assert obj.addCar(1) == True
    assert obj.addCar(2) == True
    assert obj.addCar(3) == False
    assert obj.addCar(1) == False

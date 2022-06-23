class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def mass_calculation(self, weidth=25, thinkness=5):
        return f'Масса асфальта: {(self._lenght * self._width * weidth * thinkness) / 1000}'


road_1 = Road(5000, 20)
print(road_1.mass_calculation())

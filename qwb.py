#!/usr/bin/env python3


class Bench:
    def __init__(self, width, height):
        self.grid = []
        self.source_location = None

        for i in range(height):
            self.grid.append([Space()] * width)

    def display(self):
        for row in self.grid:
            for cell in row:
                print(cell.display, end=" ")
            print()

    def place(self, x, y, component):
        if not isinstance(self.grid[y][x], Space):
            raise ValueError
        if isinstance(component, Source):
            if self.source_location:
                raise ValueError  # only one source allowed
            self.source_location = (x, y)
        self.grid[y][x] = component

    def run(self):
        x, y = self.source_location
        dx, dy = 1, 0
        while True:
            x += dx
            y += dy
            try:
                dx, dy = self.grid[y][x].hit(dx, dy)
                if (dx, dy) == (0, 0):
                    break
            except IndexError:
                break


class Space:
    display = "."

    def hit(self, dx, dy):
        return dx, dy


class Source:
    display = "S"


class Box:
    pass


class ColorBox(Box):
    pass


class HardnessBox(Box):
    pass


class Mirror:
    display = "/"

    def hit(self, dx, dy):
        return -dy, -dx


class Detector:
    display = "D"

    def __init__(self):
        self.count = 0

    def hit(self, dx, dy):
        self.count += 1
        return 0, 0


if __name__ == "__main__":
    bench = Bench(10, 10)
    bench.place(1, 8, Source())
    detector_1 = Detector()
    detector_2 = Detector()
    bench.place(8, 8, detector_1)
    bench.place(6, 6, detector_2)
    bench.display()
    bench.run()
    print(detector_1.count)
    print(detector_2.count)
    bench.place(6, 8, Mirror())
    bench.display()
    bench.run()
    bench.run()
    print(detector_1.count)
    print(detector_2.count)

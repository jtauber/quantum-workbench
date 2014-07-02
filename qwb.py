#!/usr/bin/env python3


class Bench:
    def __init__(self, width, height):
        self.grid = []
        for i in range(height):
            self.grid.append([Space()] * width)

    def display(self):
        for row in self.grid:
            for cell in row:
                print(cell.display, end=" ")
            print()


class Space:
    display = "."


class Source:
    pass


class Box:
    pass


class ColorBox(Box):
    pass


class HardnessBox(Box):
    pass


class Mirror:
    pass


class Detector:
    pass


if __name__ == "__main__":
    bench = Bench(10, 10)
    bench.display()

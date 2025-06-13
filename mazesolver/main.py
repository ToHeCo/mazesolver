from tkinter import Tk, BOTH, Canvas
from objects import Point, Line

class Window:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.__root = Tk()
        self.__root.title("Maze")
        self.canvas = Canvas(height = self.height, width = self.width)
        self.canvas.pack(fill = BOTH)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.canvas, fill_color)


def main():
    win = Window(800, 600)
    p1 = Point(200,4)
    p2 = Point(8,200)
    l1 = Line(p1, p2)
    win.draw_line(l1, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
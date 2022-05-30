import os
import random
import threading
from tkinter import *

LIVE = '#'
DEAD = ' '

class GameOfLifeWorld:

    width = 100
    height = 100
    cells = []


    def __init__(self, width, height):
        self.width = width
        self.height = height

    def InitRandom(self):
        self.cells = [[LIVE if random.random() > 0.8 else DEAD for i in range(self.width)]
                       for j in range(self.height)]

    def TryGetCell(self, h, w):
        return self.cells[min(h, self.height - 1)][min(w, self.width - 1)]

    def GetNearbyCellsCount(self, h, w):
        nearby = [self.TryGetCell(h + dy, w + dx) for dx in [-1, 0, 1]
                  for dy in [-1, 0, 1] if not (dx == 0 and dy == 0)]
        return len(list(filter(lambda x: x == LIVE, nearby)))

    def GetNewCell(self, h, w):
        count = self.GetNearbyCellsCount(h, w)
        return LIVE if count == 3 else (DEAD if count < 2 or count > 3 else self.cells[h][w])

    def Update(self):
        self.cells = [[self.GetNewCell(h, w) for w in range(self.width)]
                  for h in range(self.height)]

width = 100
height = 100
mainForm = None
canvas = None
cellSize = 5
world = None


def PrintScreen():
    global canvas
    for h in range(height):
        for w in range(width):
            tag_pos = '%d_%d' % (h, w)
            if world.cells[h][w] == LIVE:
                found = canvas.find_withtag(tag_pos)
                if len(found) == 0:
                    canvas.create_rectangle(w * cellSize, h * cellSize, (w + 1) *
                                            cellSize, (h + 1) * cellSize, fill='blue', tags=('cell', tag_pos))
            else:
                canvas.delete(tag_pos)


def Update():
    world.Update()


def Loop():
    Update()
    PrintScreen()


def BtnNext_OnClick():
    Loop()


def StartTimer():
    Loop()
    global timer
    timer = threading.Timer(1, StartTimer)
    timer.start()


def Start():
    global mainForm
    mainForm = Tk()
    size = '%dx%d' % (width * cellSize, height * cellSize + 50)
    mainForm.geometry(size)
    global canvas

    canvas = Canvas(mainForm, bg='black', width=width *
                    cellSize, height=height * cellSize)
    canvas.grid(row=0, column=0)

    Button(mainForm, text='Next', command=BtnNext_OnClick).grid(row=1, column=0)

    global world
    world = GameOfLifeWorld(width, height)
    world.InitRandom()
    PrintScreen()

    StartTimer()

    mainForm.mainloop()


timer = threading.Timer(1, StartTimer)

if __name__ == "__main__":
    Start()
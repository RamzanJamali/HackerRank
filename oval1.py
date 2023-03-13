from shapes import Paper, Rectangle, Triangle, Oval

paper = Paper()

oval = Oval()
oval.randomize(smallest=20, largest=200)

oval.draw()
paper.display()

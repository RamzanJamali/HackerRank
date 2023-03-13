from shapes import Paper, Rectangle, Triangle, Oval

paper = Paper()

rectl = Rectangle()
rectl.set_width(300)
rectl.set_height(100)
rectl.set_color("orange")
rectl.set_x(200)
rectl.set_y(100)

rectl.draw()

rectn = Rectangle()
rectn.set_width(100)
rectn.set_height(200)
rectn.set_color("orange")
rectn.set_x(200)
rectn.set_y(100)

rectn.draw()

trin = Triangle(200,300,300,300,250,350, "orange")
trin.draw()

oval = Oval()
oval.set_width(50)
oval.set_height(50)
oval.set_color("black")
oval.set_x(425)
oval.set_y(125)

oval.draw()

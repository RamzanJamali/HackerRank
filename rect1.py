from shapes import Paper, Rectangle, Triangle, Oval

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.set_x(100)
rect1.set_y(100)

rect1.draw()

rect2 = Rectangle()
rect2.set_width(100)
rect2.set_height(200)
rect2.set_color("orange")
rect2.set_x(300)
rect2.set_y(100)

rect2.draw()

rect3 = Rectangle()
rect3.set_width(200)
rect3.set_height(100)
rect3.set_color("green")
rect3.set_x(100)
rect3.set_y(200)

rect3.draw()

paper.display()

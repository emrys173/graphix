from graphix import Point, Window, Rectangle, Polygon, Line

colours = ["red", "green", "blue", "magenta", "orange", "purple"]

def main():
    while True:
        win_size = input("Enter the size of the window (5, 7, 9): ")
        if win_size in ['5', '7', '9']:
            break
        else:
            print("Please enter a valid number (5, 7, or 9)")

    used_colour = []

    colour1 = get_valid_colour("Enter the first colour (red, green, blue, magenta, orange, purple): ", used_colour)
    used_colour.append(colour1)
    colour2 = get_valid_colour("Enter the second colour (red, green, blue, magenta, orange, purple): ", used_colour)
    used_colour.append(colour2)
    colour3 = get_valid_colour("Enter the third colour (red, green, blue, magenta, orange, purple): ", used_colour)
    used_colour.append(colour3)

    win_size = int(win_size)
    tile_size = 100
    win = Window("Grid with Patterns", win_size * tile_size, win_size * tile_size)

    draw_grid(win, win_size, tile_size)  


    if win_size == 5:
        for i in range(5):
            if i % 2 ==0:
                draw_patch_window(win, start_x=400 - i * 100, start_y=i * 100, fill_colour1=colour2, fill_colour2="white")
            else:
                draw_rectangle(win, Point(400 - i * 100, i * 100), Point(500 - i * 100, (i + 1) * 100), colour2)
            
        for x in range(0, 400, 100):
            draw_chevron_pattern(win, top_left_corner_x=x, top_left_corner_y=0, patch_colour=colour1)
        for y in range(100, 400, 100):
            draw_chevron_pattern(win, top_left_corner_x=0, top_left_corner_y=y, patch_colour=colour1)

        for x in range(100, 300, 100):
            draw_rectangle(win, Point(x, 100), Point(x + 100, 200), colour1)
        for y in range(200, 300, 100):
            draw_rectangle(win, Point(100, y), Point(200, y + 100), colour1)

        for y in range(300, 500, 100):
            draw_patch_window(win, start_x=200, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(100, 500, 100):
            draw_patch_window(win, start_x=400, start_y=y, fill_colour1=colour3, fill_colour2="white")
        
        for y in range(400, 500, 100):
            draw_rectangle(win, Point(100, y), Point(200, y + 100), colour3)
        for y in range(200, 500, 100):
            draw_rectangle(win, Point(300, y), Point(400, y + 100), colour3)
        

    elif win_size == 7:
        for i in range(7):
            if i % 2 == 0:
                draw_patch_window(win, start_x=600 - i * 100, start_y=i * 100, fill_colour1=colour2, fill_colour2="white")
            else:
                draw_rectangle(win, Point(600 - i * 100, i * 100), Point(700 - i * 100, (i + 1) * 100), colour2)
        for x in range(0, 600, 100):
            draw_chevron_pattern(win, top_left_corner_x=x, top_left_corner_y=0, patch_colour=colour1)
        for y in range(100, 600, 100):
            draw_chevron_pattern(win, top_left_corner_x=0, top_left_corner_y=y, patch_colour=colour1)
        
        for x in range(100, 500, 100):
            draw_rectangle(win, Point(x, 100), Point(x + 100, 200), colour1)
        for y in range(200, 500, 100):
            draw_rectangle(win, Point(100, y), Point(200, y + 100), colour1)
        for x in range(200, 400, 100):
            draw_rectangle(win, Point(x, 200), Point(x + 100, 300), colour1)

        for y in range(500, 800, 100):
            draw_patch_window(win, start_x=200, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(300, 800, 100):
            draw_patch_window(win, start_x=400, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(100, 800, 100):
            draw_patch_window(win, start_x=600, start_y=y, fill_colour1=colour3, fill_colour2="white")

        for y in range(400, 800, 100):
            draw_rectangle(win, Point(300, y), Point(400, y + 100), colour3)
        for y in range(200, 800, 100):
            draw_rectangle(win, Point(500, y), Point(600, y + 100), colour3)
        
        draw_rectangle(win, Point(200, 300), Point(300, 400), colour1)
        draw_rectangle(win, Point(100, 600), Point(200, 700), colour3) 

        
    elif win_size == 9:
        for i in range(9):
            if i % 2 == 0:
                draw_patch_window(win,start_x=800 - i * 100,start_y=i * 100,fill_colour1= colour2,fill_colour2="white")
            else:
                draw_rectangle(win, Point(800 - i * 100, i * 100), Point(900 - i * 100, (i + 1) * 100), colour2)
        for x in range(0, 800, 100):
            draw_chevron_pattern(win, top_left_corner_x=x, top_left_corner_y=0, patch_colour=colour1)
        for y in range(100, 800, 100):  
            draw_chevron_pattern(win, top_left_corner_x=0, top_left_corner_y=y, patch_colour=colour1)
        
        for x in range(100, 700, 100):
            draw_rectangle(win, Point(x, 100), Point(x + 100, 200), colour1)
        for y in range(200, 700, 100):
            draw_rectangle(win, Point(100, y), Point(200, y + 100), colour1)
        
        for x in range(200, 600, 100):
            draw_rectangle(win, Point(x, 200), Point(x + 100, 300), colour1)
        for y in range(200, 600, 100):
            draw_rectangle(win, Point(200, y), Point(300, y + 100), colour1)
        for x in range(300, 500, 100):
            draw_rectangle(win, Point(x, 300), Point(x + 100, 400), colour1)
        
        for y in range(700, 900, 100):
            draw_patch_window(win, start_x=200, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(500, 900, 100):
            draw_patch_window(win, start_x=400, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(300, 900, 100):
            draw_patch_window(win, start_x=600, start_y=y, fill_colour1=colour3, fill_colour2="white")
        for y in range(100, 900, 100):
            draw_patch_window(win, start_x=800, start_y=y, fill_colour1=colour3, fill_colour2="white")

        for y in range(600, 900, 100):
            draw_rectangle(win, Point(300, y), Point(400, y + 100), colour3)
        for y in range(400, 900, 100):
            draw_rectangle(win, Point(500, y), Point(600, y + 100), colour3)
        for y in range(200, 900, 100):
            draw_rectangle(win, Point(700, y), Point(800, y + 100), colour3)

        draw_rectangle(win, Point(300, 400), Point(400, 500), colour1)
        draw_rectangle(win, Point(100, 800), Point(200, 900), colour3)
    
    win.get_mouse()
    win.close()

   
def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)

def get_valid_colour(prompt, used_colour):
    while True:
        colour = input(prompt).lower()
        if colour in colours and colour not in used_colour:
            return colour
        elif colour in used_colour:
            print("Colour already used, please choose another colour")
        else:
            print("Please enter a valid colour")

def draw_grid(win, grid_size, tile_size):
    for y in range(0, grid_size * tile_size, tile_size):
        for x in range(0, grid_size * tile_size, tile_size):
            p1 = Point(x, y)
            p2 = Point(x + tile_size, y + tile_size)
            rect = Rectangle(p1, p2)
            rect.fill_colour = "white"
            rect.draw(win)

def draw_patch_window(win, start_x, start_y, fill_colour1, fill_colour2):
    for i, size in enumerate(range(100, 0, -10)):
        top_left = Point(start_x + (100 - size) // 2, start_y + (100 - size) // 2)
        bottom_right = Point(start_x + (100 + size) // 2, start_y + (100 + size) // 2)
        square = Rectangle(top_left, bottom_right)
        square.fill_colour = fill_colour1 if i % 2 == 0 else fill_colour2
        square.draw(win)

def draw_chevron_pattern(window: Window, top_left_corner_x: int, top_left_corner_y: int, patch_colour: str) -> list:
    design_objects = []
    for i in range(0, 100, 10):
        for j in range(0, 100, 10):
            if i % 20 == 0:
                if j % 20 == 0:
                    points = [
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + j),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + (j + 10)),
                        Point(top_left_corner_x + i, top_left_corner_y + (j + 10))
                    ]
                else:
                    points = [
                        Point(top_left_corner_x + i, top_left_corner_y + j),
                        Point(top_left_corner_x + i, top_left_corner_y + (j + 10)),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + j)
                    ]
            else:
                if j % 20 == 0:
                    points = [
                        Point(top_left_corner_x + i, top_left_corner_y + j),
                        Point(top_left_corner_x + i, top_left_corner_y + (j + 10)),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + (j + 10))
                    ]
                else:
                    points = [
                        Point(top_left_corner_x + i, top_left_corner_y + j),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + j),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + (j + 10))
                    ]
            
            if (i in {20, 30, 60, 70} and j in {0, 10, 80, 90}) or (i not in {20, 30, 60, 70}):
                polygon = Polygon(points=points)
                polygon.fill_colour = patch_colour
                polygon.outline_colour = patch_colour
                polygon.draw(window)
                design_objects.append(polygon)
            else:
                if i == 30 or i == 70:
                    line = Line(
                        Point(top_left_corner_x + i, top_left_corner_y + j),
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + (j + 10))
                    )
                else:
                    line = Line(
                        Point(top_left_corner_x + (i + 10), top_left_corner_y + j),
                        Point(top_left_corner_x + i, top_left_corner_y + (j + 10))
                    )
                    
                line.fill_colour = patch_colour
                line.draw(window)
                design_objects.append(line)
    
    return design_objects

main()

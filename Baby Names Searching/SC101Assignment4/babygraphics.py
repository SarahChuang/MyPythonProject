"""
File: babygraphics.py
Name: Han Hsiu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x = GRAPH_MARGIN_SIZE + (width - GRAPH_MARGIN_SIZE*2)/len(YEARS) * year_index
    return x


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i)+TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # read name in order
    for i in range(len(lookup_names)):
        if i >= len(COLORS):
            color = COLORS[i % len(COLORS)]
        else:
            color = COLORS[i]
        # display the information of target name
        target_name = name_data[lookup_names[i]]
        # set up the initial position in first year
        x1 = get_x_coordinate(CANVAS_WIDTH, 0)
        y1 = -1
        # draw the line and text by years
        for j in range(len(YEARS)):
            if str(YEARS[j]) in target_name:
                y2 = (int(target_name[str(YEARS[j])]) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK) + GRAPH_MARGIN_SIZE
                if y1 == -1:
                    y1 = y2
                x2 = get_x_coordinate(CANVAS_WIDTH, j)
                canvas.create_text(x2 + TEXT_DX, y2, text=str(lookup_names[i]) + " " + target_name[str(YEARS[j])], anchor=tkinter.SW, fill=color)
            else:
                y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                if y1 == -1:
                    y1 = y2
                x2 = get_x_coordinate(CANVAS_WIDTH, j)
                canvas.create_text(x2 + TEXT_DX, y2, text=str(lookup_names[i]) + " " + "*", anchor=tkinter.SW, fill=color)
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=color)
            x1 = x2
            y1 = y2


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()

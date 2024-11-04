"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius*2, self.ball_radius*2, x=self.window_width/2-self.ball_radius, y=self.window_height/2-self.ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.move_paddle)
        self.start = False

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                self.brick = GRect(brick_width, brick_height, x=(brick_width + brick_spacing)*i, y=(brick_height + brick_spacing)*j+brick_offset)
                self.brick.filled = True
                if j == 0 or j % BRICK_ROWS == 1:
                    self.brick.fill_color = "red"
                    self.brick.color = "red"
                if j % BRICK_ROWS == 2 or j % BRICK_ROWS == 3:
                    self.brick.fill_color = "orange"
                    self.brick.color = "orange"
                if j % BRICK_ROWS == 4 or j % BRICK_ROWS == 5:
                    self.brick.fill_color = "yellow"
                    self.brick.color = "yellow"
                if j % BRICK_ROWS == 6 or j % BRICK_ROWS == 7:
                    self.brick.fill_color = "green"
                    self.brick.color = "green"
                if j % BRICK_ROWS == 8 or j % BRICK_ROWS == 9:
                    self.brick.fill_color = "blue"
                    self.brick.color = "blue"
                self.window.add(self.brick)
                # print(i, j, self.brick.y)

        # Get bricks amount
        self.brick_cols = BRICK_COLS
        self.brick_rows = BRICK_ROWS

    # move paddle
    def move_paddle(self, event):
        if event.x >= self.window.width - self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x <= self.paddle.width/2:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - self.paddle.width/2

    # start the game and define the ball speed
    def start_game(self, event):
        self.start = True
        if self.start and self.ball.x == self.window_width/2-self.ball_radius and self.ball.y == self.window_height/2-self.ball_radius:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy








"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 50        # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    lives = NUM_LIVES
    graphics = BreakoutGraphics()
    n = 0
    while lives != 0:
        vx = 0
        vy = 0
        while vx == 0:
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            pause(FRAME_RATE)
        # game start
        while graphics.start:
            graphics.ball.move(vx, vy)
            # bounce back when the ball touches the boundary of the window
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.height >= graphics.window.width:
                vx = -vx
            if graphics.ball.y <= 0 or graphics.ball.y > graphics.window.height + graphics.ball.height:
                vy = -vy
            # get the brick and remove it
            obj_upper_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            obj_upper_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y)
            obj_lower_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
            obj_lower_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.height, graphics.ball.y + graphics.ball.height)
            if obj_upper_left is not None and graphics.ball.y < graphics.paddle.y:
                graphics.window.remove(obj_upper_left)
                vy = -vy
                n += 1
            else:
                if obj_upper_right is not None and graphics.ball.y < graphics.paddle.y:
                    graphics.window.remove(obj_upper_right)
                    vy = -vy
                    n += 1
                else:
                    if obj_lower_left is not None and graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                        graphics.window.remove(obj_lower_left)
                        vy = -vy
                        n += 1
                    else:
                        if obj_lower_right is not None and graphics.ball.y + graphics.ball.height < graphics.paddle.y:
                            graphics.window.remove(obj_lower_right)
                            vy = -vy
                            n += 1
                        else:
                            # bounce back when the ball touches the paddle
                            if obj_upper_left or obj_upper_right or obj_lower_left or obj_lower_right is not None:
                                if graphics.ball.x <= graphics.paddle.x or graphics.ball.x+graphics.ball.width <= graphics.paddle.x or graphics.ball.x >= graphics.paddle.x + graphics.paddle.width or graphics.ball.x + graphics.ball.width >= graphics.paddle.x + graphics.paddle.width:
                                    vx = -vx
                                if graphics.ball.y <= graphics.paddle.y + graphics.paddle.height or graphics.ball.y+graphics.ball.height <= graphics.paddle.y + graphics.paddle.height:
                                    if vy > 0 and graphics.paddle.x <= graphics.ball.x >= graphics.paddle.x + graphics.paddle.width or vy > 0 and graphics.ball.y+graphics.ball.height <= graphics.paddle.y + graphics.paddle.height:
                                        vy = -vy
            # lose one life when the ball exceed the boundary
            if graphics.ball.y > graphics.window.height or graphics.ball.y > graphics.window.height + graphics.ball.height:
                graphics.ball.x = graphics.window_width/2-graphics.ball_radius
                graphics.ball.y = graphics.window_height/2-graphics.ball_radius
                lives -= 1
                break
            # the game ends when all the bricks are removed
            if n == graphics.brick_cols*graphics.brick_rows:
                graphics.ball.x = graphics.window_width / 2 - graphics.ball_radius
                graphics.ball.y = graphics.window_height / 2 - graphics.ball_radius
                break
            pause(FRAME_RATE)
        graphics.start = False


if __name__ == '__main__':
    main()

import constants

from game.casting.cast import Cast
# from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.snake2 import Snake2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
# from game.scripting.control_snake2_action import ControlSnake2Action
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    # cast.add_actor("foods", Food())
    cast.add_actor("snake", Snake())
    cast.add_actor("snake2", Snake2())
    player1_score = Score("Player One")
    player2_score = Score("Player Two")
    player1_score.set_position(Point(10, 10))
    player2_score.set_position(Point(int(10 + constants.MAX_X/2), 10))
    cast.add_actor("player1_score", player1_score)
    cast.add_actor("player2_score", player2_score)
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    handle_collision = HandleCollisionsAction()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service, handle_collision))
    # script.add_action("input", ControlSnake2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", handle_collision)
    # script.add_action("update", GrowTrailAction)
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
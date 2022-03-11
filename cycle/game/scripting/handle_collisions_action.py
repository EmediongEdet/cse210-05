
import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with the food, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player1 = cast.get_first_actor("cycle")
        player2 = cast.get_first_actor("cycle2")
        if not self._is_game_over:
            # self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            # self._handle_player_collision(cast)
            self._handle_game_over(cast)
            player1.start_growing()
            player2.start_growing()
     

   
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("cycle")
        player1_head = player1.get_segments()[0]
        player1_segments = player1.get_segments()[1:]

        player2 = cast.get_first_actor("cycle2")
        player2_head = player2.get_segments()[0]
        player2_segments = player2.get_segments()[1:]
        

        # Player 1 segment handling
        for segment in player1_segments:
            if player2_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

        # Player 2 segment handling
        for segment in player2_segments:
            if player1_head.get_position().equals(segment.get_position()):
                self._is_game_over = True

    def _handle_player_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        
        player1 = cast.get_first_actor("cycle")
        player2 = cast.get_first_actor("cycle2")
        cycle1 = player1.get_segments()[0:]
        
        cycle2 = player2.get_segments()[0:]

        for y in cycle2:
            for x in cycle1:
                if x.get_position().equals(y.get_position()):
                    self._is_game_over = True
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycle and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("cycle")
            player1_segments = player1.get_segments()
            # food = cast.get_first_actor("foods")

            player2 = cast.get_first_actor("cycle2")
            player2_segments = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in player1_segments:
                segment.set_color(constants.WHITE)
            
            for segment in player2_segments:
                segment.set_color(constants.WHITE)
    def get_game_over(self):
        return self._is_game_over
from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player1_score = cast.get_first_actor("player1_score")
        player2_score = cast.get_first_actor("player2_score")
        player1 = cast.get_first_actor("snake")
        player2 = cast.get_first_actor("snake2")
        player1_segments = player1.get_segments()
        player2_segments = player2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(player1_segments)
        self._video_service.draw_actors(player2_segments)
        self._video_service.draw_actor(player1_score)
        self._video_service.draw_actor(player2_score)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
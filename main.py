import constants

from game.casting.cast import Cast 
from game.casting.food import Food
from game.casting.score import Score 
from game.casting.cycle import Cycle  
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
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
    cast.add_actor("foods", Food())
    
    cast.add_actor("snake1", Cycle(1))
    cast.add_actor("snake2", Cycle(2))

    cast.add_actor("scores", Score(Point(15, 0), "Player One: "))
    cast.add_actor("scores", Score(Point(750, 0), "Player Two: "))

    scores = cast.get_actors('scores')
    scores = cast.get_actors('scores')

    # Player one score, to show at start
    scores[0].set_text('Player One:')
    scores[0].set_position(Point(15, 0))

    # Player two score, to show at start
    scores[1].set_text('Player Two:')
    scores[1].set_position(Point(750, 0))

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()
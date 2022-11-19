import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.casting.cycle import Cycle

class Handle_dead_snakes:

    def __init__(self, num_player) -> None:
        players = Cycle(Actor) 
        self._num_player = players.num_player

    def dead_snakes(self, cast):
            if self._is_game_over:
                if self._num_player == 1:
                    x = int(constants.MAX_X / 3)
                    y = int(constants.MAX_Y / 2)

                elif self._num_player == 2:
                    x = int(constants.MAX_X / 1.5)
                    y = int(constants.MAX_Y / 2)


                for i in range(constants.SNAKE_LENGTH):          
                    position = Point(x - i * constants.CELL_SIZE, y)
                    velocity = Point(1 * constants.CELL_SIZE, 0)
                    text = "8" if i == 0 else "#"
                    if self._num_player == 1:
                        color = constants.RED if i == 0 else constants.RED
                    elif self._num_player == 2:
                        color = constants.GREEN if i == 0 else constants.GREEN

                    segment = Actor()
                    segment.set_position(position)
                    segment.set_velocity(velocity)
                    segment.set_text(text)
                    segment.set_color(color)
                    self._segments.append(segment)
                """
                food = cast.get_first_actor("foods")
                food.set_color(constants.WHITE)  

                snake1 = cast.get_first_actor("snake1")
                head1 = snake1.get_segments()[0]
                segments1 = snake1.get_segments()
                
                snake2 = cast.get_first_actor("snake2")
                head2 = snake1.get_segments()[0]
                segments2 = snake2.get_segments()

                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)

                message = Actor()
                message.set_text(f'Game Over!') 
                message.set_position(position)
    """
                """
                if self._winner == 'Player One':
                    message.set_color(constants.RED)
                elif self._winner == 'Player Two':
                    message.set_color(constants.GREEN)
                """
                #cast.add_actor("messages", message)
    """
                for segment1 in segments1:
                    segment1.set_color(constants.WHITE)
                    # Set playable area
                    # Collision with the player1
                    if head2.get_position().equals(segment1.get_position()):
                        print('Hitting player 2')
                        snake2.turn_head(self._direction2)

                for segment2 in segments2:
                    segment2.set_color(constants.WHITE)
                    # Set playable area
                    # Collision with the player2 
                    if head1.get_position().equals(segment2.get_position()):
                        print('Hitting player 1')
                        snake1.turn_head(self._direction1)
    """
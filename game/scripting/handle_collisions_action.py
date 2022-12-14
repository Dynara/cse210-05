import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = ''
        self._player_one_score = 0
        self._player_two_score = 0


    def execute(self, cast, script):
        """Executes the handle collisions action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)


    def _handle_food_collision(self, cast):
        """Updates the score nd moves the food if the snake collides with the food.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        _score = cast.get_actors("scores")
        food = cast.get_first_actor("foods")

        snake1 = cast.get_first_actor("snake1")
        snake2 = cast.get_first_actor("snake2")

        head1 = snake1.get_head()
        head2 = snake2.get_head()

        if head1.get_position().equals(food.get_position()):
            points1 = food.get_points()
            snake1.grow_tail(points1, constants.RED)
            _score[0].add_points(points1)
            food.reset()
            self._player_one_score = _score[0]
            return _score[0]
        
        elif head2.get_position().equals(food.get_position()):
            points2 = food.get_points()
            snake2.grow_tail(points2, constants.GREEN)
            _score[1].add_points(points2)
            food.reset()
            self._player_two_score = _score[1]
            return _score[1]
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("snake1")
        head1 = snake1.get_segments()[0]
        segments1 = snake1.get_segments()[1:]
        
        snake2 = cast.get_first_actor("snake2")
        head2 = snake2.get_segments()[0]
        segments2 = snake2.get_segments()[1:]
        
        # Collision with own snake
        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 'Player Two'
            elif head1.get_position().equals(head2.get_position()):
                self._is_game_over = True
                self._winner = "It's a Draw!!"

            # Collision with the player1
            for segment1 in segments1:
                if head2.get_position().equals(segment1.get_position()):
                    self._is_game_over = True
                    self._winner = 'Player One'
                    return self._winner

        # Collision with own snake
        for segment in segments2:
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
                self._winner = 'Player One'
 

            # Collision with the player2 
            for segment2 in segments2:
                if head1.get_position().equals(segment2.get_position()):
                    self._is_game_over = True
                    self._winner = 'Player Two'
                    return self._winner
            

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake white and food black if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            food = cast.get_first_actor("foods")
            food.set_color(constants.BLACK)  

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
            # For winner, could add {self._winner} after 'Game Over!', but unsure 
            # if winner is player who doesn't run into the other player, or player 
            # with highest points
            message.set_text(f'Game Over!') 
            message.set_position(position)

            if self._winner == 'Player One':
                message.set_color(constants.RED)
            elif self._winner == 'Player Two':
                message.set_color(constants.GREEN)

            cast.add_actor("messages", message)


            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
                #if head2.get_position().equals(segment1.get_position() or head1.get_position()):
                        
            
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)
                #if head1.get_position().equals(segment2.get_position() or head2.get_position()):
                        

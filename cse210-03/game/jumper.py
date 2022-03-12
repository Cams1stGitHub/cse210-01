import random

class Jumper:
    """The players stats in the game.
    
    The responsibility of Jumper is to keep track of all of the letters guessed and display
    the remaining parachute.
    
    Attributes:
    -----------
        _jumper (dict[int, str]): The players remaining life.
        _word_list (list): The list of hidden words in the game.
        _current_word (str): The hidden word the player needs to guess.
        _guess_count (int): The remaining guesses the player has.
    """

    def __init__(self):
        """Constructs a new Jumper.
        
        Args:
        -----
            self (Jumper): An instance of Jumper.
        """
        self._jumper = {
            1: "  ___",
            2: " /___\\",
            3: " \\   /",
            4: "  \\ /",
            5: "   O",
            6: "  /|\\",
            7: "  / \\",
            8: "",
            9: "^^^^^^^"
        }
        self._word_list = []
        self._current_word = ""
        self._guess_count = 4
        
    def select_random_word(self):
        """"""
        self._word_list = random.choice(["burrito", "quesodilla", "taco"])

    def get_guess_count(self):
        pass

    def set_guess_count(self):
        pass

    def get_jumper_image(self):
        """Gets the image of the Jumper.
        
        Args:
        -----
            self (Jumper): An instance of Jumper.
            
        Returns:
        --------
            dictionary: An image of the remaining parachute."""
        if self._guess_count == 4:
            self._jumper = self._jumper
        elif self._guess_count == 3:
            del self._jumper[1]
        elif self._guess_count == 2:
            del self._jumper[2]
        elif self._guess_count == 1:
            del self._jumper[3]
        elif self._guess_count == 0:
            del self._jumper[4]
            self._jumper[5] = "X"
        return self._jumper
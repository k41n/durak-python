from durak.game import Game;
from durak.bot  import Bot;
from durak.ui   import UI;

game = Game();
ai = Bot();
human = UI();

game.addPlayer(human);
game.addPlayer(ai);

game.start();

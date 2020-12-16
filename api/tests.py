from django.test import TestCase
from .models import Game

# Create your tests here.

class GameTestCase(TestCase):
    
    def setUp(self):
        Game.objects.create(name="game1", original_price=15000)
        # Game.objects.create(name="cat", sound="meow")

    def test_game_name(self):
        game1 = Game.objects.get(name="game1")
        self.assertEqual(game1.__str__(), "game1")
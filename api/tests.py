from django.test import TestCase
from .models import Game

# Create your tests here.

class GameTestCase(TestCase):
    
    def setUp(self):
        Game.objects.create(name="game1", original_price=15000)
        Game.objects.create(name="game2", original_price=15000, discount=2500)

    def test_game_name(self):
        game1 = Game.objects.get(name="game1")
        self.assertEqual(game1.__str__(), "game1")

    def test_new_price(self):
        game2 = Game.objects.get(name="game2")
        self.assertEqual(15000-2500, game2.original_price - game2.discount)
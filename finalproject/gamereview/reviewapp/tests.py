from django.test import TestCase
from .models import Game, GameType, Review
from .forms import GameForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
class GameTest(TestCase):
    def test_stringOutput(self):
        game=Game(gamename='Witcher 3')
    self.assertEqual(str(game), game.gamename)

    def test_tablename(self):
        self.assertEqual(str(Game._meta.db_table), 'game')

class GameTypeTest(TestCase):
    def test_stringOutput(self):
        reviewapptype=GameType(typename='RPG')
        self.assertEqual(str(reviewapptype), reviewapptype.typename)

    def test_tablename(self):
        self.assertEqual(str(ReviewappType._meta.db_table), 'gametype')

class ReviewTest(TestCase):
    def test_stringOutput(self):
        review=Review(reviewtitle='Witcher 3')
        self.assertEqual(str(review), review.reviewtitle)

    def test_tablename(self):
self.assertEqual(str(Review._meta.db_table), 'review')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
         response=self.client.get(reverse('index'))
         self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
         response=self.client.get(reverse('index'))
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'reviewapp/index.html')

class TestGetGame(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/reviewapp/games')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getgames'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getgames'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/games.html')

class New_Game_Form_Test(TestCase):

    # Valid Form Data
    def test_gameForm_is_valid(self):
        form = GameForm(data={'gamename': "Dark Souls 3", 'reviewapptype': "Action", 'user': "zack", 'entrydate': "2019-03-04", 'gameURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = GameForm(data={'gamename': "Dark Souls 3", 'reviewapptype': "Action", 'user': "zack", 'entrydate': "2018-03-04", 'gameURL':"http:microsoft.com", 'productdescription':"lightweight laptop" })
self.assertFalse(form.is_valid())
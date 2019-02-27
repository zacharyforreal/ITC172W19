from django.test import TestCase
from .models import Meeting, MeetingMinutes
from .forms import MeetingForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='March Meeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingDateTest(TestCase):
    def test_stringOutput(self):
        meetingday=MeetingDate(meetingtime='Meeting')
        self.assertEqual(str(meetingday), meetingday.meetingtime)

    def test_tablename(self):
        self.assertEqual(str(TechType._meta.db_table), 'meetingdate')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(reviewtitle='March Meeting')
        self.assertEqual(str(resource), resource.reviewtitle)

    def test_tablename(self):
self.assertEqual(str(Resource._meta.db_table), 'resource')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/index.html')

class TestGetMeeting(TestCase):


    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/meetings')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getmeetings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/meetings.html')

class New_Product_Form_Test(TestCase):

    # Valid Form Data
    def test_meetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle': "Music study", 'meetingday': "15th", 'user': "zack", 'entrydate': "2018-12-17", 'meetingURL':"http:microsoft.com", 'meetingdescription':"lightweight laptop" })
        self.assertTrue(form.is_valid())

    # Invalid Form Data
    def test_UserForm_invalid(self):
        form = ProductForm(data={'meetingtitle': "Music study", 'meetingday': "15th", 'user': "zack", 'entrydate': "2018-12-17", 'meetingURL':"http:microsoft.com", 'meetingdescription':"lightweight laptop" })
self.assertFalse(form.is_valid())
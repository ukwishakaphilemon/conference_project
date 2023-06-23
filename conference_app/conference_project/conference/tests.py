from django.test import TestCase
from django.urls import reverse
from .models import Conference

class ConferenceTestCase(TestCase):
    def setUp(self):
        Conference.objects.create(name='Conference 1', dates='2023-07-10 - 2023-07-12', location='City A' topic= 'vote' description = 'voting committe')
  def test_conf_list_view(self):
        url = reverse('conference_list')
        response = self.client.get(url)
        self.assertContains(response, 'Conference 1')

    def test_conf_details_view(self):
        conference = Conference.objects.get(name='Conference 1')
        url = reverse('conference_details', args=[conference.id])
        response = self.client.get(url)
        self.assertContains(response, 'Conference 1')

    def test_conference_create_view(self):
            url = reverse('conference_create')
            response = self.client.get(url)

        def test_conference_update_view(self):
            conference = Conference.objects.get(name='Conference 1')
            url = reverse('conference_update', args=[conference.id])
            response = self.client.get(url)

        def test_conference_delete_view(self):
            conference = Conference.objects.get(name='Conference 1')
            url = reverse('conference_delete', args=[conference.id])
            response = self.client.get(url)

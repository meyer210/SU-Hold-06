from .models import Project
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.test.utils import setup_test_environment
from django.test import Client
from django.core.urlresolvers import reverse
# Create your tests here.

class ProjectTestCase(TestCase):
    def setUp(self):
        u = User.objects.create_user('John','john@john.dk','hello,world')
        u.save()
        Project.objects.create(title="Project 1", description="introduction to the project subject 1",
                               author=User.objects.get(username='John'), pub_date=timezone.now())
        Project.objects.create(title="Project 2", description="introduction to the project subject 2",
                               author=User.objects.get(username='John'), pub_date=timezone.now())
    def test_correct_title(self):
        """
        Testing:
        attribute:
            -title
        Excpected Result: True
        """
        project1 = Project.objects.get(title="Project 1")
        project2 = Project.objects.get(title="Project 2")
        self.assertEqual(project1.title, 'Project 1')
        self.assertEqual(project2.title, "Project 2")
    def test_correct_desc(self):
        """
        Testing:
        attribute:
            -description
        Excpected Result: True
        """
        project1 = Project.objects.get(title="Project 1")
        project2 = Project.objects.get(title="Project 2")
        self.assertEqual(project1.description, "introduction to the project subject 1")
        self.assertEqual(project2.description, "introduction to the project subject 2")
    def test_correct_author(self):
        """
        Testing:
        attribute:
            -author
        Excpected Result: True
        """
        project1 = Project.objects.get(title="Project 1")
        project2 = Project.objects.get(title="Project 2")
        self.assertEqual(project1.author, User.objects.get(username='John'))
        self.assertEqual(project2.author, User.objects.get(username='John'))
    def test_correct_pub_date(self):
        """
        Testing:
        attribute:
            -pub_date
        Excpected Result: True
        """
        now = timezone.now()
        project1 = Project.objects.get(title="Project 1")
        project2 = Project.objects.get(title="Project 2")
        project1.pub_date = now
        project2.pub_date = now
        self.assertEqual(project1.pub_date, now)
        self.assertEqual(project2.pub_date, now)

class viewTestCast(TestCase):
    def setUp(self):
        u = User.objects.create_user('John', 'john@john.dk', 'hello,world')
        u.save()
        Project.objects.create(title="Project 1", description="introduction to the project subject 1",
                               author=User.objects.get(username='John'), pub_date=timezone.now())
        Project.objects.create(title="Project 2", description="introduction to the project subject 2",
                               author=User.objects.get(username='John'), pub_date=timezone.now())
        def test_
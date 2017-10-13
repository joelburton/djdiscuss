from django.test import TestCase

from discuss.models import Discussion
from pets.models import Cat


class DiscussionModelTest(TestCase):
    """Tests for discussion threads."""

    def test_basic(self):
        """Basic tests."""

        auden = Cat(name="Auden")

        t = Discussion(content=auden)

        self.assertEqual(str(t), "Discussion {id} on Auden".format(id=t.id))

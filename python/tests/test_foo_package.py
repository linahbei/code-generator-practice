from ast import Assert
import unittest
import unittest
from src.foo import Foo


class TestFooPackage(unittest.TestCase):
    def test_say_agine(self):
        say_something = 'bar'
        say_something_again = f"{Foo.SAY_AGAINE_PREFIX}{say_something}"
        self.assertEqual(say_something_again,
                         Foo.sayAgain(say_something))

    def test_can_not_say_agine(self):
        say_something_wrong = ['bar']
        self.assertRaises(TypeError,
                          Foo.sayAgain, say_something_wrong)

"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math

# TODO write 3 tests as described above


class TestCircle(unittest.TestCase):
    """Unit tests for Circle class."""

    def setUp(self):
        """Create a circle with radius 2."""
        self.c1 = Circle(2)

    def test_add_area_two_positive_circles_radius(self):
        """Test add_area with two circle having positive radius."""
        c2 = Circle(3)
        c3 = self.c1.add_area(c2)

        expected_radius = 3
        expected_area = math.pi * expected_radius ** 2
        # Check that the radius and area of the new circle are as expected.
        self.assertAlmostEqual(c3.get_radius(), expected_radius)
        self.assertAlmostEqual(c3.get_area(), expected_area)

    def test_add_area_one_circle_radius_is_zero(self):
        """Test add_area with one circle having radius 0."""
        c2 = Circle(0)
        self.assertEqual(c3.get_radius(), 2)
        # Check that the radius is 2.
        c3 = self.c1.add_area(c2)
        # Check that the area is as expected.
        self.assertEqual(c3.get_area(), math.pi * self.c1.get_radius() ** 2)

    def test_constructor_negative_radius(self):
        """Test that constructor raises exception for negative radius."""
        with self.assertRaises(ValueError):
            c = Circle(-1)


if __name__ == '__main__':
    unittest.main()

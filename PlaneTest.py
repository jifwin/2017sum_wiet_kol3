import unittest
# import unittest.mock as mock

from Plane import Plane


class PlaneTest(unittest.TestCase):
    def test_should_sth(self):
        plane = Plane(plane_orientation=15, turbulence_gauss_mean=5, turbulence_gauss_sigma=20)

        def mocked_random_gauss(ignored1, ignored2):
            return 5

        with mock.patch('random.gauss'):
            plane.process()

        self.assertTrue(True)

    def test_should_count_number_of_steps(self):
        plane = Plane()
        number_of_steps = 100
        for i in xrange(number_of_steps):
            plane.process()

        self.assertEqual(plane.NofStep, number_of_steps+1)

if __name__ == '__main__':
    unittest.main()

import unittest

import mock

from Plane import Plane


class PlaneTest(unittest.TestCase):
    def test_should_apply_correction(self):
        plane = Plane(plane_orientation=15, turbulence_gauss_mean=5, turbulence_gauss_sigma=20)

        mocked_random_gauss = 5

        def get_mocked_random_gauss(ignored1, ignored2):
            return mocked_random_gauss

        initial_orientation = plane.plane_orientation
        with mock.patch('random.gauss', get_mocked_random_gauss):
            plane.process()

        self.assertEquals(plane.plane_orientation, initial_orientation + mocked_random_gauss)

    def test_should_count_number_of_steps(self):
        plane = Plane()
        number_of_steps = 100
        for i in xrange(number_of_steps):
            plane.process()

        self.assertEqual(plane.NofStep, number_of_steps+1)

if __name__ == '__main__':
    unittest.main()

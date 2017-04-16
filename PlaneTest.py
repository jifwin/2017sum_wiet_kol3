import unittest

import mock
from Plane import Plane


class PlaneTest(unittest.TestCase):
    def test_should_use_default_values_not_specified(self):
        # given
        plane = Plane()

        # when

        # then
        self.assertTrue(isinstance(plane.plane_orientation, int))
        self.assertTrue(isinstance(plane.turbulence_gauss_mean, int))
        self.assertTrue(isinstance(plane.turbulence_gauss_sigma, int))

    def test_should_apply_correction(self):
        # given
        plane = Plane(plane_orientation=15, turbulence_gauss_mean=5, turbulence_gauss_sigma=20)

        mocked_random_gauss = 5
        mocked_correction = -7

        def get_mocked_random_gauss(ignored1, ignored2):
            return mocked_random_gauss

        initial_orientation = plane.plane_orientation

        # when
        with mock.patch('random.gauss', get_mocked_random_gauss):
            plane.get_correction = lambda x: mocked_correction
            plane.process()

        # then
        self.assertEquals(plane.plane_orientation, initial_orientation + mocked_random_gauss + mocked_correction)

    def test_should_count_number_of_steps(self):
        # given
        plane = Plane()
        number_of_steps = 100

        # when
        for i in xrange(number_of_steps):
            plane.process()

        # then
        self.assertEqual(plane.NofStep, number_of_steps + 1)

    def test_should_use_opposite_direction_for_given_orientation(self):
        # given
        plane = Plane()
        orientation = 10

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertLess(correction, 0)

    # todo: exact value

    def test_should_not_exceed_max_in_correction(self):
        # given
        plane = Plane()
        orientation = 50

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertEqual(correction, -plane.const_maxTiltCorrectionDegree)


if __name__ == '__main__':
    unittest.main()

# todo: 12 tests

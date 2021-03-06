import unittest

import mock

from Plane import Plane
from StringIO import StringIO


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

    def test_should_use_opposite_direction_for_given_small_orientation(self):
        # given
        plane = Plane()
        orientation = 10

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertLess(correction, 0)

    def test_should_use_opposite_direction_for_given_large_orientation(self):
        # given
        plane = Plane()
        orientation = 50

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertLess(correction, 0)

    def test_should_use_opposite_value_of_orientation_for_correction(self):
        # given
        plane = Plane()
        orientation = 5

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertEqual(correction, -orientation)

    def test_should_not_exceed_max_in_correction(self):
        # given
        plane = Plane()
        orientation = 50

        # when
        correction = plane.get_correction(orientation)

        # then
        self.assertEqual(correction, -plane.const_maxTiltCorrectionDegree)

    def test_should_return_to_balance_in_one_step_for_small_orientation(self):
        # given
        plane = Plane()
        plane.plane_orientation = 5

        mocked_random_gauss = 0

        def get_mocked_random_gauss(ignored1, ignored2):
            return mocked_random_gauss

        # when
        with mock.patch('random.gauss', get_mocked_random_gauss):
            plane.process()

        # then
        self.assertEqual(plane.plane_orientation, 0)

    def test_should_return_to_balance_in_two_steps_for_large_orientation(self):
        # given
        plane = Plane()
        plane.plane_orientation = 18

        mocked_random_gauss = 0

        def get_mocked_random_gauss(ignored1, ignored2):
            return mocked_random_gauss

        # when
        with mock.patch('random.gauss', get_mocked_random_gauss):
            plane.process()
            plane.process()

        # then
        self.assertEqual(plane.plane_orientation, 0)

    def test_should_work_for_multiple_steps(self):
        # given
        plane = Plane()

        # when
        for i in xrange(100):
            plane.process()

        # then
        # no exceptions

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_should_print_each_step_on_stdout(self, stdout):
        # given
        plane = Plane()
        number_of_steps = 10

        # when
        for i in xrange(number_of_steps):
            plane.process()

        # then
        self.assertEqual(stdout.getvalue().count("Step Number"), number_of_steps)

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_should_print_orientation_with_turbulance(self, stdout):
        # given
        plane = Plane()
        initial_orientation = plane.plane_orientation

        mocked_random_gauss = 2.5

        def get_mocked_random_gauss(ignored1, ignored2):
            return mocked_random_gauss

        # when
        with mock.patch('random.gauss', get_mocked_random_gauss):
            plane.process()

        # then
        getvalue = stdout.getvalue()
        self.assertTrue(str(initial_orientation+mocked_random_gauss) in getvalue)

    @mock.patch('sys.stdout', new_callable=StringIO)
    def test_should_print_corrected_orientation(self, stdout):
        # given
        plane = Plane()

        # when
        plane.process()

        # then
        self.assertTrue(str(plane.plane_orientation) in stdout.getvalue())


if __name__ == '__main__':
    unittest.main()


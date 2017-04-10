#source_github_username NikliborcBartek
import random


class Plane(object):

    const_maxTiltCorrectionDegree = 10
    NofStep = 1

    def __init__(self, plane_orientation=15, turbulence_gauss_mean=5, turbulence_gauss_sigma=20):
        self.plane_orientation = plane_orientation
        self.turbulence_gauss_mean = turbulence_gauss_mean
        self.turbulence_gauss_sigma = turbulence_gauss_sigma

    def process(self):
            print "----Step Number {}".format(self.NofStep)
            turbulence = random.gauss(self.turbulence_gauss_mean, self.turbulence_gauss_mean)
            print "turbulence {}".format(turbulence)
            self.plane_orientation += turbulence
            print "plane_orientation {}".format(self.plane_orientation)
            correction = self.get_correction(self.plane_orientation)
            print "correction {}".format(correction)
            self.plane_orientation += correction
            print "corrected plane orientation {}".format(self.plane_orientation)
            self.NofStep += 1
            return None

    def get_correction(self, orientation):
        if orientation > self.const_maxTiltCorrectionDegree:
            return -self.const_maxTiltCorrectionDegree
        elif orientation < -self.const_maxTiltCorrectionDegree:
            return self.const_maxTiltCorrectionDegree
        else:
            return -orientation

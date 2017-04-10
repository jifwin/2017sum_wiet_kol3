#source_github_username NikliborcBartek
import argparse
from Plane import Plane


class PlaneSimulation(object):

    def __init__(self,plane_orientation, turbulence_gauss_mean, turbulence_gauss_sigma):
        self.firstPanel = Plane(plane_orientation, turbulence_gauss_mean, turbulence_gauss_sigma)
        self.iter = iter(self.default_gen())

    @staticmethod
    def default_gen():
        while True:
            yield 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--plane_orientation", nargs='?', type=int, default=15,
                        help="Initial value of plane orientation position")
    parser.add_argument("--turbulence_gauss_mean", nargs='?', type=int, default=5,
                        help="turbulence gauss mean value ")
    parser.add_argument("--turbulence_gauss_sigma", nargs='?', type=int, default=20,
                        help="turbulence gauss sigma value")
    args = parser.parse_args()
    print args.plane_orientation
    simulation = PlaneSimulation(args.plane_orientation, args.turbulence_gauss_mean, args.turbulence_gauss_sigma)

    while simulation.iter.next:
        simulation.firstPanel.process()

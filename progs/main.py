#import all the other files below
from shared_data import m_PShared
from plot import  plot_orbit

def main():
    # plot_orbit.get_all_graphs()
    plot_orbit.plot_specific_orbit("PRN 20", "Animation")

if __name__ == "__main__":
    main()
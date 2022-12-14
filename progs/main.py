#import all the other files below
from shared_data import m_PShared
from plot import  plot_orbit

def main():
    
    print("Satellite Orbit Predictor\n")
    #call the other methods
    multiple_tle_data_dic = m_PShared.get_gps_sats()
    orbit_key=multiple_tle_data_dic.keys()
    
    # key is satellite ID to plot (eg. PRN 13)
    for key in orbit_key:
        plot_orbit.plot_specific_orbit(key, "Animation") #graphType = Animation, 3d, GroundTracks
        plot_orbit.plot_specific_orbit(key, "3d") #graphType = Animation, 3d, GroundTracks
        plot_orbit.plot_specific_orbit(key, "GroundTracks") #graphType = Animation, 3d, GroundTracks
#####################################################        
        break # Remove the break for all satellites #
#####################################################

if __name__ == "__main__":
    main()
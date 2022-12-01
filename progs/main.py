#import all the other files below
from shared_data import m_PShared

def main():
    gps_sats = m_PShared.get_gps_sats()
    print("Satellite Orbit Predictor\n")
    #call the other methods


if __name__ == "__main__":
    main()
from tle_processor import process_multiple_TLEs
from datetime import datetime
from time import gmtime, strftime
from sgp4.api import jday
from sgp4.api import Satrec
from sgp4.api import SGP4_ERRORS
class m_PShared:
#
# This class hold together some variables and functions used across the code.
# These functions can be accessesed by multiple files acrosss the code base
#   
    def get_gps_sats():
        # Input: void
        # Output: GPS satellites dictionary
        # Each element in the dictionary has a key associated with satellite code name
        # For example key PRN 13 will return an arrya of two. each index is one line of two line string for that satellite
        multiFileProcessor = process_multiple_TLEs()
        gps_sats = multiFileProcessor.load_TLE("deps/GPS.TLE")
        return gps_sats
    
    def get_current_time():
        # Input: void
        # Output: returns current time as seperate elements.
        yyyy = strftime("%Y", gmtime())
        mm = strftime("%m", gmtime())
        dd = strftime("%d", gmtime())
        hh = strftime("%H", gmtime())
        MM = strftime("%M", gmtime())
        ss = strftime("%S", gmtime())

        return yyyy, mm, dd, hh, MM ,ss

    def get_jday_from_date(yyyy, mm, dd, hh, MM ,ss):
        # Input: Date and time in the specifed format
        # Output: Julian day and fraction
        jd, fr = jday(yyyy, mm, dd, hh, MM, ss)
        return jd, fr

    def make_starec_obj_from_tle(line1, line2):
        # Input: TLE string line1 and line 2
        # Output: Starec object
        satellite = Satrec.twoline2rv(line1, line2)
        return satellite
    
    def define_error_code(error_code):
        return SGP4_ERRORS.get(error_code)
            


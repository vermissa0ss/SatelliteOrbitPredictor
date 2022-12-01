from shared_data import m_PShared

class propagate_SGP4:

    def propagate_from_dic(multiple_tle_data_dic, jday, fraction):
        # Input: 
        # multiple_tle_data_dic = dictionary of satellite IDs and their TLE lines
        # jday = Julian day
        # fraction = fraction of julian day
        #
        # Output: 
        # dictionary of the satellite ID and their corresponding position(x,y,z) and velocity(x,y,z)
        dic_satID_pos_vel={}
        
        for satID, tle_line in multiple_tle_data_dic.items():
            
            tle_line_1 = tle_line[0]
            tle_line_2 = tle_line[1]
            
            m_sat = m_PShared.make_starec_obj_from_tle(tle_line_1, tle_line_2)
            error, r_xyz, v_xyz = m_sat.sgp4(jday, fraction)
            
            if (error == 0):
                dic_satID_pos_vel[satID] = [r_xyz, v_xyz]
            else:
                return m_PShared.define_error_code(error)
        
        return dic_satID_pos_vel
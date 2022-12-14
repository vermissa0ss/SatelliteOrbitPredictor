import plotly.express as px
import plotly.graph_objects as go
import plotly.io as io
from shared_data import m_PShared
from porpagate_sgp4 import propagate_SGP4
from skyfield.api import Distance, load, wgs84
from skyfield.positionlib import Geocentric
import numpy as np
import pandas as pd
from pathlib import Path

class plot_orbit:
    """
    This class has one attribute: plot_specific_orbit, in which plots the a 
    satellite's orbit given the satellite id'
    """
    def plot_specific_orbit(orbit_id ,graphType = 'Animation'):
        """
        plot_specific_orbit(orbit_id) plots the specified satellite's orbit ffrom
        the current time to 12 hours. 
        input: orbit_id: The ID of the orbit from tle file
        output: interactive plot plotted the orbit for 12 hours. 
        """
       
        # Get satellite data from tle
        multiple_tle_data_dic = m_PShared.get_gps_sats()
        lat = []; lon = [];
        orbit_key=multiple_tle_data_dic.keys()

        # Define time sequence for an hours
        t_array = np.linspace(0,12,31)
        new_plot_data={"orbit_id":[],"timeFrame":[],"latitude":[],"longitude":[] }

        for orbit in orbit_key:
            lat = []; lon = [];
            
            for time in t_array:

                # Get current date and time and convert to jday and fraction
                yyyy, mm, dd, hh, MM ,ss = m_PShared.get_current_time()
                jday, fraction = m_PShared.get_jday_from_date(float(yyyy), float(mm), float(dd), float(hh)+time, float(MM) ,float(ss))

                # Solve for position and velocity using propagate orbit
                dic_satID_pos_vel = propagate_SGP4.propagate_from_dic(multiple_tle_data_dic, jday, fraction)

                # Convert to lla coordinates using skyfield module
                ts = load.timescale()
                t = ts.now()
                d = Distance(m=[dic_satID_pos_vel[orbit_id][0][0], dic_satID_pos_vel[orbit_id][0][1], dic_satID_pos_vel[orbit_id][0][2]])
                p = Geocentric(d.km, t=t)
                g = wgs84.subpoint(p)

                lat.append(g.latitude.degrees)
                lon.append(g.longitude.degrees)
            new_plot_data["orbit_id"].append(orbit_id)
            new_plot_data["timeFrame"].append(t_array)
            new_plot_data["latitude"].append(lat)
            new_plot_data["longitude"].append(lon)
            
            
        df=pd.DataFrame.from_dict(new_plot_data)
        df.drop('timeFrame', inplace=True, axis=1)
        
        lat  = []
        long = []
#         orbit_key = []
        
        for i in df.latitude.iloc[1]:
            lat.append(i)
            
        for i in df.longitude.iloc[1]:
            long.append(i)
        
        
        df2 = pd.DataFrame(lat)
        
        df3 = pd.DataFrame(long)
        
        df3_1 = pd.DataFrame(orbit_key)
        
        
        df4_1 = pd.concat([df2, df3], axis=1)
        df4 = pd.concat([df4_1, df["orbit_id"]], axis=1)
        
        if(graphType == "GroundTracks"):
            # Ground tracks
            fig = px.line_geo(df4, lat=df4.iloc[:, 0],lon=df4.iloc[:, 1], hover_name= df4.iloc[:, 2], title=orbit_id)
        
        elif(graphType == "Animation"):
            # Scater Animation
            fig = px.line_geo(df4, lat=df4.iloc[:, 0],lon=df4.iloc[:, 1], animation_frame=t_array, markers=True, hover_name= df4.iloc[:, 2], title=orbit_id)
            #Put you own path here
            pwd = Path.cwd()
            fig.write_html(str(pwd)+"/"+orbit_id+".html")
        
        elif(graphType == "3d"):            
            #Projection 3D    
            fig = px.scatter_geo(lon = df4.iloc[:, 1], lat = df4.iloc[:, 0], projection="orthographic", hover_name= df4.iloc[:, 2], title=orbit_id) #3D globe with data points
        
       
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
       
        
        
        fig.show()
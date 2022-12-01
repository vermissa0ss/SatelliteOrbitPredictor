class process_multiple_TLEs:


    def load_TLE(self, TLE_file):
        # Input: TLE file location
        # Output: Dictionary of multiple satellites with 2line elements as values

        print('Reading TLE file ', TLE_file)
        txtFile = open(TLE_file).read() #read file
        loaded_lines = txtFile.split("\n") #split at every new line
        
        # basic TLE format for each satellite consists of three lines.
        # Line1 = GPS satellite code ID or name known as PRN
        # Line 2 = line number 1
        # Line 3 = line number 2 
        #Create a dictionary made of only PRN code as key ([-7:-1]). and keep the next two lines as its values
        dic_satellites_twoLine = { loaded_lines[i][-7:-1] : [loaded_lines[i+1], loaded_lines[i+2]] for i in range(0, len(loaded_lines),3 ) }
        return dic_satellites_twoLine

    def print_TLE_object(self, TLE_Object):
        # Input: TLE file Object of Satrec type 
        # Output: standard output of the content of the tle as orbital parameters
        
        from sys import stdout
        from sgp4.conveniences import dump_satrec

        orbital_elements_print = stdout.writelines(dump_satrec(TLE_Object))
        return orbital_elements_print

    
    def create_sat_object_from_TLE(self, Line1, Line2):
        # Input:
        # Line1 = First line of TLE FILE as a string with seperated with white spaces
        # Line2 = Second line of TLE FILE as a string with seperated with white spaces
        # Output: satellite object of type stardec. ready to be used in SGP4 propagation
        
        from sgp4.api import Satrec

        satellite = Satrec.twoline2rv(Line1, Line2)
        return satellite

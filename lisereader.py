import numpy as np
import amedata
from re import sub 

# =================== class =====================
class LISEreader:
    def __init__(self,filename):

        ame=amedata.AMEData()
        ame.init_ame_db
        self.ame_data=ame.ame_table

        self._read(filename)

    def __str__(self):
        print("You have been blessed by Nikos and The Three Greeks")

    def _read(self,filename):
        with open(filename) as f:
            lines=f.readlines()
    
        for (i, line) in enumerate(lines):
            if "[Calculations]" in line:
                file_start = i+1
            # else:
            #     raise #....

        self.data=[line.replace('+','').split()[0:6] + line.replace('=','').split()[7].split(',') 
        for line in lines[file_start:]]

    def get_index(self,name):
        return [i for i, element in enumerate(self.data) if name in element][0]

    def get_info(self,name):
        # retrieves charge state and cross section from lise data
        index       = self.get_index(name)
        from_lise   = [int(self.data[index][5]),float(self.data[index][6])]

        # retrieves name, A, Z, N from ame data
        element     = sub("[0-9]",'',name)
        mass_number = int(sub("[^0-9]",'',name))
        from_ame    = [[self.ame_data[i][6], self.ame_data[i][5], self.ame_data[i][4], self.ame_data[i][3]]
        for i,line in enumerate(self.ame_data) if (element in line and mass_number==line[5])][0]

        if bool(from_lise)==True:
            return from_ame + from_lise
        else:
            return "check search format (e.g. \"80Kr\" )"
            # or raise

    def get_lise_all(self):
        data=np.array(self.data)
        return np.transpose([data[:,0], data[:,5], data[:,6]])

    def get_info_all(self):
        return [self.get_info(line[0]) for line in self.data]

# ================== testing =====================
filename="data/E143_TEline-ESR-72Ge.lpp"
lise_data=LISEreader(filename)

def test1():
    print(lise_data.get_lise_all()[0])
    print(lise_data.get_info("80Kr"))
    print(lise_data.get_info_all()[:5])

if __name__ == "__main__":
    try:
        test1()
    except:
        raise

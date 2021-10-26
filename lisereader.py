import numpy as np
import re

# =================== class =====================
class LISEreader:
    def __init__(self,filename):
        self._read(filename)

    def __str__(self):
        print("You have been blessed by Nikos and The Three Greeks")

    def _read(self,filename):
        with open(filename) as f:
            # for (i, line) in enumerate(f):
            #     if "[Calculations]" in line:
            #         file_start = i+1
            #     # else:
            #     #     raise #....

            # lines=f.readlines()[file_start:]
            lines=f.readlines()[988:]

        self.data=[line.split()[0:6] + line.replace('=','').split()[7].split(',') for line in lines]

    def get_info(self,name):
        l=[match for match in self.data if name in match][0]
        return l[0], l[5], l[6]

    def get_info_all(self):
        data=np.array(self.data)
        return np.transpose(np.array([data[:,0], data[:,5], data[:,6]]))

    def find_index(self,name):
        return [match for match in self.data if name in match][0]

# ================== testing =====================

filename="data/E143_TEline-ESR-72Ge.lpp"

if __name__ == "__main__":
    try:
        lise_data=LISEreader(filename)
        print(lise_data.get_info("77Br"))
        mydata=lise_data.get_info_all()
        print(mydata[3])
    except:
        raise

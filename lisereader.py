import numpy as np
import amedata
from re import sub

# =================== class =====================

class LISEreader:
    def __init__(self, filename):

        ame = amedata.AMEData()
        ame.init_ame_db
        self.ame_data = ame.ame_table
        self._read(filename)

    def _read(self, filename):
        with open(filename) as f:
            lines = f.readlines()

        for (i, line) in enumerate(lines):
            if '[Calculations]' in line:
                file_start = i+1
            # else:
            #     raise #....

        self.data = [line.replace('+', '').split()[0:6] + line.replace('=', '').split()[7].split(',')
                     for line in lines[file_start:]]

    def get_index(self, name):
        try:
            return [i for i, element in enumerate(self.data) if name in element][0]
        except:
            raise ValueError(
                'get_index() search argument returned nothing. Check formatting (e.g. \"80Kr\")')

    def get_info(self, name):
        # retrieves charge state and yield from lise data
        index = self.get_index(name)
        from_lise = [int(self.data[index][5]), float(self.data[index][6])]

        # retrieves name, A, Z, N from ame data
        element = sub('[0-9]', '', name)
        mass_number = int(sub('[^0-9]', '', name))
        from_ame = [[self.ame_data[i][6], self.ame_data[i][5], self.ame_data[i][4], self.ame_data[i][3]]
                    for i, line in enumerate(self.ame_data) if (element in line and mass_number == line[5])][0]

        try:
            return from_ame + from_lise    
        except:
            raise ValueError(
                'get_info() search argument returned nothing. Check formatting (e.g. \"80Kr\"')

    def get_lise_all(self):
        data = np.array(self.data)
        return np.transpose([data[:, 0], data[:, 5], data[:, 6]])

    def get_info_all(self):
        return [self.get_info(line[0]) for line in self.data]
    
    def get_info_specific(self,param_index_list):
        data=[]
        for line in self.data:
            line_data=[]
            for i in param_index_list:
                line_data.append(LISEreader.float_check(line[i]))
            data.append(line_data)
        return data
    
    @staticmethod
    def float_check(value):
        if value.replace('.','').replace('e-','').replace('e+','').isdigit():
            return float(value)
        else:
            return value
        
# ================== testing =====================

filename = 'test/E143_TEline-ESR-72Ge.lpp'  
lise_data = LISEreader(filename)

def test1():
    print(f"get_info(\'80Kr\'): {lise_data.get_info('80Kr')}")
    print(f'get_info_all() snippet: {lise_data.get_info_all()[5:8]}')
    
def test2():
    print(f'get_info_specific([0,1,10]) snippet: {lise_data.get_info_specific([0,1,10])[5:8]}')

if __name__ == '__main__':
    try:
        test1()
        test2()
    except:
        raise

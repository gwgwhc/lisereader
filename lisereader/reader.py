import numpy as np
from barion.amedata import *
from re import sub


class LISEreader:
    def __init__(self, filename):
        ame = AMEData()
        ame.init_ame_db
        self.ame_data = ame.ame_table
        self._read(filename)

    def _read(self, filename):
        with open(filename,encoding='latin1') as f:
            lines = f.readlines()

        for (i, line) in enumerate(lines):
            if '[Calculations]' in line:
                file_start = i+1
    
        # finds point in line where separator changes from space to comma
        self.centre_index = len(lines[file_start].split()) - 1

        # splits lines and adds to list of all data
        self.data = [line.replace('+', '').split()[0:self.centre_index] 
                     + line.replace('=', '').split()[self.centre_index].split(',')
                     for line in lines[file_start:]]

    def get_index(self, name):
        returned_queries = []
        for i, element in enumerate(self.data):
            if element[0] + '+' + element[1] == name:
                returned_queries.append(i)
            elif element[0] + element[1] + '+' == name:
                returned_queries.append(i)
                
        if len(returned_queries) == 1:
            return returned_queries[0]
        
        elif len(returned_queries) > 1:
            print('get_index() returned multiple queries, returning first')
            return returned_queries[0]
        
        else:
            print(element[0] + element[1] + '+')
            raise ValueError('get_index() returned nothing. Check formatting (e.g. \"80Kr35+\")')

    def get_info(self, name):
        # retrieves charge state and yield from lise data
        index = self.get_index(name)
        from_lise = [list(map(int, self.data[index][1:self.centre_index])),
                     float(self.data[index][self.centre_index])]
        # retrieves name, A, Z, N from ame data
        element = sub('[^a-zA-Z]', '', name)
        aux= sub('[a-zA-Z]', '', name)
        for i, char in enumerate(aux):
            if char == '+': aux2=i
        mass_number = int(aux[:aux2])
        from_ame = [[self.ame_data[i][6], self.ame_data[i][5], self.ame_data[i][4], self.ame_data[i][3]]
                    for i, line in enumerate(self.ame_data) if (element in line and mass_number == line[5])][0]

        # checks if returning empty list
        try:
            return from_ame + from_lise    
        except:
            raise ValueError(
                'get_info() search argument returned nothing. Check formatting (e.g. \"80Kr\"')

    def get_lise_all(self):
        data = np.array(self.data)
        return np.transpose([data[:, 0], data[:, 5], data[:, 6]])

    def get_info_all(self):
        return [self.get_info(line[0]+'+'+line[1]) for line in self.data]
    
    def get_info_specific(self,param_index_list):
        return_list = [[LISEreader.float_check(line[i]) for i in param_index_list]
                       for line in self.data]
        return return_list

    def get_yield_sorted(self):
        name_yield = [[str(line[0]) + '+' + str(line[1]), LISEreader.float_check(line[7])] for line in self.data]
        sorted_by_yield = sorted(name_yield, key=lambda x: x[1])[::-1]
        return sorted_by_yield
        
    @staticmethod
    def float_check(value): #returns float if not string
        if value.replace('.','').replace('e-','').replace('e+','').isdigit():
            return float(value)
        else:
            return value
        
# ================== testing =====================

def test1():
    print(f"get_info(\'80Kr\'): {lise_data.get_info('80Kr')}")
    
def test2():
    print(f'get_info_all() snippet[:3]: {lise_data.get_info_all()[:3]}')
    
def test3():
    print(f"get_info_specific([0,1,10]) snippet[:3]: {lise_data.get_info_specific([0,1,10])[:3]}")

if __name__ == '__main__':
    filename = 'E143_TEline-ESR-72Ge.lpp'
    lise_data = LISEreader(filename)
    try:
        test1()
        test2()
        test3()
    except:
        raise

# =================== class =====================
class LISEreader:
    def __init__(self,filename):
        self._read(filename)

    def _read(self,filename):
        with open(filename) as f:
            lines=f.readlines()[988:]

        self.data=[line.split()[0:6] + line.replace('=','').split()[7].split(',') for line in lines]
        
        # lise_range=len(lines)
        # for i in range(lise_range):
        # for guy in splitlines:    
        #     if 
        #     float(splitlines[i][7].split(",")[0]    
        #     .replace("=",''))                #cross section

    def __str__(self):
        print("You have been blessed by Nikos and The Three Greeks")

    # def split
    # def search
    # def 
    def find_index(data,name):
        return [match for match in data if name in match][0]

# ================== testing =====================

filename="data/E143_TEline-ESR-72Ge.lpp"

def test_find_index():
    alldata=LISEreader(filename)
    # print(lisereader.find_index(alldata,"80Kr",True))
    print(alldata.find_index(alldata,"78Br"))

if __name__ == "__main__":
    try:
        lise_data=LISEreader(filename)
        print(lise_data.data[0])
    except:
        pass
    
    # except FileNotFoundError:
        # print("File was not found, please enter a valid path.")
    #     filename=input()
    #     test_read(filename)
    # else:
    #     print("read ok.")

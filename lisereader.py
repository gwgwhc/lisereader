# =================== class =====================
class LISEreader:
    def __init__(self,filename):
        self._read(filename)

    def __str__(self):
        print("You have been blessed by Nikos and The Three Greeks")

    def _read(self,filename):
        with open(filename) as f:
            lines=f.readlines()[988:]

        self.data=[line.split()[0:6] + line.replace('=','').split()[7].split(',') for line in lines]

    # def split
    # def search
    # def ...

    def find_index(self,name):
        return [match for match in self.data if name in match][0]

# ================== testing =====================

filename="data/E143_TEline-ESR-72Ge.lpp"

if __name__ == "__main__":
    try:
        lise_data=LISEreader(filename)
        print(lise_data.find_index("77Br"))
    except:
        pass
    
    # except FileNotFoundError:
        # print("File was not found, please enter a valid path.")
    #     filename=input()
    #     test_read(filename)
    # else:
    #     print("read ok.")

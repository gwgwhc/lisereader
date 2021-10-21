# =================== class =====================
class lisereader:
    def __init__(self):
        pass

    def read(data_filename):

        with open(data_filename) as f:
            lines=f.readlines()[988:]
            lise_range=len(lines) #to pass to next loop
            splitlines=[line.split() for line in lines]
            
        alldata=[]
        for i in range(lise_range):
            alldata.append([splitlines[i][0],       #name
            splitlines[i][6],                       #charge
            float(splitlines[i][7].split(",")[0]    
            .replace("=",''))])                     #cross section

        return alldata

    # def find_index(name):

# ================== testing =====================

filename="data/E143_TEline-ESR-72Ge.lpp"

def test_read(filename):
    testoutput=lisereader.read(filename)
    print(f"""\
-----------------------------------------------
The lise file will be read and formatted into a
list of strings containing the particle name,
proton number and cross section. Example below.
-----------------------------------------------
The first index is: {testoutput[0]}
-----------------------------------------------""")

if __name__ == "__main__":
    try:
        test_read(filename)
    except FileNotFoundError:
        print("File was not found, please enter a valid path.")
        filename=input()
        test_read(filename)
    except:
        print("Something went wrong!")
    else:
        print("read ok.")
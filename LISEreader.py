class LISEreader:
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

import csv, xlrd

# We counted most used techniques for each tactic from APTS only for the following 5 tactics for conference paper purposes.
# This can be utilized for every tactic.

def add_techniques_count(list):
    # count apts per technique
    with open('test.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        j = 0
        for row in spamreader:
            if j != 0 and j != 2361:
                try:
                    technique = row[4]
                    try:
                        list[technique] = list[technique] + 1
                    except Exception:
                        continue
                except Exception:
                    continue
            j = j + 1



# get techniques per tactic
initial_access={}
persistence={}
execution={}
c2={}
reconnaissance={}
book=xlrd.open_workbook("tak.xls")
sh = book.sheet_by_index(0)
for rx in range(sh.nrows):
    if sh.cell_value(rowx=int(rx),colx=7).find("Initial Access")!=-1:
        data = sh.cell_value(rowx=rx, colx=0)
        initial_access[str(data)]=0
    if sh.cell_value(rowx=int(rx),colx=7).find("Persistence")!=-1:
        data = sh.cell_value(rowx=rx, colx=0)
        persistence[str(data)]=0
    if sh.cell_value(rowx=int(rx),colx=7).find("Reconnaissance")!=-1:
        data = sh.cell_value(rowx=rx, colx=0)
        reconnaissance[str(data)]=0
    if sh.cell_value(rowx=int(rx),colx=7).find("Command And Control")!=-1:
        data = sh.cell_value(rowx=rx, colx=0)
        c2[str(data)]=0
    if sh.cell_value(rowx=int(rx),colx=7).find("Execution")!=-1:
        data=sh.cell_value(rowx=rx,colx=0)
        execution[str(data)]=0

# count apts
apts=[]
with open('test.csv') as csvfile:
    spamreader=csv.reader(csvfile)
    i=0
    for row in spamreader:
        try:
            if i!=0 and i!=2361:
                group=row[1]
                if group not in apts:
                    apts.append(group)
            i=i+1
        except Exception:
            continue
    apts.pop(10)
    #print(len(apts))


add_techniques_count(execution)
add_techniques_count(initial_access)
add_techniques_count(persistence)
add_techniques_count(reconnaissance)
add_techniques_count(c2)

# get values for each tactic : c2,execution,persistence...
print(c2.keys())
for x in c2.keys():
    print(c2.get(x))

# get keys for each tactic : c2,execution,persistence...
for x in c2:
    print(x)


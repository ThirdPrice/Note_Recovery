import csv
import os
import sys
prev = "   "

# python3 NoteRecover.py /Users/jackprice/Desktop/Notes.csv /Users/jackprice/Desktop/HTMLs/ "utf-16le"

# /Users/jackprice/Desktop/Notes.csv
_INPATH_ = sys.argv[1]
# /Users/jackprice/Desktop/HTMLs/
_OUTPATH_ = sys.argv[2]
# utf-16le
_ENCODING_ = sys.argv[3]


with open(_INPATH_, encoding=_ENCODING_) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            curr = row
            att = ""

            PATH = _OUTPATH_

            if (os.path.isdir(PATH + curr[3]) != True):
                PATH += curr[3] + "/"
                os.mkdir(PATH)
            elif (os.path.isdir(PATH + curr[3])):
                PATH += curr[3] + "/"

            if (prev[1] not in curr[1]):
                print(f'\t{row[0]}: {row[1]}')

                if (curr[7] != "None"):
                    filename =  PATH + "ATTACH-" + curr[0] + ".html"
                    att = curr[8];
                else:
                    filename = PATH + curr[0] + ".html"
                
                f = open(filename, 'w')
                f.write(curr[6])
                if (att != ""):
                    f.write(att) 
                
                f.close()

                prev = curr

            else:
                print(f'Updating {row[0]}: {row[1]}')

                if (curr[7] != "None"):
                    filename =  PATH + "ATTACH-" + prev[0] + ".html"
                    att = curr[8];
                else:
                    filename = PATH + prev[0] + ".html"

                with open(filename, "w"):
                    pass
                
                f = open(filename, 'w')
                f.write(curr[6])
                if (att != ""):
                    f.write(att) 
                
                f.close()
    print(f'Processed {line_count} lines.')
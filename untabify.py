#replaces all tabs with n spaces in a file

tabw = int(raw_input("Input tab width: "))
filename = raw_input("File to convert: ")
txt = open(filename, "r")
out = open("out_"+filename, "w")

for line in txt:
    while '\t' in line:
        index = line.find('\t')
        line = line[:index] + (tabw - index%tabw)*' ' + line[index+1:]
    out.write(line)
txt.close()
out.close()
             

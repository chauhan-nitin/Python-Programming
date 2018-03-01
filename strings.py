#Python function search_file(filename,target) to print string target preceded by line number
def search_file(filename,target):
    file=open(filename,"r")
    line_num=0
    for line in file:
        if line.find(target)!=-1: #search the target keyword in line
            print("{0} - {1}".format(line_num,line))
        line_num+=1
search_file("Fields-of-Athenry.txt","the")


print("\n\n") #Adding spacing between two program outputs
#Python function squeeze(filename) which prints the lines with preceded line number
def squeeze(filename):
    lines_seen = set() # holds lines already seen
    line_num=0
    file = open(filename, "r")
    for line in file:
        if line not in lines_seen: #non-duplicate
            print("{0} - {1}".format(line_num,line[:-1]))
            line_num+=1
            lines_seen.add(line)
    file.close()
squeeze("Fields-of-Athenry.txt")

#Python function join_files(inputfilenames,outputfilename) to copy contents of all input files in output file
def join_files(inputfilenames,outputfilename):
    out = open(outputfilename,"a")
    for each_file in inputfilenames:
        with open(each_file,"r") as input_file:
            for line in input_file:
                out.write(line+"\n")
    out.close()
join_files(["int1.txt","int2.txt"],"out.txt")


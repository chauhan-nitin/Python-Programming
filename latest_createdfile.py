import glob
import os
filelist = glob.glob('C:\\Users\\Public\\Downloads\\*') # *.txt means text format, for all formats use *
latestfile = max(filelist, key=os.path.getctime)
# Print the latest created file
print(latestfile)


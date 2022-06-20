import os
from datetime import datetime

folder = "IMG"
filelist = os.listdir(folder)

start = datetime(2022,6,20,10,34,49);

n_removed = 0
for name in filelist:
	cam, y,m,d,h,mm,ss,rest = name.split("_")
	curr = datetime(int(y),int(m),int(d),int(h),int(mm),int(ss))
	if curr < start :
		os.remove("{}//{}".format(folder,name))
		n_removed = n_removed + 1

print("{} files deleted".format(n_removed))
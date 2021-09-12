import numpy as np
import csv

fw = open('./new/8test_dot.csv','w')
wr = csv.writer(fw)

fr = open('./new/re_point.csv','r')
rdr = csv.reader(fr)
count = 1

for line in rdr:
  line_comp = [str(line[0])]
  for i in range(1,5):
      tmpp = line[i][1:-1]
      tmppp = tmpp.split(",")
      print(tmppp)
      comp1 = int(tmppp[0]) // 8
      comp2 = int(tmppp[1][1:]) // 8
      line_comp.append(comp1)
      line_comp.append(comp2)
  wr.writerow(line_comp)

fw.close()
fr.close()
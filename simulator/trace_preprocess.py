import csv
from random import random
import sys

data_path = sys.argv[1]
trace_name = sys.argv[2]
zero_time_percent = float(sys.argv[3])
out_name = sys.argv[4]

with open(data_path+"/"+trace_name, "r") as input_file:
    with open(data_path+"/"+out_name, "w") as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        cnt_zero = 0
        cnt_all = 0

        for line_id,line in enumerate(csv_reader):
            if line_id > 0:
                if random() < zero_time_percent:
                    line[2] = "0"

            if line[2] == "0":
                cnt_zero += 1
            cnt_all += 1

            csv_writer.writerow(line)

print(f"Zeros percentage: {cnt_zero}/{cnt_all}={cnt_zero/cnt_all}")

#!/bin/bash

data_path="trace-data"
trace_names=("trace1.csv" "trace2.csv" "trace3.csv" "trace4.csv")
zero_time_percent=0.8
#out_names=("trace1_A1.csv" "trace2_B1.csv" "trace3_C1.csv" "trace4_D1.csv")
out_names=("trace1_A2.csv" "trace2_B2.csv" "trace3_C2.csv" "trace4_D2.csv")

i=0
for trace in ${trace_names[@]};do
    out=${out_names[i]}
    cmd="python trace_preprocess.py ${data_path} ${trace} ${zero_time_percent} ${out}"
    echo ${cmd}
    python trace_preprocess.py ${data_path} ${trace} ${zero_time_percent} ${out}
    i=$i+1
done

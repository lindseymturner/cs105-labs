# set yrange[0:1e-5]

plot 'power1_time.txt' using "exp":"time1", \
     "power2_time.txt" using "exp":"time2", \
     "power3_time.txt" using "exp":"time3"

pause 100

#!/bin/bash
hhs=("10.3.50.221" "10.3.50.222" "10.3.50.224" "10.3.50.225" "10.3.50.226" "10.3.50.117" "10.3.50.118" "10.3.51.1"
 "10.3.50.227" "10.3.50.228" "10.3.50.90" "10.3.50.91" "10.3.50.223" "10.3.51.2" "10.3.51.3" "10.3.50.33" "10.3.50.34" "10.3.50.38" "10.3.50.39"
 "10.3.50.40" "10.3.50.41" "10.3.50.44" "10.3.50.85" "10.3.50.240" "10.3.50.245" "10.3.50.246"
 "10.3.50.241" "10.3.50.234" "10.3.50.219" "10.3.50.249" "10.3.50.215")
for i in ${hhs[@]};do
	echo "`ping -c 1 $i`"
done;

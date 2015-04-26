#!/bin/bash
datetime=$(date +"D%Y%m%dT%H%M%S")
dir=/home/tyrick/Documents/python/wikipedia

scrapy crawl new -o $dir/new/new.json

scrapy crawl parse -a file=$dir/new/new.json -a needle="different than" -o $dir/hits/hits_$datetime.json
rm $dir/new/new.json

exit

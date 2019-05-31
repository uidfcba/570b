#!/bin/bash
#
# Assume notebooks have already been copied into html directory
# and there are eight modules
# Convert ipynb extensions in URLs to html

for i in {1..8} ; 
do 
    cd Module$i/notebooks ; 
    for file in m?l?.html ; 
    do 
        sed -i '' 's/.ipynb/.html/g' $file ; 
    done ; 
    cd ../.. ; 
done


#!/bin/bash
#
# Assume notebooks have already been copied into html directory
# and there are eight modules

for i in {1..8} ;  
do 

cd ../html ;

cd Module$i ; 

jupyter nbconvert --template full index.ipynb ;

jupyter nbconvert --template full assignment/assignment.ipynb ;

jupyter nbconvert --template full notebooks/*.ipynb ;

cd .. ; 

done


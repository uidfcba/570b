#!/bin/bash
for i in {1..8} ;  
do 

cd ../html ;

cd Module$i ; 

rm -rf index.ipynb ;

rm -rf assignment/assignment.ipynb ;

rm -rf  notebooks/*.ipynb ;

cd .. ; 

done


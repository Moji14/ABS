#!/bin/bash
#Software validation script
#This script will test the "blurry-or-not.py" and "flared-or-not.py" sctipts by testing them on the set of images
# given on the "training-data" directory


#Loop to test "blurry-or-not.py" on blurred images
blurry_counter=0
for path in ~/training-data/blurry-data/*; do
    ./blurry-or-not.py -i $path -t 115
    aux=$?
    let blurry_counter=($blurry_counter+$aux)
    #echo $blurry_counter
done
#Loop to test "flared-or-not.py" on flared images
flared_counter=0
for path in ~/training-data/flare-data/*; do
    ./flared-or-not.py -i $path -t 73
    aux=$?
    let flared_counter=($flared_counter+$aux)
    #echo $flared_counter
done

#Loop to test "blurry-or-not.py" and "flared_or_not on" good data
non_blurry_counter=0
non_flared_counter=0
for path in ~/training-data/good-data/*; do
    ./blurry-or-not.py -i $path -t 115
    aux=$?
    let non_blurry_counter=($non_blurry_counter+$aux)

    ./flared-or-not.py -i $path -t 73
    aux=$?
    let non_flared_counter=($non_flared_counter+$aux)

    #echo $non_blurry_counter
    #echo $non_flared_counter
done
#Blurry detector statistics
echo $blurry_counter
echo $non_blurry_counter

#Flared detector statistics
echo $flared_counter
echo $non_flared_counter
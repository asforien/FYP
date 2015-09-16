#!/bin/bash

for f in cantonese/part-1/*
do 
	echo -n $f >> durations;
	ffmpeg -i $f 2>&1 | grep Duration | sed 's/.*Duration: 00:00:\(.*\), start.*/ \1/' >> durations;
done

for f in cantonese/part-2/*
do 
	echo -n $f >> durations;
	ffmpeg -i $f 2>&1 | grep Duration | sed 's/.*Duration: 00:00:\(.*\), start.*/ \1/' >> durations;
done

for f in cantonese/part-3/*
do 
	echo -n $f >> durations;
	ffmpeg -i $f 2>&1 | grep Duration | sed 's/.*Duration: 00:00:\(.*\), start.*/ \1/' >> durations;
done

for f in cantonese/part-4/*
do 
	echo -n $f >> durations;
	ffmpeg -i $f 2>&1 | grep Duration | sed 's/.*Duration: 00:00:\(.*\), start.*/ \1/' >> durations;
done


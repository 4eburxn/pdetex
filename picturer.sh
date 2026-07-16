#!/bin/bash

mkdir -p pics
cd pics

for fname in $(ls ../plotters)
do
  echo "plotting $fname"
  python3 ../plotters/$fname &
done






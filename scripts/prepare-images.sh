#!/bin/bash

usage() {
    echo "Usage: $0 --in [input dir] --out [output dir]"
    exit 1
}

if [ "$#" -ne 4 ]; then
    usage
fi

if [ "$1" == "--in" ] && [ "$3" == "--out" ]; then
    in_dir="$2"
    out_dir="$4"
else
    usage
fi

if [ ! -d "$in_dir" ]; then
    echo "Error: Input directory '$in_dir' does not exist."
    exit 1
fi

mkdir -p "$out_dir"
rm -f "$out_dir"/*

echo "Input directory: $in_dir"
echo "Output directory: $out_dir"

for file in "$in_dir"/*.png; do
    if [ -f "$file" ]; then
        base=$(basename "$file" .png)
        convert "$file" "$in_dir/${base}.jpg"
    fi
done

for img in "$in_dir"/*.jpg; do
    if [ -f "$img" ]; then
        base=$(basename "$img" .jpg)
        
        # need sampling factor for the dqt thingy
        convert "$img" -sampling-factor 2x2,1x1,1x1 -colorspace sRGB -strip -interlace none "$out_dir/${base}_ssdv.jpg"
        
        ssdv -e -n -q 6 -c "VK5QI" -i "$base" "$out_dir/${base}_ssdv.jpg" "$out_dir/${base}.bin"
    fi
done

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

counter=1
for img in "$in_dir"/*.jpg; do
    if [ -f "$img" ]; then
        new_filename="${counter}.jpg"
        convert "$img" -sampling-factor 2x2,1x1,1x1 -colorspace sRGB -strip -interlace none "$out_dir/$new_filename"
        ssdv -e -n -q 6 -c "VK5QI" -i "$ " "$out_dir/$new_filename" "$out_dir/${counter}_raw.bin"        
        
        ((counter++))
    fi
done


# prepare hashes
./hash-dir.sh $in_dir > hashes.txt
convert 11.jpg -sampling-factor 2x2,1x1,1x1 -colorspace sRGB -strip -interlace none 11.jpg
./stego/stego.sh -e --m hashes.txt --in 11.jpg --out "$out_dir/11.jpg"
ssdv -e -n -q 6 -c "VK5QI" -i "$ " "$out_dir/11.jpg" "$out_dir/11_raw.bin"        




# deal with final image
# convert 12.jpg -sampling-factor 2x2,1x1,1x1 -colorspace sRGB -strip -interlace none 12.jpg
cp 12.jpg $out_dir/12.jpg
ssdv -e -n -q 6 -c "VK5QI" -i "$ " "$out_dir/12.jpg" "$out_dir/12_raw.bin"        



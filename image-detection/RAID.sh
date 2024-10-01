#!/bin/bash

echo "Welcome to RAID: Reese's Awesome Image Detection"

# clean up these stupid export files
if [ -fe roboflow/README.dataset.txt ]
then 
    rm roboflow/README.dataset.txt
    rm roboflow/README.roboflow.txt
fi 




usage () {
    echo "Usage:"
    echo " --train             Re-train the death star detector"
    echo " --dir [path]        Run the image classifier on every file in a directory"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi



if [[ "$1" == "--train" ]]; then

    rm -r runs
    echo "Training!"

    python3 src/train-detection.py
    exit 0
fi

if [[ "$1" == "--dir" ]]; then
    if [ -z "$2" ]; then # len == 0
        echo "Ooops no path. Need path."
        usage
        # exit 1
    fi

    echo "Classifying images in directory: $2"

    python3 src/detection.py


    exit 0
fi


# bad args otherwise
usage
exit 1

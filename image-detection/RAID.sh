#!/bin/bash

echo "Welcome to RAID: Reese's Awesome Image Detection"

# clean up these stupid export files
if [ -f "roboflow/README.dataset.txt" ]; then 
    rm roboflow/README.dataset.txt
    rm roboflow/README.roboflow.txt
fi 


usage () {
    echo "Usage:"
    echo " --train [num_epochs]          Re-train the death star detector with number of epochs"
    echo " --in [path] --out [path]      Run the image classifier on every file in a directory"
}

if [ $# -eq 0 ]; then
    usage
    exit 1
fi



if [[ "$1" == "--train" ]]; then

    if [ -z "$2" ]; then
        echo "Error: missing number epochs"
        usage
        exit 1
    fi

    # rm old runs to make sure file path matches on check
    rm -r runs
    echo "Training..."

    python3 src/train-detection.py $2 
    exit 0
fi

if [[ "$1" == "--in" ]]; then
    if [ -z "$2" ]; then 
        echo "Error: Ooops no path. Need path."
        usage
        exit 1
    fi

    if [ "$3" != "--out" ]; then
        echo "Error: Need to specify output dir"
        usage
        exit 1
    fi

    if [ -z "$4" ]; then
        echo "Error: Need to specify output dir"
        usage
        exit 1
    fi


    OUTDIR="$4"
    mkdir -p $OUTDIR
    
    # clean anything from past run
    rm $OUTDIR/*.png
    rm $OUTDIR/*.bin

    echo "Classifying images in directory: $2"

    python3 src/detection.py $2 $OUTDIR


    cp 11-signal-finished.png $OUTDIR

    exit 0
fi


# bad args otherwise
usage
exit 1

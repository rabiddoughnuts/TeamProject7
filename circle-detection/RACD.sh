
echo "Welcome to RACD: Reese's awesome circle detection"

usage () {
    echo "Usage:"
    echo " --in [path] --out [path] Detect circles in every file in path and save to out path "
}


if [ "$#" -ne 4 ]; then
    echo "Error: Expected 4 arguments, but got $#."
    usage
    exit 1
fi

if [ "$1" != "--in" ]; then
    echo "Bad --in arg"
    usage
    exit 1
fi

if [ "$3" != "--out" ]; then
    echo "Bad --out arg"
    usage
    exit 1
fi


if [ ! -d "$2" ]; then
    echo "Error: Input path '$2' is not a valid directory."
    exit 1
fi

if [ ! -d "$4" ]; then
    echo "Error: Output path '$4' is not a valid directory."
    exit 1
fi

in_path=$(realpath "$2")
out_path=$(realpath "$4")


python3 src/detect-circles.py $in_path $out_path



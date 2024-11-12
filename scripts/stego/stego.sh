#!/bin/bash

usage() {
    echo "Usage:"
    echo " -e --m [message_file] --in [input file] --out [name of output file]"
    echo " -d --in [decodeable file]"
    exit 1
}

mode=""
message=""
input_file=""
output_file=""

while [[ "$#" -gt 0 ]]; do
    case "$1" in
        -e)
            mode="encode"
            shift
            ;;
        -d)
            mode="decode"
            shift
            ;;
        --m)
            if [[ -n "$2" ]]; then
                message="$2"
                shift 2
            else
                echo "Error: --m requires a message"
                usage
            fi
            ;;
        --in)
            if [[ -n "$2" ]]; then
                input_file="$2"
                shift 2
            else
                echo "Error: --in requires an input file"
                usage
            fi
            ;;
        --out)
            if [[ -n "$2" ]]; then
                output_file="$2"
                shift 2
            else
                echo "Error: --out requires an output file"
                usage
            fi
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# I love bash arg parsing
if [[ "$mode" == "encode" ]]; then
    if [[ -z "$message" || -z "$input_file" || -z "$output_file" ]]; then
        echo "Error: -e mode requires --m, --in, and --out"
        usage
    fi
elif [[ "$mode" == "decode" ]]; then
    if [[ -z "$input_file" ]]; then
        echo "Error: -d mode requires --in"
        usage
    fi
else
    echo "Error: You must specify either -e or -d mode"
    usage
fi

echo "Mode: $mode"
echo "Message: $message"
echo "Input file: $input_file"
echo "Output file: $output_file"


if [[ "$mode" == "encode" ]]; then

    steghide embed -cf "$input_file" -ef "$message" -sf "$output_file" -p ""

elif [[ "$mode" == "decode" ]]; then

    steghide extract -sf "$input_file" -p ""
    
fi

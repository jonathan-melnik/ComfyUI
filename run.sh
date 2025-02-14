#!/bin/bash

# Function to display usage
usage() {
    echo "Usage: $0 --port <port_number> (--cpu | --gpu)"
    exit 1
}

# Default values
PORT=""
TYPE=""

# Parse arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --port) PORT="$2"; shift ;;
        --cpu|--gpu) TYPE="$1" ;;
        *) echo "Unknown parameter: $1"; usage ;;
    esac
    shift
done

# Check required arguments
if [[ -z "$PORT" || -z "$TYPE" ]]; then
    echo "Error: Missing required arguments."
    usage
fi

# Run the Python script
BACKEND_TOKEN="FLOYO-210439231032askljds2313213mnk" python main.py --port "$PORT" "$TYPE" --express-server-url http://localhost:3000

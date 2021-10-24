SCRIPT_PATH="`dirname "$0"`"
INPUT_PATH="$SCRIPT_PATH"/../array-api/spec/API_specification
OUTPUT_PATH="$SCRIPT_PATH"/../generated
sphinx-build -b gen -c "$SCRIPT_PATH" "$INPUT_PATH" "$OUTPUT_PATH"

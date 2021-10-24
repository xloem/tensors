SCRIPT_PATH="`dirname "$0"`"
cd "$SCRIPT_PATH"
ROOT_PATH=..
INPUT_PATH="$ROOT_PATH"/extern/array-api/spec/API_specification
OUTPUT_PATH="$ROOT_PATH"/arrays_api
sphinx-build -b gen -c . "$INPUT_PATH" "$OUTPUT_PATH"

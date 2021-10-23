SCRIPT_PATH="`dirname "$0"`"
sphinx-build -b gen -c "$SCRIPT_PATH" "$SCRIPT_PATH"/../array-api/spec/API_specification "$SCRIPT_PATH"/../generated

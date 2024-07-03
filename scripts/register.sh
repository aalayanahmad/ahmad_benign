#!/bin/bash

handle_error() {
  local error_code=$?
  local line_number=$1
  local command=$2
  echo "Error occurred in register when executing $command at line $line_number with exit code: $error_code"
  exit $error_code
}

trap 'handle_error ${LINENO} "$BASH_COMMAND"' ERR

./nr-ue -c "config/ue$1.yaml" -n 1

#!/bin/bash

handle_error() {
  local error_code=$?
  local line_number=$1
  local command=$2
  echo "Error occurred in deregister when executing $command at line $line_number with exit code: $error_code"
  exit $error_code
}

trap 'handle_error ${LINENO} "$BASH_COMMAND"' ERR

echo "UE $1 is trying to deregister..."

./nr-cli "$1" -e 'deregister switch-off'

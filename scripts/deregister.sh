#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

echo "UE $1 is trying to deregister..."

./nr-cli "$1" -e 'deregister switch-off'
sleep 1

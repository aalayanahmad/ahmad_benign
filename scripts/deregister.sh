#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error UE $1 while deregistering with exit code: $error_code"
  exit $error_code
}

trap 'handle_error "$1"' ERR

echo "UE $1 is trying to deregister..."

./nr-cli "$1" -e 'deregister switch-off'

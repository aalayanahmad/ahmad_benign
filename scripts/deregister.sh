#!/bin/bash

echo "ue $1 is trying to deregister..."

handle_error() {
  local error_code=$?
  echo "An error occurred while trying to deregister ue $1! The error code is: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

./nr-cli $1 -e 'deregister switch-off'
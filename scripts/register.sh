#!/bin/bash

handle_error() {
  local error_code=$?
  echo "Error occurred with exit code: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

echo "UE $1 is trying to register..."

./nr-ue -c config/ue$1.yaml -n 1
sleep 2

#!/bin/bash

echo "ue $1 is trying to register..."

handle_error() {
  local error_code=$?
  echo "An error occurred while trying to register ue $1! The error code is: $error_code"
  exit $error_code
}

trap 'handle_error' ERR

./nr-ue -c config/$1 -n 1

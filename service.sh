#!/bin/bash
if [[ "$1" == "start" ]]; then
  # start kafka
  brew services restart kafka
  brew services restart zookeeper
elif [[ "$1" == "stop" ]]; then
  # stop kafka
  brew services stop kafka
  brew services stop zookeeper
else
  echo "Specify action"
fi
brew services
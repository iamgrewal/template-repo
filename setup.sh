#!/bin/bash
read -p  "What is the name of your project ?  :" Project_NAME
# Check if the user provided a name
if [ -z "$Project_NAME" ]; then
  echo "No Project Name provided. Exiting."
  exit 1
fi
conda create -n $Project_NAME python=3.12.4 poetry=1.8.3 --file conda-linux-64.lock
conda activate $Project_NAME
poetry install
conda-lock -k explicit --conda mamba
mamba update --file conda-linux-64.lock
poetry init
poetry lock
conda env export | grep -v "^prefix: " > environment.yml
# Update Poetry packages and re-generate poetry.lock
poetry update

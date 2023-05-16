#!/bin/bash

#---------------------------------------------------------
# Example usage:./run_trial.sh nist_competitor trial_name
#---------------------------------------------------------
if [[ ! $1 ]] ; then
    echo "Team configuration argument not passed" 
    exit 1
fi

# if [[ ! $2 ]] ; then
#     echo "Trial name not specified" 
#     exit 1
# fi


teamName=$(python3 get_team_name.py $1)
# echo "Team name: $teamName"

if [[ ! $teamName ]] ; then
    echo "Team name not found" 
    exit 1
fi

export ARIAC_TEAM_NAME="$teamName"

if [[ $2 ]] ; then
    echo "==== Running trial: $2"
    docker exec -it $teamName bash -c ". /home/ubuntu/scripts/run_trial.sh $1 $2"
fi

if [[ ! $2 ]] ; then
    echo "==== Running all trials in trials directory"
    # absolute path of the current script
    trials_dir="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )" # https://stackoverflow.com/a/4774063/99379
    # get each file in the trials folder
    for entry in "$trials_dir"/trials/*
    do
        # e.g., kitting.yaml
        trial_file="${entry##*/}"
        # echo "$trial_file"
        # e.g., kitting
        trial_name=${trial_file::-5}
        # echo "$trial_name"

        # ARIAC_DONE=$(printenv | grep ARIAC_DONE)
        # if [[ $ARIAC_DONE ]] ; then
        docker exec -it $teamName bash -c ". /home/ubuntu/scripts/run_trial.sh $1 $trial_name"
        fi
        
    done
fi



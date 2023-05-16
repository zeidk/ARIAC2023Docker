#!/usr/bin/env python3

import os
import sys
import subprocess
import yaml
import signal


def main():
    
    # if len(sys.argv) != 2 and len(sys.argv) != 3:
    #     print("==== Wrong format: ./run_trial.sh <team_name> [trial_name]")
    #     exit()
        
    # Get team file name
    yaml_file = sys.argv[1] + '.yaml'

    if not os.path.isfile(yaml_file):
        print(f'{yaml_file} not found')
        exit()

    # Parse yaml file
    with open(yaml_file, "r") as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError:
            print("Unable to parse yaml file")
            exit()

    # Store data from yaml filyaml_path
    try:
        package_name = data["competition"]["package_name"]
    except KeyError:
        print(f"Unable to find package_name {package_name}")
        exit()

    try:
        launch_file = data["competition"]["launch_file"]
    except KeyError:
        print(f"Unable to find launch_file {launch_file}")
        exit()

    # Grab each file in the directory 'trials'
    trials_folder = os.path.join("/home/ubuntu/ariac_ws/src/ariac/ariac_gazebo/config/trials")
    trial_file = os.path.join(trials_folder, sys.argv[2] + ".yaml")
    
    
    # Run 
    # if (len(sys.argv) == 3):
    #     launch_cmd = f"ros2 launch {package_name} {launch_file} trial_name:={sys.argv[2]}"
    #     subprocess.run(launch_cmd, shell=True, env=dict(os.environ, DISPLAY=":1.0"))
    
    
    
    # Parse trial file to retrieve the time limit
    with open(trial_file, "r") as stream:
        try:
            trial_data = yaml.safe_load(stream)
        except yaml.YAMLError:
            print(f"Unable to parse yaml file {trial}")
            exit()
    
    # get the time limit for the trial
    try:
        time_limit = trial_data["time_limit"]
    except KeyError:
        print("Unable to find time_limit in file")
        exit()
    
    # default time limit is 500 seconds
    time_out = 500
    
    if time_limit != -1:
        time_out  = time_limit + 100 # add 100 seconds to account for real time
    
    trial_name = sys.argv[2]  # remove .yaml
    print(f"==== Running trial {trial_name} with time limit {time_out}")
    
    launch_cmd = f"ros2 launch {package_name} {launch_file} trial_name:={trial_name}"
    subprocess.run(launch_cmd, shell=True, timeout=time_out, env=dict(os.environ, DISPLAY=":1.0"))
    
    print(f"==== Trial {trial_name} completed")


if __name__=="__main__":
    main()

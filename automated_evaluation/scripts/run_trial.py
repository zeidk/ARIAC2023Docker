#!/usr/bin/env python3

import os
import sys
from subprocess import Popen
from signal import SIGINT
import yaml


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

    trial_name = sys.argv[2]  # remove .yaml
    
    launch_cmd = f"ros2 launch {package_name} {launch_file} trial_name:={trial_name}"
    # subprocess.run(launch_cmd, shell=True, timeout=time_out, env=dict(os.environ, DISPLAY=":1.0"))
    
    process = Popen(["ros2", "launch", package_name, launch_file,
                    "trial_name:=", trial_name, '--noninteractive'], text=True)

    while True:
        TRIAL_DONE = os.environ.get('TRIAL_DONE')
        if TRIAL_DONE == trial_name:
            break
        
    process.send_signal(SIGINT)
    # Might raise a TimeoutExpired if it takes too long
    return_code = process.wait(timeout=10)
    print(f"return_code: {return_code}")

    print(f"==== Trial {trial_name} completed")


if __name__=="__main__":
    main()

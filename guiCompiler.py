# An attempt to create a gui compiler like the .sh script
# The script is a lot simpler and the syntax is also a lot clearer
import os
import subprocess

for ui_file in os.listdir(os.path.curdir):
    # Loop through current directory
    if ui_file.endswith(".ui"):
        # We have a candidate file
        print(f"Found {ui_file}")
        base_name, _ = os.path.splitext(os.path.basename(ui_file))
        target_name = f"frm_{str.capitalize(base_name)}.py"
        print(target_name)
        result = subprocess.run(["pyuic5", "-o", target_name, f"{ui_file}"], capture_output=True)
        if result.returncode == 0:
            print(f"Form compiled to {target_name}")
        else:
            print(f"An error occured {result}")

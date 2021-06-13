# An attempt to create a gui compiler like the .sh script
# The script is a lot simpler and the syntax is also a lot clearer
import os
import subprocess

for ui_file in os.listdir(os.path.curdir):
    # Loop through current directory
    if ui_file.endswith(".ui"):
        # We have a candidate file
        print(f"---> Found {ui_file}")
        # get the filename without extension
        base_filename, _ = os.path.splitext(os.path.basename(ui_file))
        # Make the target name
        target_filename = f"frm_{str.capitalize(base_filename)}.py"
        # Run!
        result = subprocess.run(["pyuic5", "-o", target_filename, f"{ui_file}"], capture_output=True)
        if result.returncode == 0:
            print(f"[v] Form compiled to {target_filename}")
        else:
            print(f"[e] An error occured {result}")

print("Compilation terminated!")

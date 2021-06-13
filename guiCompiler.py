# An attempt to create a gui compiler like the .sh script
# The script is a lot simpler and the syntax is also a lot clearer
import os
import subprocess


def compile_ui(prefix: str):
    form_count_ok = 0
    form_count_ko = 0

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
                form_count_ok += 1
            else:
                print(f"[e] An error occured {result}")
                form_count_ko += 1

    return form_count_ok, form_count_ko


if __name__ == "__main__":
    res_ok, res_ko = compile_ui("frm_")
    print("Compilation terminated!")
    print(f"{res_ok} ui files converted without error")
    print(f"{res_ko} ui files contain errors")

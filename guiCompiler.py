"""
    guiCompiler.py
    Script that goes through a folder containing Qt Designer .ui files
    and .qrc files and compiles all occurences.
    Author : DenkaTech Software (Danny Van Geyte)
    Created : 13/06/2021
"""
import os
import subprocess


def compile_ui(prefix="frm_", location="."):
    """
    Compile the .ui files to .py files.
    :param location: path to file
    :param prefix: Prefix for the form final name eg frmMain.py
    :return: Tuple contains (count of file compiled without error,
                             count of files unable to compîle)
    """
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
            target_filename = f"{prefix}{str.capitalize(base_filename)}.py"
            # Run!
            result = subprocess.run(["pyuic5", "-o", target_filename, f"{ui_file}"], capture_output=True)
            if result.returncode == 0:
                print(f"[v] Form compiled to {target_filename}")
                form_count_ok += 1
            else:
                print(f"[e] An error occured {result}")
                form_count_ko += 1

    return form_count_ok, form_count_ko


def compile_resources(resourcename="images", location="."):
    """
    Compile the .qrc (Qt Designer resource files) into .py files.
    :param location: Path to file(s)
    :param resourcename: Name of the source resource file
    :return:
    """
    # echo "Compiling Resource file"
    # pyrcc5 -o icons_rc.py ./ui/icons.qrc


if __name__ == "__main__":
    res_ok, res_ko = compile_ui("frm")
    print("Compilation terminated!")
    print(f"{res_ok} ui files converted without error")
    print(f"{res_ko} ui files contain errors")

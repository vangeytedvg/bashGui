# bash script to automate compiling .ui files
# for PyQt5 projects
DIR=$(pwd)
echo "$DIR"
echo "Compiling GUI files"
# loop through files and select only the .ui files
for FILE in "$DIR"/*.ui; do
  # Show what is compiling
  echo "--> Compiling ${FILE##*/}"
  # Get the basename of the file (no extension). We know the extension
  # is .ui, so get rid of it. We will use this to createt the .py file below
  SOURCE=$(basename "$FILE" .ui)
  # The original <file>.ui filename
  COMPILESOURCE="${FILE##*/}"
  # Make the target filename, the syntax for bash 4 will uppercase the
  # first letter of the filename
  TARGET="frm${SOURCE^}".py
  echo "Target is --> $TARGET"
  # Compile!
  pyuic5 -o "$TARGET" "$COMPILESOURCE"
done
echo "Complation is done!"
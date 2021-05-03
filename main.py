import pathlib
import sys
import os
import re

def parse_file(path: pathlib.Path, package_set: set, import_set: set, content: list):
  """Parses a given java file and seperates the file content into a package set, an import set and the other content.

  Args:
      path (pathlib.Path): A path to the file
      package_set (set): A set with all
      import_set (set): A set with all imports
      content (list): A list of all lines of content
  """
  with open(path, "r") as file:
    while line := file.readline():
      # Its a package line
      if (package_match := re.match(r"\s*package\s+(\S*)\s*;\n", line)):
        package_set.add(package_match.groups()[0])

      # Its an import line
      elif line.startswith("import"):
        import_set.add(line)

      # Its a class definition, remove the visibility modifier
      elif (class_definition_match := re.match(r"\s*(public|private|protected)\s+((abstract\s+)?(class|enum|interface).*\n)", line)):
        content.append(class_definition_match.groups()[1])

      # Anythin else just add to content if not whitespace
      elif not line.isspace():
        content.append(line)

  # Add newline as delimiter
  content.append("\n")

def remove_package_imports(package_set: set, import_set: set):
  """Remove package imports from a given import set.

  Args:
      package_set (set): A set containing all packages
      import_set (set): A set containing all imports
  """
  package_imports = [element for element in import_set if any([True for x in package_set if element.split()[1].startswith(x)])]
  import_set.difference_update(package_imports)

def find_files(dir: pathlib.Path):
  """Finds all files in the given directory recursively.

  Args:
      dir (pathlib.Path): The root directory for finding files

  Yields:
      pathlib.Path: The next file in the given directory
  """
  for dirpath, _dirname, files in os.walk(dir):
    for name in files:
      if name.lower().endswith(".java"):
        yield pathlib.Path(dirpath) / name

if __name__ == "__main__":
  root_dir = pathlib.Path(sys.argv[1])
  out_file = root_dir / "Output.java"
  package_set = set()
  import_set = set()
  content = list()

  # Remove Output.java if it already exists
  if out_file.exists():
    out_file.unlink()

  # Parse all files in current directory recursively
  for file in find_files(root_dir):
    parse_file(file, package_set, import_set, content)

  # Purge package imports
  remove_package_imports(package_set, import_set)

  # Write output file
  with open(out_file, "w") as file:
    file.writelines(import_set)
    file.writelines(content)
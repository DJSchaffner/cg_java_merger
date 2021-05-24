# CG Java Merger

This is a very basic parser that will parse a Java project into a single file for websites like CodinGame.  
It will recursively find all java files in the java project and insert everything into a single file in the order the files are found.

No guarantess this is bug free and respects all possible file structures in Rust but as of now this works for my purposes.  
Feel free to open a ticket with feature requests or bug reports if you have / find any.

# Usage

Call cg_java_merger.exe <PathToProject>
ex: ./ cg_java_merger.exe C:/myjavaproject/
  
Example `tasks.json` file for VSCode:
```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "merge",
      "type": "process",
      "command": "C:/cg_java_merger/cg_java_merger.exe",
      "args": ["${workspaceFolder}/src"],
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared",
        "showReuseMessage": true,
        "clear": false
      }
    }
  ]
}
```

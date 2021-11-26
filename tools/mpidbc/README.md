# mpidbc

Helper tool that formats output of *mpidb* according to one of the available templates.

## Currently available templates

* txt
  * Easy-to-read plain-text format.
* vscode
  * Launch-configuration file (`launch.json`) for [Visual Studio Code](https://github.com/Microsoft/vscode).
  * To launch the debugging session from within the IDE:
    1. Make sure that you have the necessary debugging extensions (e.g. [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)).
    2. Choose *File->Open Folder* to open the root directory of the code being debugged.
    3. Create a subfolder called `.vscode` in this directory.
    4. Generate or place the `launch.json` inside the `.vscode` directory.
    5. Place breakpoints, etc.
    5. From the debug panel, choose the compound configuration to debug all MPI ranks concurrently.

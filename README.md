# Generate Function Graph using IDAPYTHON

## Working

Given an entry point EA(Effective address) (the first address of the program you want to start building call graph from) it will generate the call graph.
```shell
if __name__ == '__main__':
    name, ea = getMainEntryPoint()
#     ea = 4199680
```

In case if you want to specify your own EA then simply uncomment the last line as shown in above snippet in main.py file.

## How to execute Script

1. You have to open your PE file in the Portable Executable in IDAPro.
2. Select the File > Script file option from menu bar.
3. Browse to main.py file.
4. This will simply execute the IDAPython script.
5. The **graph.json** file will be generated in the same directory of your executable file.

## Generating Graph 

1. Make sure to create VirtualEnv if not already created.
2. One created, active the virtualenv
```shell
.\venv\Scripts\activate
```
3. Install the requirements
```shell
pip install -r requirements.txt
```
4. Change the path of the file variable in CreateGraph.py file respectively.
```shell
file = "./graph.json"
```
> Here, graph.json file is present in current directory.
5. Execute the script 
```shell
python CreateGraph.py
```
> This will open the graph in the browser.

## Keyword:

- IDAPython
- Malware Analysis
- Call Graph

## Contributer:
Daud Ahmed (daudahmed@zoho.com)
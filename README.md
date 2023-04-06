# programming_search

## It would be handy to be able to search for a solution of your problem using terminal, don’t you think?
### A basic Python command prompt script that utilizes the webbrowser module to refine search results to only include websites related to programming

### Configuration on Windows
- Hop into Powershell and type:
- New-item -Type file -Path $PROFILE -Force
- Notepad $PROFILE
- In Notepad:
- function search {$Query=Read-Host -Prompt "Provide search query"  
                    python C:\PATH_TO_PYTHON_SCRIPT\main.py $Query}
- Save file
- Restart Powershell
- You are good to go

### Configuration on MacOS
- Open terminal
- Vim ~/.bashrc
- Alias search='python3 ~/PATH_TO_PYTHON_SCRIPT/main.py'
- Save and quit
- Source ~/.bashrc
- You are good to go

### How to use:
- Turn on powershell or Terminal 
- on windows - type "search" in powershell and prompt will ask you about your query
- on macos - type "search YOUR_QUERY" in terminal, should  work

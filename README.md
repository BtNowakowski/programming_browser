# Programming browser

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
- nano ~/.zshrc
- In nano:
- Alias search='python3 ~/PATH_TO_PYTHON_SCRIPT/main.py'
- Save and quit
- Source ~/.zshrc
- You are good to go

### How to use:
- Turn on powershell or Terminal 
- on windows - type "search" in powershell and prompt will ask you about your query
- on macos - type "search YOUR_QUERY" in terminal, should  work

<img width="695" alt="image" src="https://user-images.githubusercontent.com/107316656/230400990-118340b1-d55f-409d-acbd-adcbee23eb03.png">
<img width="1029" alt="image" src="https://user-images.githubusercontent.com/107316656/230401176-17a153da-4f0c-454b-a868-ed3678f98d4f.png">

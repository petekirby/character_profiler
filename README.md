# character_profiler 

## System Requirements - OSX Only 

### Python3

You'll need python3+ to run character_profiler. Follow these steps:

#### - 1. Install brew (a package manager for OSX).

  - Open Terminal.app (located in Applications/Utilities/Terminal.app)
  - Paste this line into the command prompt:
  `ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"`
  - The installation may take a few minutes.
  - When it has successfully run, type this command into the command line:
  `brew -v`, and you should see confirm the version (currently 0.9.9) of brew you just installed.
  
#### - 2. Install python3 with brew
  - In your terminal window type:
  `brew install python3`
  - Wait for the packages to install. When it has successfully run, in the same propmt window, type:
  `python3`
  - You should see an interactive python3 shell with the prompt `>>>`.
  - You have sucessfully installed python3.
  - You can exit the interactive shell by pressing Ctrl+z

## Installation 

### 1. Local Set-up

Download this whole repository by selecting the "Clone/Download" buttom from the root url: https://github.com/cklog/character_profiler.

Save the folder to your Desktop.

Navigate to Desktop/character_profiler/modules/console.py and open this file in a text editor.

Go to the second last line of code:

`console = ParseHandler('/Users/{Your User Name}/Desktop/character_profiler/texts')`

And change the {Your User Name} field to your actual username. A few such examples might be:

```
    console = ParseHandler('/Users/johnsmith/Desktop/character_profiler/texts')
    console = ParseHandler('/Users/janedoe/Desktop/character_profiler/texts')
```

If you don't know your username you can grab it by doing the following:
  - Open Terminal.app
  - type `pwd`
  - the name after /Users/{name} is the name you will type in the above string, i.e. /Users/johnsmith
  
Save console.py and close the file.

### 2. Test your installation
 
Open Terminal.app and paste in the following line:

`cd ~/Desktop/character_profiler/modules/`

This will direct the terminal to the 'modules' directory.

Then type:

`python3 console.py` 

This command runs the program. You should be greeted by:

````
Welcome to console:
=>>
```

Next type: 

`help` 

This command should return:

```
Welcome to console!
=>> help

Documented commands (type help <topic>):
========================================
EOF                    dirpath  jobs          set          summary
classes                exit     load          set_dirpath  text_nodes
count_all_focal_edges  help     profiles      set_max
count_all_focal_nodes  hist     run_profile   shell
count_all_nodes        hz       save_summary  spcc

Undocumented commands:
======================
text_names
```

This should confirm that your installation is correct.

Exit the prompt with Ctrl+z.

### 3. Configure the collocation parameters. 







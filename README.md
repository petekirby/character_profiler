# character_profiler 

## System Requirements - OSX Only 

### Python3

You'll need python3+ to run character_profiler. Follow these steps:

#### 1. Install brew (a package manager for OSX).

  - Open Terminal.app (located in Applications/Utilities/Terminal.app)
  - Paste this line into the command prompt:
  `ruby -e "$(curl -fsSkL raw.github.com/mxcl/homebrew/go)"`
  - The installation may take a few minutes.
  - When it has successfully run, type this command into the command line:
  `brew -v`, and you should see confirm the version (currently 0.9.9) of brew you just installed.
  
#### 2. Install python3 with brew
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

There are two relevant files that need to be modified when you want to run different jobs. First, jobs.py.

#### Jobs.py

This file lists all the collocations a user can run when they are inside the console prompt.

Jobs must have unique names.

I would suggest running no more than 20 jobs (20 lines in jobs.py) at a time. Optimizations to come, but don't rely on this 
becoming more efficient any time soon.

Two select 20 jobs, remove the hash (#) before each job. Like this:

```python

#  'raw_freq' : ('all_chars', 'dummy_set', 'stopwords', 'delimiters', 50), DON'T UNCOMMENT THIS LINE
    'job1' : ('high_god', 'punishment', 'stopwords', 'delimiters', 50),
    'job2' : ('high_god', 'reward', 'stopwords', 'delimiters', 50),
    'job3' : ('high_god', 'reduced_punishment', 'stopwords', 'delimiters', 50),
    'job4' : ('high_god', 'reduced_reward', 'stopwords', 'delimiters', 50),
    'job5' : ('high_god', 'ubc_emotion', 'stopwords', 'delimiters', 50)
   # 'job6' : ('high_god', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job7' : ('high_god', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job8' : ('high_god', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job9' : ('high_god', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job10' : ('high_god', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),

```

If you do this, only jobs1-jobs5 will be run. Everything else will be ignored. Add the # back once finished.
Sometimes you will have a list of hundreds of jobs. The easiest way to keep track is to take note of completed jobs.

In python all collections or lists of items are comma separated, make sure that each line has a comma at the end if you intend to perform that job. 

Any line in the whole body of code that begins with a # will not be read or "ran" by the python compiler.

#### Classes.py

Classes.py and jobs.py work together. Classes.py contains the lists of character classes that the user wants to generate collcations for. You will notice that the names given to classes are the same used in jobs.py. If they don't match, they wont run.

Example:

```python

From jobs.py
 'job1' : ('high_god', 'punishment', 'stopwords', 'delimiters', 50),
 
From classes.py
 'high_god' : ('天','帝','上帝','后帝','天主','天地','神君','天子'),
```

Note that high_god is the same in both places.

You can add or remove any classes from this file as you please. Note the syntax, however:

The name has quotes: `'class_name'`
Followed by a colon: `:`
Followed by an open bracket: `(`
Followed by a list of characters, each comma separated and single-quoted: `'A', 'B', 'C'`



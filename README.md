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

This command should return a list of commands (type 'help' and then the command name for help).

This should confirm that your installation is correct.

Exit the prompt with Ctrl+z.

### 3. Configure the collocation parameters. 

There are two relevant files that need to be modified when you want to run different jobs. First, jobs.py.

#### Jobs.py

This file lists all the collocations a user can run when they are inside the console prompt.

Jobs must have unique names.

It is no longer necessary to limit the number of jobs run at the same time.

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

The name has quotes:                                                      `'class_name'`<br>
Followed by a colon:                                                      `:`<br>
Followed by an open bracket:                                              `(`<br>
Followed by a list of characters, each comma separated and single-quoted: `'A', 'B', 'C'`<br>
Followed by a closed bracket:                                             `)`<br>

**As with any changes you make to files in this package, if you are not familiar with python, look carefully at how the syntax is implemented and make your content changes accordingly.

### 2. Generate Collocation Data

* Note, the profiler will currently generate data at the 50,10,5,2,1,sentence levels. This configuration can be changed.

Open Terminal.app and paste in the following line:<br>

`cd ~/Desktop/character_profiler/modules/`<br>

Then type:<br>

`python3 console.py` <br>

You will see the `=>>` prompt you saw before when testing the installation. To load all the texts and generate profiles for each character in each character class type: <br>

`load`<br>

This process can take a long time, depending on how long your character class lists are. Be prepared to wait anywhere from 20-40 minutes, perhaps longer.<br>

Once loaded, you'll see the `=>>` prompt again. To generate the collocation data, type:

`jobs`<br>

This will run all the jobs in jobs.py. They should only take a matter of minutes (the bulk of work resides in the first step). Once finished, all the collocation data is cached, which means you have to export to CSV before you can read it. Do this by typing: <br>

`save_summary` <br>

into the prompt.

To summarize:

1. Get to prompt: `cd...`
2. `=>>python3 console.py`
3. `=>>load`
4. `=>>jobs`
5. `=>>save_summary`
6. Exit, ctrl+z, the prompt.
7. Change name of output file to something unique (i.e. jobs1.csv)
8. Comment out jobs/classes from previous job (if applicable). Remove (#) hashes from the next set of jobs/classes. Save jobs.py and classes.py after the changes.
9. Go to #2.

This will save a document called 'summary.csv' to your character_profiler directory. <br>
<br>
<br>
<br>
####Change the file from summary.csv to 'jobs1.csv' or something unique before proceeding to the next job--otherwise your previous data will be overwritten.
<br>
<br>
<br>

Each line in this files output represents something like:

[collocationPairs_textName, countAt10, countAt5, ....]

Please read the CSV header line to get the specifics.

### 3. Finishing Touches

After running all your jobs (if 100, then 5 * 20 runs) and saving your csv's uniquely, combine them into a single file. Now you have a master csv file that can be parsed or analysed with your favorite tool or statistics package (R, Excel, etc.).

#### Please create an issue for any changes, suggestions, or comments.

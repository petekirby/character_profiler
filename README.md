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

To select a number of jobs, remove the hash (#) before each job. Like this:

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
Sometimes you will have a list of hundreds of jobs. The easiest way to keep track is to take note of completed jobs. Instructions to run jobs is below.

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


**For the classes/jobs you are not using in classes.py/jobs.py, comment them out. To 'comment something out' in programming-speak is to remove them from executable code. You can do this, as noted above, by putting a # before any line you want commented out. So if you aren't using the high_god and punishent class in a current job, comment out those lines of code.


## Running character_profiler

### 1. Confirm File Configurations
Once you have selected your classes and jobs, and commented out all unused code, you should have something like:

classes.py

```python

classes = {

    'ignore' : (' ','\n','\r','\t'),

    'delimiters' : ('。'),

    'stopwords' : ('#@','，','、','「','」','：','；','『','』','《','》','，','、','「','」','：','；','『','』','之','不','也','以','而','其','為','曰','者','子','有','於','十','則','無','所','故','三','二','一','是','與','夫','可','五','將','使','何','至','四','矣','自','此','太','謂','如','乃','百','皆','乎','于','在','非','六','諸','必','然','若','及','未','萬','吾','焉','我','復','千','亦','九','七','方','元','正','多','西','足','又','高','內','當','去','北','來','氏','外','同','受','反','少','常','過','后','作','因','雖','始','里','請','女','右','敢','前','易','求','說','左','起','會','定','通','對','哉','難','稱','屬','宜','聽','終','遠','盡','異','進','初','甚','本','止','興','耳','廣','益','應','還','絕','往','己','邪','固','首','由','共','徒','任','更','惠','少','文','景','武','昭','宣','元','成','哀','平','更始','光武','章','和','殤','安','順','沖','質','桓','獻','昭烈'),

   

    ### High Gods and Deities ###


     'high_god' : ('天','帝','上帝','后帝','天主','天地','神君','天子'),

     'deity' : ('仙','土','妖','姦','岳','河','神','辟','靈','風','鬼','魅','人鬼','仙人','仙者','儺神','夜叉','大神','天子','明神','神仙','神明','神祇','螭魅','鬼神'),

    # 'stoplisted_di' : ('惠帝','少帝','文帝','景帝','武帝','昭帝','宣帝','元帝','成帝','哀帝','平帝','更始帝','光武帝','章帝','和帝','殤帝','安帝','順帝','沖帝','質帝','桓帝','獻帝','昭烈帝'),

    ....
    ....
    ....

     'punishment' : ('刑','坐','完','尸','廢','懲','拶','枷','法','治','箠','箈','耐','誅','讞','辜','阱','髡','五刑','刀杖','刑戮','刑罰','刑辟','奪爵','戮辱'),

     'reward' : ('償','勞','胙','賞','賜','酬','勞酒','報償','慶賞','爵賞'),

    # 'reduced_punishment' : ('刑','坐','完','尸','廢','懲','拶','枷','法','治','箠','箈','耐','誅','讞','辜','阱','髡'),

    # 'reduced_reward' : ('償','勞','胙','賞','賜','酬'),
    
    ....
    ....
    ....
    # 'super_reduced_reward' : ('償','賞','賜')
    }

```

Note the final closing brace `}` has no # in front of it.
The `....` refer to omitted code.


jobs.py

```python
jobs = {
  ....
  ....
  ....

#  'raw_freq' : ('all_chars', 'dummy_set', 'stopwords', 'delimiters', 50), DON'T UNCOMMENT THIS LINE
   'job1' : ('high_god', 'punishment', 'stopwords', 'delimiters', 50),
   'job1' : ('high_god', 'punishment', 'stopwords', 'delimiters', 50),
   'job13' : ('deity', 'punishment', 'stopwords', 'delimiters', 50),
   'job14' : ('deity', 'reward', 'stopwords', 'delimiters', 50),
   # 'job25' : ('stoplisted_di', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job26' : ('stoplisted_di', 'reward', 'stopwords', 'delimiters', 50),
   
   ....
   ....
   ....
}
```

Having something 'like' the above to configurations will ensure that you can run the profiler.


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

### 3. Frequency

If you want to get frequencies for characters do exactly the sames steps as in '2. Generate Collocation Data', except in step five, change <br>

5. `=>>save_summary` <br>

to <br>

5. `=>>hz` <br>

You will be asked to add a character class and characters. In a text editor create a list with your class and characters that will look something like: <br>

`high_god,天,帝,上帝,后帝`

Please note the syntax changes. The class name is exactly as written in the code, followed by any characters you want to get the frequency of. Each of these is comma-separated, no quotes.

After entering the class and characters for which you want collocations, press enter. This will immediately run the frequency count and save a file in your character_profiler directory. 

### 4. Finishing Touches

After running all your jobs (if 100, then 5 * 20 runs) and saving your csv's uniquely, combine them into a single file. Now you have a master csv file that can be parsed or analysed with your favorite tool or statistics package (R, Excel, etc.).

#### Please create an issue for any changes, suggestions, or comments.

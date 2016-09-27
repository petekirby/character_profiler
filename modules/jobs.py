jobs = {

    
'''
Order : focal, compare, stopwords, delimiters, maxcost

Take note, the focal character comes first.

For Chinese texts in the ctext corpus, please use the standard stopword list included in classes.py

Delimiters list was created after some general text scrubbing so will not be reliable on any corpus.

*****
Maxcost
*****

Maxcost refers to the total distance that character_profiler will look to the left and right of a 
given focal character. Setting this number low/high will decrease/increase processing time linearly. 
Unless interested in generating large collocation profiles, try and keep it low lest it eat all your RAM.


Note also that job names (i.e. 'job1', 'job2') are totally arbitrary. So long as no two names collide,
any name will do.

'''

#  'raw_freq' : ('all_chars', 'dummy_set', 'stopwords', 'delimiters', 50), DON'T UNCOMMENT THIS LINE
   # 'job1' : ('high_god', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job2' : ('high_god', 'reward', 'stopwords', 'delimiters', 50),
   # 'job3' : ('high_god', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job4' : ('high_god', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job5' : ('high_god', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job6' : ('high_god', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job7' : ('high_god', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job8' : ('high_god', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job9' : ('high_god', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job10' : ('high_god', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job11' : ('high_god', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job12' : ('high_god', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job13' : ('deity', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job14' : ('deity', 'reward', 'stopwords', 'delimiters', 50),
   # 'job15' : ('deity', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job16' : ('deity', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job17' : ('deity', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job18' : ('deity', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job19' : ('deity', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job20' : ('deity', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job21' : ('deity', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job22' : ('deity', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job23' : ('deity', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job24' : ('deity', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job25' : ('stoplisted_di', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job26' : ('stoplisted_di', 'reward', 'stopwords', 'delimiters', 50),
   # 'job27' : ('stoplisted_di', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job28' : ('stoplisted_di', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job29' : ('stoplisted_di', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job30' : ('stoplisted_di', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job31' : ('stoplisted_di', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job32' : ('stoplisted_di', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job33' : ('stoplisted_di', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job34' : ('stoplisted_di', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job35' : ('stoplisted_di', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job36' : ('stoplisted_di', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job37' : ('stoplisted_tian', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job38' : ('stoplisted_tian', 'reward', 'stopwords', 'delimiters', 50),
   # 'job39' : ('stoplisted_tian', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job40' : ('stoplisted_tian', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job41' : ('stoplisted_tian', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job42' : ('stoplisted_tian', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job43' : ('stoplisted_tian', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job44' : ('stoplisted_tian', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job45' : ('stoplisted_tian', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job46' : ('stoplisted_tian', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job47' : ('stoplisted_tian', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job48' : ('stoplisted_tian', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job49' : ('reduced_deity', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job50' : ('reduced_deity', 'reward', 'stopwords', 'delimiters', 50),
   # 'job51' : ('reduced_deity', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job52' : ('reduced_deity', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job53' : ('reduced_deity', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job54' : ('reduced_deity', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job55' : ('reduced_deity', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job56' : ('reduced_deity', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job57' : ('reduced_deity', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job58' : ('reduced_deity', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job59' : ('reduced_deity', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job60' : ('reduced_deity', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job61' : ('reduced_gods', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job62' : ('reduced_gods', 'reward', 'stopwords', 'delimiters', 50),
   # 'job63' : ('reduced_gods', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job64' : ('reduced_gods', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job65' : ('reduced_gods', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job66' : ('reduced_gods', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job67' : ('reduced_gods', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job68' : ('reduced_gods', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job69' : ('reduced_gods', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job70' : ('reduced_gods', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job71' : ('reduced_gods', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job72' : ('reduced_gods', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job73' : ('tianzi', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job74' : ('tianzi', 'reward', 'stopwords', 'delimiters', 50),
   # 'job75' : ('tianzi', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job76' : ('tianzi', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job77' : ('tianzi', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job78' : ('tianzi', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job79' : ('tianzi', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job80' : ('tianzi', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job81' : ('tianzi', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job82' : ('tianzi', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job83' : ('tianzi', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job84' : ('tianzi', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job85' : ('barbarians', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job86' : ('barbarians', 'reward', 'stopwords', 'delimiters', 50),
   # 'job87' : ('barbarians', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job88' : ('barbarians', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job89' : ('barbarians', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job90' : ('barbarians', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job91' : ('barbarians', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job92' : ('barbarians', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job93' : ('barbarians', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job94' : ('barbarians', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job95' : ('barbarians', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job96' : ('barbarians', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job97' : ('chinese', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job98' : ('chinese', 'reward', 'stopwords', 'delimiters', 50),
   # 'job99' : ('chinese', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job100' : ('chinese', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job101' : ('chinese', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job102' : ('chinese', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job103' : ('chinese', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job104' : ('chinese', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job105' : ('chinese', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job106' : ('chinese', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job107' : ('chinese', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job108' : ('chinese', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job109' : ('kinship', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job110' : ('kinship', 'reward', 'stopwords', 'delimiters', 50),
   # 'job111' : ('kinship', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job112' : ('kinship', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job113' : ('kinship', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job114' : ('kinship', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job115' : ('kinship', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job116' : ('kinship', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job117' : ('kinship', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job118' : ('kinship', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job119' : ('kinship', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job120' : ('kinship', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job121' : ('ancestors', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job122' : ('ancestors', 'reward', 'stopwords', 'delimiters', 50),
   # 'job123' : ('ancestors', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job124' : ('ancestors', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job125' : ('ancestors', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job126' : ('ancestors', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job127' : ('ancestors', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job128' : ('ancestors', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job129' : ('ancestors', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job130' : ('ancestors', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job131' : ('ancestors', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job132' : ('ancestors', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job133' : ('father', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job134' : ('father', 'reward', 'stopwords', 'delimiters', 50),
   # 'job135' : ('father', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job136' : ('father', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job137' : ('father', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job138' : ('father', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job139' : ('father', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job140' : ('father', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job141' : ('father', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job142' : ('father', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job143' : ('father', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job144' : ('father', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job145' : ('father_in_law', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job146' : ('father_in_law', 'reward', 'stopwords', 'delimiters', 50),
   # 'job147' : ('father_in_law', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job148' : ('father_in_law', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job149' : ('father_in_law', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job150' : ('father_in_law', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job151' : ('father_in_law', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job152' : ('father_in_law', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job153' : ('father_in_law', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job154' : ('father_in_law', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job155' : ('father_in_law', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job156' : ('father_in_law', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job157' : ('parent', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job158' : ('parent', 'reward', 'stopwords', 'delimiters', 50),
   # 'job159' : ('parent', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job160' : ('parent', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job161' : ('parent', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job162' : ('parent', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job163' : ('parent', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job164' : ('parent', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job165' : ('parent', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job166' : ('parent', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job167' : ('parent', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job168' : ('parent', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job169' : ('mother', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job170' : ('mother', 'reward', 'stopwords', 'delimiters', 50),
   # 'job171' : ('mother', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job172' : ('mother', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job173' : ('mother', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job174' : ('mother', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job175' : ('mother', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job176' : ('mother', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job177' : ('mother', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job178' : ('mother', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job179' : ('mother', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job180' : ('mother', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job181' : ('mother_in_law', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job182' : ('mother_in_law', 'reward', 'stopwords', 'delimiters', 50),
   # 'job183' : ('mother_in_law', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job184' : ('mother_in_law', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job185' : ('mother_in_law', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job186' : ('mother_in_law', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job187' : ('mother_in_law', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job188' : ('mother_in_law', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job189' : ('mother_in_law', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job190' : ('mother_in_law', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job191' : ('mother_in_law', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job192' : ('mother_in_law', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job193' : ('grandfather', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job194' : ('grandfather', 'reward', 'stopwords', 'delimiters', 50),
   # 'job195' : ('grandfather', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job196' : ('grandfather', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job197' : ('grandfather', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job198' : ('grandfather', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job199' : ('grandfather', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job200' : ('grandfather', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job201' : ('grandfather', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job202' : ('grandfather', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job203' : ('grandfather', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job204' : ('grandfather', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job205' : ('human_controls', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job206' : ('human_controls', 'reward', 'stopwords', 'delimiters', 50),
   # 'job207' : ('human_controls', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job208' : ('human_controls', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job209' : ('human_controls', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job210' : ('human_controls', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job211' : ('human_controls', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job212' : ('human_controls', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job213' : ('human_controls', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job214' : ('human_controls', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job215' : ('human_controls', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job216' : ('human_controls', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job217' : ('evil_humans', 'punishment', 'stopwords', 'delimiters', 50),
   # 'job218' : ('evil_humans', 'reward', 'stopwords', 'delimiters', 50),
   # 'job219' : ('evil_humans', 'reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job220' : ('evil_humans', 'reduced_reward', 'stopwords', 'delimiters', 50),
   # 'job221' : ('evil_humans', 'ubc_emotion', 'stopwords', 'delimiters', 50),
   # 'job222' : ('evil_humans', 'ubc_cognition', 'stopwords', 'delimiters', 50),
   # 'job223' : ('evil_humans', 'ubc_religion', 'stopwords', 'delimiters', 50),
   # 'job224' : ('evil_humans', 'ubc_morality', 'stopwords', 'delimiters', 50),
   # 'job225' : ('evil_humans', 'ubc_morality_positive', 'stopwords', 'delimiters', 50),
   # 'job226' : ('evil_humans', 'ubc_morality_negative', 'stopwords', 'delimiters', 50),
   # 'job227' : ('evil_humans', 'super_reduced_punishment', 'stopwords', 'delimiters', 50),
   # 'job228' : ('evil_humans', 'super_reduced_reward', 'stopwords', 'delimiters', 50),
}

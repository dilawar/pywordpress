~~~~ 
title: Using Python to download submitted assignments from Moodle
type: post
status: publish
id: 546
tag: download assignment from moodle
tag: moodle
tag: python-moodle
category: Programming
category: Python
~~~~

UPDATE : This will not work on new moodle used in IIT Bombay. New moodle
allows downloading all assignments as a single file. You can use[this
script](https://github.com/dilawar/Scripts/blob/master/moodle_assignment_part.py)
to extract individual assignments. Downloading each student's assignment
from moodle could be a real pain especially when you have to grade them.
Last night, I worked my ass off and created this [Python
scripts](https://github.com/dilawar/MyPublic/tree/master/MoodleIITB)
which can fetch assignments from Moodle course page. In your home folder
`.moodlerc` file must exists with all details (see the sample file on
[git
repository](https://github.com/dilawar/MyPublic/tree/master/MoodleIITB)).
It depends heavily of `mechanize` python-library. Each line (not
suffixed with char \#) is configuration variable in `key = value `
format. Username and password fields are usual moodle username and
password. If you leave password field empty then you have to submit it
during exectution. Next is `course` which should be a regular pattern
i.e. if course is ` EE 705 : V L S I Design Lab ` then
`course = EE 705 ` would be fine. Notice that you do not have to enclose
any text string using commas etc. If you have two courses with same
regular pattern then only first of them will be selected. Then we have
`activities` which shout be set to `Assignments` (open your moodle
course page and see what is exact spelling in your course page for
assignment, casing of characters matters.) Once you will click on
assignments, there would be more than one assignments, all of them can
be put using `activity = ` line. For instance, in sample file
`Lab session 1` and `Lab session 2` are two assignments. It will take
care of the rest. It will go to each student, create a directory in
his/her name and download submission into that directory. If
`extract=true` then it will also extract archive files. Make sure only
one archive file is submitted per assignment. This is the first version
of this script and I may work on it after some time. If you make any
change please share it with online community. PS : Some moodle server
does not allow robots and automatic logging. To overcome this, this
scripts sends wrong information to moodle-server. It mimics "mozilla
firefox on ubuntu". If you dont have any ethical issues with such
non-sense then you are more than welcome to use this script.  Released
under GNU-GPL Lesser Public License.

~~~~ 
title: Managing music using mpd/mpc
type: post
status: publish
id: 1029
tag: Advanced Linux Sound Architecture
tag: MPC
tag: MPD
tag: Music Player Daemon
category: Linux category: NoGuiNoMouseNoProblem
~~~~

*Music Player Daemon* (MPD) is a lightweight application. It hardly
takes any cpu. Moreover it runs in background and does not clutter and
workspace. If you dont use mouse frequently or wants to avoid it
(programmers use keyboard), then mpd is for you. It is one of those
applications which does one job at a time and does it really well (well,
if you get is working once which is not very hard). The job of MPD is to
read/decode audio files available in its music directory on demand (one
can specify it in config file) and create sound. It them make sound
available to user using
[ALSA](http://www.alsa-project.org "Advanced Linux Sound Architecture")
(or some other) soundcard driver. How to setup MPD is explained nicely
on arch-linux wiki (gentoo wiki should also have something) otherwise
there is some help always available on
[http://unix.stackexchange.com](http://unix.stackexchange.com) or
[http://superuser.stackexchange.com](http://superuser.stackexchange.com).
Here is my config file stored as \~/.mpd/mpdconf. All of my music is
kept in/download to `~/Bhandar/Music` .

A minimal example for mpdconf file which works on my system.

~~~~ {.sourceCode .bash}
music_directory "~/Bhandar/Music/"
playlist_directory "~/.mpd/playlists" 
db_file "~/.mpd/tag_cache" 
log_file "~/.mpd/mpd.log"
pid_file "~/.mpd/pid" 
state_file "~/.mpd/state"
bind_to_address "127.0.0.1" 
port "6600" log_level "default"
save_absolute_paths\_in\_playlists "yes" 
metadata_to_use "artist,album,title,track,name,genre,date,composer,performer,disc"
follow_inside_symlinks "yes" password "gabbar@read,add,control,admin"
default_permissions "read,add,control" 
input { 
    plugin "curl" 
} 
audio_output {
    type "alsa" name "My ALSA Device" 
}
~~~~

On ubuntu, if you install mpd, a file is automatically created in
/etc/mpd.conf. You can edit this file also. You have to create some
paths before you can continue, if you create a config file like mine.

     $ mkdir -p ~/.mpd/playlists 
     $ touch ~/.mpd/playlists 

Now type mpd in terminal, if it starts without any messages then we are
good to go. Sometimes, you might get this warning. Failed to bind to
'[127.0.0.1:6600](http://127.0.0.1:6600)': Address already in use. This
means mpd is already running. Check the running process

     $ ps -e | grep mpd 
     14073 ?    00:00:28 mpd 

Terminate it,

     $ sudo pkill mpd 
     $ sudo pkill mpd 

or \$ sudo kill -9 14073 \$ sudo kill -9 14073

Check again.

     $ ps -e | grep mpd 
     $ ps -e | grep mpd 

This time we should have an empty line. Run mpd again. If there is a
problem, then time to ask people or debug by yourself.

Music player client (MPC)
-------------------------

Now we need a client to send commands to mpd. MPC is a command line tool
(perl scripts) while gmpc is a gui-based client. Mind you, mpd does not
have those advance features of rythmbox and bashee. If you like to use
amplifier and other fancy feature to enhance the sound, there is no
point reading further. The very first thing we need to do, it to update
database.

     $ mpc -h gabbar@localhost update 
     Updating DB (#1) ... 

Password 'gabbar' was given in conf file. Without it, we will not have
access to update the database. Check what password you have given and
see the results. This much we need to do only once.

Creating playlists and playing them
-----------------------------------

\`mpc help\` command will show you how to search for songs and add them
to playlist. I woluld suggest to learn it the hard way. I have written
few scripts to make my life slightly easier (short term memory losses).
Script [1] does search for a given word in an of songs and add them all
matched songs.

     $./mpc_search_add.sh "bhimsen joshi" 
     $./mpc_search_add.sh "bhimsen joshi" 

It will add songs having 'bhimsen joshi' in their metadata, if they are
not already added. Another common problem is to play the fav song
quickly. There is script [3] for this also. For instance if I want to
listen to "Yellow, Cold play" then I do the following.

     $./mpc_play "yellow" 
     [INFO] Searching for yellow 
     [INFO] No song found for your query. 

Ok, yellow is not found that means it is not added to playlist. Use
script 2 to add "Coldplay" to playlist. Menwhile, lets play a song which
I am pretty sure of having in my playlist: 'Seene main jalan'. It will
play the first match.

     #./mpc_play "seene" 
     [INFO] A matching song is found in playlist at 1911 
     Seene main jalan - Gaman.mp3 
     [playing] #1911/1911  0:00/4:30 (0%) volume:100%  repeat: on  random: on  single: off  consume: off 

Depending on size of playlist, this might take 1-3 seconds. Next,
previous,

Play/pause and volume
---------------------

MPC comes with standard command to do them `mpc next`, `mpc previous`,
`mpc toggle` etc etc. Each windown manager allows key mapping. Map these
commands to some key combination. I use `Alt+Ctlr+<some_key>` for user
defined commands.

Deleting currently playing song or adding it to favs
----------------------------------------------------

A lot of songs gets downloaded and once in a while suddenly some random
guy starting singing about somebodys butt and breasts. Who wants such
sort of non-sense in ones playlist :-p. Sometimes a great songs appears
and you wish to add it to your a folder. Script [2] does both of these
functions. This acts on currently playing song. If you path to
music\_dir is different than mine, then you have to change the paths
accordingly. To delete currently playing song

     $./manage_mpc.sh -d 

To add the song to a folder of gems `~/Bhandar/Music/MyCollection`

     $./manage_mpc.sh -a 

You can bind these two commands to some keys. The important thing is
that these scripts must be executable (`chmod +x scipt_name`) and
available in system path (copy them to `/usr/local/bin` ). Script [4]
provides color-support in terminal which is needed for other scripts to
work. It should be in the same folder as other scripts. One can use it
for other purposes. Everyone loves colors.

[1]
[https://raw.github.com/dilawar/Scripts/master/mpc\_search\_add.sh](https://raw.github.com/dilawar/Scripts/master/mpc\_search\_add.sh)
[2]
[https://raw.github.com/dilawar/Scripts/master/manage\_mpc.sh](https://raw.github.com/dilawar/Scripts/master/manage\_mpc.sh)
[3]
[https://raw.github.com/dilawar/Scripts/master/manage\_play.sh](https://raw.github.com/dilawar/Scripts/master/mpc\_play.sh)
[4]
[https://raw.github.com/dilawar/Scripts/master/colors.sh](https://raw.github.com/dilawar/Scripts/master/colors.sh)

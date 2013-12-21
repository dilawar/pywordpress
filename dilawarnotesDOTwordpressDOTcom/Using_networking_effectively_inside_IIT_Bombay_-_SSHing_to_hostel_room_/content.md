~~~~ 
title: Using networking effectively inside IIT Bombay : SSHing to hostel room 
type: post
status: publish
id: 782
tag: ip
tag: nmap
tag: openssh
tag: scp
tag: ssh in iit bombay
category: IIT Bombay
~~~~

Having LAN is great for downloading movies and other stuff from other
connected computers really fast. And perhaps it is also good for playing
those taxi games. These are good enough reason for LAN to exists in the
life of an undergraduate. But a man (are you a man?) also need to work
(especially when he has finished his 2nd year of engineering) and how
can one uses this LAN to work effectively in IIT Bombay. First, do
yourself a favour, install Linux in your machine before continuing. And
do not pollute my blog by accessing it from windows [making a sarcastic
face]. Let's not be Homo Neanderthal and promise ourself that we will
not carry our laptop and its charger everywhere we go inside the campus
(unless there is no escape, such as showing-off your new-laptop etc.).
[Install openssh](https://help.ubuntu.com/community/AptGet/Howto) in
your machine and make sure that port 22 is listening to incoming
connections. You can check it by **`nmap`**  command. You need to
install it first. It is more powerful than primitive pinging (ping
10.14.42.7).

    dilawar@hobbes:~$ nmap localhost

    Starting Nmap 5.21 ( http://nmap.org ) at 2013-02-21 21:29 IST
    Nmap scan report for localhost (127.0.0.1)
    Host is up (0.00027s latency).
    Not shown: 995 closed ports
    PORT     STATE SERVICE
    22/tcp   open  ssh
    53/tcp   open  domain
    80/tcp   open  http
    631/tcp  open  ipp
    9418/tcp open  gitNmap done: 1 IP address (1 host up) scanned in 0.15 seconds

Great! We were interested in `22/tcp` port which is open. Now note down
the ip of your system which you can get it by `ip addr` or `ifconfig`
command. For example my ip is `10.14.42.7` and username is `dilawar`. 
Now my laptop is ready to accept any connection from any other computer
on LAN. Leave it on and roam in campus like a leopard. You can access
your laptop from anywhere now. Now I go to `pc-lab` and get a computer
with terminal (repeat with me 4 times, Windows sucks!). From there you
can check if you can ping your system. You must know the ip of your
laptop Now I can connect to my pc using `ssh` command. Do the following.

    ssh -X dilawar@10.14.42.7

And launch any command from terminal. Make sure to write capital X and
not small x. You can also use capital Y instead of 'y'. Now next time
you see someone carrying his/her laptop with him/her, you can call them
idiots and laugh like a maniac (in your head). You should also learn to
use **`scp`** command. Install `pinfo` and say `pinfo scp` and read the
damn thing. In next post, we'll learn how to setup git repository on
sharada server (or any server where you have account which you can
connect to using ssh.)

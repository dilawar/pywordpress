~~~~ 
title: IIT Bombay DC-Hub Network and Hub's IP Address
type: post
status: publish
id: 634
tag: IIT Bombay DC hublist
category: Linux
~~~~

If there are lot of enlightened (and pervert) users over LAN then there
would definitely be some Direct Connection (DC) hubs. And IIT Bombay is
no exception. DC-hubs are maintained by undergraduate students. They
download and share most of the data. I am greatly thankful to them for
sharing latest animated movies etc. They have the enthusiasm and energy
of young.

There is no fixed IP scheme for these hubs. When a new hub is created,
it is usually assigned a new ip-address according to the whims of its
creator. Therefore, there are no standard addressing scheme for hubs
besides 10.\*.\*.\*. The digit which follows the 10 is usually hostel
number, but I wouldn't count on it.

[This link](http://www.tinyurl.com/iitbdchubs) claims to maintain
currently active hubs. I have also started keeping ips of hub-list. See
this [page for
hub-list](https://github.com/dilawar/MyPublic/blob/master/OpenDC/hublist.txt).

To browse these hubs, one uses  open-dc clients. For windows, there are
many such applications as opendc, dcplusplus etc (ask your neighbor.).
For Linux users, at least following applications are available.

-   linuxdcpp - Sometimes this application hangs, slows down the system
    and refuses to start. But works well most the of the time. It's been
    around for a long time on Linux. Available in Ubuntu repositories.
-   valknut - User-interface is not great but it is lightweight and
    never hangs. Available in Ubuntu repositories. A great tool indeed.
    I will not slow down your system. Downside, not a great user
    interface.
-   [Eisalktdcpp](http://code.google.com/p/eiskaltdc/) - It is
    under-development and cross platform. It slows down the system
    significantly but it has many features e.g. scripting. Available in
    Ubuntu repositories. **UPDATE** It is working fine now on my Ubuntu
    machine. I have been using it for two-months and have given up the
    idea of modifying microdc2 for personal use. Eisalktdcpp is great
    and perhaps the best-bet around. You can also enable `spy-mode` to
    see what people are searching.
-   microdc2 - For command line junkies. You can get a fork from [my
    github](https://github.com/dilawar/microdc2). Irritating user-status
    are not printed in console in this fork. Also available in official
    Ubuntu repositories.

****

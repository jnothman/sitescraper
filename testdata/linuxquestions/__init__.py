#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [
    ('1.html', [
    """i just installed amarok and whenever i start it it says please select gstreamer output plugin but gstreamer is not an option for output plugings for me, but i do have gstreamer installed.""",
    """
    Quote:
    Originally posted by doralsoral
    i just installed amarok and whenever i start it it says please select gstreamer output plugin but gstreamer is not an option for output plugings for me, but i do have gstreamer installed.
    You may have to install gstreamer plugins. I would just ditch gstreamer for xine. Amarok can use the xine engine and thus play more media types.
    """,
    """gstreamer-plugins are already installed.""",
    """
    Quote:
    Originally posted by doralsoral
    gstreamer-plugins are already installed.
    So did you try using xine as the output plugin? Some distros have extra gstreamer plugins (not packaged with gstreamer-plugins), so also take a look into that.""",
    """Which version of gstreamer are you using? I think I ran into a similar problem and ended up downgrading to version 0.8.6 you might try that.""",
]),
    ('2.html', [
    """i have a problem...im on slackware 9 using webmin 1.100...but heres the problem..im trying to setup a virtual server so when sombody browses my site...example: something.mydomain.com it takes them to whatever i got the document root set to..but i cant get rid of the default for sum reason...if anybody can tell me how to get rid of the default virtual server i would really appreciate it...the default looks like this..therefore any address i put on my box...it auto takes em to the default virtual server which i dont want...

    Address Any
    Port Any
    Server Name myservername
    Document Root /home/artistik/public_html/

    i need to find a way to delete this offa webmin but it wont let me...""",
    """
    Quote:
    Originally posted by artistik
    i need to find a way to delete this offa webmin but it wont let me...
    What you should do if you're unhappy with what webmin does, is edit your /etc/apache/httpd.conf by hand, remove these entries, and put in your documentroot or whatever as you want.""",
    """well i did do that...i want so when ppl browse my web adress it takes em to what the document root says....but when i setup a virual server ie: something.mydomain.com and i got that set to a diff documentroot it still goes to the main document root...because webmin has the default virtual server set to any address...and i cant find a way to delete the default server on webmin =p""",
]),
    ('3.html', [
    """Hi,
    I've been trying to use my gmail from CLI.
    Here's my .fetchmailrc

    Code:

    poll pop.gmail.com with proto POP3 and options no dns
    user 'username@gmail.com' is 'username' here options ssl

    Obviously username is replaced with the real one. Also, POP is enabled in my gmail settings (I've been using thunderbird for a while)


    Here's my .muttrc
    Code:

    set pop_user="username@gmail.com"

    # My email account password
    set pop_pass="my password"

    # Too many email headers make reading a message difficult
    ignore *
    unignore From: To: Cc: Subject: Date: #Only these are shown in the header

    #To ensure that mutt does not put
    #'username@localhost.localdomain in From
    set from="username@gmail.com"
    set use_from=yes
    set envelope_from="yes"

    #The text editor I want to use to write emails
    #The default is emacs
    set editor="emacs -nw"


    the output of fetchmail -vk

    Code:

    sycamorex@debian205:~$ fetchmail -vk
    Enter password for username@gmail.com@pop.gmail.com: 
    fetchmail: 6.3.8 querying pop.gmail.com (protocol POP3) at Sun 23 Dec 2007 14:42:05 GMT: poll started
    Trying to connect to 66.2bla...bla..bla09/995...connected.
    fetchmail: Issuer Organisation: Equifax
    fetchmail: Unknown Issuer CommonName
    fetchmail: Server CommonName: pop.gmail.com
    fetchmail: pop.gmail.com key fingerprint: 44:A8:E9:2C:FB.....bla bla..blaB2:9E:F1:A9
    fetchmail: Server certificate verification error: unable to get local issuer certificate
    fetchmail: Server certificate verification error: certificate not trusted
    fetchmail: Server certificate verification error: unable to verify the first certificate
    fetchmail: POP3< +OK Gpop ready for requests from 83.4.bla... bla..blao24pf3879126ugd.0
    fetchmail: POP3> CAPA
    fetchmail: POP3< +OK Capability list follows
    fetchmail: POP3< USER
    fetchmail: POP3< RESP-CODES
    fetchmail: POP3< EXPIRE 0
    fetchmail: POP3< LOGIN-DELAY 300
    fetchmail: POP3< X-GOOGLE-VERHOEVEN
    fetchmail: POP3< UIDL
    fetchmail: POP3< .
    fetchmail: POP3> USER username@gmail.com
    fetchmail: POP3< +OK send PASS
    fetchmail: POP3> PASS *
    fetchmail: POP3< +OK Welcome.
    fetchmail: POP3> STAT
    fetchmail: POP3< +OK 0 0
    fetchmail: No mail for hemarcin@gmail.com at pop.gmail.com
    fetchmail: POP3> QUIT
    fetchmail: POP3< +OK Farewell.
    fetchmail: 6.3.8 querying pop.gmail.com (protocol POP3) at Sun 23 Dec 2007 14:42:07 GMT: poll completed
    fetchmail: normal termination, status 1

    when I open mutt and want to write an email - it says that email has been sent but then when I want to check it on my other email account nothing has been delivered.

    can you give me any hint. I'm working with mutt, fetchmail for the first time.

    thanks
    """,
    """Well, that's because you maybe just configured GETTING your mail, but not SENDING your mail?

    POP and fetchmail are about getting your mail from your POP/IMAP-account.

    Mutt is just your tool to compose the mail (your mail user agent) - now you need something to get it out there.

    In your case of using gmail it possibly involves relaying over gmail - which is possible.

    I use msmtp to send mail out after composing it in mutt. Msmtp is small and very simple - I don't need an entire sendmail on my notebook just to send out 50 mails a day.

    From within mutt, this would be something like this in your muttrc:

    set sendmail="/usr/local/bin/msmtp"

    And my msmtprc says for gmail-relaying something like this:

    account default
    host smtp.gmail.com
    port 587
    user YOU@gmail.com
    password PASSWORD
    protocol smtp
    tls_starttls on
    logfile /home/MYHOME/.msmtp.log

    This is totally independent from your POP-fetchmail-setting.""",
    """thanks, makes sense

    However, what I get in Mutt when I try to send an email is:

    Quote:
    msmtp: envelope from address YOU@gmail.com not accepted by the server
    msmtp: server message: 530 5.7.0 Must issue a STARTTLS command first k5sm707424nfh.18
    msmtp: could not send mail (account default from /home/sycamorex/.msmtprc)
    Quote:
    Error sending message, child exited 65 (Data format error.).
    and the log entry from .msmtp.log

    Quote:
    Dec 23 16:10:12 host=smtp.gmail.com tls=off auth=off from=YOU@gmail.com recipients=SOMEBODY@gmail.com smtpstatus=530 smtpmsg='530 5.7.0 Must issue a STARTTLS command first k5sm707424nfh.18' errormsg='envelope from address YOU@gmail.com not accepted by the server' exitcode=EX_DATAERR
    my .msmtprc

    Quote:
    account default
    host smtp.gmail.com
    port 587
    user YOU@gmail.com
    password blablabal
    protocol smtp
    tls_starttls on
    logfile /home/sycamorex/Mail/.msmtp.log
    thanks""",
    
]),
    ('4.html', [
    """Hi. I use fluxbox as my window manager under Ubuntu, and recently I have been hearing a lot about XGL and Compiz. I know Compiz is a window manager, so I can't get the neat effects with fluxbox. I was wondering, however, if Compiz can run stand alone, without having to load a window environment. Is this possible? If so, how would I go about doing this? Thanks.""",
    """You run xgl and compiz with gnome or kde.""",
    """So there is no ability to run compiz in stand-alone? Are there any other xgl window managers that support this that you know of?""",
    """Hi, After posting this I did some more research, and it turns out that you need a 'Desktop Environment', rather than a 'window manager' in order to use it. You can use KDE, Gnome, or XFCE since they are Desktop Environments. You can't use it with fluxbox or other plain window managers.""",
    """
    Quote:
    Originally Posted by Blazeix
    Hi, After posting this I did some more research, and it turns out that you need a 'Desktop Environment', rather than a 'window manager' in order to use it. You can use KDE, Gnome, or XFCE since they are Desktop Environments. You can't use it with fluxbox or other plain window managers.
    What is you are using gdm (or kdm i guess) with fluxbox on top of it?"""
]),
    ('5.html', [
    """Just wondering the topic of enson vs Cpanel, can someone clear up which one is better and the major differences please?""",
    """
    Quote:
    Originally posted by clacy
    Just wondering the topic of enson vs Cpanel, can someone clear up which one is better and the major differences please?
    Okay first of all, what does your Title of this thread have to do with your question?

    And secondly, this question is not a question in regards to this site itself, which the forum you placed it in was made for. I've requested to have this thread moved to a more appropiate forum and I'd like to ask you make better thread titles in the future.""",
    """Moved: This thread is more suitable in Linux - Software and has been moved accordingly to help your thread/question get the exposure it deserves.

    --jeremy""",
]),
    ('6.html', [
    """Is there any software on linux that can kind of mock or be better than Macromedia's Dreamweaver, I want to be able to do a website with the capability of changing form design view to code view and for it to do the html for you because that is just a waist of time. If anyone knows something similar please tell me. Thanks.

    -luis""",
    """have you given bluefish a try?""",
    """is there any others?""",
    """Originally posted by lramos85
    is there any others?
    There is also Quanta and Screem that I know of but nothing in comparison as these are really true WYSIWYG editors. Your not going to have the "view page" type function with these.

    It is possible to just load Dreamweaver using wine.

    www.frankscorner.org"""
]),
    ('7.html', [
    """Ok, MDK 10, 2.6 Kernel, trying to help out my wireless problem (using intelpro2200 wireless) and I get this:
    [jaster@localhost jaster]$ cd ipw2200-0.2
    [jaster@localhost ipw2200-0.2]$ ls
    CHANGES ipw2200_eeprom.c ipw2200_main.c ipw2200_wx.h README.ipw2200
    FILES ipw2200_fw_dma.c ipw2200_rxtx.c ISSUES
    INSTALL ipw2200.h ipw2200_rxtx.h LICENSE
    ipw2200_bh.c ipw2200_hw.c ipw2200_wx.c Makefile
    [jaster@localhost ipw2200-0.2]$ make
    <stdin>:1:28: linux/rhconfig.h: No such file or directory
    make -C /lib/modules/2.6.3-7mdk/build SUBDIRS=`pwd` modules
    make[1]: Entering directory `/usr/src/linux-2.6.3-7mdk'
    CC scripts/empty.o
    cc1: Permission denied: opening dependency file scripts/.empty.o.d
    Assembler messages:
    FATAL: can't create scripts/.tmp_empty.o: Permission denied
    make[2]: *** [scripts/empty.o] Error 1
    make[1]: *** [scripts] Error 2
    make[1]: Leaving directory `/usr/src/linux-2.6.3-7mdk'
    make: *** [default] Error 2


    Can anyone interpret what the problem is and how I might go about solving it? I'm a newb so keep it simple lol, thanks.""",
    """
    Code:

    FATAL: can't create scripts/.tmp_empty.o: Permission denied

    that's your problem... what are the permissions on /usr/src/linux-2.6.3-7mdk? have you tried running the "make" as root?""",
    """The permissions would all be at defualt levels. How do I 'run as root'? The stuff is in my home directory atm, please enlighten me lol (yes I'm a total newb but this is how I learn, thanks)""",
]),
    ('8.html', [
    """Hi everybody,
    I want to know that whether we can talk on Gtalk network in Linux. Although there is no official software from google, it has released some code for other clients to connect to the network so that people can talk thru Gtalk in Linux. Plz help me, as most of my friends use Gtalk and Windows and they get irritated when they hear the word "Linux".

    Robin""",
    """
    Quote:
    Originally Posted by arun-linux View Post
    Hi everybody,
    I want to know that whether we can talk on Gtalk network in Linux. Although there is no official software from google, it has released some code for other clients to connect to the network so that people can talk thru Gtalk in Linux. Plz help me, as most of my friends use Gtalk and Windows and they get irritated when they hear the word "Linux".

    Robin
    A brief Google search turns up:

    http://www.google.com/talk/otherclients.html

    Pidgin and Kopete both support Gtalk, and run native on Linux.""",
    """Gtalk uses the Jabber protocol.
    I use Gaim(now Pidgin).

    Add a new account.

    select the jabber protocol.
    enter your gmail id (the part before the '@' in full id) as screen name.
    enter "gmail.com" as server

    example:
    Protocol: jabber
    screen name: john.mccain
    server: gmail.com
    password: ********
    local alias: john

    Voila!!!"""
]),
    ('9.html', [
    """I have installed iscsi-target RHEL Machine with the following steps:

I have the following partition table:

1. I downloaded iscsi-target package and followed the process:
Code:

[root@localhost iscsitarget]# df -h
Filesystem            Size  Used Avail Use% Mounted on
/dev/sda2              29G  7.4G   20G  27% /
/dev/sda1             107M  9.6M   92M  10% /boot
none                  721M     0  721M   0% /dev/shm
/dev/sda3              20G   76M   19G   1% /home

Code:

#vi /etc/ietd.conf
Target iqn.2008-07.com.scsilinux:storage.disk2.sys1.xyz
        # Users, who can access this target. The same rules as for discovery
        # users apply here.
        # (no users means anyone can access the target)
        #IncomingUser joe secret
        #OutgoingUser jim 12charpasswd
        # Logical Unit definition
        # You must define one logical unit at least.
        # Block devices, regular files, LVM, and RAID can be offered
        # to the initiators as a block device.
        Lun 0 Path=/dev/sda3,Type=fileio

Saved the file.
And Then Started the service:
Code:

[root@localhost iscsitarget]# service iscsi-target restart
Stoping iSCSI target service:                              [  OK  ]
Starting iSCSI target service:                             [  OK  ]

Now, I went to setup iscsi-client on new system as:
Installed the Needed PAckage.
Pointed iscsi.conf to the target Machine.
And Then:
Code:

[root@BL02DL385 ~]# iscsi-ls
*******************************************************************************
SFNet iSCSI Driver Version ...4:0.1.11-6(03-Aug-2007)
*******************************************************************************
TARGET NAME             : iqn.2008-07.com.logica.bl04mpdsk:storage.lun1
TARGET ALIAS            :
HOST ID                 : 2
BUS ID                  : 0
TARGET ID               : 0
TARGET ADDRESS          : 10.14.236.134:3260,1
SESSION STATUS          : DROPPED AT Thu Jul 10 05:19:36 IST 2008
SESSION ID              : ISID 00023d000001 TSIH 300
*******************************************************************************
[root@BL02DL385 ~]# iscsi-rescan

It means Its Working and showing the target machine.

Now I am confused of "entry being made in iscsi.conf.Is entry
Code:

Path=/dev/sda3

correct?

All I am attempting to setup is Red Hat Cluster with two nodes as initiator and the one target Machine.I havent any shared storage an dI am setting up Alternative to the Shared Storage.

Pls Help""",
"""Its Done.Just Pointed the Entry to /dev/sda6 which is unformatted partition.
I need few more help.
Code:

When I click on File System on Cluster Tool...It asked for Mount point, Device, Option,Name,filesystem id, filesystem type..What Entry I need to make ?

pls help"""
]),
    ('10.html', [
"""Got to the final step of setup.

Start the apache daemon by using

Quote:
[root@cpe-24-195-24-133 httpd-2.2.0]# /usr/local/apache2/bin/apachect1 start
-bash: /usr/local/apache2/bin/apachect1: No such file or directory
any clue? Maybe I downloaded something wrong or im in the wrong dir to be doing this?

update:

Quote:
[root@cpe-24-195-24-133 ~]# cd /
[root@cpe-24-195-24-133 /]# ls
bin dev home lost+found misc net proc sbin srv tmp var
boot etc lib media mnt opt root selinux sys usr
[root@cpe-24-195-24-133 /]# cd /usr/local
[root@cpe-24-195-24-133 local]# ls
apache2 bin etc games include lib libexec mysql sbin share src
[root@cpe-24-195-24-133 local]# cd apache2
[root@cpe-24-195-24-133 apache2]# ls
bin cgi-bin error icons lib man modules
build conf htdocs include logs manual
[root@cpe-24-195-24-133 apache2]# cd bin
[root@cpe-24-195-24-133 bin]# ls
ab apu-1-config dbmmanage htcacheclean htpasswd logresolve
apachectl apxs envvars htdbm httpd rotatelogs
apr-1-config checkgid envvars-std htdigest httxt2dbm
[root@cpe-24-195-24-133 bin]# apapchect1
-bash: apapchect1: command not found
[root@cpe-24-195-24-133 bin]# apachect1 start
-bash: apachect1: command not found
[root@cpe-24-195-24-133 bin]# cd apachect1
-bash: cd: apachect1: No such file or directory
[root@cpe-24-195-24-133 bin]#
everything by envvars and envvars-std is green. Don't know if that means much. I wanted to see if I actually had the files.""",
"""The last character is the number one... change it to lower case L => apachect"hell" not apachect"one" """,
"""This is the error I got, but that worked! Thanks!

Quote:
[mbenoit@cpe-24-195-24-133 ~]$ /usr/local/apache2/bin/apachectl start
(13)Permission denied: make_sock: could not bind to address [::]:80
(13)Permission denied: make_sock: could not bind to address 0.0.0.0:80
no listening sockets available, shutting down
Unable to open logs
[mbenoit@cpe-24-195-24-133 ~]$ """,
"""
Quote:
Originally Posted by Markness
This is the error I got, but that worked! Thanks!
That means something else is running and listening on port 80.

Run these commands:

$ ps ax | grep http
$ ps ax | grep inetd

Please post the output from both commmands.

Peace...""",
"""Huzzah! Here it is.

Quote:
[mbenoit@cpe-24-195-24-133 ~]$ ps ax | grep http
27883 pts/3 S+ 0:00 grep http
[mbenoit@cpe-24-195-24-133 ~]$ ps ax | grep inetd
27886 pts/3 R+ 0:00 grep inetd
[mbenoit@cpe-24-195-24-133 ~]$ """,
]),
]


model = [
    '/html/body/div/div/div/table[2]/tbody/tr/td/div[4]/div/div/div/div/div/table/tbody/tr[2]/td[2]/div[3]',
    '/html/body/div/div/div/table[2]/tbody/tr/td/div[4]/div/div[position()>2]/div/div/div/table/tbody/tr[2]/td[2]',
]

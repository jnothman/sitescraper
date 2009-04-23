#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [
    ('1.html', ["How I disable automatic menu entries in Gnome?", 
"""
Hi

I have the problem, when i install a programm with synaptic the menu entries will write automatic in den Gnomemenu of all users. But i have about 50 Users with a very small menu. They should not have these entries. How i can disable this functional?

Rename the folder /usr/share/menu or Change of Rights or delete this folder have no impact.

Greetings
Dark Wolf
""",
"""
You may want to rename the *.desktop files unders /usr/share/applications/ folder
""",
]),
    ('2.html', ["Piclens For Linux (Request For Piclens Plugin)", 
"""
hi guys i came across the piclens plugin for firefox and i found it really cool and amazing ( you can check it here http://www.piclens.com/site/firefox/win/ )
but the sad thing is that they have not yet made a linux version an thats totally disgusting. I have send a mail to their feedback requesting a linux version. I know people here (linuxbees) can make more amazing things than piclens, but its also a matter of acceptance, so i am asking you a hand in letting them know, there are people here still alive and we are not happy with their ignorance. Here is their mail ID
feedback@piclens.com
Lets Bombard Them..............................
""",
"""
I already sent them an e-mail some months ago...
http://www.piclens.com/site/support/feedback.php
It seems that it works, they began thinking about Linux support which is not bad...
""",
"""
They said that they haven't made it for linux yet because of "resource constraints," or at least that is what their FAQ page says. If someone could make something that would do the same thing as piclens (or better) that is only for linux, that would be pretty cool.
"""]),
    ('3.html', ["GNOME stops working after login", 
"""
Hi..
Today I tried to login on my Ubuntu 8.04 GNOME.
Before I can start anything (the pointer still like a wheel scrolling) the pointer freezes.. I cannot move the mouse or keyboard. I tried to press Ctrl+Alt+Backspace but nothing happens

help me..
""",
"""
Go to your terminal by pressing ctrl+alt+f2 - it should show any errors that came up. Probably a display driver error.
""",
"""
I can't.
After log in (from GDM) it suddenly freezed (before it finishes to load GNOME fully). So how to fix it??
I've tried to reset X server but it not useful (no effect)
"""]),
    ('4.html', ["xorg.conf Unable to be backed up.", 
"""
I'm still a bit of a newbie to all this so bear with me in case this is a really simply issue.

I just switched from Windows XP to Ubuntu on Monday due to my XP install randomly destroying itself. So far, I've been very happy with Ubuntu, everything has worked easier, the programs run smoother, etc. However, I have a Dual 22" 16:10 Widescreen monitor setup, and I've figured out that setting it up is evidently is 1 part luck and 2 parts black magic. I am using a nVidia 7600GT graphics card, so I followed the standard advice and installed the proprietary drivers for it, then after much confusion with how Terminal worked, finally found the nvidia-settings tool. Now, I've figured out how to use the tool, and set it up, I set it for Twinview, and applied it, but that just made my monitors into one abnormally wide monitor that was cumbersome to use, so I tried the other option, "Use monitor as separate X Screen." Now, when I hit apply after setting that, it shuts off my 2nd monitor and gives some message about not having applied everything. So i tried the "Save to X Configuration file, Except when I tell it to do it, it pops up an error saying "Unable to create new X config backup file '/etc/x11/xorg.conf.backup'. Do you have any idea why this might be happening and what I need to do to fix it?

Thanks for reading the huge block of text... If you need more info, I can give it.
""",
"""
Run nvidia-settings as root. At a terminal, type in:
Code:

gksudo nvidia-settings
""",
]),
    ('5.html', ["how to run microsoft office live messnger in ubuntu", 
"""
My computer at my office is XP on which Windows Messenger is installed which is connected to Office Live communication server 2003 for instant messaging.

now i m migrating my XP to Hardy Heron and i lost instant messaging for inter office communication. what do i do??

could you please help me ASAP???
""",
"""
nstall aMSN, the MSN Messenger for Linux.

Get it from GetDeb at http://www.getdeb.net/
""",
"""
Check out Emesene it's a nice alternative to Windows Live Messenger. You can also try Pidgin which is installed by default in Ubuntu (Applications>Internet>Pidgin).
"""]),
    ('6.html', ["ubuntu and kubuntu setenv DISPLAY problem", 
"""
I have a ubuntu 7.10 desktop next to me, to which i would like to have a "xhost" ssh connection from my kubuntu PC. Here i am not able to "setenv DISPLAY my_pc_ip_address:0.0 and see the xsession of ubuntu in my machine.

Anybody can give me a solution for the above in a step by step manner, Thanks a lot in advance, i am totally new to this OS.

Rgds,
CRS.
""",
]),
]


model = [
    ('/html/body/div/div[3]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/strong', 0),
    ('/html/body/div/div[3]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div[2]', 0),
]

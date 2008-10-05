#!/usr/bin/python
# -*- coding: utf-8 -*-


data = []


data.append(('forum/slashdot', [
    ('file:html/news/slashdot/1.html', ["NYT Ponders the Future of Solaris In a Linux/Windows World",
"""
JerkBoB links to a story at the New York Times about the future prospects of Sun's Solaris, excerpting: "Linux is enjoying growth, with a contingent of devotees too large to be called a cult following at this point. Solaris, meanwhile, has thrived as a longstanding, primary Unix platform geared to enterprises. But with Linux the object of all the buzz in the industry, can Sun's rival Solaris Unix OS hang on, or is it destined to be displaced by Linux altogether?"
"""
]),
    ('file:html/news/slashdot/2.html', ["GNOME 2.24 Released",
"""
thhamm writes "The GNOME community hopes to make our users happy with many new features and improvements, as well as the huge number of bug fixes that are shipped in this latest GNOME release! Well. What else to say. I am happy." Notably, this release is also the occasion for the announcement of videoconferencing app Ekiga's 3.0 release.
"""
]),
    ('file:html/news/slashdot/3.html', ["Is There a Linux Client Solution for Exchange 2007?",
"""
CrazedSanity writes "I have been working at my state job for about 7 months now, using the Exchange plugin for Evolution to check my email. Very recently the higher-ups decided to migrate to Exchange 2007, which effectively destroyed my ability to check my email through any method other than webmail (which means I have to constantly refresh/reload the webmail window). I'm sure somebody else has encountered the problem, but I'm wondering if anybody has come up with a working solution?" Note: CrazedSanity's looking for a client that will work with Exchange in a situation where replacing the Exchange install with an open-source equivalent isn't an option. 
"""
]),
    ('file:html/news/slashdot/4.html', ["OpenSUSE Beta Can Brick Intel e1000e Network Cards",
"""
An anonymous reader writes "Some Intel cards don't just not work with the new OpenSUSE beta, they can get bricked as well. Check your hardware before you install!" The only card mentioned as affected is the Intel e1000e, and it's not just OpenSUSE for which this card is a problem, according to this short article: "Bug reports for Fedora 9 and 10 and Linux Kernel 2.6.27rc1 match the symptoms reported by SUSE users."
"""
]),
    ('file:html/news/slashdot/5.html', ["How the LSB Keeps Linux One Big Happy Family",
"""
 blackbearnh writes "The Linux Standard Base is the grand attempt to create a binary-level interface that application developers can use to create software which will run on any distribution of Linux. Theodore Tso, who helps maintain the LSB, talked recently with O'Reilly News about what the LSB does behind the scenes, how it benefits ISVs and end users, and what the greatest challenges left on the plate are. 'One of the most vexing problems has been on the desktop where the Open Source community has been developing new desktop libraries faster than we can standardize them. And also ISVs want to use those latest desktop libraries even though they may not be stable yet and in some ways that's sort of us being a victim of our own success. The LSB desktop has been getting better and better and despite all the jokes that for every year since I don't know probably five years ago, every year has been promoted as the year of the Linux desktop. The fact of the matter is the Linux desktop has been making gains very, very quickly but sometimes as a result of that some of the bleeding edge interfaces for the Linux desktop haven't been as stable as say the C library. And so it's been challenging for ISVs because they want to actually ship products that will work across a wide range of Linux distributions and this is one of the places where the Linux upstream sources haven't stabilized themselves.'"  
"""
]),
    ('file:html/news/slashdot/6.html', ["Mandriva Joins Ubuntu With a Linux For Netbooks",
"""
Slatterz writes "Linux publisher Mandriva has unveiled a version of its platform designed specifically for the new breed of mini laptops. Mandriva Mini features a fast boot-up, comprehensive connectivity support and multimedia codecs, and is adapted to work on key netbook platforms such as Intel's Atom. Mandriva previously offered a customised version of its 2008 Spring release for the Asus Eee PC, and was a distributor of Linux for Intel's Classmate PC initiative."
"""
]),
]))


data.append(('stocks/googlefinance', [
    ('file:html/stocks/googlefinance/1.html', ['44.43', '44.98', '43.39']),
    ('file:html/stocks/googlefinance/2.html', ['35.84', '36.90', '35.46']),
    ('file:html/stocks/googlefinance/3.html', ['19.00', '19.11', '18.25']),
    ('file:html/stocks/googlefinance/4.html', ['23.98', '24.34', '23.55']),
    ('file:html/stocks/googlefinance/5.html', ['25.80', '25.80', '24.90']),
    ('file:html/stocks/googlefinance/6.html', ['101.00', '103.25', '98.92']),
]))


data.append(('weather/yahooweather', [
    ('file:html/weather/yahooweather/1.html', ['Tonight: Mainly clear skies. Low 62F. Winds NE at 5 to 10 mph.', 'Tomorrow: Sunny skies. High around 95F. Winds NNE at 10 to 20 mph.', 'Tomorrow night: Clear. Low 64F. Winds NNE at 5 to 10 mph.']),
    ('file:html/weather/yahooweather/2.html', ['Tonight: Mainly clear. Low 59F. Winds NE at 5 to 10 mph.', 'Tomorrow: Mainly sunny. High 94F. Winds N at 5 to 10 mph. ', 'Tomorrow night: Clear skies. Low 62F. Winds SSW at 5 to 10 mph.']),
    ('file:html/weather/yahooweather/3.html', ['Tonight: Partly cloudy. Low 48F. Winds light and variable. ', 'Tomorrow: Except for a few afternoon clouds, mainly sunny. High around 75F. Winds light and variable. ', 'Tomorrow night: Mostly cloudy skies. Low 52F. Winds light and variable.']),
    ('file:html/weather/yahooweather/4.html', ['Tonight: Mainly clear skies. Low 58F. Winds NW at 5 to 10 mph. ', 'Tomorrow: Mainly sunny. High 78F. Winds NNW at 5 to 10 mph. ', 'Tomorrow night: Clear skies. Low 61F. Winds NNW at 5 to 10 mph. ']),
    ('file:html/weather/yahooweather/5.html', ['Tonight: Mostly cloudy skies this evening will become partly cloudy after midnight. Low 41F. Winds NW at 5 to 10 mph. ', 'Tomorrow: Mostly cloudy skies. High near 60F. Winds NNW at 5 to 10 mph. ', 'Tomorrow night: Mostly cloudy skies. Low 47F. Winds NW at 10 to 15 mph. ']),
    ('file:html/weather/yahooweather/6.html', ['Tonight: Mainly clear. Low 51F. Winds SE at 5 to 10 mph. ', 'Tomorrow: Mainly sunny. High 83F. Winds N at 10 to 15 mph.', 'Tomorrow night: A mostly clear sky. Low 52F. Winds SSW at 5 to 10 mph. ']),
]))


data.append(('forum/stackoverflow', [
    ('file:html/forum/stackoverflow/1.html', [
"""
If i open an image with open("image.jpg"), how can i get the rgb values of a pixel, if i have the 'coordinates' ( or co-ordinates?) of the pixel?

Then how can i do the reverse of this? Starting with a blank graphic, 'write' a pixel with a certain rgb value?

It would be so much better if i didn't have to download any additional libraries
""",
"""
It's probably best to use the Python Image Library to do this which I'm afraid is a separate download.

The easiest way to do what you want is via the load() method on the Image object which returns a pixel access object which you can manipulate like an array:

pix = im.load()
print pix[x,y]
pix[x,y] = value

Alternatively, look at ImageDraw which gives a much richer API for creating images.

""",
"""
I think the Python Image Library would help here

PIL

"""
]),
    ('file:html/forum/stackoverflow/2.html', [
"""


I'm fast approaching the point in my coding where I would like to quickly write object oriented code in languages other than C++ for a variety of reasons.

After a lot of research, my choices have pretty much narrowed down to Python and Java. I'm leaning towards Python because of its relationship to C, but with Java, from what I can see, I get a good introduction to using and creating test suites with Eclipse - there is also Processing which is pulling me towards Java.

I'm not the kind of guy to tackle two languages at once, so which one would you recommend and why? What I want at the end is to have an additional language I can use for rapid development. Ease of learning isn't important to me as I'm willing to put in the time regardless. Ability to use the new language widely is.

""",
"""
It depends on what your goals are. In terms of your resume, Java certainly has a much larger market than Python. In terms of your personal "knowledge portfolio", Python offers a greater potential for growth than Java does.

As many people have pointed out already, Java is very similar to C++ syntactically and has a better library. Python makes it very easy to just Get Things Done. Yes there is a performance plenty for interpreted languages, but often times this is of little to no consequence for a project. CPU time is much cheaper than developer time. Without digressing into a comparative languages discussion, I wouldn't worry about the performance too much. Use your head and pick the right tool for the job.

I believe you can write your applications "faster" in Python than you can in Java - the language is certainly more terse. Python is a better choice for rapid prototype in my opinion. Also, you can use Eclipse w/ Python as a first class language (with things like PyDev) and do unit testing (with things like PyUnit).

As a slight aside, if you are considering Java, I would highly suggest you seriously consider C# instead. C# has broad market applicability (similar to Java), "evolutionary" rather than revolutionary syntax from C++ (like Java), is a newer and in many ways, better language than Java (from a purely language perspective). Quite frankly, I find C# a much more enjoyable language than Java, as do many others. In terms of the goals you have laid out however, the Python vs C# decision has all the same points as the Python vs Java decision.

""",
"""
Java is just C++ with a decent library, you don't learn a lot by putting an extra word in front of the class definition.
"""
]),
    ('file:html/forum/stackoverflow/3.html', [
"""
Is there something like Python's getattr() in C#? I would like to create a window by reading a list which contains the names of controls to put on the window.
""",
"""
There is also Type.InvokeMember.

public static class ReflectionExt
{
    public static object GetAttr(this object obj, string name)
    {
        Type type = obj.GetType();
        BindingFlags flags = BindingFlags.Instance | 
                                 BindingFlags.Public | 
                                 BindingFlags.GetProperty;

        return type.InvokeMember(name, flags, Type.DefaultBinder, obj, null);
    }
}

Which could be used like:

object value = ReflectionExt.GetAttr(obj, "PropertyName");

or (as an extension method):

object value = obj.GetAttr("PropertyName");


""",
"""
Use reflection for this.

Type.GetProperty() and Type.GetProperties() each return PropertyInfo instances, which can be used to read a property value on an object.

var result = typeof(DateTime).GetProperty("Year").GetValue(dt, null)

Type.GetMethod() and Type.GetMethods() each return MethodInfo instances, which can be used to execute a method on an object.

var result = typeof(DateTime).GetMethod("ToLongDateString").Invoke(dt, null);

If you don't necessarily know the type (which would be a little wierd if you new the property name), than you could do something like this as well.

var result = dt.GetType().GetProperty("Year").Invoke(dt, null);


"""
]),
    ('file:html/forum/stackoverflow/4.html', [
"""


Hello. I'm starting with Python coming from java.

I was wondering if there exists something similar to JavaDoc API where I can find the class, its methods and and example of how to use it.

I've found very helpul to use help( thing ) from the Python ( command line )

I have found this also:

http://docs.python.org/

http://docs.python.org/modindex.html

But it seems to help when you already the class name you are looking for. In JavaDoc API I have all the classes so if I need something I scroll down to a class that "sounds like" what I need. Or some times I just browse all the classes to see what they do, and when I need a feature my brain recalls me We saw something similar in the javadoc remember!?

But I don't seem to find the similar in Python ( yet ) and that why I'm posting this questin.

BTW I know that I would eventually will read this:

http://docs.python.org/lib/lib.html

But, well, I think it is not today.

""",
"""
pydoc?

I'm not sure if you're looking for something more sophisticated, but it does the trick.

""",
"""
You can also use in the python shell:

dir( someobject )

To get a listing of the object members.

"""
]),
    ('file:html/forum/stackoverflow/5.html', [
"""


Why was looking for something that included many of the common modern-day tools, such as:

    * Code refactoring
    * Code navigation
    * Debugger
    * etc...
""",
"""
Eclipse with the PyDev plugin.

http://pydev.sourceforge.net/

""",
"""
This question, this question and this question all deal with this topic, or one like it.
"""
]),
    ('file:html/forum/stackoverflow/6.html', [
"""


My Google-fu has failed me.

In Python, are these:

n = 5
# Test one.
if n == 5:
    print 'Yay!'

# Test two.
if n is 5:
    print 'Yay!'

two tests for equality equivalent (ha!)? Does this hold true for objects where you would be comparing instances (a list say)?

Okay, so this kind of answers my question:

l = list()
l.append(1)
if l == [1]:
    print 'Yay!'
# Holds true, but...

if l is [1]:
    print 'Yay!'
# Doesn't.

So == tests value where is tests to see if they are the same object?

""",
"""
is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

>>> a = [1, 2, 3]
>>> b = a
>>> b is a 
True
>>> b == a
True
>>> b = a[:]
>>> b is a
False
>>> b == a
True

In your case, the second test only works because Python caches small integer objects, which is an implementation detail. For larger integers, this does not work:

>>> 1000 is 10**3
False
>>> 1000 == 10**3
True

The same holds true for string literals:

>>> "a" is "a"
True
>>> "aa" is "a" * 2
True
>>> x = "a"
>>> "aa" is x * 2
False
>>> "aa" is intern(x*2)
True

""",
"""
== determines if the values are equivalent, while "is" determines if they are the exact same object. 
"""
]),
]))


data.append(('search/msnsearch', [
    ('file:html/search/msnsearch/1.html', ['toyota',
    "Toyota - Australia", "Gives locations of dealerships in every state, financial services advice and motorsport news. Email requests regarding parts and accessories.", "www.toyota.com.au",
    "Toyota Australia: New Car: Details: Prices: Brochure: Dealer: Test ...", "Toyota Australia Official Website: New Car Range: Prices: Test Drive: Parts & Service: Dealer Locations: Finance: New Car Great Offers.", "www.toyota.com.au/toyota/main/HomePage/0,,1354_402,00.html",
    "Toyota Cars, Trucks, SUVs & Accessories", "Official Site of Toyota Motor Sales - Cars, Trucks, SUVs, Hybrids, Accessories & Motorsports.", "www.toyota.com",
    ]),
    ('file:html/search/msnsearch/2.html', ['holden',
    "Holden Australia", "Official site with pictures of vehicles, specifications, pricing, and features.", "www.holden.com.au",
    "Holden Australia - Latest offers and information on new and used ...", "www.holden.com.au: The official website for Holden Australia. Find out Holden vehicle prices, specifications, accessories, safety information and more.", "www.holden.com.au/www-holden",
    "Holden Motorsport > Home", "The Toll Holden Racing Team’s Garth Tander and Mark Skaife have pulled off one of the most amazing comebacks in V8 Supercar history to win a spectacular L&H 500 at Phillip Island ...", "www.holdenmotorsport.com",
    ]),
    ('file:html/search/msnsearch/3.html', ['ford',
    "Ford Australia - Ford Australia", "Official site for Ford Motor Company of Australia. Visit our vehicle showroom, view genuine Ford parts and accessories, find dealers.", "www.ford.com.au",
    "Ford Australia", "Official site for Ford Motor Company of Australia. Discover the great Ford range of vehicles, request a quote online or find your nearest Dealer.", "www.ford.com.au/servlet/ContentServer?cid=1137384063052&pagename=FOA%2FDFYPage%2FDefault10...",
    "Ford Motor Company: Cars, Trucks, SUVs, Hybrids, Parts - Ford", "Official site featuring investor, career, news, and media information.", "www.ford.com",
    ]),
    ('file:html/search/msnsearch/4.html', ['honda',
    "Honda - Australia", "Includes a brief history of Honda in Australia, information on new models and a search facility for locating dealers nationwide.", "www.honda.com.au",
    "Honda", "Enter your postcode", "www.honda.com.au/wps/wcm/connect/Honda.com.au/Home",
    "Honda Legend Home", "Honda Legend Home ... Recommended retail price, excluding dealer delivery & government statutory charges.", "legend.honda.com.au"
    ]),
    ('file:html/search/msnsearch/5.html', ['mitsubishi',
    "Mitsubishi Home", "Offers information on the range of Mitsubishi motor vehicles distributed and manufactured in Australia.", "www.mitsubishi-motors.com.au",
    "Mitsubishi Electric Australia", "Mitsubishi Electric creates high quality electrical and electronic products - for the home, business and industry. No matter where you find our products you'll see the same ...", "www.mitsubishielectric.com.au",
    "mitsubishi.com Mitsubishi Companies", "The mitsubishi.com website provides general information on Mitsubishi and an entrance to the individual websites of the Mitsubishi companies and related organizations. It is ...", "www.mitsubishi.com/e/index.html",
    ]),
    ('file:html/search/msnsearch/6.html', ['sony',
    "SONY - Australia", "Manufacturers of a product range spanning hi-fi systems, camcorders, video cassette recorders, TVs, computer monitors, portable audio, car audio, recording media and ...", "www.sony.com.au",
    "SONY - Australia", "Notice to Owners of VAIO VGN-TZ Notebooks More : Stay in touch with Sony's latest innovations by email. More : For extensive support information for your products, please visit our ...", "www.sony.com.au/vaio/category.jsp?id=22006",
    "Sony USA", "Manufacturer of a wide range of consumer electronics products including audio, video, communications, and computer systems.", "www.sony.com",
    ]),
]))


data.append(('search/altavista', [
    ('file:html/search/altavista/1.html', ['honda',
    "Honda Cars Motorcycles Watercraft ATVs Engines Generators, Acura", "Read about Honda history or jump to any of our web sites to find out more ... Honda Issues Fourth-Annual North American Environmental Report ...", "honda.com",
    "Honda Cars", "Honda vehicles site featuring new model photos and specs, safety information, current offers, and a dealer locator.", "automobiles.honda.com",
    "Find a new Honda at Yahoo! Autos", "Select a new Honda model name for more detailed vehicle information, including pictures, specs and reviews. Find your new Honda at Yahoo! Autos", "autos.yahoo.com/honda",
    ]),
    ('file:html/search/altavista/2.html', ['toyota',
    "Toyota.com - Official Site of Toyota Cars, Trucks, SUVs, & Hybrids", "Toyota cars, trucks, hybrids, and SUVs, plus new car and truck accessories. Explore the 2009 Camry and 2008 Tundra 4x4 Pickup Truck. Check prices, models, and features.", "www.toyota.com",
    "2009 Toyota Camry - Official Toyota Site", "View 2009 Camry models, features, pictures, options, performance, specs, accessories and more. LE, SE, XLE and Hybrid Camry models are available.", "www.toyota.com/camry",
    "Find a new Toyota at Yahoo! Autos", "Select a new Toyota model name for more detailed vehicle information, including pictures, specs and reviews. Find your new Toyota at Yahoo! Autos", "autos.yahoo.com/toyota",
    ]),
    ('file:html/search/altavista/3.html', ['ford',
    "Ford Motor Company", "Official site for the Ford Motor Company, manufacturer of SUVs, cars, trucks, and wagons. The Ford family brand includes Lincoln, Mercury, Mazda, Volvo, Jaguar, ...", "www.ford.com",
    "Ford Motor Company Ford Vehicles", "Learn about Ford cars, trucks, minivans, and SUVs. Get price quotes, search dealer inventory, compare vehicles, and find out about incentives and financing.", "www.fordvehicles.com",
    "Find a new Ford at Yahoo! Autos", "Select a new Ford model name for more detailed vehicle information, including pictures, specs and reviews. Find your new Ford at Yahoo! Autos", "autos.yahoo.com/ford",
    ]),
    ('file:html/search/altavista/4.html', ['mitsubishi',
    "Mitsubishi Motors", "Official site with information on new models, retailers, and financing.", "www.mitsucars.com",
    "Mitsubishi Digital Electronics America, Inc.", "Maker of DVD players, VCRs, and projection and HDTVs.", "www.mitsubishi-tv.com",
    "Mitsubishi Accessories", "Large Selection Mitsubishi DLP Projectors and Screens.Easy Dealer Search to Help You Find an Authorized Dealer Near You.", "www.mitsubishi-presentations.com",
    ]),
    ('file:html/search/altavista/5.html', ['holden',
    "Holden", "Official site of the General Motors division. Features a vehicle showroom, retail offers, finance details, dealer locator, and more.", "www.holden.com.au",
    "Holden Australia - Latest offers and information on new and used Holden ...", "www.holden.com.au: The official website for Holden Australia. Find out Holden vehicle prices, specifications, accessories, safety information and more.", "www.holden.com.au/www-holden",
    "Holden - Wikipedia, the free encyclopedia", "Over the years, Holden has offered a broad range of locally produced vehicles, ... Holden bodyworks are manufactured at Elizabeth, South Australia, and engines are ...", "en.wikipedia.org/wiki/Holden",
    ]),
    ('file:html/search/altavista/6.html', ['ipod',
    "Apple - iPod + iTunes", "Learn about iPod, Apple TV, and accessories. Download iTunes software free and ... and download them directly to iPod touch. Learn more. iPhone 2.1 ...", "www.apple.com/itunes",
    "Apple - iPod classic", "With 120GB of storage, iPod classic is the take-everything-everywhere iPod, with space for up to 30,000 songs, 150 hours of video, or 25,000 photos.", "www.apple.com/ipodclassic",
    "iPod - Wikipedia", "Article describing Apple's iPod, including hardware and software features, history, models, criticisms, sales, and other aspects.", "en.wikipedia.org/wiki/IPod",
    ]),
]))


data.append(('news/theonion', [
    ('file:html/news/theonion/1.html', ["I'm Fryin' My Nuts Off!", """
Hola, amigos. I know it's been a long time since I rapped at ya, but things have been getting plenty hairy around here. First, I been running like a chicken with its head cut off trying to find some new tires for my Festiva. I know, a tire is a tire, but these are some weird-ass size that no one makes anymore. I caught a flat on one and I've been driving on my spare for about a month now. It don't worry me none, but if I get another flat, I'm screwed.

On top of that, I had my hours cut at the electronics store. My manager told me it was because of the economic downturn that people weren't buying anything. I told him that without a full-time check, I wasn't going to be buying anything either, so how did this help? That stumped him but good.

In order to live the lifestyle I'm accustomed to, I had to find me another part-time job. I went around to the pizza joints, because they always need delivery guys, but they were all hung up on having proof of insurance. I told them I had insurance, but I was just a couple months late on payments, but they weren't hearing it. Man, when did everyone start getting so tight-assed?

The thing that's really been chafing me is how hot it is. They say it ain't the heat, it's the humidity, but I really don't give a shit which it is. Either way, after being outside a while, my undies are stuck to my ass, and I got pit stains that meet at my chest. Last year, I pulled an air conditioner off my neighbor's curb and put that in my window. It did the trick. Wound up costing me a boatload when I got my electrical bill, but it was worth it. This year, it wouldn't turn on, so I dragged it back over to my neighbor's.

During the day, it wasn't so bad, because I was at work and they keep the electronics store a chilly 72 degrees. At quittin' time, I would go to the discount movie theater. But after seeing the cartoon where the chimps go to space for the fourth time, I couldn't take it anymore. It wasn't just the movie, but all the families with kids in there were looking at me like I had a turd growing on my head.

Really, I don't mind it being hot when I'm just sitting in my apartment chilling out and watching some TV, but it's a real bitch to get to sleep. I've tried everything. I put some cardboard down so I could sleep on my floor, but it smelled like moldy pizza crust and socks. I got an old box fan from Ron and plugged that in, but it rattled all night and barely cooled me down. Then I tried sleeping with a six-pack of ice-cold Miller Genuine Draft in my bed, but I wound up drinking it all. I guess that sort of worked anyway.

Finally, after my fourth night of not sleeping, I came up with a plan. I figured that since they had to keep the store cool even at night, I should just sleep in there. Why not? I could just kick back in a video game chair and finally get some decent shut-eye.

The only thing was, I had to find some way to stay in the store until after they locked up. I was only supposed to work until 6:00, and since I usually leave around 5:30, it would look weird for me to be hanging around for an extra four and a half hours until they closed. I asked all around to see if I could pick up someone else's shift, you know, kill two birds with one stone and make a little extra money. I almost had this guy Wayne on the hook, but he was taking off the next weekend and he needed all the hours he could get. What a dick.

Since I wasn't going to be able to hide in plain sight, I figured that I should do the next best thing and hide out of sight. Now, if I knew I was gonna have to lay low until everyone left, I would've cased out a place to park comfortably for a couple of hours. Since I didn't, I had to do like my man Vin Diesel and improvise.

I went about my business like I was leaving, and clocked out and headed to the door. At the last minute, I pretended like I was interested in looking at the computer display. In order to throw people off my trail, I told one of my coworkers that it looked like some kid was going to steal video games. He went off to tell security, and once the coast was clear, I ducked back by the TVs. Sure enough, there was plenty of room on the shelves behind the display models. I climbed up there and got myself situated.

It didn't look comfortable, but I was wiped. As soon as I was sure I was out of sight, I dozed off.

When I came to, everything was dark. Perfect. It worked just like I had planned. I just had to go down, find the video game chair, and finish the night. That's when I realized that my leg was asleep. Not just asleep, but pretty much dead. It must have been from lying on that tangle of cords. I tried to wiggle my toes, but it didn't seem to be working. All of a sudden, my leg spasmed, and I kicked one of the TVs off the shelf.

My first thought was that I could just pick it up in the morning, before anyone got there, and I could catch some more Z's in the meantime. That's when the alarm went off. I looked all around for another hiding spot, but there wasn't one I could get to with my leg all dead. Plus, I wasn't going to be able to sleep with that alarm going off. I hightailed it to the emergency exit, which set off another alarm. I wasn't about to try and make it to my car, because I could hear the cops coming, so I had to limp away as fast as I could to the parking lot of the mall across the way, where I could wait it out until the coast was clear.

I mostly got away with it, but the next Monday, my coworker Wayne told me that he knew that I was the guy who set off the alarm, since my car was still in the parking lot when he left that night. So now, to keep him quiet, I got to pick up a shift for him some time, only I got to punch in on his card so he still gets the money.

One of these days, I'm gonna put the hurt on that guy, but it's going to be served cold. If any of you got a lead on a job, that would be awesome. I can't live on mac and cheese much longer. Well, I could, but I'm getting real sick of it."""]),
    ('file:html/news/theonion/2.html', ["Hanna Montana's Secret Identity…Revealed!", """
Item! Have you ever noticed that you never see Miley Cyrus and Hanna Montana in the same room at the same time? (She's kind of like Superman and Peter Parker in that way.) Well, that's because the hot Disney singer and the hot teen singer are one and the same person! I hope I haven't put her father, country superstar Billy Ray Cyrus, in danger by revealing her secret identity, but it's news, and my job is to break big news.

Is it just me, or are there too many computer cartoons? Maybe my age is showing, but I'll take a good old-fashioned animated classic like Nimm's Secret over a dozen computer cartoons any day.

Item! One of the things that makes this country great is the way we choose our representatives, and we recently chose one of our most important representatives of all: Miss USA. It was nice to know that, in the midst of high gas prices and war and the subprime mortgage mess, we could come together as a nation and pick a young woman to stand for beauty and talent and womanhood for all America. And the winner this year, in a magical ceremony, was Miss Texas! As much as I like Donnie and Marie as hosts, I think that they made a mistake getting rid of Bert Parks. Now, there was a host! There was a voice! If they don't bring him back I'm not going to stop watching, but if someone could put a word in, that would be great.

Spring is in the air, so if you have bulbs that need planting, now is the time. What are you waiting for? Roll up those sleeves and get digging!

Item! Are they or aren't they? That question could apply to just about anyone or anything but, music fans, you know what I'm talking about! Rumor has it Bootylicious chanteuse Beyond and rap mogul Jay Zee tied the knot recently. Or did they? There's all sorts of conflicting stories behind these so-called nuptials, so I'll just put this out there: Jay, Beyond, you make a great couple, and you've been together for a while. So even if you didn't get married, you are married in my mind and in the minds of your fans. Why not just trot on down to city hall and get the paper?

Why do I know the name Kim Kardashian? I woke up in the middle of the night and it took me a few minutes before I realized that she was in a sex tape and is now on a reality show. But really, so what? She is just taking up the space in my brain that good, honest celebrities like Gabreille Carteris should hold. If it's that easy to get a reality show, I need to get an agent. But first, I need to get a good night's sleep.

Item! An anonymous New York businessman recently paid $1.5 million for a sex film of Marilyn Monroe. He says it will be kept private. All I can say is wow. No trashy sex tapes for Marilyn—no, she went for film. And it will be kept private. That's real class. You hear that, Miss Kardashian?

Item! I was walking down the street last week, when I started to get a powerful thirst for some peppermint tea (I cut out the coffee after noon as part of my new health regimen). I stopped by my favorite coffee shop and who should I spot but Ron Howard's brother! I have no idea what he was doing in my neck of the woods, but I decided I should just leave him alone. That didn't mean I couldn't watch him, though! Howard's brother seemed really down to earth. He ordered a latte, but he added his own sugar. Then he sat down and started reading The Cries Of 49 or something like that. I'll have to get that book and read it so I have an in next time I see him.

I just bought Bob & Doug McKenzie's album on CD the other day. And you know what? It still holds up. Take off, eh?

Item! It looks like the great lost cause of pop stardom Britney Spears is back on track. The head-shaving diva was recently in a car accident, but according to police on the scene, she passed the field sobriety test. You hear that, haters? There was no liquor involved. You go girl! We knew you could do it! You're only one step away from getting your kids back now. Let me know if you need a character witness.

A lot of people have wondered why I haven't weighed in on the Heath Leger tragedy yet. Well, you're just going to have to wonder a while longer.

Blind item! MTV gave a certain tubby gossip hack a series of one-hour specials about the goings-on of Hollywood. Hey, MTV, if you're so desperate to get commentary on the who, what, where, why, and when of celebrities that you'll hire any pathetic fatty who can bang on a keyboard and steal other people's pictures to post online, my number is in the book. And I don't work blue.

Well, that about wraps it up for this week's installment of "The Outside Scoop." I didn't get to everything I wanted to—like Jeff Bridge's parking problems or the identity of Hanna Montana—but that was only because of space. I meant to, honest! Hopefully, I'll put a little something in there about those jaw-droppers next time. But until then, the velvet rope is up, so I'll have to see you again…on the Outside! """]),
    ('file:html/news/theonion/3.html', ["Smoove Is Waiting", """
Girl, there comes a time when even a strong, well-dressed man must admit defeat.

It has been a long time since we broke up and you left me standing in the rain outside of your condo. As I walked home that evening, it never would have crossed my mind that four years from now you would not have returned to me, that you would have nearly gotten married, that you would not even receive one of my phone calls. Or my letters, text messages, faxes, or instant messages.

Four years ago this would have been inconceivable that you, my one true girl, could have stayed away from me for this long. Do you not remember how it once was? We were like two love prospectors who discovered richer and richer veins of pure ecstasy. We would bump and grind in the dimly lit tunnels as shining white donkeys would carry wagons of our love to be washed off and then smelted down into fine pieces of jewelry, which I would place on your naked chocolate body while you slept. When you awoke, we would freak again.

How could a love this sexy end? After many long nights in my round circular bed wondering, and long days looking at myself in my large oval mirror, I have come to the realization that we may never do the nasty again.

Damn.

I just wanted to use this opportunity to say that no matter what happens in my life or what happens I will be here, waiting for you. Even if I am married, living in the suburbs with three children, if you were to send me a note saying "Let's give it another chance" I would immediately abandon my life, rent out my old penthouse apartment, take my clothes out of storage, and immediately start creating a sumptuous dinner or breakfast for me to feed you, depending on the time of the day it was. That is what you mean to me.

I would, at this point, like to ask any women that I am currently dating to stop reading this column.

So, girl, if you doubt that I no longer love you, I ask you to remove that doubt, for this love is deep. Too deep to fade by the mere passage of time. If you worry about how you have treated me in the past, which, I think we both can admit, was cold, I would say that having you back in my arms was worth the pain and torment I have endured by your absence. If you worry that we will no longer be physically compatible, that somehow we will no longer be able to light the fuse of the atom bomb that is our sexuality, I have to say, you know that not to be true.

While a small sliver of hope will always remain inside of me, Smoove has come to the hard understanding that you are not coming back to me. It is like a part of Smoove has died and, for this part, he has begun to grieve. I am not certain of which stage of the mourning process it is that one begins making lists, but Smoove has begun making them. I now present to you Smoove's Happiest Memories Of When We Were Together:

#5: That time I broke you off nasty outside of that club.

#4: Making love until the dawn on Christmas morning.

#3: The night you invited your friend Cherise into our bedroom and I then hand-fed both of you the succulent berries before getting freaky with both of you in my whirlpool.

#2: The many nights you rode my pony until I couldn't take it anymore.

#1: Waking up before you, and just holding you in my arms until you woke up and then hitting you doggy-style until you lost your mind.

That is only one list of many. I have many complex emotions to work though. And while my hair remains impeccable and my clothes are fresh, the feelings that lie beneath Smoove's surface roil like a volcano waiting for you to calm the tempest by saying those three little words; "I need you." If you were to add the words "now" or "right here on the floor" I would have no problem with that.

Even if you are not interested in once again contacting Smoove, arranging a time to meet, getting picked up in fine white automobile, dancing all night at a popular nightspot, enjoying a late dinner before being loved so hard and long you will think your heart may explode from pure 100 percent uncut pleasure, I will accept this. It has taken Smoove a long time and many heart-to-heart talks with my main man, Darnell, but I have come to grips with the situation.

What Smoove would like you to understand is this: No matter where you are or who you are with, there is a man who smells of exotic lotions who loves you and wants you to be happy. And if you are ever need another taste, Smoove will always be here, ready to break you off some.

Smoove out."""]),
    ('file:html/news/theonion/4.html', ["Comedy Tonight!", """
I'm still not sure what possessed me to walk into Laughingstock's Comedy Club and sign up for their open-mic night. But I guess sometimes the less you think about doing something, the more apt you are to do it. For years I had dreamed about bringing my gift for comedy to the live stage. True, I might be more known for the written word, but I'm always coming up with funny things to say out loud. Yet I was way too shy to actually go through with it. Then one day I happened to be driving by the place. I pulled into the parking lot, walked in, and the rest is history. I don't know, maybe it was the big, inviting W.C. Fields stenciled on the front window, or the $8.99 all-you-can-eat popcorn shrimp special, which you've got to admit is pretty cheap. Whichever, there was something right about it all.

Of course, try telling all that to Hubby Rick! Boy, I guess he must have permanently lent his sympathetic ear to his barfly buddies at Tacky's Tavern, because when it came to my decision he acted like he was stone deaf! You know what the first thing he asked me was? "Are you getting paid?" Sheesh, with him it's always about the do-re-mi! When I told him no, he scoffed. "I don't get out of bed for less than $9.50 an hour," Rick said. Then he said that hookers have more sense than I do, because they know not to give it away for free. Doesn't he know anything about the world of comedy? It's based entirely on love and truth. The money is secondary. (But like all good clowns, I decided to convert my hubby's grouchy ways into fodder for my act, as you shall see!)

As it turned out, open-mic night didn't take up the whole night; it actually was used as a warm-up thing for the two professional cutups who were performing. I spotted one of them at the bar eating popcorn shrimp—he looked just like the photo tacked up in the glass signboard out front, only a little older, and his hair was less gray. I don't remember his name (he was kind of tall and burly and wore a leather jacket—does that ring a bell for anyone?), but I was eager to say a few kind, encouraging words to the merry jester. I placed my hand on his. He looked a little surprised. I looked straight into his eyes and told him, "Thank you for being a clown. Thank you for making the world laugh and forget its troubles for a minute or two. You provide an invaluable service." Then I walked away. I felt any other words would kill the moment. I had shared something real. I'm sure he very much appreciated it, for as I understand it, clowns live for the attention.

I introduced myself to the club's MC, who took me to a little room where two other amateurs sat. One looked like he was no older than 13, and the other looked to be a college kid. I didn't really talk to them, though, because this was about the time I started to feel really, really nervous and sick to my stomach. Fortunately, I didn't have to go on straightaway, since the college kid went first. I started to gather my wits. That was a good thing, because I almost forgot to put on my funny costume I planned just for this event—a red clown nose, huge polka-dot necktie, and propeller beanie! I thought it was a funny little touch that heightened the spirit of fun.

Soon it was my turn. To hear my name called and the smattering of applause it received was both exhilarating and terrifying! I climbed onstage and was immediately hit with a blinding light pointing at the stage. How do the jokesters put up with that? I could hardly see the notes I wrote on my hand! It so unnerved me that for a few seconds I couldn't say anything into the mic. The silence roared in my ears.

After my eyes got a little more used to the light, I launched into an observational-humor joke. I talked about bottled water, and how it seemed weird to pay for something free. I thought it was pretty funny, but no one really laughed at it. Maybe it went over their heads a little. The younger people probably don't remember a time in which we only drank tap water.

Then I did my couch potatoes joke: "If two couch potatoes mate, does that make their offspring hash browns?" That didn't get too many laughs either. I don't get why not—that joke could be printed in a joke book; it's that solid. Undeterred, however, I launched into that hilarious evergreen, my Pet Rock joke. "I had to put my Pet Rock to sleep recently," I said. "I felt sad, but old Sedi—that's short for sedimentary—had a good run. It lived to 32!"

You could have heard a pin drop. Again, perhaps the reference was too old. So I decided to haul out the big guns and talk about Hubby Rick, because who can't relate to a louse of a spouse who can be a real pain in the patoot? "My hubby drinks so much that the state granted him his own liquor license!" I said. "When we first got married, he promised me a house, and he came through—we're now the proud owners of a Barbie Dream House. 'But you didn't specify the size!' he said."

"Show us your tits," a voice from the audience said.

A couple others immediately screamed "Noooo!" I raised my hands to silence them all. "I don't expect everyone to appreciate clean humor," I said. "Thanks for your time. Enjoy the rest of the show. Good night."

I left the stage. The MC looked a little startled—I guess he expected my act to last much longer. But I tell you, because I refused to stoop to demeaning behavior, I walked off that stage with my head held high (though it made my red nose fall off and I had to pick it up in front of everyone). I returned to the little room to pack my gear, and watched the third act, the 13-year-old, on the closed-circuit TV. He got some big laughs talking about school cafeteria food and mean gym teachers, even though in my view he wasn't any funnier than me. But no matter—my dream of being a clown had come true, and completely on my own terms!

But seriously, I think that Pet Rock joke was a pretty good one. I mean, rocks obviously don't die! Who saw that one coming? """]),
    ('file:html/news/theonion/5.html', ["When Are They Going To Finish The Arthur Trilogy?", """
Where were you in July 17, 1981?

Like most Americans, I was standing in line for the premiere of the most awaited film event of the century: Arthur. Dudley Moore had just wowed the critics for his turn in the hit 10, and there was much speculation that this would be an even bigger hit. What an understatement!

Nobody, not even the studio that released Arthur, could've imagined the impact it would have on the world. It was just a simple love story about a drunk millionaire who falls for a poor girl and must choose between following his fortune or his heart. But, oh, the power of that story! Dudley Moore, Liza Minnelli and Sir John Gielgud became household names. Christopher Cross' theme song went platinum. And, of course, millions of people imitated Arthur every day by getting blitzed.

And where was I during all this hubbub? Why, waiting in line to see Arthur again, of course! I saw Arthur a grand total of 218 times in the theater and 735 times on video, and I read the novelization 416 times before the cover fell off and the binding turned to dust. I went to the Arthur conventions, dressed like Arthur for Halloween, and wrote a manual that includes schematics of all the rooms in Arthur's mansion (Attention publishers: The book still hasn't been optioned. Hint! Hint!) I even started my own fan club, King Arthur's Court. Our peak membership was seven Arthurians, but three of them have since died of liver cancer.

Yes, I'm quite proud to say that Arthur has been the guiding force in my life. Though I'm not much of a drinker, I gleaned as much from the film as possible and applied it to my daily life. I hired an acid-tongued butler named Hobson. I started shoplifting like Liza Minnelli's character, Linda. I even wore a top hat in the bathtub!

>Imagine my joy in 1988 when the long-awaited sequel, Arthur 2: On the Rocks, finally arrived. At long last, I could see more adventures of my favorite characters. There they were, Arthur and Linda, on screen together again, and they were married! Imagine my surprise when I learned they were trying to adopt a child, even though Arthur had lost his fortune. Even Hobson, who died in the original movie, came back as a ghost. I was in heaven! I saw Arthur 2: On the Rocks about 150 times, then I bought the video and watched it until it burned up in my VCR and, ultimately, reduced my apartment to cinders.

So now it's been more than eight years since Arthur 2, and I haven't heard boo about Arthur 3. Let's get cracking, Hollywood--the teeming masses are waiting!

The other Arthurians and I have done a lot of research, and we've uncovered some incredible facts. Did you know that Steve Gordon, the writer and director of the original Arthur, wrote three complete Arthur trilogies before he died? The one in which Arthur takes place is actually the second of the trilogies. The first covers the story of how Arthur's father acquired his fortune, and details his battles with opium addiction. In the third trilogy, Arthur's son returns to his grandfather's native country to become a fig farmer, only to come face to face with a rival Hobson's great-grandson! Word also has it that the only characters who will appear in all three trilogies are the Droids.

Much ink has been spilled about next year's theatrical re-release of Arthur. Apparently, Warner Brothers has uncovered some lost footage, and is re-incorporating it into the movie. The missing scenes include one in which Arthur drunkenly falls into a swimming pool at a fancy dinner party.

Warner Brothers also plans to replace all the old special effects with fancy new digital effects, claiming that Arthur will seem even more drunk than before. Well, I say, why fix what ain't broken?! Give us what we really want: the final installment of the trilogy! My fellow Arthurians and I may be a small group, but we're very vocal. We've petitioned Bud Yorkin, the director of Arthur 2, to break the silence on Arthur 3, but he won't return our calls. We've camped out in front of Dudley Moore's mansion and sung Arthur's Theme in all-night vigils, only to be manhandled by Dudley's thuggish security personnel. Even Liza Minnelli, who could use the kind of career boost Arthur 3 would give her, has refused to meet us at the front desk at the detox clinic.

But, by God, we won't give up! We've just got to know what happens next! Will Arthur be able to stay on the wagon long enough to see his son grow to be a man? Will Linda ever return to the stage to reprise her role in Cabaret? And will Arthur and Linda be able to get Hobson out of the carbon freeze? Dammit, Warner Brothers, we demand to know!
"""]),
    ('file:html/news/theonion/6.html', ["It Wuz Always 'Bout Tha Numbahs", """
Sleepless hours and dreamless nights and far aways / Ooo ooo ooo, wishing you were here.

—Chicago, "Wishing You Were Here"

I be blastin' this def tune outta tha Nite Rida's sweet-ass factory-installed speakas a lot lately. Suckas always comin' up 2 me sayin', damn Dog, we thought you down wit' tha gangsta rap, not no Chicago VII. I say hell no, I gots mad hate foe that wack hip-hop shit. Hall N' Oatz, Neily D, that band that supply air: now that's tha mad slammin' shit, word dat. Tha H-Dog listens easy, always has, always will.

Plus tha tune remind me o' my ol' homie an' mentor, CPA-ONE (R.I.P.). Damn, I wish he wuz still here. I don't mean that in no homo way. It just that we could use a few moe strong Accountz Reeveevin' bruthahs among tha livin', 'cuz down here it be war all around.

Times be hard as hell in tha A.R. bruthahood. Sir Casio KL7000, AirGoNomic, Kount Von Numbakrunch, Petty Ka$h, an' tha rest o' my krew in lockdown on some bullshit freestyle accountin' charges. They tried 2 bust my ass, but they couldn't get no charges 2 stick. So now I'm one o' tha few A.R. playas representin' on tha outside while them punk-ass Accountz Payabo knockas run wild. (3-Holepunch got three-hole-punched back last July. Mourn ya till I join ya, bro, an' much luv.)

Heaven knows and Lord it shows when I'm away / Ooo ooo ooo, wishing you were here.

Midstate be changin', too. Back in tha day, they used 2 pipe in them supafly Muzak beatz. But now they just play some mystical Irish flute shit off a satellite feed. Shitload o' turnovah in tha hizzy, too. Peeps used 2 make a career o' this place; ain't that way no moe. I no soona done sexin' up a Cash Room bitch than some new big-hair ho take her place.

An' peep this: Don't nobody want no office coffee no moe. It all 'bout tha Starbux now. Ain't shit wrong with office coffee, 'specially tha way I makes it: two an' three-eighths scoops o' Folgers wit' three an' one-quarter cups o' water. That tha perfect proportion.

Jus' about only thang still tha same be Myron Schabe. That fucka coulda died at his deks tan' turned into a skeleton an' no one would notice anyhow.

Tha biggest change? Full-scale, crazy-ass turf war between tha A.R. an' tha A.P. Not a day go by without me havin' 2 use tha Letta Opener O' Death on a Accountz Payabo punk.

Back in tha day, tha A.P. posse used 2 be weak-ass amateurs. Kickin' they asses wuz like takin' a nice, long, satisfyin' shit: Y'all could bring a magazine. But now tha A.P. be thirstin' foe serious payback, an' tha H-Dog in they crosshairs. Plus, them Blueshirts still ain't particularly pleased I wasted five o' they best enforcas with my Office-Fu skeelz back in tha '04.

Tha H-Dog sleep wit' one eye open now.

My man Gary, tha assistant A.R. supervisa at Midstate, left 'bout five months ago. "I can't put my wife and daughter in danger anymore, Herbert," he say. He say I should leave Midstate an' accountz reeceeve undah a new moniker, but I say hell no, I ain't runnin' scared foe nobody. I can't. Gary never really rolled wit' my krew, but I gots mad respect foe him. Rocked Midstate's calculatas foe 11 years an' never had an overage moe than 50 cent. Big ups 2 ya, Gary.

Everythang fallin' 2 shit, know what I'm sayin'? Check it out: Not only tha A.P. out foe blood, now tha new breed o' A.R. punks be fuckin' up everythang they ol' school foefatherz worked foe. They ain't got no respect foe tha traditions o' tha past. They just clockpunchin' hos afta tha office chedda. Some-a them be comin' outta bidness college thinkin' they can round up 2 tha nearest dolla. No lie. Wack-ass wannabes.

Ain't nobody moe wack than Irving Weinbaum, Gary's replacement. I'd fire his ass wit' a quickness, but tha comptrolla Gerald Luckenbill say he one-a tha few A.R. peeps not doin' time right now an' we needs him. Hell, I don't needs him.

Irving, he think he all dat, but he ain't. Got his accountin' degree from some bullshit diploma mill an' he have tha muhfukkin' balls 2 step 2 me jus' 'cuz he landed a sweet-ass Midstate gig. Yesterday, I called tha fool into my dope cubicle and told him 2 resolve a $2 variance. "Two dollar variance?" he say. "Woot!"

"'Woot'?" I say. "You fuckin' fool, it gotta balance."

"Why?" he say. "Midstate's in the black. They can eat the cost. It's all good."

Wuz tha bitch straight trippin'? "Muhfukka, you want yo head flown?" I say, mah H-Kool slippin'. "I wants that variance resolved."

"Don't tell me what to do, bra," he say.

"Don't call me no goddamn bra," I say. "I ain't no Maidenform shit. Fuck all y'all! What, y'all sayin' I'm a bra? What? What? What? Whadju say, fucka? What? What?"

"Chill out, geezer," he say.

DAMN.

Next thang I knew, my Letta Opener headin' straight foe his forehead. Next thang I knew afta that, tha L.O.'s bouncin' off a phone book that Irving thrust in fronta his face, an' fallin' 2 tha flo'. Irving picked it up an' peeped it, then flashed this crazy-ass smile, his grill fulla white veneers. "That, Dog, is for opening letters," he say. He bend tha L.O. in two, an' place it in my deks drawer. Then he smile an' fold his hands ovah his chest, waitin' foe my next move. An' suddenly I freeze. 'Cuz I wuz lookin' into a mirror o' my ol' self.

"This ain't ovah, fucka," I say.

"No, it's not," he say.

Aahhhh-aahhh-aahhhhhhhhh.

Know what? Fuck Irving Weinbaum. Fuck tha A.P., an' fuck tha system that keep an A.R. bruthah down. Fuck a bitch ex who won't let her babydaddy see his shortie no moe 'cuz he supposedly "a bad influence," when she out chickenheadin' tha whole damn A.P. an' I.T. put togetha. Fuck that flute bullshit, an' fuck them Starbux-havin', no-balancin', disrespectin' Midstate punk-ass muhfukkaz. If tha world gonna dis me foe keepin' it real an' kickin' it ol' school, then fuck tha world. I can't do no else. Honor above all, CPA-ONE used 2 say. Homie would undahstand, if no one else here do.

And I'd like to change my life, and you know I would / Just to be with you tonight, baby, if I could / But I've got my job to do, and I do it well, / So I guess that's how it is.

(horn solo)

Daddy H still in full effect, y'all. Tha bling, tha fame, an' tha bitchez keep flowin' in, but that shit ain't what matta. They ain't what kept me in tha game foe so long when so many o' my A.R. bruthahs never got promoted, or got hooked on Sharpies, or gave up on tha reeceevin' an' went into tax preparin' or auditin' or some other pitiful shit.

No, it wuz always 'bout tha numbahs. Tha numbahs. An' this Stone-Col' Funkee-Fresh Mack Daddy Supastar Enforca O' Midstate Office Supply will be crunchin' 'em an' balancin' 'em 2 tha grave. Much luv 2 ya, mah G's. H-Dog OUT. Peace."""]),
]))


data.append(('news/bbc', [
    ('file:html/news/bbc/1.html', ["Regulator shuts Washington Mutual", """
Washington Mutual (WaMu) has been closed by its regulator, making it the biggest US bank to fail.

The Office of Thrift Supervision (OTS) stepped in to shut the mortgage lender before selling its assets to JPMorgan Chase for $1.9bn (£1.0bn).

The OTS said it was worried WaMu would run out of cash as $16.7bn of deposits had been withdrawn since 15 September.

WaMu was one of the lenders worst-hit by the collapse of the US housing market and soaring mortgage defaults.

"With insufficient liquidity to meet its obligations, WaMu was in an unsafe and unsound condition to transact business," the OTS said. The bank had about $307bn of assets but only about $188bn of deposits.

It raised an extra $7bn of capital from a consortium led by the private equity group TPG in April.

Sub-prime lending

It is less than three weeks since WaMu dismissed its chief executive Kerry Killinger, who it blamed for the bank's expansion into sub-prime and other comparatively risky lending.

Sub-prime mortgages are offered to borrowers with inferior credit records or unpredictable incomes.

WaMu is JPMorgan's second big fire-sale acquisition since the start of the credit crunch. It bought Bear Stearns in March.

The WaMu deal means it is now the second-biggest US bank, with 5,410 branches in 23 states. "This deal makes excellent strategic sense for our company and our shareholders," said Jamie Dimon, chairman of JPMorgan Chase.

Before WaMu's closure was announced, it had a stock market value of $2.9bn.

The Federal Deposit Insurance Agency (FDIA) was quick to reassure customers that their money was safe.

"For bank customers, it will be a seamless transition," said FDIA chairman Stella Blair.

"Bank customers should expect business as usual come Friday morning."

In February this year, WaMu unveiled a new Whoo Hoo! advertising campaign, aiming to "capture the essence of what it feels like to bank at WaMu". """]),
    ('file:html/news/bbc/2.html', ["More cash is injected into banks", """
Central banks are taking co-ordinated action to lend extra cash to banks.

The Bank of England, US Federal Reserve, European Central Bank and Swiss National Bank will be involved.

The Bank of England will be lending an extra $30bn (£16bn) for a one week period, $10bn overnight and $40bn in three-month loans.

The central banks said that the extra cash was intended to help banks as they approach the end of the financial third quarter next week. Banks have been turning to their central banks for funding because they have been struggling to borrow from each other as they would usually do.

One of the reasons they have been reluctant to lend to each other has been the fear of further bank failures and the news that Washington Mutual has become the biggest US bank to fail will do nothing to help that situation.

Banks will be able to use their mortgage books as security on the loans.

Separately, the Bank of Japan injected cash into the Tokyo money markets on Friday for the eighth trading day in a row.

It injected 1.5 trillion yen ($14bn; £8bn) into the market, although it later removed 300bn yen of that.
"""]),
    ('file:html/news/bbc/3.html', ["Alitalia gets temporary reprieve", """
Alitalia, the airline which is struggling to survive, has been given a temporary reprieve by the Italian civil aviation authority.

ENAC said it would not revoke Alitalia's licence to fly "for now" after Italy's biggest union agreed to a revised rescue plan.

The authority had threatened to ground Alitalia's planes unless it presented an agreed plan by the end of Thursday.

Unions representing pilots and crew are yet to agree to the deal, however.

"For now, the feared risk of yanking the licence isn't there," said ENAC civil aviation chief Vito Riggio.

But he added that ENAC "will monitor Alitalia's financial situation month by month".

The CGIL union said it had signed an agreement with Alitalia, after winning concessions on pay, leave, contracts and temporary jobs.

Four of the nine unions have now agreed to the terms of the rescue deal proposed by investors group CAI. CGIL has urged the remaining five to end their opposition.

Alitalia's government-appointed administrator Augusto Fantozzi said ticket sales had fallen by 100,000 in September, hit by the uncertainty surrounding the airline. """]),
    ('file:html/news/bbc/4.html', ["Bail-out debate: For and against", """
As the debate rages about the US $700bn (£379bn) financial bail-out plan, BBC News looks at the arguments for and against this rescue package.

FOR THE DEAL

    * Global financial stability: the plan is aimed at bringing calm to an extremely volatile global financial system. The world's richest nations, the Group of Seven (G7) say the package will, "protect the integrity of the international financial system".
    * Investor wellbeing: Investors worldwide need a shot of confidence. As billionaire investor Warren Buffett put it: the plan was "absolutely necessary" to help pull the financial system out of an "economic Pearl Harbour".
    * Global slowdown: All sides agree that we want to avoid recession in the world's biggest economy and the knock-on effect that would have for countries that rely on America for trade.

    * Job security: Safeguarding jobs across the economy and preventing bankruptcies that "threaten American families' financial well-being" according to US Treasury Secretary Henry Paulson.
    * Credit freeze: Keeping funds flowing through the money markets so that financial institutions are happy to lend to each other, to businesses and to consumers is vital for any functioning economy.

    * Toxic profits: The $700bn cost of mopping up banks' toxic debts may seem a high price, but when authorities eventually sell these assets in the future, their value may have risen enough to make a profit.

AGAINST THE DEAL

    * Taxpayer burden: The government plans to buy up mortgage-backed assets at its "maturity" value, which is well above the current market value. If the value of these assets does not recover in the next few years, it will get expensive for taxpayers.
    * Ballooning state debt: The plan would swell the budget deficit, which could fuel inflation, economists warn (Mr Paulson has asked to raise state borrowing to $11.3 trillion, from $10.6 trillion).

    * True cost of the deal or how long is piece of string? Since authorities would have the power to buy almost any asset at any price and sell it at any future date, it is almost impossible to calculate the real cost of this deal.

    * Bankers' big pay: There are worries about controlling the mega-bucks bosses earn at the very banks being bailed out - given the view that it was Wall Street "that got us into this mess in the first place".

    * The phenomenal power of US Treasury Secretary Henry Paulson: The rescue plan is his baby and he will control how the $700bn is spent.

    * Too much exposure: Some congressmen object that they want the government to have the right to take a minority stake in any firm that is being bailed out, which would give the state the right to purchase stock in companies in the future.

    * Governance: The plan is a twice-yearly report - critics insist on greater oversight and reporting.
    * Main Street versus Wall Street: There are calls for this package to be extended to help ordinary Americans who are at risk of losing their homes.
"""]),
    ('file:html/news/bbc/5.html', ["What would financial Armageddon look like?", """
The US government's $700bn (£376bn) bail-out package is designed to avert a complete financial meltdown. Many people have compared the current financial crisis with the Wall Street crash of 1929 and the Great Depression of the 1930s that followed it.

Yet current events are clearly not in the same league.

"I don't think so, considering that the Great Depression had thousands of banks failing and people losing their life savings, 25% unemployment and social unrest and tent cities of the poor," says Allan Sloan, Washington Post and Fortune magazine columnist.

Could be worse

The US government may end up spending trillions of dollars dealing with the problems, but so far, with unemployment at about 6% and arguments going on about whether the US economy is even in recession, it seems frivolous to mention the current crisis in the same sentence as the Great Depression.

However bad things seem at the moment, they could be a great deal worse.

The Financial Times referred to last Friday's stock market recoveries as marking the end of the "Armageddon discount", and yet markets fell again on Monday, suggesting that investors may not be discounting Armageddon.

So what would it look like?

"It would be like an exaggerated version of last week," says stock market historian David Schwartz.

"There will be frightening news, frightened investors and news stories suggesting the end of the world has come."

Going bust

There would also be a widening of the types of companies going under.

So far, many of the firms going bust have been in the financial sector, but if things get worse there are many other vulnerable sectors. Analysts are looking carefully for the most heavily indebted companies, because there is concern that if banks do not resume lending to each other, then those are the firms that will fold.

Of course, more companies going under would mean hefty job losses.

Insurance problems

The other threat to non-financial companies was the danger that prompted the Federal Reserve to bail out the giant insurer AIG.

"What AIG threatened was a non-functioning derivatives market," says financial historian Edward Chancellor.

Many non-financial companies use the derivatives market as a sort of insurance policy.

Airlines use it to protect themselves against the price of aviation fuel rising while exporters may use it to offset movements in currencies.

Local currencies

In the current crisis, there is still relatively strong confidence in the banks and financial system as a whole.

"In the 1930s, people would hoard money rather than keep it in the banking system," Mr Chancellor says.

"They started coming up with local currencies instead of using dollars."

All these are bleak prospects, but there always comes a point at which the economy hits the bottom and things start improving.

"The problem with stock market bottoms is that very few people see them - there is no announcement," Mr Schwartz says.

"Everybody who has shares that they want to liquidate has done so and shares start rising because there are no sellers left."

At that point, people start piling into the market and the recovery is underway.
"""]),
    ('file:html/news/bbc/6.html', ["Bank giant HSBC axes 1,100 jobs ", """
Banking giant HSBC is to axe 1,100 jobs worldwide, blaming the current financial turmoil for the decision.

About half of the cuts, which will affect back room jobs at its global banking and markets operation, will take place in the UK.

HSBC employs about 335,000 people around the world.

Last month, HSBC said half year profits fell 28% to $10.2bn (£5.2bn), as it was forced to write-off $14bn from bad debts in the US and asset write-downs.

Meanwhile, pre-tax profits fell 35% to $2.1bn during the same period.

An HSBC spokesman said the firm had opted to reduce its workforce, "because of market conditions and the economic environment, and our cautious outlook for 2009".

Many of the job-losses will be at the headquarters of HSBC's investment banking division, which are in London's Canary Wharf.

Banks around the world have been coming under increased pressure from the credit crisis currently affecting financial markets.

The problems have forced governments to step in and boost money markets as well as bail out a number of companies.

Earlier this year, the UK government had to buy mortgage lender Northern Rock, while in the US lenders Fannie Mae and Freddie Mac have been rescued as well as insurer AIG and investment bank Lehman Brothers filed for bankruptcy. """]),
]))

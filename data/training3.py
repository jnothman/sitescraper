#!/usr/bin/python
# -*- coding: utf-8 -*-


data = []


data.append(('yahoo finance', [
    ('file:html/stocks/yahoofinance/1.html', ['19.150', '17.710', '19.490']),
    ('file:html/stocks/yahoofinance/2.html', ['24.700', '23.540', '24.250']),
    ('file:html/stocks/yahoofinance/3.html', ['44.600', '42.700', '45.500']),
    ('file:html/stocks/yahoofinance/4.html', ['24.300', '23.000', '25.450']),
    ('file:html/stocks/yahoofinance/5.html', ['39.700', '35.400', '39.750']),
    ('file:html/stocks/yahoofinance/6.html', ['111.000', '101.500', '110.000']),
]))

data.append(('bom', [
    ('file:html/weather/bom/1.html', ['Sydney - Observatory Hill', 'Sydney Airport', 'Sydney Olympic Park']),
    ('file:html/weather/bom/2.html', ['Melbourne', 'Melbourne Airport', 'Avalon']),
    ('file:html/weather/bom/3.html', ['Darwin', 'Batchelor', 'Cape Don']),
    ('file:html/weather/bom/4.html', ['Perth', 'Perth Airport', 'Bickley']),
    ('file:html/weather/bom/5.html', ['Adelaide', 'Adelaide Airport', 'Edinburgh']),
    ('file:html/weather/bom/6.html', ['Hobart', 'Hobart Airport', 'Bushy Park']),
]))

data.append(('theaustralian', [
    ('file:html/news/theaustralian/1.html', ["""
STOCKS closed above 5000 points for the first time in two weeks today, after the short-selling ban and the US rescue plan.

The US unveiled its $US700 billion ($841 billion) rescue proposal late on Friday after global financial markets were rattled over the past two weeks.

The benchmark S&P/ASX 200 index climbed 216.4 points, or 4.5 per cent, to 5020.5, while the All Ordinaries gained 209.4 points, or 4.3 per cent, to 5050.1.

But the opening of local trading was delayed for an hour today after the ban on short selling created widespread confusion among institutional investors.

Complaints from the options, warrants and derivative markets prompted trading on the Australian Securities Exchange to be delayed until 11am AEST.

The ban on short-selling, which will be reviewed by regulators in a month, surprised market participants, and has been labelled by some commentators as “dumb”.

AMP Capital Investors chief economist Shane Oliver said the short-selling ban on all stocks - over and above moves by international markets - might reflect a degree of panic.

“I can't see why a potential short-seller in US financials would decide to short Woolworths or BHP Billiton. What's the logic there?” Mr Oliver said.

“It's probably a bit heavy handed.”

Prime Minister Kevin Rudd said the ban was necessary in these volatile markets.

“While appropriately regulated and disclosed short-selling has a role to play in the effective operation of markets, it is appropriate to curtail its use at a time of heightened market volatility,” Mr Rudd told parliament.

“That precisely is what we have at present around the world.”

The Australian Securities and Investment Commission (ASIC) last Friday had only banned so called “naked” shorts, under which investors sell stocks they do not actually have, but extended that to “covered” shorts as well.

But ASIC said the controversial move last night to ban all short-selling was designed to “maintain fair and orderly markets” after the gyrations in global markets.

In a move to ease concerns in the financial markets over the ban, ASIC said today existing short positions would be exercised.

The US rescue plan came after the bailout of Fannie Mae and Freddie Mac and insurance behemoth AIG as well as the collapse of Lehman Brothers.

Stock markets throughout the region also rallied today on the US proposal, although markets eased from earlier highs ahead of Wall Street’s open tonight.

In Japan, the benchmark Nikkei 225 index closed 1.4 per cent higher.

The Australian dollar was at US83.13 cents.

Macquarie Equities associate director Lucinda Chan said: “What (Henry) Paulson (the US Treasury Secretary) has done has created a very positive market sentiment, and that's the key.

“People are feeling a little bit more confident, but they're not totally over-confident in the sense we've still got to wait and see how this thing pans out.

“The sentiment has changed, and that's very important for moving forward.”

Short-selling targets Macquarie Group and Babcock & Brown bounced strongly as market participants sought to unwind short positions and bought up stock.

Babcock leapt 54 per cent (43.5c) to $1.23 after over 14.7 million shares changed hands.

Australia's largest investment bank, Macquarie, rallied 5.2 per cent ($1.90) to $37.80.

Australia's major trading banks also benefited from a strong rebound in investor sentiment, on a day when around $51.5 billion was added to the value of the All Ordinaries.

ANZ jumped $1.44 (8.13 per cent) to $19.15, while National Australia Bank climbed $1.30 (5.65 per cent) to $24.30.

Commonwealth Bank added $1.90 (4.45 per cent) to $44.60, Westpac put on $1.16 (4.93 per cent) to $24.70 and its takeover target, St George Bank, edged up 94c (3.08 per cent) to $31.49.

Ms Chan said: “I think (the US authorities) would like to see these markets lifted and the share prices find a floor somewhere.”

Liquidity may take some time to return to the market, she said.

“It may take a little while as it all depends on how quickly the Paulson plan is approved by Congress.”

Australian insurance stocks were also strengthened, with QBE leaping 7 per cent ($1.80) to $27.50 and Insurance Australia Group adding 5.12 per cent (21c) to $4.31.

In mining, BHP Billiton recorded a “very solid” rise, Ms Chan said. The big Aussie surged 12.1 per cent ($4.30) to $39.70, and Rio Tinto jumped 9.3 per cent ($9.50) to $111.

Oil stocks were mixed, with Oil Search losing 9c to $5.62, while Santos gained 25c to $18.53 and Woodside Petroleum added 5.4 per cent ($2.94) to $57.

Gold stocks posted healthy gains - Lihir Gold added 20c to $2.65, while Newcrest Mining added 6.9 per cent ($1.65) to $25.50.

Making news today, Sigma Pharmaceuticals rose 4c to $1.39 after it reconfirmed full-year guidance and booked a 1 per cent rise in first-half net profit.

Retailers were mixed, with Woolworths steady at $27.53 and Wesfarmers gaining 95c to $31.75.

Telstra was the most traded stock, with 75.9 million shares worth $307.7 million changing hands. The telco dropped 11c to $4.02.

Preliminary national turnover reached 1.6 billion shares worth $7.28 billion, with 704 stocks up, 382 down and 308 unchanged.
"""]),
    ('file:html/news/theaustralian/2.html', ["""
A SURPRISE move last night by the corporate watchdog to impose a blanket ban on short selling all securities could reduce much-needed market liquidity, senior market players warn.

The Australian Securities and Investments Commission announced that all stocks short selling would not be permitted from the opening of trade today.

ASIC had announced on Friday that the ban would include only uncovered, or "naked" short-selling, under which investors sell stocks they do not actually have, and covered short positions would need to be reported to the market.

The upgraded restrictions go beyond those announced in foreign markets, the US, Britain, France, Germany, Switzerland, Ireland and Canada imposing bans only on shorting financial stocks.

But according to ASIC, restrictions on shorting overseas increased the risk of hedge funds conducting shorting raids here, where the relatively small size of the market made it particularly vulnerable.

"Because global funds can move quickly, the risk of unwarranted activity on the Australian market has intensified," ASIC said.

It said it would decide after 30 days whether to allow covered short selling to recommence, but even then, would limit the activity to stocks outside the financial sector.

Doug Clark, policy executive at stockbroking and investment banking industry body, The Securities and Derivatives Association, said ASIC's decision was "extraordinary".

"It will impact on liquidity, the stock-lending industry, and possibly on the over-the-counter derivatives industry," he said.

AMP Capital Investors head of investment strategy Shane Oliver said the measure was "a bit of an over-reaction".

"Obviously it will have a positive impact on the market in the short term because short selling allows people who are bearish to push the market further down," Dr Oliver said.

But he said it would be wrong to blame short selling for the recent sharp falls in the equity market.

"In the economic uncertainty that we're facing, the share market would have gone down anyway, whether there was short selling or not," he said.

Dr Oliver agreed the ban would reduce market liquidity and disrupt legitimate trading strategies.

"It could have a disruptive impact because short selling is a fairly common strategy -- there are a lot of long-short funds that will be long on one bank and short on another, betting on one bank over another -- and this will virtually wipe that out," he said.

Natalie Floate, chairwoman of the Australian Securities Lending Association, whose members will be effectively put out of business by the decision, had only just been notified of the changes when contacted last night and was unable to comment.

John O'Shaughnessy, deputy chief executive of the Investment and Financial Services Association, said he supported a temporary ban while the regulator assessed the effect of the global financial crisis.

"If there's a moratorium in the US and UK, it makes sense that Australia follows suit," he said.

"The moves on Friday night were understandable and we're not surprised they've extended it today."

Australian Shareholders Association spokesman John Curry also supported the regulator's decision.

"Some people claim that short selling gives some needed volatility in the market and that's a good thing, but I'm not sure that's the case for the retail shareholders who I represent," he said.

"I think they'd prefer the market to be something that over a period of time gave them a reasonable return, and I'm not sure short selling contributes tothat."

Since reports that the US ban had caused problems with the automated trading systems of a number of US financial institutions on Friday, Australian Securities Exchange spokesman Matthew Gibbs said the ASX had been working over the weekend with market participants to ensure the changes could be implemented when the market opened today.

ASIC said it would reassess the ban and advise the market in 30 days.

"These measures are necessary to maintain fair and orderly markets in these exceptional times of global crises of confidence in financial markets," ASIC chief Tony D'Aloisio said.

"Because of the relatively small size and the structure of the Australian market, it is necessary to extend the prohibition to all stocks." 
"""]),
    ('file:html/news/theaustralian/3.html', ["""
THE federal Government last night increased its controls on short selling of shares by imposing a total ban, in a move aimed at offering Australia some protection from the storm engulfing financial markets worldwide.

On Friday the Government banned so-called naked short sales, which make up a small part of the Australian market, but merely tightened its disclosure rules on covered short selling.

Naked short sellers sell shares they do not own with the hope of buying them back later at lower prices; covered sellers insure their position by borrowing shares. Last night, this was taken a step further with a ban on short sales on all Australian stocks for at least 30 days in a move aimed at protecting Australia from being attacked by global hedge funds. The ban will be reviewed after 30 days to determine whether it should be eased by limiting it to financial stocks.

Australia has gone further than any other country, banning short selling on all 2600-odd stocks listed here, whereas in the US and Britain short selling has been banned only in financial stocks such as banks.

Last week, the British and US governments imposed bans in the wake of the global meltdown in banking and other shares. Other countries followed, including Canada and Germany.

The latter moves prompted action by the Rudd Government and the Australian Securities and Investments Commission. The ban was extended because they were worried that by limiting controls on financial stocks, it would put more pressure on other stocks such as mining and real estate.

ASIC chairman Tony D'Aloisio said in a statement last night that "in light of the action taken by other regulators we need a circuit-breaker to assist in maintaining and restoring confidence". Australian regulators also found late on Friday that they were being effectively outbid, when shortly after their announcement US regulators banned short selling in all financial stocks.

Although the US share market had strong rises on Thursday and Friday, the staggering events of last week, most particularly the $US85 billion ($102.5 billion) bailout of insurer American International Group, have left investors more skittish than they have been for decades.

The Bush administration is asking Congress for more than $US700 billion to rescue the US economy in an unprecedented bailout, handing a huge advantage to Democrats in the imminent presidential election. While details of the rescue package are yet to be hammered out, news that relief is on the way should lift Australian stocks sharply higher today, adding to the gains made on Friday after central banks around the world pumped a combined $228 billion into money markets to shore up the financial system.

The White House has so far drafted just a three-page plan that amounts to the costliest taxpayer-funded effort in history to reflate the US banking system and stop the economy from plunging into a depression like that witnessed in the 1930s.

Senior White House officials and the chairman of the Federal Reserve, Ben Bernanke, have been providing stark warnings to the US Congress about the consequences of not agreeing to a bailout, the cost of which, for example, is 35 per cent more than next year's budget for the entire US military.

"If it doesn't pass, then heaven help us all," US Treasury Secretary Henry Paulson told legislators in meetings while Dr Bernanke - who has extensively studied the Great Depression - is said to have given a chilling description of the problems and told legislators "if we don't do this, we risk an uncertain fate".

While some warn that the final bill for taxpayers will end up being in the trillions, global financial markets are cheering the new plan. "We should see some great gains - we haven't seen anything like the rise in the US and Europe, and our market could be up 150 points or more," CommSec senior analyst Craig James said yesterday.

The Australian stock market surged by 4.3 per cent on Friday, bouncing back from a 34-month low on the back of the co-ordinated injection of liquidity from the world's central banks.

Financial stocks were expected to be the key beneficiaries today, Mr James said, while gold stocks could be held back by a sharp fall in the gold price, which fell as much as 7.6 per cent to $US828.50 on Friday on news of the massive US bailout.

Trading could be volatile later in the week as the focus shifts to the political wrangling in the US over the huge bailout amid a growing backlash against the plan, as well as questions about how it will work.

The Democrats are likely to benefit politically as the implications make it appear Main Street is saving Wall Street from its meltdown.

Democrat presidential candidate Barack Obama is using the crisis as evidence for his argument that the deregulation of the financial markets has failed US taxpayers.

Senator Obama and Republican candidate John McCain are waiting to see details of the bailout plan, which are likely to emerge today as the White House pushes for agreement on a framework for taking hundreds of billions in toxic debt off the balance sheet of the financial institutions and putting it in a public institution.

The fund is highly controversial, particularly among conservative Republicans who object to taxpayers underwriting Wall Street failures.

"The free market for all intents and purposes is dead in America," said senator Jim Bunning, a Republican from Kentucky and the most vocal critic of the plan. "The action proposed today by the Treasury Department will take away the free market and institute socialism in America."

There are many questions on how a newly funded taxpayer entity would work, such as how it pays for debt.

"This fund will help restore confidence in the financial system, but there is no quick fix for the underlying problems, so the global economy will continue to face significant challenges," said Paul Fiani, managing director of Sydney-based Integrity Investment Management. "The process for transferring the problem assets to the fund is not yet clear, but it is likely many banks will have to make significant write-offs in the coming weeks, so the rally in bank stocks exposed to these problem assets may well be short-lived."

Finance Minister Lindsay Tanner said yesterday Australia's financial system was strong and would withstand international pressures placed on it by the global credit crisis.

"We have very strong banks that are very highly regarded internationally, and of course we have world-class regulators," he said.
"""]),
    ('file:html/news/theaustralian/4.html', ["""
THE financial crisis on Wall Street would produce the greatest restructuring of the financial system since the Great Depression.

The Depression led to the US Congress passing the Glass-Steagall Act of 1933 that banned commercial banks from doing broking and investment banking, said the head of Citi's Australian operations, Stephen Roberts.

Mr Roberts said the latest changes would lead to a decline in the role of investment banks -- which would concentrate in future on more traditional advisory services -- and a rise in the relative role of universal banks such as Citi that had a strong equity and deposit base.

"The way that financial services are provided will be forever changed by these last few weeks," he told The Australian yesterday.

"This is one of the most transformational periods since the Depression and the Glass-Steagall Act. Investors, analysts and commentators are looking at what is the most secure, stable type of institution.

"It is those where the assets and liabilities are matched and access to long-term funding is secure and liquidity, therefore, is robust."

Mr Roberts said Citi had tier one capital of 8.7 per cent and more than $US800 billion in deposits worldwide. Its ratio of assets to total equity, deposits and long-term debt was about 65 per cent.

"At the other end of the scale you have the monoline investment backs such as Morgan Stanley, which are at 25 per cent, and the European investments banks at 29 per cent, and UBS at 40 per cent," Mr Roberts said.

He said this difference was being much more closely scrutinised by analysts and investors in the current crisis.

"That is what people are starting to look at. The strength of deposits, tier one capital and long-term debt is a vindication of the universal bank model," he said.

Mr Roberts said the model of the universal bank was being questioned late last year, as the US sub-prime crisis began to hit big US banks such as Citi.

In November last year, Citibank was given a $US7.5 billion injection of capital by the Abu Dhabi Investment Authority, which was followed by a $US50 billion capital raising earlier this year. "This year we had an analyst calling for the break up of the company, saying that the sum of the parts was greater than the whole," Mr Roberts said. "But we reaffirmed out commitment to the universal banking model."

Mr Roberts predicted that the investment banks of the future would concentrate on their traditional advisory services rather than proprietary trading where they took large equity positions.

"We will see very, very successful boutique advisory services firms, but the activity of the monoline investment banks taking significant proprietary positions will now be a lot more heavily scrutinised, given the necessity to fund it," he said.

Mr Roberts said the financial crisis would mean there was a lot more scrutiny by regulators across the spectrum of the financial services industry. "All financial service companies will attract a degree of scrutiny and will have to anticipate in this in their business model," he said. "This is not a bad thing. There is a change in sentiment. It may not be tomorrow, but it is going to be a very different environment."


"There are clearly significant volumes of risk that haven't been appropriately managed or priced, whether it is leveraged finance or private equity or whether it is having a huge amount of the balance sheet outstanding without getting the proper return from that."

Mr Roberts said universal banks had been pressured into taking a riskier approach by the activities of the investment banks, which were making much larger profits on their more risky trading.

"The universal banks were coerced into that sector of the market because of the competition," he said.

"But the pendulum has swung back to a more sustainable operating model.

"We will start to see further differentiation, which I think is healthy.

"The model with strong equity and strong depositor base is the model that works in today's environment and that has been rewarded.

"That is the model we are comfortable with and we are committed to.

"That has been validated in the most recent crisis."

Mr Roberts expects a positive week for the Australian markets in the wake of a package of measures by US regulators and international central banks to shore up the world financial system.

"We will have a pretty positive week down here from a continuation of the short covering in the market," he said.

"We will see a pretty positive week in Australia.

"There's not a lot that will take it (the market) down.

"The short covering in the market has reached a point where we are at a giant turning point."

But he said it would take some time before the crisis in the world financial system was over.

"I'm not suggesting that we are out of the trauma," he said.

"It's going to take a long time.

"We will continue to see weakness in those institutions that are vulnerable tosignificant short-term refinancing requirements."
"""]),
    ('file:html/news/theaustralian/5.html', ["""
WALL Street is anxiously waiting for more detail on US Treasury Secretary Hank Paulson's dramatic plan to saddle US taxpayers with what could be $US1 trillion ($1.2 trillion) worth of rotten mortgage-backed securities sitting on the books of US financial institutions.

Paulson has told Congress he needs urgent approval this week for what has been called "the mother of all bailouts" in order to prevent the possibility of a global financial meltdown.

But with few details emerging about the mechanics of the plan, there are concerns on Wall Street that Paulson will meet resistance and that last week's strong rally on the New York Stock Exchange will be short-lived.

Wall Street also wants more clarity on the ban on short selling announced on Friday, particularly in the area of convertible bonds where selling short is a normal part of the market.

Also on Friday, the Treasury said it was giving $US50 billion to prop up the rattled US money market mutual fund industry.

The industry has $US3.5 trillion in deposits and has always been regarded as a safe haven, but nervous investors have been pulling out their money at an alarming rate.

The biggest concerns, however, remain with Paulson's intervention, described by one critic at the weekend as the first blush of 21st century socialism.

After trying to address crises in individual companies as they arise, Paulson now believes the only practical solution is for the taxpayer to bail out all US financial institutions facing trouble.

The White House has put the cost at $US700 billion but the expectation is it will go much higher. So far, Paulson has produced only a broad-brush, three-page overview of the situation that leaves crucial issues unanswered but asks Congress to entrust him with more financial authority than any American has held before.

Specifically, the Street wants to know how distressed an asset must be before it is bought, how the assets will be housed, what price Paulson intends to pay for them, who he's going to buy them from, whether there will be a priority list and will discounts be fixed or flexible.

The price issue is crucial given the July 27 decision of Merrill Lynch CEO John Thain to sell a cache of mortgage-related collateralised debt obligations with a face value of $US30.6 billion for just $US6.7 billion.

Thain was praised for having the courage to charge off assets so boldly but now that Washington is a buyer the market has changed and holders of bad assets may want much more than Merrill's US22c in the dollar.

There is further concern that Paulson's bailout may risk America's AAA international credit rating.

"It brings up the more troubling question of whether the US Government is big enough to take on this problem," Mirko Mikelic, senior portfolio manager at Fifth Third Asset Management, told Bloomberg news. 
"""]),
    ('file:html/news/theaustralian/6.html', ["""
THE Australian stock market is expected to open higher tomorrow after the United States Treasury unveiled details of a $US700 billion ($A871 billion) rescue plan for the troubled US financial sector.

The US Treasury has said it was seeking authority to issue up to $US700 billion of Treasury securities to finance the purchase of bad assets from financial institutions, such as residential and commercial mortgage-related assets.

Wall Street jumped on Friday as investors were buoyed by news of the US government's plan to save banks wallowing in bad debts.

The Dow Jones Industrial Average surged 368.75 points, or 3.35 per cent, to 11,388.44, and the broader Standard & Poor's 500 index lifted 48.57 points, or 4.03 per cent, to 1,255.08.
The Nasdaq rose 74.8 points, or 3.4 per cent, to 2,273.9.

On Friday, Australia's benchmark S&P/ASX200 index gained 196.8 points, or 4.27 per cent, to 4804.1, while the broader All Ordinaries index rose 188.8 points, or 4.06 per cent, to 4840.7.
Commsec chief equities economist Craig James said the US rescue plan and a ban introduced on naked short-selling last week should boost the Australian bourse tomorrow.

"I think things are going to look very, very good,'' he said.

"Futures trading is pointing to a gain of 130 points, but it could be much more than that following the US rescue and also the outlawing of short-selling.

"The restrictions on short-selling are very much a positive.''

Mr James said financial stocks should do well tomorrow, and mining stocks may also benefit from expectations that the moves in the US will restore some health to the overall global economy over time.

Naked short-selling will be banned on the Australian stock exchange from this week to help curb excessive market volatility.

Short-selling, where traders seek to profit by selling borrowed shares of companies to then buy them back, in the anticipation their prices will drop, has been partly blamed for the sharp falls of stocks such as Macquarie Group Ltd.

A form of the practice, known as naked short-selling, involves selling without first borrowing the stock, or even ensuring they can be borrowed.

The Australian Securities Exchange (ASX) on Friday said that it would remove all securities from its list of stocks approved for naked short-selling from tomorrow.

In company news this week, Sigma Pharmaceuticals Ltd releases its half year results tomorrow, retailer David Jones Ltd releases its full year results on Wednesday, and diversified industrial and financial group Washington H Soul Pattinson & Co Ltd unveils its annual results on Thursday, as does agricultural chemicals firm Nufarm Ltd.

On the economic front, tomorrow the Australian Bureau of Statistics releases new motor vehicle sales data for August, and on Thursday, the Housing Industry Association of Australia releases new home sales data for August. 
"""]),
]))


data.append(('rotten tomatoes', [
    ('file:html/film/rottentomatoes/1.html', ["George Clooney", "John Malkovich", "Frances McDormand", "Brad Pitt", "Joel Coen", "Ethan Coen"]),
    ('file:html/film/rottentomatoes/2.html', ["Dane Cook", "Kate Hudson", "Jason Biggs", "Alec Baldwin", "Howard Deutch"]),
    ('file:html/film/rottentomatoes/3.html', ["John Cusack", "Steve Buscemi", "John Cleese", "Jennifer Coolidge", "Tony Leondis"]),
    ('file:html/film/rottentomatoes/4.html', ["Robert De Niro", "Al Pacino", "Curtis Jackson", "Brian Dennehy", "Jon Avnet"]),
    ('file:html/film/rottentomatoes/5.html', ["Kathy Bates", "Alfre Woodard", "Tyler Perry", "Cole Hauser", "Tyler Perry"]),
    ('file:html/film/rottentomatoes/6.html', ["Meg Ryan", "Annette Bening", "Eva Mendes", "Debra Messing", "Diane English"]),
]))


data.append(('google', [
    ('file:html/search/google/1.html', [
    "Holden Australia", "Official site with pictures of vehicles, specifications, pricing, and features.", "www.holden.com.au/", 
    "Holden Australia - Latest offers and information on new and used ...", "www.holden.com.au: The official website for Holden Australia. Find out Holden vehicle prices, specifications, accessories, safety information and more.", "www.holden.com.au/www-holden/", 
    "Holden Special Vehicles", "Holden Special Vehicles is Australia's luxury and performance car manufacturer. HSV produces a range of high performance car models, merchandise and apparel ...", "www.hsv.com.au/"
    ]),
    ('file:html/search/google/2.html', [
    "Ford Australia - Ford Australia", "Official site for Ford Motor Company of Australia. Visit our vehicle showroom, view genuine Ford parts and accessories, find dealers.", "www.ford.com.au/", 
    "Ford Motor Company: Cars, Trucks, SUVs, Hybrids, Parts - Ford", "Ford Motor Company maker of cars, trucks, SUVs and other vehicles. View our vehicle showroom, get genuine Ford parts and accessories, find dealers.", "www.ford.com/", 
    "Andrew Ford: homepage", "This is the authorised home page of composer Andrew Ford, English-born Australian composer, radio presenter and music writer.", "www.andrewford.net.au/"
    ]),
    ('file:html/search/google/3.html', [
    "Volvo Cars - www.volvocars.com/au", "Welcome to Volvo Car Australia, where you can find information on your next Volvo car, special offers, financial services and information on Australian car ...", "www.volvocars.com/au", 
    "Volvo Cars country selector - www.volvocars.com", "Welcome to Volvo Cars global homepage and country selector. You can find your next Volvo car, or more information about Volvo Car Corporation, in our Volvo ...", "www.volvocars.com/",
    "Volvo Group : home", "Manufacture trucks, buses, construction equipment, marine and industrial power systems, and aerospace systems . Includes links to operating companies.", "www.volvo.com/", 
    ]),
    ('file:html/search/google/4.html', [
    "Toyota Australia: New Car: Details: Prices: Brochure: Dealer: Test ...", "Toyota Australia Official Website: New Car Range: Prices: Test Drive: Parts & Service: Dealer Locations: Finance: New Car Great Offers.", "www.toyota.com.au/", 
    "Toyota Cars, Trucks, SUVs & Accessories", "Official Site of Toyota Motor Sales - Cars, Trucks, SUVs, Hybrids, Accessories & Motorsports.", "www.toyota.com/", 
    "Canberra Toyota", "Welcome to Canberra Toyota! Australia's No 1 motor vehicle brand, Toyota, is available from Canberra Toyota. You can be sure we’ll provide the best Toyota ...", "www.canberratoyota.com.au/"
    ]),
    ('file:html/search/google/5.html', [
    "Mitsubishi Home", "Welcome to the homepage of Mitsubishi Motors Australia. Find out more about Lancer, Pajero, Outlander, Triton, Colt, Grandis, Ralliart.", "www.mitsubishi-motors.com.au/", 
    "Mitsubishi Electric Australia", "Mitsubishi Electric creates high quality electrical and electronic products - for the home, business and industry. No matter where you find our products ...", "www.mitsubishielectric.com.au/", 
    "mitsubishi.com Mitsubishi 三菱", "mitsubishi.com is a portal site of the Mitsubishi Companies. Available in English and Japanese.mitsubishi.comは三菱グループのポータルサイトです。", "www.mitsubishi.com/"
    ]),
    ('file:html/search/google/6.html', [
    "BMW Australia > BMW Australia Home", "Welcome to BMW Australia, the official website that offers a range of information and services about new and used BMW vehicles.", "www.bmw.com.au/", 
    "BMW - Wikipedia, the free encyclopedia", "BMW is a worldwide manufacturer of high-performance and luxury automobiles and motorcycles, and is the current parent company of both the MINI and ...", "en.wikipedia.org/wiki/BMW", 
    "Federation Square - The Centre of Melbourne - BMW Edge", "The BMW Edge offers a unique audience experience. See a play, attend a launch, hear a speaker or listen to a recital, all against the dramatic backdrop of ...", "www.federationsquare.com.au/index.cfm?pageID=92"
    ]),
]))


data.append(('ebay', [
    ('file:html/commerce/ebay/1.html', ["car", "Garmin StreetPilot c340 Street Pilot c-340 Car GPS", "$116.99", "Sirius HI GAIN Car Antenna Sportster 3 4 S50 Stiletto 2", "$9.99", "Hands-Free Car Kit & FM Transmitter for Apple iPhone 3G", "$34.88"]),
    ('file:html/commerce/ebay/2.html', ["football", "Brett Favre Official Jets NFL Reebok Jersey Brand New", "$57.95", "NCAA FOOTBALL 09 PS2 2009 ROSTER MEMORY FILE NEW MADDEN", "$9.99", "PS3 NCAA College Football 2009 Roster Playstation3 09", "$3.79"]),
    ('file:html/commerce/ebay/3.html', ["hockey", "Harvard Arena Air Hockey Table", "$52.00", "77 Card Hockey Lot Inserts, Rookies & Regulars", "$25.00", "102 card hockey lot inserts, rookies, regulars", "$25.00"]),
    ('file:html/commerce/ebay/4.html', ["squash", "ORGANIC SEEDS TOMATO BEANS RADISH LETTUCE MELON SQUASH", "$7.50", "Sterling America S Western Squash & Earrings Turquoise", "$95.00", "Unusual Coral Squash Blossom Necklace!", "$69.50"]),
    ('file:html/commerce/ebay/5.html', ["golf", "Skycaddie SG5 Brand New in Box Golf Range Finder GPS!!!", "$329.99", "GBF Golf Ball Finder Makes finding lost balls easy !", "$8.89", "NEW SQUARE DRIVER ILLEGAL 525 NON CONFORMING GOLF CLUBS", "$59.00"]),
    ('file:html/commerce/ebay/6.html', ["tennis", "New Wilson nCode nTour MP 95 Tennis Racquet Racket tour", "$69.95", "5.50CTS 14 KT WHITE GOLD DIAMOND TENNIS BRACELET WOW!!!", "$3,599.00", "NEW Head Flexpoint 6 MP Tennis Racquet FXP Racket Cover", "$49.95"]),
]))


data.append(('ubuntuforums', [
    ('file:html/forum/ubuntuforum/1.html', ["How I disable automatic menu entries in Gnome?", 
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
    ('file:html/forum/ubuntuforum/2.html', ["Piclens For Linux (Request For Piclens Plugin)", 
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
    ('file:html/forum/ubuntuforum/3.html', ["GNOME stops working after login", 
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
    ('file:html/forum/ubuntuforum/4.html', ["xorg.conf Unable to be backed up.", 
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
    ('file:html/forum/ubuntuforum/5.html', ["how to run microsoft office live messnger in ubuntu", 
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
    ('file:html/forum/ubuntuforum/6.html', ["ubuntu and kubuntu setenv DISPLAY problem", 
"""
I have a ubuntu 7.10 desktop next to me, to which i would like to have a "xhost" ssh connection from my kubuntu PC. Here i am not able to "setenv DISPLAY my_pc_ip_address:0.0 and see the xsession of ubuntu in my machine.

Anybody can give me a solution for the above in a step by step manner, Thanks a lot in advance, i am totally new to this OS.

Rgds,
CRS.
""",
]),
]))

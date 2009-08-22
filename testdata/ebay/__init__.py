#!/usr/bin/python
# -*- coding: utf-8 -*-

data = [
    ('1.html', ["LOT 2 Mary Kay TimeWise Targeted-Action Line Reducer", "$31.00", "NASCAR 2008 Ford Fusion Action COT 1/64th Scale Car", "$1.25", "Lot of Batman and Superman animated action figures.", "$5.00"]),
    ('2.html', ["NEW NINTENDO WII FIT GAME BALANCE BOARD +GAMES", "$100.00", "THE BEST AMOS 'N ANDY ANYWHERE! All 79 TV SHOWS. EXTRAS", "$39.95", " Icon-The Complete Miniseries-Swayze-NEW-FREE SHIPPING!!", "$7.98"]),
    ('3.html', ["Sexy French Maid Adult Halloween Costume Mini dress", "$19.37", " Aussie Lingerie 2 Pr Adult Hot FishNet Sock White+Black", "$0.77", "Adult Mature Brass Corkscrew Bottle Opener New In Box", "$8.95"]),
    ('4.html', ["FOR VERIZON ADVENTURE MOTOROLA V750 NEW COVER CASE+CLIP", "$9.99", "Leather Case Pouch for Verizon Motorola Adventure v750", "$5.12", "CAR CHARGER+CASE for VERIZON MOTOROLA V750 ADVENTURE", "$8.99"]),
    ('5.html', ["Enlarge British Africa - South Africa #B1-4 MH-LH VF CV $48.25", "$12.15", "British Africa - South Africa #C5-6 MLH VF CV $36.00", "$9.15", "29.44cts 26x27mm PICTURE JASPER PEAR CAB AFRICA $NR!", "$0.99"]),
    ('6.html', ["Breaking Ice -ANTHOLOGY OF AFRICAN AMERICAN FICTION", "$1.99", "Sweeter Than Honey M. Morrison african american fiction", "$7.99", "Can't Say No by Bette Ford african american fiction", "$2.99"]),
]


# ebay's formatting is inconsistent depending on whether the price is marked down
# consequently this model will get duplicate results for the prices
model = [
    '/html/body/div[3]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tr/td[2]/a',
    '/html/body/div[3]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tr/td[5]/div',
    '/html/body/div[3]/div[4]/div[2]/div/div/div[2]/div[2]/div/div[4]/div/div[3]/table/tr/td[5]',
]

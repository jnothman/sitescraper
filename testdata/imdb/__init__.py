#!/usr/bin/python
# -*- coding: utf-8 -*-


data = [
    ('1.html', ["The Shawshank Redemption", ["Tim Robbins", "Morgan Freeman", "Bob Gunton"], ["Andy Dufresne", "Ellis Boyd 'Red' Redding", "Warden Norton"]]),
    ('2.html', ["The Godfather", ["Marlon Brando", "Al Pacino", "James Caan"], ["Don Vito Corleone", "Michael Corleone", "Santino 'Sonny' Corleone"]]),
    ('3.html', ["The Dark Knight", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"], ["Bruce Wayne / Batman", "The Joker", "Harvey Dent / Two-Face"]]),
    ('4.html', ["The Godfather: Part II", ["Al Pacino", "Robert Duvall", "Diane Keaton"], ["Don Michael Corleone", "Tom Hagen", "Kay Corleone"]]),
    ('5.html', ["Buono, il brutto, il cattivo., Il", ["Eli Wallach", "Clint Eastwood", "Lee Van Cleef"], ["Tuco", "Blondie", "Sentenza / Angel Eyes"]]),
    ('6.html', ["Pulp Fiction", ["John Travolta", "Samuel L. Jackson", "Tim Roth"], ["Vincent Vega", "Jules Winnfield", "Pumpkin - Ringo"]]),
]


model = [
    '/html/body/div/div[2]/layer/div[2]/div/div[4]/div/h1',
    ['/html/body/div/div[2]/layer/div[2]/div/div[4]/div[3]/div[14]/table/tr/td[2]/a'],
    ['/html/body/div/div[2]/layer/div[2]/div/div[4]/div[3]/div[14]/table/tr/td[4]'],
]

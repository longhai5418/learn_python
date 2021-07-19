#!/usr/bin/python3
# -*- coding: UTF-8 -*-
class Tiger:
    places = []
    def __init__(self, name):
        self.name = name
        self.my_places = []

    def go_place(self, place):
        self.places.append(place)
        self.my_places.append(place)

a = Tiger("Kiro")
b= Tiger('Zim')

a.go_place('北京')
b.go_place('上海')

print(a.places, a.my_places)
print(b.places, b.my_places)
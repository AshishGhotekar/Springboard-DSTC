#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 11:55:30 2021

@author: aghotekar
"""

#Functions that you have implemented in the Queue section

def enqueue(queue, new_item):
    queue.append(new_item)

def dequeue(queue):
    #We have added return here, just to return the item that is being removed
    return queue.pop(0)

def is_empty(queue):
    return len(queue) == 0

def size(queue):
    return len(queue)

# Do not change code above this line

def hot_potato_simulator(players, turns):
    hot_potato_queue = []

    for player in players:
        enqueue(hot_potato_queue, player) #Using enqueue function add a player to the queue
#    print(hot_potato_queue)

    while size(hot_potato_queue) > 1: #Using size function check how many elements are there in the queue

        for i in range(turns):

            enqueue(hot_potato_queue, dequeue(hot_potato_queue)) #Enqueue the next-to-last element from the queue to the end
#            print(hot_potato_queue)

        dequeue(hot_potato_queue) # Dequeue the HOT POTATO player
#      print(hot_potato_queue)

    return dequeue(hot_potato_queue) #Dequeue last element from the queue (The winner)


## Do not change code below this line
players = ["Peter", "John", "Luka", "Maria", "Sophia", "Derek"]
turns = 3
print(hot_potato_simulator(players, turns))
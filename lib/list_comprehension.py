#!/usr/bin/env python3

def return_evens(num_list):
    
    num_list=([0,1,3,5,7,8,9]) 
    evens= (((n%2)==0)for n in num_list)
    print(evens)


def make_exclamation(sentence_list):
    
    sentence_list=(["Hello", "I'm doing great", "Python is fun"])
    exclamation =(s.append("!") for s in sentence_list)
    print (sentence_list)
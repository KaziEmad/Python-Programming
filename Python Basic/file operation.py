# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:34:02 2022

@author: kazie
"""
word_all = []
with open("input.txt", mode="r") as s_file:
    for line in s_file.readlines():
        # print(line, end="")
        # print(line, end="\n")
        # print(line.strip())
        words = line.strip().split(" ")
        # print(words)
        word_all += words
    unique_words = set(word_all)
    print(f"Total words in the list is : {len(word_all)}")
    print(f"Total unique words in the list is : {len(unique_words)}") #without duplicate words
    print(word_all)
    
    with open("output.txt", mode="w") as write_file:
        write_file.write(str(word_all))
        # for item in sorted(unique_words):
        #     write_file.write(item)
        #     # write_file.write(" ")
        #     write_file.write("\n")
            
    
        
        
        
print("Finished!")
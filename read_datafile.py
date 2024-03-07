#!/usr/bin/env python
# coding: utf-8


# This function reads data from a file, parses it, and stores it in a list.

def read_data(file_name):
    resultlist = []

    with open(file_name, 'r', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:    # If reading the file has finished
                break
                
            strings = line.split() 
            
            if (not strings[0].isnumeric()):
                continue
                
            state = int(strings.pop(0))    # Extract the state from the first element
            struct_candi = strings         # Remaining elements are structural candidate
            
            # Read textual candidate lines
            text_candi = []
            itemline = f.readline()
#             print(itemline) 
            strings = itemline.split() 
                
            while len(strings) != 0:
                strs = itemline.split()
                ln_cols = strs[0].split(':')
                ln_col = ln_cols[0].split(',')
                ln = int(ln_col[0])         # line number
                col = int(ln_col[1])        # column number
                item = strs[1] 
                text_item = (ln, col, item) # line number, column number, textual candidate
                text_candi.append(text_item)
                itemline = f.readline()     # Read the next line
                strings = itemline.split() 
                
            resultlist.append([state,struct_candi,text_candi])  # state, structural candidate, textual candidate
            
#         print(resultlist)
        
        for state,struct_candi,text_candi in resultlist:
            print(state,struct_candi,text_candi)                


# infile = './datafile/01_HelloWorld.data'
# infile = './datafile/02_FontYellowColor.data'
infile = './datafile/any.i.textual_collection.txt'

read_data(infile)








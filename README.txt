This README describes the files for COMP90049 2019S2, Project 1. 

### Environment  
Python Version: 2.7.10  
External Packages:
+ [python-editdistance](https://pypi.org/project/editdistance/). `pip install editdistance`
+[python-Trie](https://blog.csdn.net/ANNILingMo/article/details/80879910)

### Dataset
  - dict.txt: This is a list of approximately 370K English entries, which should
    comprise the dictionary for your approximate string search method(s). This
    dictionary is a slightly-altered version of the data from:
    https://github.com/dwyl/english-words
    The format of this file is one entry per line, in alphabetical order.
    
  - tweets.txt: This is a list of the text from 62345 tweets, one tweet per line.
    (The ordering is random.)

  - wordforms.txt: This is an alphabetically-sorted list of 31763 unique tokens present
    within the tweets.
    To construct this list, the tweets were separated based on one (or more) characters
    of whitespace (\s), and tokens not consisting entirely of English alphabetic
    characters (^[a-zA-Z]+$) were excluded.
    Obviously, there are better ways in which the tweets could be tokenised; this 
    was intentionally simplistic.

  - candidates.txt: This is the list of 16925 tokens present in wordforms.txt, except
    that any token appearing in the dictionary has been excluded.
    One logical framework for the problem of finding lexical blends is that any token
    not present within the dictionary is potentially a blend. 

  - blends.txt: This is a tab-delimited list of tokens appearing in the tweets,
    which have been manually identified as being lexical blends.
    Each line takes the form: blend token, tab character, component word, tab character,
    component word, newline.
    some of the blends do not appear in the candidates list, because they have
    been excluded in the preprocessing stage. You might be interested to try out other
    preprocessing strategies instead.

### py files
  - Blends.py: The method of finding the Prefix and Suffix.
  - BlendsJudge.py: The method of using GED.
  - Trie.py: A external file used to creat dictionary tree.(https://blog.csdn.net/ANNILingMo/article/details/80879910)
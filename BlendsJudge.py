import tire
import Trie

import editdistance
#open dict

def opendict():
    dictlist=[]
    f1 = open("dict.txt", "r")
    for words in f1:
        lenword=len(words)
        if duplicate(words) ==1 and lenword<=14:
            dictwords = words.strip()
            dictlist.append(dictwords)
    f1.close()
    return dictlist


#open blends
def openblends():
    blendlist=[]
    f3 = open("blends.txt","r")
    blendline=f3.readlines()
    for line in blendline:
        blend,part1,part2=line.split()
        blendlist.append(blend)
    f3.close
    return blendlist

def duplicate(word):
    temp=1
    count=0
    lenword=len(word)
    for i in range(lenword-1):

        if word[i]==word[i+1]:
            temp=temp+1
        else:
            if temp>count and temp>=2:
                count=temp
            temp=1
    if count>=3:
        return 0
    return 1


def creattree():
    diclist=opendict()
    blendssearch = Trie.Trie()
    lendict=len(diclist)
    for i in range(lendict):
        blendssearch.insert(diclist[i])
    return blendssearch

def creatreversetree():
    dictlist = []
    f1 = open("dict.txt", "r")
    for words in f1:
        if duplicate(words) == 1:
            dictwords = words.strip()
            dicwords=dictwords[::1]
            dictlist.append(dicwords)
    f1.close()
    research =Trie.Trie()
    lendict = len(dictlist)
    for i in range(lendict):
        research.insert(dictlist[i])
    return research


def getpre(word,length):
    pre=""
    for i in range(length):
        pre=pre+word[i]
    return pre

blendlist=openblends()
blendssearch = creattree()
research = creatreversetree()
candilist=[]
reverselist=[]
prelist = []
sulist=[]
wordlist=[]

f2=open("candidates.txt","r")
for words in f2:
    if duplicate(words) == 1:#remove useless words
        candiwords=words.strip()#remove the "\n"
        #reverseword=candiwords[::1]
        candilist.append(candiwords)
        #reverselist.appned(reverseword)
f2.close()
lencan=len(candilist)
for i in range(lencan):
    if i==1:
        print("begin")
    if i==1500:
        print("p1")
    if i==3000:
        print("p2")
    if i==5000:
        print("p3")
    if i==8000:
        print("p4")

    word=candilist[i]
    reverseword=word[::-1]
    #print(word)
    lenword = len(word)  # length of word
    #print(lenword)
    if lenword<=3 or lenword>12:
         continue
    else:
        for j in range(2,lenword-1):
            del prelist[:]
            prefixes=getpre(word,j)
            #print(prefixes)
            sufiex=getpre(reverseword,lenword-j)
            if blendssearch.startsWith(prefixes) and research.startsWith(sufiex):
                prelist=blendssearch.getstart(prefixes)
                #print(prelist)
                sulist=research.getstart(sufiex)
                lenpre=len(prelist)
                lensu=len(sulist)
                for i in range(lenpre):
                    for j in range(lensu):
                        blendps=prelist[i]+sulist[j]
                        thisv = editdistance.eval(blendps, word)

                        if word not in wordlist and thisv<=5:
                            wordlist.append(word)
                #blendword=prefixes+sufiex
                #print(blendword)
                #thisv = editdistance.eval(blendword, word)
                #print(thisv)
                #print(thisv)
                #if thisv<minthisv:
                    #minthisv=thisv
                    #print(minthisv)
                #if word not in wordlist :
                    #wordlist.append(word)
num=0.0
lenlist=len(wordlist)
print(lenlist)
for i in range(lenlist):
    if wordlist[i] in blendlist:
        num=num+1
print(num)

recall=num/151
pre=num/lenlist
recallper = int(recall * 100)
preper = int(pre * 100)
print len(candilist)
print "recall:",recall
print "precision:",pre

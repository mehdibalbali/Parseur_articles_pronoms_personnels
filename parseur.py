# coding: utf-8
import re
import fonctions as fun


blanks_between_points = re.compile('(?<=[\!\?\.]) (?=[\!\?\.])')

points       = re.compile('[\.]+')
interogation = re.compile('[\?]+')
deuxPoints   = re.compile('[\:]+')
exclamation  = re.compile('[\!]+')
retourchariot = re.compile('[\n]+')
underscore    = re.compile('[\_]+')

intermediate_punctuation = re.compile('[\.]+')

word_breaks = re.compile('\-[\n\r]+')

def split_to_sentence(text):
    ending_punctuation = re.compile('[\!\?\.]+')
    text=ending_punctuation.split(text)
    return text

def clean_text(text):
    text0 = underscore.sub(' ',text)
    text1 = retourchariot.sub(' ',text0)
    text2 = points.sub('.\n',text1)
    text3 = exclamation.sub('!\n',text2)
    text4 = interogation.sub('?\n',text3)
    text5 = deuxPoints.sub(':\n',text4)
    
    return text5

def parser(txt):
    txt=clean_text(txt)
    phrases=split_to_sentence(txt)
    text_tagged=[]
    for x in phrases:
        if "l'" in x or "L'" in x or "la" in x or "les" in x or "Les" in x or "le" in x or "Le" in x:
            tagged=fun.check_sentence(x)
            for x in tagged:
                text_tagged.append(x+" ")
        else:
            text_tagged.append(x)
        
    
    return text_tagged
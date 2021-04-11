import definition as dec
import re

def split_to_word(text):
    separtion_punctuation = re.compile('[\s\']+')
    text =separtion_punctuation.split(text)
    return text

def write_pronom(text):
	with open("resultats/pronom.txt",'a') as txt:
		txt.write(text)


def write_article(text):
	with open("resultats/article.txt",'a') as txt:
		txt.write(text)

def write_unknown(text):
	with open("resultats/unknown.txt",'a') as txt:
		txt.write(text)


def check_sentence(phrase):
	text=split_to_word(phrase)
	list_of_check=["l'","L'","le","Le","la","La","les","Les"]
	for i in range(len(text)):
		if text[i]in list_of_check:
			if(dec.preposition_test(text[i-1].lower())):
				text[i]="<article>"+text[i]+"</article>"
				write_article(text[i]+" "+text[i+1]+"\n")
			elif (dec.negation_test(text[i-1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_possessifs_test(text[i+1].lower())) :
				text[i]="<article>"+text[i]+"</article>"
				write_article(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_possessifs_test(text[i-1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_personnel_test(text[i-1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_demonstratif_test(text[i+1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_indefinis_test(text[i+1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.pronom_relatifs_test(text[i+1].lower())) or (dec.pronom_relatifs_test(text[i-1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.infinitif_test(text[i+1].lower())) or (dec.infinitif_test(text[i-1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.liaisons_test(text[i-1].lower())):
				text[i]="<article>"+text[i]+"</article>"
				write_article(text[i]+" "+text[i+1]+"\n") 
			elif ( dec.preposition_test(text[i-1].lower()) and dec.infinitif_test(text[i+1].lower())):
				text[i]="<pronom>"+text[i]+"</pronom>"
				write_pronom(text[i]+" "+text[i+1]+"\n")
			elif (dec.gerondif_test(text[i+1].lower())):
				text[i]="<article>"+text[i]+"</article>"
				write_article(text[i]+" "+text[i+1]+"\n")
			else :
				text[i]="<article>"+text[i]+"</article>"
				write_article(text[i]+" "+text[i+1]+"\n")

	
	return text

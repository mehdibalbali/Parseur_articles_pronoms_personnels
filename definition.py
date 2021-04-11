def preposition_test(word): 
	preposition = ["À","à", "chez", "dans", "de", "entre", "jusque", "hors", "par", "pour", "sans", "vers","dés","sur",
				"devant","sous","derrière","avant","après","depuis","pendant","jusqu'à","en","avec","selon",
				"envers","sauf","contre","malgré"]
	if word in preposition : 
		return 1
	return 0

def pronom_personnel_test(word):
	pronom_personnel = ["je","me", "moi" ,"soi", 
				"tu", "te",  "toi",
				"il","lui", "le",
				"elle","la",
				"se", "en", "y",
				"nous", "vous" , "eux",
				"ils", "elles", 
				"les", "leur"]
	if word in pronom_personnel: 
		return 1
	return 0

def pronom_demonstratif_test(word) : 
	pronom_demonstratif = ["celui", "celui-ci", "celui-là" ,
				"celle", "celle-ci", "celle-là",				
				"ceux", "ceux-ci", "ceux-là" , "celles", "celles-ci", "celles-là",
				"ce", "ceci", "cela", "ça"]
	if word in pronom_demonstratif:
		return 1
	return 0

def pronom_relatifs_test(word): 
	pronom_relatifs = ["qui", "que", "quoi", "dont", "où",
				"lequel", "auquel", "duquel ", "laquelle", "lesquels" , 
				"auxquels", "desquels ", "lesquelles", "auxquelles", "desquelles","qu'est-ce"]
	if word in pronom_relatifs: 
		return 1
	return 0

def pronom_indefinis_test(word):
	pronom_indefinis = ["on", "tout","un", "une", "l'un", "l'une" , "uns", "unes",
				"autre", "d'autres", "l'autre", "autres","aucun", "aucune", "aucuns", "aucunes",
				"certains", "certaine", "certains", "certaines","tel", "telle", "tels", "telles ",
				" toute", "tous", "toutes","même","mêmes" , "null", "nulle", "nuls", "nulles",
				"quelqu'un", "quelqu'une" , "personne", "autrui", "quiconque",
				"d’aucuns"]
	if word in pronom_indefinis:
		return 1
	return 0

def negation_test(word): 
	if (word =="ne" or word == "non" or "n'" in word ):
		return 1
	return 0


def pronom_possessifs_test(word):
	pronom_possessifs = ["mien", "tien", "sien" ,"mienne",  "tienne", "sienne",
				 "miens", "tiens", "siens ","miennes", "tiennes", "siennes",
				 "nôtre", "vôtre", "leur" , "nôtre", "vôtre", "leur",
				 "nôtres", "vôtres", "leurs"]
	if word in pronom_possessifs:
		return 1
	return 0

def gerondif_test(word):
	if word[-3:]=="ant":
		return 1
	return 0

def liaisons_test(word):
	if word=="et":
		return 1
	return 0

def infinitif_test(word):
	try:
		if word[-2:]=="er" or word[-2:]=="re" or word[-2:]=="ir" or word[-3]=="oir":
			return 1
	except IndexError as e:
		return 0
import sys
import parseur as ps
import re 

#PROJET : Parseur et désambiguïsation entre un article défini et un pronom personnel complément d'objet direct 
#BALBALI MEHDI 
#L3 informatique université Paris 8 
#Ingénierie des langues 
#17806393
#Mehdibalbali@yahoo.fr


def usage():
	print("<usage> main.py *.txt")
	print("Vous trouvez les ficheris textes dans /files")


def write_file(name,txt):
	header = '<?xml version="1.0" encoding="utf-8"?>\n<?xml-stylesheet href="res.xsl" type="text/xsl"?>\n<texte>\n'
	filename_end = re.compile('(?<=\w\.)txt$')
	with open(filename_end.sub('xml', name), 'w') as xml_file:
		xml_file.write(header)
		for x in txt:
			xml_file.write(x)
				
		xml_file.write("\n</texte>")


def main():
	if len(sys.argv)==2:
		file=open(sys.argv[1],'r')
		text=file.read()
		text=ps.parser(text)
		write_file(sys.argv[1],text)
		print("Les résulats sont dans le dossier /resultats")
		print("un fichier XML est générer dans /files")
	else:
		usage()


if __name__ == '__main__':
	main()

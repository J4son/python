import binwalk,argparse,os,sys,re
from binwalk import modules

rep_extract = modules.extractor.ExtractInfo()
rep_extract_directory = "/Users/brur/Downloads/"
fichier_to_extract = "/Users/brur/Downloads/pwnpi-3.0.img"
resultat= " "
pattern = " " 

def extract(fichier_to_extract):
    try:
        if fichier_to_extract:
            for resultat in binwalk.scan(fichier_to_extract,signature=True,extract=True):
                print("%s,%s,%s,%s,%s:" %  (resultat.name,resultat.valid,resultat.display,resultat.extract,resultat.description))
        else:
            print("pas de firmware a traiter")
    except binwalk.ModuleException as error:
        print("Critical faillure:",error)

def liste_fichier(rep_extract_directory):
    print("voici la liste de fichiers")
    for dossier, sous_dossiers, fichiers in os.walk(rep_extract_directory):
        for fichier in fichiers:
            print(os.path.join(dossier, fichier))
            
def open_files(filenames):
    for name in filenames:
        yield open(name)

def recherche_pattern(pattern,lines):
    patc = re.compile(pattern)
    for line in lines:
        if patc.search(line):
            yield line
            
def version():
      print ("version du programme: BINWALK_TOOLS 1.0")
        
def action_all():
    #extract(fichier_to_extract)
    liste_fichier()
    version()
    recherche_pattern()

parser = argparse.ArgumentParser()
parser.add_argument('--extract',help='extrait les fichiers,repertoires du firmware donne en argument')
parser.add_argument('--version',help='affiche la version du script')
parser.add_argument('--liste_fichier',help='liste les fichiers du firmware dans le repertoire donne en argument')
parser.add_argument('--recherche',help='cherche la pattern donnee en argument')
parser.add_argument('--all',help='execute tout !!!')
args = parser.parse_args()

if args.liste_fichier:
    liste_fichier()

if args.recherche:
    recherche_pattern()
     
if args.version:
    version()
     
if args.all:
    action_all()

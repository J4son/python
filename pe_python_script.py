#!/usr/bin/python -O
import pefile
fichier_windows = "/Users/brur/Downloads/crackme2015.zip"

analyse = pefile.PE(fichier_windows)

print("Voici l entete du fichier: \n")
for section in analyse.sections:
    print(section.Name.split('\'')[0],   hex(section.VirtualAddress),hex(section.Misc_VirtualSize),section.SizeOfRawData)


print("\n\nVoici la liste des symboles importes \n")
for entry in analyse.DIRECTORY_ENTRY_IMPORT:
    print entry.dll
    for imp in entry.imports:
        print(hex(imp.address),imp.name)
        
print("\n\nVoici la liste des symboles exporte \n")
for export in analyse.DIRECTORY_ENTRY_EXPORT.symbols:
    print hex(analyse.OPTIONAL_HEADER.ImageBase + export.address), export.name

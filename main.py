"""

hiaba nezegeted a kodot ugyse fogod erteni btw ez egy easter egg xdddd golyofeju kapitany ci,,,,,g


"""



from pathlib import Path
import requests
import time

list = ["http://www.kapitany.webtelek.hu/pr.pdf",
"http://www.kapitany.webtelek.hu/taplalkozas.pdf",
"http://www.kapitany.webtelek.hu/vulkan.pdf",
"http://www.kapitany.webtelek.hu/noiszaporito.pdf",
"http://www.kapitany.webtelek.hu/legzes.pdf",
"http://www.kapitany.webtelek.hu/paksiatomeromu.pdf",
"http://www.kapitany.webtelek.hu/elektronburok-atommag.pdf",
"http://www.kapitany.webtelek.hu/atomkatasztrofak.pdf",
"http://www.kapitany.webtelek.hu/komplex3.pdf",
"http://www.kapitany.webtelek.hu/szerves1.pdf",
"http://www.kapitany.webtelek.hu/kivalaszto.pdf",
"http://www.kapitany.webtelek.hu/keringes.pdf",
"http://www.kapitany.webtelek.hu/izomrendszer.pdf",
"http://www.kapitany.webtelek.hu/immun.pdf",
"http://www.kapitany.webtelek.hu/radioaktivitas.pdf",
"http://www.kapitany.webtelek.hu/betferjar.pdf",
"http://www.kapitany.webtelek.hu/bor.pdf",
"http://www.kapitany.webtelek.hu/csontok.pdf",
"http://www.kapitany.webtelek.hu/csontvazrendszer.pdf",
"http://www.kapitany.webtelek.hu/cukorbetegseg.pdf",
"http://www.kapitany.webtelek.hu/egitestek.pdf",
"http://www.kapitany.webtelek.hu/ember.pdf",
"http://www.kapitany.webtelek.hu/emberrevalas.pdf",
"http://www.kapitany.webtelek.hu/felepitoanyagaink.pdf",
"http://www.kapitany.webtelek.hu/ferfiszaporito.pdf",
"http://www.kapitany.webtelek.hu/taplalkozas-gundel.pdf",
"http://www.kapitany.webtelek.hu/foldrengesek.pdf",
"http://www.kapitany.webtelek.hu/foldtortenet.pdf",
"http://www.kapitany.webtelek.hu/genetika.pdf",
"http://www.kapitany.webtelek.hu/hormonrendszer.pdf",
"http://www.kapitany.webtelek.hu/idegrendszer.pdf"]

print("\nGetting links...")
time.sleep(1)
print("\nLoaded links:", len(list))

print("\nStarting...\n")
time.sleep(0.7)

for x in list:
    url = x
    name = url.split('/')
    name2 =  str(name[3])
    #print(name2)
    filename = Path("./downloaded",name2)
    response = requests.get(url)
    filename.write_bytes(response.content)
    print(name2, '√')
        
print("\nCompleted", '√') 

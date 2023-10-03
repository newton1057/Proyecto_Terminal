import requests
from bs4 import BeautifulSoup
import json
from colorama import Fore
import re

List_Publications = []
List_Authors = []
List_ID_Authors = []

class Author:
    def __init__(self):
        self.MRAuthor_ID = "" # ID del Autor
        self.Name = "" # Nombre del Autor
        self.Gender = "" # Genero del Autor
        self.Classifications = [] # Clasificacion o Areas de Investigacion
        self.Activity_since = 0 # Año de su primera Publicacion
        self.Total_Publications = 0 # Numero total de Publicaciones del Autor

class Publication:
    def __init__(self):
        self.MR_Publication = "" # ID de la publicacion
        self.Name_Publication = "" # Nombre de la publicacion
        self.Authors = [] # Autores relacionados
        self.Classification = "" # Clasificacion de la publicacion

#Función para realizar la conexión a la pagina web para extracción de datos, se recibe un diccionario con las variables de Username y Password
def Connect_Mathscinet(data_access):
    session = requests.session()
    response = session.post("https://uam.elogim.com/auth-meta/login", data=data_access)
    if(response.status_code == 200):
        print(Fore.GREEN + "Sesion correcta ✅")
        print("")
        return session
    else:
        print(Fore.RED + "Sesion erronea ❌")
        exit()

def get_Author(MR_Autor, session: requests):
    page_web = session.get("https://mathscinet.uam.elogim.com/mathscinet/2006/mathscinet/search/author.html?mrauthid=" + MR_Autor)
    page_web = BeautifulSoup(page_web.text, 'html.parser')
    name_author = page_web.find("span", class_="authorName").text
    print (name_author)



def getPublications (session: requests):
    page_web = session.get("https://mathscinet.uam.elogim.com/mathscinet/2006/mathscinet/search/publications.html?arg3=2023&b=4629060&b=4629006&b=4629005&b=4629004&b=4629003&b=4629002&b=4629001&b=4629000&b=4628999&b=4628998&b=4628997&b=4628996&b=4628995&b=4628994&b=4628993&b=4628992&b=4628991&b=4628990&b=4628989&b=4628988&batch_title=Selected%20Matches%20for%3A%20pubyear%3D2023&bdlall=&co4=AND&co5=AND&co6=AND&co7=AND&dr=pubyear&fmt=amsrefs&pg4=AUCN&pg5=TI&pg6=PC&pg7=ALLF&pg8=ET&review_format=html&s4=&s5=&s6=&s7=&s8=All&searchin=&sort=newest&vfpref=html&yearRangeFirst=&yearRangeSecond=&yrop=eq&r=1&extend=1")
    page_web = BeautifulSoup(page_web.text, 'html.parser')
    publications = page_web.find_all('pre') #Limitar a X numero de busquedas Ejemplo publications = page_web.find_all('pre', limit=10) 

    list_publications = []

    print("")
    print(Fore.YELLOW + "Publications")
    print("")
    #For con recorrido de list
    for publication in publications:
        obj_publication = Publication()
        #print("")
        #print(Fore.BLUE + "Publication")
        data_publication = publication.get_text()
        data = []
        data = data_publication.split('\n')
        authors = list(filter(lambda content: 'author' in content, data))
        for author in authors:
            index_1 = author.index('{')
            index_2 = author.index('}')
            author = author[index_1+1:index_2]
            obj_publication.setAuthor(author)

        list_publications.append(obj_publication)
    """
    For con Index
    for publication in range(0, len(publications)):
        obj_publication = Publication()
        print("")
        print(Fore.BLUE + "Publication")
        data_publication = publications[publication].get_text()
        data = []
        data = data_publication.split('\n')
        authors = list(filter(lambda content: 'author' in content, data))
        for author in range(0,len(authors)):
            index_1 = authors[author].index('{')
            index_2 = authors[author].index('}')
            authors[author] = authors[author][index_1+1:index_2]
            obj_publication.setAuthor(authors[author])

        list_publications.append(obj_publication)
    """

    print("Number of publications: " + str(len(list_publications)))
    print("")
    for publication in list_publications:
        print (publication.Authors)
    
def view_Author (Author: Author):
    print ("Datos del Autor")
    print ("MRAutor: " + Author.MRAuthor_ID)
    print ("Name: " + Author.Name) 
    print ("Gender: " + Author.Gender)
    print ("Activity Since: " + Author.Activity_since )
    print ("Total Publications: " + Author.Total_Publications)
    print ("Classifications: ")
    for Classification in range(len(Author.Classifications)):
        print(" * " + Author.Classifications[Classification])
    
    print ("")

def get_Data_Author( session: requests, MR_Author):
    DataWeb = session.get("https://mathscinet.uam.elogim.com/mathscinet/2006/mathscinet/search/author.html?mrauthid=" + MR_Author) # Extrae la data de la Web del Autor
    DataWeb = BeautifulSoup(DataWeb.text, 'html.parser') # Convierte en un objeto BeautifulSoup
    Name = DataWeb.find("span", class_="authorName").text # Buscar el Nombre del Autor
    Table = DataWeb.find("table", class_="table-hover").text # Buscar la primera tabla con los datos del Autor
    author = Author() #Crea el objeto Autor
    author.MRAuthor_ID = MR_Author # Asigna el ID del Autor
    author.Name = Name # Asigna el Nombre del Autor
    
    Table = Table.split('\n') # Divide la tabla del autor en un arreglo por cada salto de linea
    author.Activity_since = Table[20]
    author.Total_Publications = Table[25]
    resp = requests.get('https://api.genderize.io/?name='+ Name[Name.index(',')+2:] +'&country_id=MX') # Genera la peticion a la API para determinar el genero con una probabilidad
    resp = json.loads(resp.text)
    author.Gender = resp['gender'] # Obtiene el genero calculado por la API
    
    Classifications = DataWeb.find_all("div", class_="tagCloud") # Busca el DIV donde se encuentra las Clasificaciones del Autor
    Classifications = Classifications[1].text.split("\n") 
    Classifications = list(filter(None, Classifications)) # Elimina elementos vacios
    Classifications = list( filter(lambda Classification: Classification != "Other", Classifications) ) # Elimina en caso de que exista la clasificacion Other
    author.Classifications = Classifications
    view_Author (author)
    
    return author

def get_Publications_Author (session: requests, MR_Author):
    DataWeb = session.get("https://mathscinet.uam.elogim.com/mathscinet/2006/mathscinet/search/publications.html?pg1=INDI&s1="+ MR_Author +"&sort=Newest&vfpref=html&r=1&extend=1&fmt=amsrefs")
    DataWeb = BeautifulSoup(DataWeb.text, 'html.parser')
    Publications = DataWeb.find_all('pre', limit=2)
    print("")
    print(Fore.YELLOW + "Publications of author: " + MR_Author)
    print("")
    for publication in Publications:
        Object_Publication = Publication()
        data_publication = publication.get_text()
        #print(data_publication)
        data = []
        data = data_publication.split('\n')
        #print (data)

        #Obtener MR de la Publicacion
        MR_Publication = list(filter(lambda content: '\\bib' in content, data))
        index_1 = MR_Publication[0].index('{')
        index_2 = MR_Publication[0].index('}')
        MR_Publication = MR_Publication[0][index_1+1:index_2]
        print("ID Publication: " + MR_Publication)
        Object_Publication.MR_Publication = MR_Publication
        
        authors = list(filter(lambda content: 'author' in content, data))
        for author in authors:
            index_1 = author.index('{')
            index_2 = author.index('}')
            author = author[index_1+1:index_2]
            print("Author: " + author)
            Object_Publication.Authors.append(author)
        print("")
        List_Publications.append(Object_Publication)
        get_Data_Publication(session, MR_Publication)
        #if(not validate_publication_in_list(List_Publications, MR_Publication)):
         #   get_Data_Publication(session, MR_Publication)
        
def get_Data_Publication (session: requests, MR_Publication):
    DataWeb = session.get("https://mathscinet.uam.elogim.com/mathscinet/2006/mathscinet/search/publdoc.html?arg3=&co4=AND&co5=AND&co6=AND&co7=AND&dr=all&pg4=AUCN&pg5=TI&pg6=MR&pg7=ALLF&pg8=ET&r=1&review_format=html&s4=&s5=&s6="+ MR_Publication +"&s7=&s8=All&sort=Newest&vfpref=html&yearRangeFirst=&yearRangeSecond=&yrop=eq")
    DataWeb = BeautifulSoup(DataWeb.text, 'html.parser')
    DataWeb = DataWeb.find("div", class_="headline")
    #print (DataWeb)
    DataWeb = DataWeb.find_all('a', href=True)
    print("")
    print("")
    
    for Elements in range(0, len(DataWeb)):
        if('author.html' in str(DataWeb[Elements]['href'])):
            URL = str(DataWeb[Elements]['href'])
            #print (URL)
            URL = URL[URL.index('=') + 1:]
            
            print("Author ID: "+ URL)
            if not URL in List_ID_Authors:
                print("No existe")
                Author_ = get_Data_Author(session, URL)
                List_Authors.append(Author_)
                List_ID_Authors.append(URL)

                get_Publications_Author(session, URL)
            else:
                print("Ya ha sido agregado")
            #

def validate_publication_in_list(List_Publications : [], MR_Publication): 
    for i in range(0, len(List_Publications)):
        if List_Publications[i].MR_Publication == MR_Publication:
            print ("Publicacion ya agregada previamente! ✅")
            return True
    return False

def main():    
    with open('config.json') as config_file:
        data = json.load(config_file)

    Mathscinet = data['Mathscinet']
    data_access = {"httpd_username" : Mathscinet['username'],"httpd_password" : Mathscinet['password']}
    session = Connect_Mathscinet(data_access)

    List_MR_Authors = data['MR_Authors_Seeds']

    for i in range(0, len(List_MR_Authors)):
        Author_ = get_Data_Author(session, List_MR_Authors[i])
        List_Authors.append(Author_)
        List_ID_Authors.append(Author_.MRAuthor_ID)

    get_Publications_Author(session, List_Authors[0].MRAuthor_ID)

    print(List_ID_Authors)
    for i in range(0, len(List_Authors)):
        print("Author")
        print(List_Authors[i].MRAuthor_ID)
        print(List_Authors[i].Name)
        print(List_Authors[i].Gender)

    print(len(List_ID_Authors))

if __name__ == "__main__":
    main()
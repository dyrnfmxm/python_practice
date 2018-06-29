import requests
from bs4 import BeautifulSoup

urls=["https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Bolly Nan",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Casa Pepe",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Aux Artistes",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Kyobashi",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Delitaly",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chez Georges",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+PNY OBK - Paris New York",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chikoja",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Taing Song-Heng",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Thai-Vien",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Dauphin",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+CopperBay",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Cantine de Belleville",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Progrès",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Starvin’Joe",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+L’Esplanade",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+231 East Street",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Crêperie Traditionnelle",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Frog Burger",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chez Monsieur",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Petit Villiers",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Extra Old Cafe",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Monteverdi",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chez Léa",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Café Madeleine",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Pottoka",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Casa Bini",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Valmy",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Pooja",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+King Falafel Palace",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+BocaMexa",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+A Noste",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Beurre Noisette",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Willi’s Wine Bar",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Wagon Bleu",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Castiglione",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Pipos",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chez Ginette",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Bastringue",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Brasserie Printemps",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Cantine Du Troquet",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Bistrot Beaubourg",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Murat",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Bibimbap",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Mamie Burger",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Chez Barbara",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Fondus de la Raclette",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Petits Plats",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Contrescarpe",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Duc des Lombards",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Indiana Café",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Vache et le Cuisinier",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Heureux Comme Alexandre",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Lhassa",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Villa Papillon",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Komptoir",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Mondes Bohèmes",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Léon de Bruxelles",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Bistrot 31",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Al-Ajami",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Udon Jubey",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Tribal Café",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Pasdeloup",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Cerise Sur la Pizza",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Café Louise",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Dédé la Frite",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Bistrot Mélac",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Café Cassette",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+HD Diner",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Darai",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Coffee Parisien",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Sushi Wa",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Matamata Coffee Bar",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Pharmacie",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Boucherie Roulière",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Au Verre Luisant",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Oresto",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Golden Pat",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Mondrian",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Little Cantine",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Aux Prés",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Little Cantine",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+L’Afghanistan",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Little Hanoï",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Ma Bourgogne",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Petite Chaise",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Bistro des Oies",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Comptoir Moderne",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Negus",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+6 New York",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Paname Art Café",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Falstaff",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+L’Auberge des Deux Ponts",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+The Sunken Chip",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Rachel’s",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Mandalay",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Cosi",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Nos Ancêtres les Gaulois",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Petit Bleu",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+L’Ambroisie",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Tien Hiang",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Champs de Mars",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+New Jawad",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Backstage Café",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Pink Flamingo",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Les Fabricants",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Patio",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Cantine du Troquet Dupleix",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Cristal Room Baccarat",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Afghani",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Fidélité",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Lavomatic",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Le Campanella",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+HD Diner",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+La Grille Montorgueil",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Café du Centre",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Creperie Le Crepuscule",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+A La Casa Del Fox",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Ethiopia",
"https://www.google.co.kr/search?source=hp&ei=iDD6WqveOISn8QXL944omwAg&q=paris+Lazare",
]
values=0
def page_download(url):
    response = requests.get(url)
    return response.text

def page_parse(html):
    ret_dict = {}
    parser = BeautifulSoup(html, "html.parser")
    ret_dict["review"]= parser.find('div', class_= "slp").text.strip()
    
    return ret_dict

while values < 1000:
    if __name__ == '__main__':
        html = page_download(urls[values])
        result = page_parse(html)
        for key, value in result.items():
            print(value)
            values +=1

            

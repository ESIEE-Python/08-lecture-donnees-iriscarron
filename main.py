"""
docstring
"""
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename,  mode='r', encoding='utf8') as f:
        reader = csv.reader(f,  delimiter=';')
        l = []
        for e in reader:
            ligne=[]
            for i in e:
                ligne.append(int(i))
            l.append(ligne)
    return l

def get_list_k(data, k):
    """
    data 
    """
    return data[k]

def get_first(l):
    """
    premier element 
    """
    return l[0]

def get_last(l):
    """
    dernier 
    """
    return l[-1]

def get_max(l):
    """
    max 
    """
    return max(l)

def get_min(l):
    """
    min 
    """
    return min(l)

def get_sum(l):
    """
    somme 
    """
    return sum(l)


def main():
    """
    fonction principale 
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))


if __name__ == "__main__":
    main()

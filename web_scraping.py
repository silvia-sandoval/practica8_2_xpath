from lxml import etree, html
from sys import stdout
import requests


def main():
    ###################### PETICIÓ WEB ######################
    request = requests.get('https://scrapepark.org')
    tree = html.fromstring(request.content)
    ##########################################################

    ######################### XPATH ##########################
    xpath = "//head/title"
    ##########################################################

    # Avalua l'expressió XPath
    resultat = tree.xpath(xpath)
    printXPath(resultat)


# Funció que imprimeix correctament el resultat de la cerca amb XPath en funció de
# si el resultat és un XML, un HTML, un string, o bé una llista.
def printXPath(result):
    # si és string
    if type(result) is str or type(result) is etree._ElementUnicodeResult:
        print(result)

    # si és xml
    elif type(result) is etree._Element:
        et = etree.ElementTree(result)
        et.write(stdout.buffer, pretty_print=True)

    # si és html
    elif type(result) is html.HtmlElement:
        print(str(html.tostring(result))
              .replace("b'", "").replace("'", "")   # esborra la marca de bytes
              .replace("\\r\\n", "\n"))             # aplica els salts de línia marcats

    # si és llista, un a un recursivament.
    elif type(result) is list:
        if len(result) == 0:
            print([])

        for recursion in result:
            printXPath(recursion)

    # error
    else:
        print("No es reconeix el tipus (", type(result), ") de ", result)


# Main del programa
if __name__ == '__main__':
    main()

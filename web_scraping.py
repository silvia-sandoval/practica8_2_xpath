from lxml import etree, html
from sys import stdout
import requests


def main():

    request = requests.get('https://scrapepark.org/')

    ############ FITXER XML ############
    # tree = etree.parse('ods.xml')
    tree = html.fromstring(request.content)
    ####################################

    ############## XPATH ###############
    xpath = "//div/div/h5/text()[normalize-space()='12']/../../h6/text()normalize-space()"
    xpath = "/html/body/footer//div[@class='information-f']/p[3]/span/text()"
    ####################################

    # Evalua l'expressió XPath
    resultat = tree.xpath(xpath)
    printXML(resultat)


# Funció que imprimeix correctament el resultat de la cerca amb XPath en funció de si el resultat
# és un XML o bé un string, o bé una llista.
def printXML(xml):
    # si és string
    if type(xml) is etree._ElementUnicodeResult:
        print(xml)

    # si és xml, prettyprint
    elif type(xml) is etree._Element:
        et = etree.ElementTree(xml)
        et.write(stdout.buffer, pretty_print=True)

    elif type(xml) is html.HtmlElement:
        print(html.tostring(xml))

        # si és llista, un a un recursivament.
    elif type(xml) is list:
        if len(xml) == 0:
            print([])
        for x in xml:
            printXML(x)

    # error
    else:
        print("No es reconeix el tipus (", type(xml), ") de ", xml)


# Main del programa
if __name__ == '__main__':
    main()

import owlready2


if __name__ == "__main__":
    CSO = owlready2.get_ontology(r"file://C:\Users\Cosmin\Desktop\CSO.3.1.owl").load()
    word = input("Input : ")
    print(CSO.search(iri="*" + word + "*"))

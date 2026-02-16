class Acervo:
    def __init__(self):
        self.__acervo = {}
    
    def getacervo(self):
        return self.__acervo
    def adicionar_livro(self,livro,quantidade):
        idlivro = livro.get_id()
        if idlivro in self.__acervo:
            self.__acervo[idlivro]["Quantidade"] += quantidade
        else:
            self.__acervo[idlivro]  = {
                "livro": livro,
                "Quantidade": quantidade
            }    
    


    def consultar_acervo(self):
        acervo = self.__acervo
        return {
            dados["livro"]: dados["Quantidade"]
            for dados in acervo.values()
        }
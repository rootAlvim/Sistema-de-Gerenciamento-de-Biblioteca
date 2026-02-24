class Acervo:
    def __init__(self):
        self.__acervo = {}
    
    def getAcervo(self):
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
    
    def remover_livro_nome(self,nome,quantidade):
        for n in self.__acervo.values():
            livro = n['livro']
            if livro.titulo.lower() == nome.lower():
                if  n['Quantidade'] < quantidade:
                    raise ValueError("Quantidade indisponivel")
                elif n['Quantidade'] == quantidade:
                    del self.__acervo[livro.get_id()]
                    return True
                else:
                    n['Quantidade'] -= quantidade
                    return True
        raise ValueError('Livro não encontrado')
    
    def remover_livro_id(self,id,quantidade = None):
        if id in self.__acervo:
            if quantidade is None:
                del self.__acervo[id]
            else:
                if self.__acervo[id]['Quantidade'] < quantidade:
                    raise ValueError("Quantidade indisponivel")
                elif self.__acervo[id]['Quantidade'] == quantidade:
                    del self.__acervo[id]
                else:
                    self.__acervo[id]['Quantidade'] -= quantidade
        else:
            raise ValueError("Livro não encontrado")
      
    def livro_disponibilidade(self,id,quantidade):
        if id not in self.__acervo:
            raise ValueError("Livro não encontrado")
        if self.__acervo[id]['Quantidade'] < quantidade:
            raise ValueError('Quantidade indisponivel no acervo')
            
    def consultar_acervo(self):
        acervo = self.__acervo
        return {
            dados["livro"]: dados["Quantidade"]
            for dados in acervo.values()
        }


    def consultar_livro_nome(self,nome):
        for n in self.__acervo.values(): 
            if n['livro'].titulo.lower() == nome.lower():
                livro = n['livro']
                qntd = n['Quantidade']
                return livro,qntd
            
    def consultar_livro_id(self,id):
        if id in self.__acervo:
            livro = self.__acervo[id]['livro']
            qntd = self.__acervo[id]['Quantidade']
            return livro,qntd
        
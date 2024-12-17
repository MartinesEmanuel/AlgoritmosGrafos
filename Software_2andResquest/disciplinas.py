from enum import Enum
from typing import List, Optional

class OFERTA(Enum):
    PRIMEIRO_SEMESTRE = 1
    SEGUNDO_SEMESTRE = 2
    DESCONHECIDO = 3

class Disciplina: # Classe vazia para poder definir tipo de argumento List[Disciplina] no construtor da classe abaixo
    pass

class Disciplina:
    def __init__(self, sigla: str, nome: str, oferta: OFERTA, requisitosDiretos: List[Disciplina], optativa: bool = False):
        self.__sigla = sigla
        self.__nome = nome
        self.__oferta = oferta
        self.__requisitosDiretos = requisitosDiretos
        self.__optativa = optativa

    @property
    def sigla(self) -> str:  
        return self.__sigla
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def oferta(self) -> OFERTA:  
        return self.__oferta
    
    @property
    def requisitosDiretos(self) -> List[Disciplina]:  
        return self.__requisitosDiretos
    
    @property
    def optativa(self) -> bool:  
        return self.__optativa

class CURSO(bytes, Enum):
    def __new__(cls, id: int, nome: str, sigla: str):
        obj = bytes.__new__(cls, [id])
        obj._value_ = id
        obj.__nome = nome
        obj.__sigla = sigla
        obj.__disciplinas = []
        obj.__disciplinas_optativas = []
        obj.__grafo = {}
        return obj

    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def sigla(self) -> str:
        return self.__sigla

    @property
    def disciplinas(self) -> List[Disciplina]:
        return self.__disciplinas
    
    @property
    def disciplinas_optativas(self) -> List[Disciplina]:
        return self.__disciplinas_optativas
    
    @property
    def grafo(self) -> dict:
        return self.__grafo
    
    @grafo.setter
    def grafo(self, grafo: dict):
        self.__grafo = grafo

    @property
    def grafo_invertido(self) -> dict:
        return self.__grafo_invertido
    
    @grafo.setter
    def grafo_invertido(self, grafo: dict):
        self.__grafo_invertido = grafo

    CCO = (1, "CCO", "Ciência da Computação")
    SIN = (2, "SIN", "Sistemas de Informação")

def registrarDisciplinasCCO():
    #1 sem
    MAT00A = Disciplina("MAT00A", "Cálculo A", OFERTA.PRIMEIRO_SEMESTRE, [])
    XMAC01 = Disciplina("XMAC01", "Matemática Discreta", OFERTA.PRIMEIRO_SEMESTRE, [])
    XDES01 = Disciplina("XDES01", "Fundamentos de Programação", OFERTA.PRIMEIRO_SEMESTRE, [])
    CRSC03 = Disciplina("CRSC03", "Arquitetura de Computadores I", OFERTA.PRIMEIRO_SEMESTRE, [])
    CAHC04 = Disciplina("CAHC04", "Projeto Integrado", OFERTA.PRIMEIRO_SEMESTRE, [])

    #2 sem
    CMAC04 = Disciplina("CMAC04", "Modelagem Computacional", OFERTA.SEGUNDO_SEMESTRE, [MAT00A])
    MAT00B = Disciplina("MAT00B", "Cálculo B", OFERTA.SEGUNDO_SEMESTRE, [MAT00A])
    CDES05 = Disciplina("CDES05", "Programação Lógica e Funcional", OFERTA.SEGUNDO_SEMESTRE, [XMAC01])
    CTCO01 = Disciplina("CTCO01", "Algoritmos e Estrutura de Dados I", OFERTA.SEGUNDO_SEMESTRE, [XDES01])
    CRSC04 = Disciplina("CRSC04", "Arquitetura de Computadores II", OFERTA.SEGUNDO_SEMESTRE, [CRSC03])

    #3 sem
    XMAC02 = Disciplina("XMAC02", "Métodos Matemáticos para Análise de Dados", OFERTA.PRIMEIRO_SEMESTRE, [MAT00A, XMAC01, CTCO01])
    XDES02 = Disciplina("XDES02", "Programação Orientada a Objetos", OFERTA.PRIMEIRO_SEMESTRE, [XDES01])
    CMAC03 = Disciplina("CMAC03", "Algoritmos em Grafos", OFERTA.PRIMEIRO_SEMESTRE, [CTCO01])
    XDES04 = Disciplina("XDES04", "Engenharia de Software I", OFERTA.PRIMEIRO_SEMESTRE, [])
    CTCO02 = Disciplina("CTCO02", "Algoritmos e Estrutura de Dados II", OFERTA.PRIMEIRO_SEMESTRE, [CTCO01])
    CRSC02 = Disciplina("CRSC02", "Sistemas Operacionais", OFERTA.PRIMEIRO_SEMESTRE, [CRSC04])

    #4 sem
    CMAC05 = Disciplina("CMAC05", "Cálculo Numérico para Computação", OFERTA.SEGUNDO_SEMESTRE, [MAT00A])
    XDES03 = Disciplina("XDES03", "Programação Web", OFERTA.SEGUNDO_SEMESTRE, [XDES02])
    CTCO04 = Disciplina("CTCO04", "Projeto e Análise de Algoritmos", OFERTA.SEGUNDO_SEMESTRE, [CTCO02])
    CRSC05 = Disciplina("CRSC05", "Sistemas Embarcados", OFERTA.SEGUNDO_SEMESTRE, [CTCO01, CRSC04])
    XRSC01 = Disciplina("XRSC01", "Redes de Computadores", OFERTA.SEGUNDO_SEMESTRE, [CRSC02])

    #5 sem
    XMCO01 = Disciplina("XMCO01", "Inteligência Artificial", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02])
    CMCO05 = Disciplina("CMCO05", "Introdução à Computação Visual", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02, XDES02])
    CTCO03 = Disciplina("CTCO03", "Análise e Projeto Orientados a Objetos", OFERTA.PRIMEIRO_SEMESTRE, [XDES02])
    CTCO05 = Disciplina("CTCO05", "Teoria da Computação", OFERTA.PRIMEIRO_SEMESTRE, [CDES05, CTCO04])
    XPAD01 = Disciplina("XPAD01", "Banco de Dados I", OFERTA.PRIMEIRO_SEMESTRE, [CTCO02])

    #6 sem
    XAHC02 = Disciplina("XAHC02", "Interação Humano-Computador", OFERTA.SEGUNDO_SEMESTRE, [XDES03])
    CTCO06 = Disciplina("CTCO06", "Compiladores", OFERTA.SEGUNDO_SEMESTRE, [CTCO05])
    XAHC01 = Disciplina("XAHC01", "Computação e Sociedade", OFERTA.SEGUNDO_SEMESTRE, [])

    # Não optativas
    CURSO.CCO.disciplinas.extend([
        MAT00A, XMAC01, XDES01, CRSC03, CAHC04, CMAC04, MAT00B, CDES05, CTCO01, CRSC04,
        XMAC02, XDES02, CMAC03, XDES04, CTCO02, CRSC02, CMAC05, XDES03, CTCO04, CRSC05,
        XRSC01, XMCO01, CMCO05, CTCO03, CTCO05, XPAD01, XAHC02, CTCO06, XAHC01
    ])


    #Optativas
    #Administração e gestão
    INTADM = Disciplina("INTADM", "Introdução à Administração", OFERTA.DESCONHECIDO, [], True)
    SADG01 = Disciplina("SADG01", "Gestão e Governança", OFERTA.PRIMEIRO_SEMESTRE, [INTADM], True)
    SADG02 = Disciplina("SADG02", "Economia da Informação", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    IEPG01 = Disciplina("IEPG01", "Empreendedorismo e Inovação", OFERTA.DESCONHECIDO, [], True)
    IEPG14 = Disciplina("IEPG14", "Comportamento Organizacional I", OFERTA.DESCONHECIDO, [], True)
    ADM03E = Disciplina("IEPG14", "Empreendedorismo Tecnológico", OFERTA.DESCONHECIDO, [IEPG01], True)
    CURSO.CCO.disciplinas_optativas.extend([
        INTADM, SADG01, SADG02, IEPG01, IEPG14, ADM03E
    ])


    #Aspectos Humanos em Computação
    XAHC06 = Disciplina("XAHC06", "Tópicos em AHC", OFERTA.DESCONHECIDO, [], True)
    ADM08H = Disciplina("ADM08H", "Psicologia: As relações Indivíduo-Grupo", OFERTA.DESCONHECIDO, [], True)
    ADM52H = Disciplina("ADM52H", "Comportamento Organizacional II", OFERTA.DESCONHECIDO, [], True)
    ADM54H = Disciplina("ADM54H", "Gestão de Carreira", OFERTA.DESCONHECIDO, [], True)
    ADM58H = Disciplina("ADM58H", "Psicologia Organizacional e do Trabalho", OFERTA.DESCONHECIDO, [], True)
    ADM51H = Disciplina("ADM51H", "Ciências, Tecnologias e Organizações", OFERTA.DESCONHECIDO, [], True)
    CURSO.CCO.disciplinas_optativas.extend([
        XAHC06, ADM08H, ADM52H, ADM54H, ADM58H, ADM51H
    ])


    #Redes e Sistemas Computacionais
    XRSC09 = Disciplina("XRSC09", "Sistemas Distribuídos", OFERTA.SEGUNDO_SEMESTRE, [XRSC01], True)
    ECOS04 = Disciplina("ECOS04", "Simulação e Avaliação de Desempenho", OFERTA.DESCONHECIDO, [XRSC09], True)
    XRSC10 = Disciplina("XRSC10", "Tópicos em RSC", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    XRSC08 = Disciplina("XRSC08", "Programação Paralela", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    XRSC07 = Disciplina("XRSC07", "Computação em Nuvem", OFERTA.SEGUNDO_SEMESTRE, [XRSC01], True)
    XRSC06 = Disciplina("XRSC06", "Auditoria e Segurança de SI", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    CURSO.CCO.disciplinas_optativas.extend([
        XRSC09, ECOS04, XRSC10, XRSC08, XRSC07, XRSC06
    ])


    #Metodologias Computacionais e Otimização
    CMCO06 = Disciplina("CMCO06", "Modelagem Geométrica e Visual", OFERTA.SEGUNDO_SEMESTRE, [XMAC02, CMCO05], True)
    CMCO07 = Disciplina("CMCO07", "Visão Computacional", OFERTA.PRIMEIRO_SEMESTRE, [XMAC01, CMCO05], True)
    XMCO03 = Disciplina("XMCO03", "Métodos Exatos", OFERTA.SEGUNDO_SEMESTRE, [XMAC02, CMAC03], True)
    XMCO04 = Disciplina("XMCO04", "Metaheurísticas", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02, CMAC03], True)
    XMCO05 = Disciplina("XMCO05", "Tópicos em MCO", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02, CMAC03], True)
    CURSO.CCO.disciplinas_optativas.extend([
        XMCO05, XMCO04, XMCO03, CMCO07, CMCO06
    ])

    #Persistência e Análise de Dados
    SPAD02 = Disciplina("SPAD02", "Bancos de Dados II", OFERTA.SEGUNDO_SEMESTRE, [XPAD01], True)
    SPAD03 = Disciplina("SPAD03", "Introdução à Análise de Dados", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02], True)
    XPAD04 = Disciplina("XPAD04", "Banco de Dados NoSQL", OFERTA.SEGUNDO_SEMESTRE, [XPAD01], True)
    XPAD08 = Disciplina("XPAD08", "Tópicos em PAD", OFERTA.DESCONHECIDO, [XPAD01], True)
    CURSO.CCO.disciplinas_optativas.extend([
        SPAD02, SPAD03, XPAD04, XPAD08
    ])

    #Desenvolvimento e Engenharia de Software
    XDES08 = Disciplina("XDES08", "Arquitetura de Software", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES09 = Disciplina("XDES09", "Padrões de Projeto", OFERTA.SEGUNDO_SEMESTRE, [XDES03, XDES04], True)
    XDES10 = Disciplina("XDES10", "Engenharia de Software Experimental", OFERTA.SEGUNDO_SEMESTRE, [XDES04], True)
    XDES11 = Disciplina("XDES11", "Tópicos em DES I", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES12 = Disciplina("XDES12", "Tópicos em DES II", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES13 = Disciplina("XDES13", "Desenvolvimento de Jogos", OFERTA.SEGUNDO_SEMESTRE, [XDES01], True)
    XDES14 = Disciplina("XDES14", "Desenvolvimento para Dispositivos Móveis", OFERTA.PRIMEIRO_SEMESTRE, [XDES03], True)
    SDES05 = Disciplina("SDES05", "Engenharia de Software II", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES15 = Disciplina("XDES15", "Reutilização de Software", OFERTA.PRIMEIRO_SEMESTRE, [SDES05, XDES02, XDES09], True)
    SDES06 = Disciplina("SDES06", "Gerência de Projetos de Software", OFERTA.SEGUNDO_SEMESTRE, [SDES05], True)
    SDES07 = Disciplina("SDES07", "Desenvolvimento de Sistemas Web", OFERTA.PRIMEIRO_SEMESTRE, [XDES04, XPAD01, XDES03], True)
    ECOX21 = Disciplina("ECOX21", "Maratona de Programação I", OFERTA.DESCONHECIDO, [CTCO01], True)
    ECOX22 = Disciplina("ECOX22", "Maratona de Programação II", OFERTA.DESCONHECIDO, [ECOX21], True)
    CURSO.CCO.disciplinas_optativas.extend([
        XDES08, XDES09, XDES10, XDES11, XDES12,
        XDES13, XDES14, XDES15, SDES05, SDES06,
        SDES07, ECOX21, ECOX22
    ])

    
    CURSO.CCO.grafo = {'INICIO': []}
    for disciplina in CURSO.CCO.disciplinas:
        CURSO.CCO.grafo[disciplina.sigla] = []
        for requisito in disciplina.requisitosDiretos:
            CURSO.CCO.grafo[disciplina.sigla].append(requisito.sigla)
        if len(disciplina.requisitosDiretos) == 0:
            CURSO.CCO.grafo[disciplina.sigla] = ['INICIO'] 

    CURSO.CCO.grafo_invetido = {}
    for disciplina in CURSO.CCO.grafo:
        for requisito in disciplina:
            if not requisito in CURSO.CCO.grafo_invetido:
                CURSO.CCO.grafo_invetido[requisito] = [disciplina]
            else:
                CURSO.CCO.grafo_invetido[requisito].append(disciplina)


def registrarDisciplinasSIN():
    MAT00A = Disciplina("MAT00A", "Cálculo A", OFERTA.PRIMEIRO_SEMESTRE, [])
    XDES01 = Disciplina("XDES01", "Fundamentos de Programação", OFERTA.PRIMEIRO_SEMESTRE, [])
    STCO01 = Disciplina("STCO01", "Algoritmos e Programação I", OFERTA.SEGUNDO_SEMESTRE, [XDES01])
    SRSC03 = Disciplina("SRSC03", "Organização e Arquitetura de Computadores", OFERTA.PRIMEIRO_SEMESTRE, [])
    STCO02 = Disciplina("STCO02", "Algoritmos e Programação II", OFERTA.PRIMEIRO_SEMESTRE, [STCO01])
    XDES02 = Disciplina("XDES02", "Programação Orientada a Objetos", OFERTA.SEGUNDO_SEMESTRE, [XDES01])
    XDES03 = Disciplina("XDES03", "Programação Web", OFERTA.PRIMEIRO_SEMESTRE, [XDES02])
    XDES04 = Disciplina("XDES04", "Engenharia de Software I", OFERTA.SEGUNDO_SEMESTRE, [])
    SDES05 = Disciplina("SDES05", "Engenharia de Software II", OFERTA.PRIMEIRO_SEMESTRE, [XDES04])
    SDES06 = Disciplina("SDES06", "Gerência de Projetos de Software", OFERTA.SEGUNDO_SEMESTRE, [SDES05])
    XPAD01 = Disciplina("XPAD01", "Banco de Dados I", OFERTA.SEGUNDO_SEMESTRE, [STCO02])
    SDES07 = Disciplina("SDES07", "Desenvolvimento de Sistemas Web", OFERTA.PRIMEIRO_SEMESTRE, [XDES03, XDES04, XPAD01])
    SPAD02 = Disciplina("SPAD02", "Banco de Dados II", OFERTA.PRIMEIRO_SEMESTRE, [XPAD01])
    XMAC01 = Disciplina("XMAC01", "Matemática Discreta", OFERTA.SEGUNDO_SEMESTRE, [STCO01])
    XMAC02 = Disciplina("XMAC02", "Métodos Matemáticos para Análise de Dados", OFERTA.SEGUNDO_SEMESTRE, [MAT00A, XMAC01, STCO01])
    SPAD03 = Disciplina("SPAD03", "Introdução à Análise de Dados", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02])
    XMCO01 = Disciplina("XMCO01", "Inteligência Artificial", OFERTA.SEGUNDO_SEMESTRE, [XMAC02])
    SRSC02 = Disciplina("SRSC02", "Sistemas Operacionais", OFERTA.SEGUNDO_SEMESTRE, [STCO01, SRSC03])
    XRSC01 = Disciplina("XRSC01", "Redes de Computadores", OFERTA.PRIMEIRO_SEMESTRE, [SRSC02])
    SMAC03 = Disciplina("SMAC03", "Grafos", OFERTA.SEGUNDO_SEMESTRE, [STCO02])
    IEPG14 = Disciplina("IEPG14", "Comportamento Organizacional I", OFERTA.SEGUNDO_SEMESTRE, [])
    ECN001 = Disciplina("ECN001", "Economia", OFERTA.PRIMEIRO_SEMESTRE, [])
    IEPG01 = Disciplina("IEPG01", "Empreendedorismo e Inovação", OFERTA.PRIMEIRO_SEMESTRE, [])
    ADM03E = Disciplina("ADM03E", "Empreendedorismo Tecnológico", OFERTA.SEGUNDO_SEMESTRE, [IEPG01])
    IEPG10 = Disciplina("IEPG10", "Engenharia Econômica", OFERTA.SEGUNDO_SEMESTRE, [])
    ADM51E = Disciplina("ADM51E", "Gestão do Conhecimento", OFERTA.PRIMEIRO_SEMESTRE, [])
    IEPG22 = Disciplina("IEPG22", "Administração Aplicada", OFERTA.PRIMEIRO_SEMESTRE, [])
    SADG01 = Disciplina("SADG01", "Gestão e Governança de TI", OFERTA.PRIMEIRO_SEMESTRE, [IEPG22])
    IEPG04 = Disciplina("IEPG04", "Mapeamento de Processos", OFERTA.SEGUNDO_SEMESTRE, [])
    XAHC01 = Disciplina("XAHC01", "Computação e Sociedade", OFERTA.SEGUNDO_SEMESTRE, [])
    XAHC02 = Disciplina("XAHC02", "Interação Humano-Computador", OFERTA.PRIMEIRO_SEMESTRE, [XDES03])
    SAHC04 = Disciplina("SAHC04", "Projeto Integrado", OFERTA.PRIMEIRO_SEMESTRE, [])
    SAHC05 = Disciplina("SAHC05", "Fundamentos de Sistemas de Informação", OFERTA.PRIMEIRO_SEMESTRE, [])

    # Não optativas
    CURSO.SIN.disciplinas.extend([
        XDES01, XDES02, XDES03, XDES04, SDES05, SDES06, SDES07,
        SPAD02, SPAD03, XMCO01, XRSC01, SRSC02, SRSC03, STCO01,
        STCO02, MAT00A, XMAC01, XMAC02, SMAC03, IEPG14, ECN001,
        IEPG01, ADM03E, IEPG10, ADM51E, SADG01, IEPG22, IEPG04,
        XAHC01, XAHC02, SAHC04, SAHC05
    ])


    #Optativas
    XDES08 = Disciplina("XDES08", "Arquitetura de Software", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES09 = Disciplina("XDES09", "Padrões de Projeto", OFERTA.SEGUNDO_SEMESTRE, [XDES03, XDES04], True)
    XDES10 = Disciplina("XDES10", "Engenharia de Software Experimental", OFERTA.SEGUNDO_SEMESTRE, [XDES04], True)
    XDES11 = Disciplina("XDES11", "Tópicos em DES I", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES12 = Disciplina("XDES12", "Tópicos em DES II", OFERTA.PRIMEIRO_SEMESTRE, [XDES04], True)
    XDES13 = Disciplina("XDES13", "Desenvolvimento de Jogos", OFERTA.SEGUNDO_SEMESTRE, [XDES01], True)
    XDES14 = Disciplina("XDES14", "Desenvolvimento para Dispositivos Móveis", OFERTA.PRIMEIRO_SEMESTRE, [XDES03], True)
    XDES15 = Disciplina("XDES15", "Reutilização de Software", OFERTA.PRIMEIRO_SEMESTRE, [SDES05, XDES02, XDES09], True)
    ECOX21 = Disciplina("ECOX21", "Maratona de Programação I", OFERTA.SEGUNDO_SEMESTRE, [STCO01], True)
    ECOX22 = Disciplina("ECOX22", "Maratona de Programação II", OFERTA.PRIMEIRO_SEMESTRE, [ECOX21], True)
    CURSO.SIN.disciplinas_optativas.extend([
        XDES08, XDES09, XDES10, XDES11, XDES12, XDES13,
        XDES14, XDES15, ECOX21, ECOX22
    ])


    XPAD04 = Disciplina("XPAD04", "Bancos de Dados NoSQL", OFERTA.SEGUNDO_SEMESTRE, [XPAD01], True)
    SPAD05 = Disciplina("SPAD05", "Análise de Dados Geoespaciais", OFERTA.PRIMEIRO_SEMESTRE, [SPAD02, XDES03], True)
    SPAD06 = Disciplina("SPAD06", "Mineração de Dados ", OFERTA.SEGUNDO_SEMESTRE, [SPAD03], True)
    SPAD07 = Disciplina("SPAD07", "Armazém de Dados", OFERTA.PRIMEIRO_SEMESTRE, [SPAD03], True)
    XPAD08 = Disciplina("XPAD08", "Tópicos em PAD", OFERTA.DESCONHECIDO, [XPAD01, SPAD03], True)
    CURSO.SIN.disciplinas_optativas.extend([
        XPAD04, SPAD05, SPAD06, SPAD07, XPAD08
    ])

    XMCO03 = Disciplina("XMCO03", "Métodos Exatos", OFERTA.SEGUNDO_SEMESTRE, [XMAC02, SMAC03], True)
    XMCO04 = Disciplina("XMCO04", "Metaheurísticas", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02, SMAC03], True)
    XMCO05 = Disciplina("XMCO05", "Tópicos em MCO", OFERTA.PRIMEIRO_SEMESTRE, [XMAC02, SMAC03], True)
    CURSO.SIN.disciplinas_optativas.extend([
        XMCO03, XMCO04, XMCO05
    ])

    CRSC05 = Disciplina("CRSC05", "Sistemas Embarcados", OFERTA.SEGUNDO_SEMESTRE, [SRSC02], True)
    XRSC06 = Disciplina("XRSC06", "Auditoria e Segurança de SI", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    XRSC07 = Disciplina("XRSC07", "Computação em Nuvem", OFERTA.SEGUNDO_SEMESTRE, [XRSC01], True)
    XRSC08 = Disciplina("XRSC08", "Programação Paralela", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    XRSC09 = Disciplina("XRSC09", "Sistemas Distribuídos ", OFERTA.SEGUNDO_SEMESTRE, [XRSC01], True)
    XRSC10 = Disciplina("XRSC10", "Tópicos em RSC", OFERTA.PRIMEIRO_SEMESTRE, [XRSC01], True)
    ECOS04 = Disciplina("ECOS04", "Tópicos em RSC", OFERTA.DESCONHECIDO, [XRSC09], True)
    CURSO.SIN.disciplinas_optativas.extend([
        CRSC05, XRSC06, XRSC07, XRSC08, XRSC09,
        XRSC10, ECOS04
    ])

    SADG02 = Disciplina("SADG02", "Economia da Informação", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    XADG03 = Disciplina("XADG03", "Tópicos em ADG ", OFERTA.DESCONHECIDO, [], True)
    ADM01F = Disciplina("ADM01F", "Finanças: Conceitos e Aplicações", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    IEPG05 = Disciplina("IEPG05", "Finanças para Executivos", OFERTA.SEGUNDO_SEMESTRE, [], True)
    IEPG13 = Disciplina("IEPG13", "Custos Empresariais", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    IEPG15 = Disciplina("IEPG15", "Logística e Gestão da Cadeia de Suprimentos", OFERTA.SEGUNDO_SEMESTRE, [], True)
    CURSO.SIN.disciplinas_optativas.extend([
        SADG02, XADG03, ADM01F, IEPG05, IEPG13,
        IEPG15
    ])
    
    XAHC06 = Disciplina("XAHC06", "Tópicos em AHC", OFERTA.DESCONHECIDO, [], True)
    IEPG21 = Disciplina("IEPG21", "Ciências Humanas e Sociais", OFERTA.DESCONHECIDO, [], True)
    ADM08H = Disciplina("ADM08H", "Psicologia: As relações Indivíduo-Grupo", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    ADM52H = Disciplina("ADM52H", "Comportamento Organizacional II", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    ADM54H = Disciplina("ADM54H", "Gestão de Carreira", OFERTA.SEGUNDO_SEMESTRE, [], True)
    ADM58H = Disciplina("ADM58H", "Psicologia Organizacional e do Trabalho", OFERTA.SEGUNDO_SEMESTRE, [], True)
    ADM51H = Disciplina("ADM51H", "Ciências, Tecnologias e Organizações", OFERTA.PRIMEIRO_SEMESTRE, [], True)
    CURSO.SIN.disciplinas_optativas.extend([
        XAHC06, IEPG21, ADM08H, ADM52H, ADM54H,
        ADM58H, ADM51H
    ])

    CURSO.SIN.grafo = {'INICIO': []}
    for disciplina in CURSO.SIN.disciplinas:
        CURSO.SIN.grafo[disciplina.sigla] = []
        for requisito in disciplina.requisitosDiretos:
            CURSO.SIN.grafo[disciplina.sigla].append(requisito.sigla)
        if len(disciplina.requisitosDiretos) == 0:
            CURSO.SIN.grafo[disciplina.sigla] = ['INICIO'] 

    CURSO.SIN.grafo_invetido = {}
    for disciplina in CURSO.SIN.grafo:
        for requisito in disciplina:
            if not requisito in CURSO.SIN.grafo_invetido:
                CURSO.SIN.grafo_invetido[requisito] = [disciplina]
            else:
                CURSO.SIN.grafo_invetido[requisito].append(disciplina)

registrarDisciplinasCCO()
registrarDisciplinasSIN()

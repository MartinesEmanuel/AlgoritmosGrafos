
grafoSIN = {
  # PRIMEIRO SEMESTRE
  "IEPG01 - Empreendedorismo e Inovação": ["ADM03 - Empreendedorismo Tecnológico"],
  "IEPG02 - Administração Aplicada": ["SADG01 - Gestão e Governança em TI"],
  "MAT00A - Cálculo A": ["XMAC02 - Métodos Matemáticos para Análise de Dados","XMAC03 - Cálculo B"],
  "XDES01 - Fundamentos da Programação": ["ST0001 - Algoritmos e Programação I", "XDES02 - Programação Orientada a Objetos"],
  "SAMC05 - Fundamentos de Sistemas de Informação": [],
  "SAMC02 - Projeto Integrado": [],

  # SEGUNDO SEMESTRE
  "IEPG04 - Mapeamento de Processos": [],
  "XMAC01 - Matemática Discreta":
  ["XMAC02 - Métodos Matemáticos para Análise de Dados"],
  "ST0001 - Algoritmos e Programação I": [
    "XMAC02 - Métodos Matemáticos para Análise de Dados", "SMAC03 - Grafos",
    "ST0002 - Algoritmos e Programação II", "SRSC02 - Sistemas Operacionais"
  ],
  "XDES02 - Programação Orientada a Objetos": ["XDES03 - Programação Web"],
  "XDES04 - Engenharia de Software I": [
    "SDES05 - Engenharia de Software",
    "SDES07 - Gerência de Projeto de Software",
    "DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE"
  ],

  # TERCEIRO SEMESTRE
  "ECN001 - Economia": [],
  "ST0002 - Algoritmos e Programação II": ["XPAD01 - Banco de Dados I"],
  "SRC03 - Organização e Arquitetura de Computadores":
  ["SRSC02 - Sistemas Operacionais"],
  "XDES03 - Programação Web": [
    "XAMC002 - Interação Humano-Computador",
    "SDES07 - Desenvolvimento de Sistemas Web",
    "PERSISTÊNCIA DE DADOS",
    "DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE"
  ],
  "SDES05 - Engenharia de Software II":
  ["SDES06 - Gerência de Projeto de Software"],

  # QUARTO SEMESTRE
  "IEPG14 - Comportamento Organizacional": [],
  "XMAC02 - Métodos Matemáticos para Análise de Dados": [
    "XMC001 - Inteligência Artificial",
    "SPAD03 - Introdução à Análise de Dados II",
    "METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"
  ],
  "SMAC03 - Grafos": ["METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"],
  "XPA001 - Banco de Dados I":
  ["SPA002 - Bancos de Dados II", "SDES07 - Desenvolvimento de Sistemas Web","PERSISTÊNCIA DE DADOS"],
  "SRC02 - Sistemas Operacionais": ["XRS01 - Redes de Computadores"],

  # QUINTO PERÍODO
  "ADMS1E - Gestão do Conhecimento": [],
  "SPAD03 - Introdução à Análise de Dados": ["PERSISTÊNCIA DE DADOS"],
  "SPAD02 - Bancos de Dados II": [],
  "XRS01 - Redes de Computadores": ["REDES E SISTEMAS COMPUTACIONAIS"],

  # SEXTO PERÍODO
  "IEPG10 - Engenharia Econômica": [],
  "XMC001 - Inteligência Artificial": [],
  "SDES06 - Gerência de Projeto de Software": [],

  # SÉTIMO PERÍODO
  "XAM02 - Interação Humano-Computador": [],
  "SDES07 - Desenvolvimento de Sistemas Web": [],

  # OITAVO PERÍODO
  "ADM03E - Empreendedorismo Tecnológico": [],
  "XAM001 - Computação e Sociedade": [],
  "XAMC03 - Metodologia Científica": [],
  "TCC1 - TCC1": [],

  # NONO PERÍODO
  "SADG01 - Gestão e Governança em TI": [],
  "TCC2 - TCC2": [],

  #OPTATIVAS
  "ADMINISTRAÇÃO E GESTÃO":[],
  "METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO":[],
  "PERSISTÊNCIA DE DADOS":[],
  "REDES E SISTEMAS COMPUTACIONAIS":[],
  "DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE":[]
  
}

#--------------------------------------------------------

grafoCCO = {
  # Primeiro Semestre
  "MAT00A - Cálculo A": [
    "CMAC04 - Modelagem computacional", "MAT00B - Cálculo B",
    "XMAC02 - Métodos matemáticos para Análise de Dados",
    "CMAC05 - Cálculo Numérico para Computação",
    "METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"
  ],
  
  "XMAC01 - Matemática Discreta":
  ["XMAC02 - Métodos matemáticos para Análise de Dados", "CDES05 - Programação Lógica e Funcional"],
  
  "XDES01 - Fundamentos de Programação":
  ["XDES02 - Programação Orientada a Objetos", " CTCO01 - Algoritmos e Estruturas de Dados I"],
  "CRSC03 - arquitetura de computadores I": [" CRCS04 - Arquitetura de Computadores II"],
  "CAM004 - Projeto Integrado": [],
  "Optativa em Aspectos Humanos em computação": [],

  # Segundo Semestre
  "MAT00B -  Cálculo B": [],
  "CMAC04 - Modelagem computacional": [],
  "CDES05 - Programação Lógica e Funcional": ["CTC004 - Teoria da computação"],
  "CTCO01 - Algoritmos e Estruturas de Dados I": [
    "XMAC02 - Métodos matemáticos para Análise de Dados",
    "XDES02 - Programação Orientada a Objetos", "CMAC03 Algoritmos em grafos",
    "XDES04 - Engenharia de Software I", "CTCO02 - Algoritmos e Estruturas de Dados II",
    "CRSC05 - Sistemas Embarcados", "CRSC02 - Sistemas Operacionais"
  ],
  "CRSC04 - Arquitetura de Computadores II":
  ["CRSC02 - Sistemas Operacionais", "CRSC05 - Sistemas Embarcados"],

  # Terceiro Semestre
  "XMAC02 - Métodos Matemáticos para Análise de Dados":
  ["XMCO01 - Inteligência Artificial", "CMCO05 - Introdução à Computação Visual","PERSISTÊNCIA  E ANÁLISE DE DADOS"],
  "XDES02 - Programação Orientada a Objetos": [
    "CMCO05 - Introdução à Computação Visual", "XDES04 - Programação Web",
    "CTCO03 - Análise e Projeto Orientados a Objetos",
    "METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"
  ],
  "CMAC03 - Algoritmos em Grafos": ["METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"],
  "XDES04 - Engenharia de Software": ["DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE"],
  "CTCO02 - Algoritmos e Estruturas de Dados II": ["CTCO04 - Projeto e Análise de Algoritmos"],
  "CRSC02 - Sistemas Operacionais": ["XRSC01 -Rede de Computadores"],

  # Quarto Semestre
  "CMAC05 - Cálculo Numérico para Computação": [],
  "XDES03 - Programação Web": [" XAMC02 - Interação Humano-Computador", "DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE"],
  "CTCO03 - Projeto e Análise de Algoritmos": ["CTCO05 - Teoria da Computação"],
  "CRSC05 - Sistemas Embarcados": [],
  "XRSC01 - Redes de Computadores": ["REDES E SISTEMAS COMPUTACIONAIS"],

  # Quinto Semestre
  "XMCO01 - Inteligência Artificial": ["METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"],
  "CMCO05 - Introdução à Computação Visual": ["METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO"],
  "CTCO03 - Análise e Projeto Orientado a Objetos": [],
  "CTCO05 - Teoria da Computação": [],
  "XPAD01 - Banco de Dados I": ["PERSISTÊNCIA  E ANÁLISE DE DADOS"],

  # Sexto Semestre
  "XAMC02 - Interação Humano-Computador": [],
  "CTCO06 - Compiladores": [],
  "XMAC01 - Computação e Sociedade": [],

  # Sétimo Semestre
  "XAMC03 - Metodologia Científica": ["TCC1"],
  "TCC1": ["TCC2"],

  # Oitavo Semestre
  "TCC2": [],

 
  #OPTATIVAS
  "ADMINISTRAÇÃO E GESTÃO":[],
  "METODOLOGIAS COMPUTACIONAIS E OTIMIZAÇÃO":[],
  "DESENVOLVIMENTO E ENGENHARIA DE SOFTWARE":[],
  "PERSISTÊNCIA  E ANÁLISE DE DADOS":[],
  "REDES E SISTEMAS COMPUTACIONAIS":[]
  
}


import networkx as nx
import matplotlib.pyplot as plt

def plotar_grafo(grafo):
    # Criar um objeto do tipo grafo direcionado
    G = nx.DiGraph()

    # Adicionar as arestas ao grafo
    for disciplina, adjacencias in grafo.items():
        G.add_edges_from([(disciplina, adj) for adj in adjacencias])

    plt.figure(figsize=(24, 12))

    # Calcular a posição dos nós no plano
    pos = nx.planar_layout(G)

    # Configurar estilo dos nós e arestas
    nx.draw_networkx(G,
                     pos,
                     with_labels=True,
                     node_color='lightblue',
                     edge_color='gray',
                     arrows=True,
                     font_size=5,
                     node_size=300,
                     width=0.5,
                     alpha=0.8)

    # Ajustar margens
    plt.margins(0.15, 0.15)
    plt.axis('off')

    # Exibir e salvar o grafo
    plt.title('Grafo Planar')
    plt.savefig('grafo_planar.png', dpi=300)
    plt.show()

# Plotar o grafo do curso de Sistemas de Informação (grafoSIN)
plotar_grafo(grafoSIN)

# Plotar o grafo do curso de Ciência da Computação (grafoCCO)
plotar_grafo(grafoCCO)



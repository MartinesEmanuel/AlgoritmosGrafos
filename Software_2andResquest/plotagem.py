import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import networkx as nx
from typing import List, Optional
from disciplinas import CURSO, OFERTA, Disciplina

NODE_SIZE = 150

def interrogarDisciplinasConcluidas(curso: CURSO) -> Optional[List[Disciplina]]:
    G = nx.DiGraph(curso.grafo).reverse()
    rG = nx.to_dict_of_dicts(G)
    reversed_graph = {}

    for node in rG:
        reversed_graph[node] = []
        for n in rG[node]:
            reversed_graph[node].append(n)
    
    pos = nx.planar_layout(G, scale=2)
    current_state = []
    node_names = {}
    node_indexes = []
    node_descriptions = {}
    i = 0
    for node in pos:
        node_indexes.append(node)
        node_names[node] = i
        i += 1
        current_state.append(0)
    current_state[0] = 1
    
    disciplinas = {}

    for disciplina in curso.disciplinas:
        disciplinas[disciplina.sigla] = disciplina
        oferta = "Desconhecido"
        if disciplina.oferta == OFERTA.PRIMEIRO_SEMESTRE:
            oferta = "Segundo semestre"
        else:
            oferta = "Primeiro semestre"
    
        node_descriptions[disciplina.sigla] = {
            "Nome": disciplina.nome,
            "Sigla": disciplina.sigla,
            "Oferta": oferta,
            "Optativa": "Sim" if disciplina.optativa else "Não"
        }

    node_descriptions['INICIO'] = {"Descrição": "Apenas uma forma de organizar as diciplinas sem requisitos"}

    nx.set_node_attributes(G, node_descriptions)

    
    fig, ax = plt.subplots()
    plt.title('Selecione as diciplinas já concluídas')

    color_map = []
    for i in current_state:
        color_map.append('red' if i == 0 else 'green')

    edges_plt = nx.draw_networkx_edges(G, pos=pos, ax=ax, node_size=NODE_SIZE, edge_color='lightgray')
    nodes_plt = nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=color_map, node_size=NODE_SIZE, )
    nx.draw_networkx_labels(G, pos=pos, ax=ax, font_weight="bold", font_size=8, font_color='black')
    
    annotate = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                            bbox=dict(boxstyle="round", fc="w"),
                            arrowprops=dict(arrowstyle="->"))
    annotate.set_visible(False)

    def on_hover(event):
        if event.inaxes != ax:
            return
        
        cont, index = nodes_plt.contains(event)
        if cont:
            node = node_indexes[index["ind"][0]]
            annotate.xy = pos[node]
            node_attribute = {}
            node_attribute.update(G.nodes[node])
            text = '\n'.join(f'{k}: {v}' for k, v in node_attribute.items())
            annotate.set_text(text)
            annotate.set_visible(True)
            fig.canvas.draw_idle()
            return
        
        if annotate.get_visible():
            annotate.set_visible(False)
            fig.canvas.draw_idle()


    def on_click(event):
        if event.inaxes == ax:
            nonlocal nodes_plt
            cont, ind = nodes_plt.contains(event)
            if cont:
                index = ind["ind"][0]
                node = node_indexes[index]
                if node == 'INICIO':
                    for i in range(1, len(current_state)):
                        current_state[i] = 0
                    
                    color_map = []
                    for i in current_state:
                        color_map.append('red' if i == 0 else 'green')

                    nodes_plt.remove()
                    nodes_plt = nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=color_map, node_size=NODE_SIZE)
                    fig.canvas.draw()
                    return
                current_state[index] = 1 if current_state[index] == 0 else 0
                
                if current_state[index] == 1:
                    # Selecionar todos os requisitos necessários
                    q = [node]
                    while len(q) != 0:
                        node = q.pop()
                        for n in curso.grafo[node]:
                            q.append(n)
                        index = node_names[node]
                        if current_state[index] == 0:
                            current_state[index] = 1
                else:
                    # Desselecionar todos para os quais este é um requisito
                    q = reversed_graph[node].copy()
                    while len(q) != 0:
                        node = q.pop()
                        index = node_names[node]
                        if current_state[index] == 0:
                            continue
                        
                        for n in reversed_graph[node]:
                            q.append(n)
                        
                        current_state[index] = 0
                
                
                color_map = []
                for i in current_state:
                    color_map.append('red' if i == 0 else 'green')

                nodes_plt.remove()
                nodes_plt = nx.draw_networkx_nodes(G, pos=pos, ax=ax, node_color=color_map, node_size=NODE_SIZE)
                fig.canvas.draw()
                

    fig.canvas.mpl_connect("button_press_event", on_click)
    fig.canvas.mpl_connect("motion_notify_event", on_hover)

    ok = False
    def on_click_ok(e):
        nonlocal ok
        ok = True
        plt.close()

    def on_click_cancel(e):
        plt.close()
    
    ok_button = Button(fig.add_axes([0.80, 0.03, 0.1, 0.075]), 'Ok')
    ok_button.on_clicked(on_click_ok)
    cancel_button = Button(fig.add_axes([0.68, 0.03, 0.1, 0.075]), 'Cancelar')
    cancel_button.on_clicked(on_click_cancel)

    plt.show()

    if not ok:
        return None

    disciplinas_concluidas = []
    for i in range(1, len(current_state)):
        if current_state[i] == 0:
            continue
        disc = disciplinas[node_indexes[i]]
        disciplinas_concluidas.append(disc)

    return disciplinas_concluidas

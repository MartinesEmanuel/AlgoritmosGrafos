
from enum import Enum
from typing import List, Optional
import operator

from disciplinas import CURSO, OFERTA, Disciplina
from plotagem import interrogarDisciplinasConcluidas

class UsuarioDecidiuSair(Exception):
    pass

def interrogarCurso() -> CURSO:
    print('-' * 30)
    print('Selecione o curso:')
    print('[1] CCO')
    print('[2] SIN')
    print('[3] Sair')
    print('-' * 30)
    
    try:
        opcao = int(input('Digite a opção: '))
        if opcao == 3:
            raise UsuarioDecidiuSair
        return CURSO(opcao)
    except ValueError:
        print('Opção inválida, digite novamente')
        return interrogarCurso()

def interrogarSemestre() -> int:
    print('-' * 30)
    print('Selecione o próximo semestre: ')
    print('[1] Primeiro semestre')
    print('[2] Segundo semestre')
    print('[3] Sair')
    print('-' * 30)

    try:
        opcao = int(input('Digite a opção: '))
        if opcao == 3:
            raise UsuarioDecidiuSair
        if opcao == 1 or opcao == 2:
            return opcao
        raise ValueError
    except ValueError:
        print('Opção inválida, digite novamente')
        return interrogarSemestre()

def encontrarDisciplinasPossiveis(curso: CURSO, semestre: OFERTA, disciplinas_concluidas: List[Disciplina]) -> List[Disciplina]:
    disciplinas_concluidas_sigla = []
    for disciplina in disciplinas_concluidas:
        disciplinas_concluidas_sigla.append(disciplina.sigla)

    disciplinas = []

    for disciplina in CURSO.CCO.disciplinas:
        if disciplina in disciplinas_concluidas:
            continue
        ok = True
        for requisito in disciplina.requisitosDiretos:
            if not requisito.sigla in disciplinas_concluidas_sigla:
                ok = False
                break
        if not ok:
            continue
        if disciplina.oferta == semestre:
            disciplinas.append(disciplina)
        elif disciplina.oferta == OFERTA.DESCONHECIDO:
            disciplinas.append(disciplina)
    
    for disciplina in CURSO.CCO.disciplinas_optativas:
        if disciplina in disciplinas_concluidas:
            continue
        ok = True
        for requisito in disciplina.requisitosDiretos:
            if not requisito.sigla in disciplinas_concluidas_sigla:
                ok = False
                break
        if not ok:
            continue
        if disciplina.oferta == semestre:
            disciplinas.append(disciplina)
        elif disciplina.oferta == OFERTA.DESCONHECIDO:
            disciplinas.append(disciplina)
    return disciplinas

def listarDisciplinasMaisApropriadas():
    curso = interrogarCurso()
    semestre = OFERTA.PRIMEIRO_SEMESTRE if interrogarSemestre() == 1 else OFERTA.SEGUNDO_SEMESTRE
    disciplinas_concluidas = interrogarDisciplinasConcluidas(curso)
    if disciplinas_concluidas == None:
        print('Operação cancelada')
        return
    selecionadas_texto = ', '.join([x.sigla for x in disciplinas_concluidas])
    print('-' * 30)
    print('Disciplinas selecionadas: ' + selecionadas_texto)

    disciplinas_possiveis = encontrarDisciplinasPossiveis(curso, semestre, disciplinas_concluidas)
    recomendadas_semestre_atual = ', '.join([x.sigla for x in disciplinas_possiveis if x.oferta == semestre and not(x.optativa)])
    recomendadas_semestre_desconhecido = ', '.join([x.sigla for x in disciplinas_possiveis if x.oferta == OFERTA.DESCONHECIDO and not(x.optativa)])
    recomendadas_semestre_atual_opt = ', '.join([x.sigla for x in disciplinas_possiveis if x.oferta == semestre and x.optativa])
    recomendadas_semestre_desconhecido_opt = ', '.join([x.sigla for x in disciplinas_possiveis if x.oferta == OFERTA.DESCONHECIDO and x.optativa])
    
    print('-' * 30)
    print('Disciplinas mais apropriadas:')
    print('Fixas do semestre atual: ' + recomendadas_semestre_atual)
    print('Fixas de semestre desconhecido: ' + recomendadas_semestre_desconhecido)
    print('Optativas do semestre atual: ' + recomendadas_semestre_atual_opt)
    print('Optativas de semestre desconhecido: ' + recomendadas_semestre_desconhecido_opt)
    print('-' * 30)
    

def analisarFragilidade():
    curso = interrogarCurso()
    
    disciplinasCriticas = {}

    for disciplina in curso.disciplinas:
        for requisito in disciplina.requisitosDiretos:
            if not requisito.sigla in disciplinasCriticas:
                disciplinasCriticas[requisito.sigla] = [disciplina.sigla]
            else:
                disciplinasCriticas[requisito.sigla].append(disciplina.sigla)

    disciplinasCriticas = sorted(disciplinasCriticas.items(), key=lambda x:len(x[1]), reverse=True)
    print('-' * 30)
    print('Disciplinas mais críticas:')
    for x in disciplinasCriticas:
        print(f"{x[0]}: É requisito direto de ({len(x[1])}): {', '.join(x[1])}")
    print('-' * 30)
    
def main():
    print('-' * 30)
    print('Selecione a operação:')
    print('[1] Listar disciplinas mais apropriadas para se matricular')
    print('[2] Mostrar análise da fragilidade da grade')
    print('[3] Sair')
    print('-' * 30)

    try:
        opcao = int(input('Digite a opção: '))
        if opcao == 3:
            raise UsuarioDecidiuSair
        
        if opcao == 1:
            listarDisciplinasMaisApropriadas()
        elif opcao == 2:
            analisarFragilidade()

        input('Pressione Enter para continuar.')
    except UsuarioDecidiuSair:
        return
    except ValueError:
        print('Opção inválida, digite novamente')
    
    main()

if __name__ == '__main__':
    main()
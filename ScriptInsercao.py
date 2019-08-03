# -*- coding: utf-8 -*-
import pandas

planilha = pandas.read_csv('PlanilhaAlunos.csv', sep=',')

#put 'emp','1','personal data:name','raju'
#create 'Alunos', 'DadosPessoais', 'DadosMaterias'

for i in range(0, 300):
    print('put \'Alunos\',', i, ',' #('\'' + str(i) + '\','),
          '\'DadosPessoais:Nome\',', ('\'' + planilha.values[i][1] + '\''))
    print('put \'Alunos\',', i, ',' #('\'' + str(i) + '\','),
          '\'DadosPessoais:Sexo\',', ('\'' + planilha.values[i][2] + '\''))
    print('put \'Alunos\',', i, ',' #('\'' + str(i) + '\','),
          '\'DadosPessoais:Turno\',', ('\'' + planilha.values[i][3] + '\''))
    print('put \'Alunos\',', i, ',' #('\'' + str(i) + '\','),
          '\'DadosPessoais:Idade\',', ('\'' + str(planilha.values[i][4]) + '\''))
    print('put \'Alunos\',', i, ',' #('\'' + str(i) + '\','),
          '\'DadosPessoais:Endereco\',', ('\'' + planilha.values[i][5] + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosPessoais:Telefone\',', ('\'' + str(planilha.values[i][6]) + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosMaterias:CUV\',', ('\'' + str(planilha.values[i][7]) + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosMaterias:LP\',', ('\'' + str(planilha.values[i][8]) + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosMaterias:FBM\',', ('\'' + str(planilha.values[i][9]) + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosMaterias:QG\',', ('\'' + str(planilha.values[i][10]) + '\''))
    print('put \'Alunos\',', i, ','#('\'' + str(i) + '\','), 
          '\'DadosMaterias:CTS\',', ('\'' + str(planilha.values[i][11]) + '\''))


Last login: Tue Mar 24 14: 23: 30 on ttys001

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh - s / bin/zsh`.
For more details, please visit https: // support.apple.com/kb/HT208050.
iMac-de-Rogerio: ~ rogermac$ ptpython
>> > if 1 == 1:
... print('Brasil')
Brasil

>> > 1 > 1
False


>> > 1 > 1 or 2 == 2
True


>> > bool(True)
True


>> > bool(1 == 1)
True


>> > bool(1)
True


>> > bool(0)
False


>> > bool('Rogerio')
True


>> > bool('')
False


>> > bool(-1)
True


>> > bool(0)
False


>> > bool(1)
True


>> > if 'Rogerio' and 0:
... print('O rato roeu a roupa do rei de roma')

>> > nomes = [1, 2, 3]

>> > nomes
[1, 2, 3]


>> > len(nomes)
3


>> > if nomes:
... print('Tem numeros')
Tem numeros

>> > lista = []

>> > bool(lista)
False


>> >
>> > def soma(a, b):
... return a + b

>> > r = soma(6, 7)

>> > r
13


>> > diff = lambda x, y: x + y

>> > diff = lambda x, y: x - y

>> > r = diff(8, 5)

>> > r
3


>> > def do_twice(funcao, x, y):
... print(funcao(x, y))
... print(funcao(x, y))

>> > do_twice(soma, 5, 6)
11
11

>> > do_twice(diff, 5, 6)
-1
-1

>> > do_twice(lambda x, y: x*y, 5, 6)
30
30

>> > do_twice(soma(5, 6), 5, 6)
Traceback(most recent call last):
    File "<stdin>", line 1, in < module >
    File "<stdin>", line 2, in do_twice
TypeError: 'int' object is not callable

'int' object is not callable

>> >
>> >
>> > def somar(*valores):
... print(len(valores))

>> > somar(1)
1

>> > somar(1, 2)
2

>> > somar(1, 2, 4)
3

>> > def somar(*valores):
...     soma = 0
... for v in valores:
...         soma = soma + v
... return soma

>> > r = somar(1)

>> > r
1


>> > r = somar(1, 4, 5, 6, 777)

>> > r
793

>> >
>> >
>> > import time

>> > now = time.time()

>> > now
1585422191.409896


>> > inicio = time.time()

>> > for i in range(10):
...     time.sleep(0.7)
... print('.')
.
.
.
.
.
.
.
.
.
.

>> > fim = time.time()

>> > intervalo = fim - inicio

>> > intervalo
50.284631967544556


>> > help(time.time)


>> > import time

>> > time.time()
1585422316.179923


>> > time.time()
1585422321.2598379


>> > __name__
'__main__'


>> > time.__name__
'time'

>> > __name__
'__main__'


>> > import time

>> > time.__name__
'time'


>> > quit()
iMac-de-Rogerio: ~ rogermac$


iMac-de-Rogerio: ~ rogermac$ cd Desktop/
iMac-de-Rogerio: Desktop rogermac$ ls
Banner Ana Vitória.png
Captura de Tela 2020-03-24 às 14.02.37.png
Captura de Tela 2020-03-24 às 14.03.03.png
Captura de Tela 2020-03-24 às 14.42.47.png
Captura de Tela 2020-03-24 às 14.59.51.png
Captura de Tela 2020-03-28 às 13.44.55.png
Como-Aprendemos-Tabela-William-Glasser.jpg
Configuracao IT.png
Contrato - Aluguel - Village.rtf
Eleicoes
Erick-Silva-Plaquinha-RecemNascido.png
Exames-Lab-Dez2018.pdf
Exames_Laboratoriais_14Nov2019.pdf
Flatiron_SE_OnCampus_Syllabus_2_11_19.pdf
Flatiron_SE_Online_Syllabus_2_20_2019.pdf
Fotos_Niver_Ana_Vitoria
Guia-de-Declaração-IRPF-2020-Ações-FIIs - \
    Stocks-REITs-e-ETFs-Canal-do-Holder.pdf
IR Açoes 2020.xlsx
LE WAGON - part_time_syllabus_opti.pdf
Livros-2019-Lerote
NFC-E Moto G6 .pdf
NFC-e - Celular Mamae Extra Nov2018.pdf
Nomeacao-Francineide.pdf
Pensamento Computacional.pdf
Portaria_Coordenacao_TDS_Ago2019.pdf
RG-CPF-Francinete-Rosa-Da-Silva.pdf
Referenciais de Formacao para Cursos de Graduacao em Computacao - Outubro 2017.pdf
Regimento Interno - Bosque Leste.pdf
SBC_Revista_CompBrasil_41_Comp_Educ.Basica.pdf
Seu Proposito.png
Simulator Screen Shot - iPhone 11 Pro Max - 2020-02-10 at 22.15.23.png
Simulator Screen Shot - iPhone 11 Pro Max - 2020-02-10 at 22.21.20.png
Simulator Screen Shot - iPhone 11 Pro Max - 2020-02-11 at 20.42.54.png
Simulator Screen Shot - iPhone Xʀ - 2020-02-09 at 21.41.09.png
Software Laboratórios 2020.pdf
Vagas_Estagio.png
algoritmo.jpeg
jack-ma-never-be-jobless-again.jpeg
pensamento_computacional
percentual-de-gordura-em-homens.jpg
percentual-de-gordura-em-mulheres.jpg
postman
potencia.py
somario_python.png
sono.png
teste2.py
work with people.jpg
~$TDS_20191.xlsx
iMac-de-Rogerio: Desktop rogermac$ cd pensamento_computacional/
iMac-de-Rogerio: pensamento_computacional rogermac$
iMac-de-Rogerio: pensamento_computacional rogermac$
iMac-de-Rogerio: pensamento_computacional rogermac$ ls
__pycache__			f2b_q16_tabajaras.py
alinhar_direita.py		ferramentas.py
delta.py			ir_progressivo.py
f1_p1_q11_inverso.py		projeto_turtle.py
f1_p2_q15_soma_fracao.py	soma_sequencia.py
f1_p2_q22_cedulas.py		velocidade.py
f1_q1_velocidade.py		verificar_faixa.py
f2a_q17_crazy.py
iMac-de-Rogerio: pensamento_computacional rogermac$ ptpython
>> > import ir_progressivo
Renda: 3000
R$ 95.20

>> > ir_progressivo.calcular_ir(15000)
3255.637


>> > ir_progressivo.main()
Renda: 7000
R$ 1055.64

>> > ir_progressivo.__name__
'ir_progressivo'


>> > quit()
iMac-de-Rogerio: pensamento_computacional rogermac$


iMac-de-Rogerio: pensamento_computacional rogermac$ ptpython
>> > import ir_progressivo

>> > ir_progressivo.main()
Renda: 7000
R$ 1055.64

>> > quit()
iMac-de-Rogerio: pensamento_computacional rogermac$ python ir_progressivo.py
File "ir_progressivo.py", line 7
print(f'R$ {imposto:.2f}')
^
SyntaxError: invalid syntax
iMac-de-Rogerio: pensamento_computacional rogermac$

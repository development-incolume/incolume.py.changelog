EXAMPLES
==========

Atualizações disponíveis em:
https://brito.blog.incolume.com.br/search/label/development-incolume

Example incolumpy.utils.fake_cpf
--
c1 = gen_fake_cpf()
print([next(c1) for x in range(5)])
# ['773.552.588-66', '959.954.188-10', '238.604.439-34', '382.437.455-81', '870.384.823-36']

c2 = gen_fake_cpf(False)
print([next(c2) for x in range(5)])
# ['79513660721', '06283805873', '91521854282', '09569983076', '99565733840']

Example incolumepy.utils.files.ll
--
from incolumepy.utils.files import ll
ll('/tmp') or ll('/tmp', True) or ll('/tmp', string=True)
# ['/tmp/ased']

ll('/tmp', False) or ll('/tmp', string=False)
# [('/tmp','ased')]

Example incolumepy.utils.files.realfilename
--
from incolumepy.utils.files import realfilename

    with open(realfilename(
            os.path.join('tmp', 'britodfbr','diretorio', 'para', 'teste'),
            ext='.dat', separador=True), 'w') as file:
        file.write('teste ok')

    #tmp/britodfbr/diretorio/para/teste.dat
    #tmp/britodfbr/diretorio/para/teste_01.dat

    with open(realfilename(
            os.path.join('tmp', 'diretorio', 'para', 'teste'),
            separador=True, ext='md'),'w') as file:
        file.write('teste ok')
    # tmp/diretorio/para/teste.md
    # tmp/diretorio/para/teste_01.md

    with open(realfilename(('tmp/teste/test.json'),
            separador=True, ext='bash'),'w') as file:
        file.write('teste ok')
    # tmp/teste/test.bash
    # tmp/teste/test_01.bash

    with open(realfilename(('tmp/teste/lll'),
            separador=True),'w') as file:
        file.write('teste ok')

    # tmp/teste/lll.txt
    # tmp/teste/lll_01.txt

    with open(realfilename(('tmp/teste/jjj.json'),
            separador=True),'w') as file:
        file.write('teste ok')

    # tmp/teste/jjj.json
    # tmp/teste/jjj_01.json


    with open(realfilename('../utils/tmp/registro.xml'), 'w') as file:
        file.write(file.name)

Example incolumepy.utils.sequencia.Sequencia
--
from incolumepy.utils.sequencia import Sequencia
a = Sequencia.Primos()
for i in range(10):
    print(next(a))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

a = Sequencia.Fibonacci()
for i in range(10):
    print(next(a))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

a = Sequencia.Impares()
for i in range(10):
    print(next(a))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

a = Sequencia.Pares()
for i in range(10):
    print(next(a))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

a = Sequencia.Naturais()
for i in range(10):
    print(next(a))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



Example incolumepy.utils.utils.namespace
--
from incolumepy.utils.utils import namespace

namespace('incolumepy.package.subpackage')
# ['incolumepy', 'incolumepy.package']

namespace('incolumepy.package.subpackage.module')
# ['incolumepy','incolumepy.package','incolumepy.package.subpackage']


Example incolumepy.utils.utils.read
--
from incolumepy.utils.utils import read
read('version.txt')
# 0.7.2

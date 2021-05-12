import os
import sys

"""Esta append no path é um pequeno workaround para o problema de import
de um caminho relativo no modulo de invoke do serverless.

A issue encontra-se em aberto e existem diversas outras saídas.

https://github.com/UnitedIncome/serverless-python-requirements/issues/520

"""

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
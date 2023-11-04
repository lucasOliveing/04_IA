import sys
sys.path.append('../')

from operacoes import *

def test_inital_1():
    test = {'A': (0.0,0.0),
            'B': (1.0,2.0),
            'C': (2.0,0.0),
            'D': (0.0,2.0),
            'E': (1.0,1.0),
            'F': (1.0,3.0),
            'G': (3.0,2.0)
            }
    test_1 = {
        'A': (3.0,0.1),
        'B': (5.0,4.6),
        'C': (1.2,7.3),
        'D': (2.7,4.2)
    }

    assert test == initial_1()
    assert test_1 == initial_1('teste_cordenadas.txt')
    assert "File not found" == initial_1('dontExist.txt') 

def test_calcCust():
    a_b = 2.23606797749979
    b_c = 2.23606797749979
    c_d = 2.82842712474619
    d_e = 1.414213562373095
    e_f = 2
    f_g = 2.23606797749979
    g_a = 3.605551275463989

    total = a_b + b_c + c_d + d_e + e_f + f_g + g_a
    assert round(total,5) == round(calcCust(initial_1()),5)
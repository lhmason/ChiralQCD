# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Wed 15 May 2019 14:03:14


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.Ka0__tilde__, P.Ka0__tilde__, P.Ka0, P.Ka0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_2})

V_2 = Vertex(name = 'V_2',
             particles = [ P.Ka0__tilde__, P.Ka0, P.Kap__tilde__, P.Kap ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_3})

V_3 = Vertex(name = 'V_3',
             particles = [ P.Kap__tilde__, P.Kap__tilde__, P.Kap, P.Kap ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_7})

V_4 = Vertex(name = 'V_4',
             particles = [ P.Ka0__tilde__, P.Ka0, P.pi0, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1})

V_5 = Vertex(name = 'V_5',
             particles = [ P.Kap__tilde__, P.Kap, P.pi0, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_4})

V_6 = Vertex(name = 'V_6',
             particles = [ P.pi0, P.pi0, P.pi0, P.pi0 ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_9})

V_7 = Vertex(name = 'V_7',
             particles = [ P.Ka0, P.Kap__tilde__, P.pi0, P.pim ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_11})

V_8 = Vertex(name = 'V_8',
             particles = [ P.Ka0__tilde__, P.Kap, P.pi0, P.pip ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_12})

V_9 = Vertex(name = 'V_9',
             particles = [ P.Ka0__tilde__, P.Ka0, P.pim, P.pip ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_8})

V_10 = Vertex(name = 'V_10',
              particles = [ P.Kap__tilde__, P.Kap, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_6})

V_11 = Vertex(name = 'V_11',
              particles = [ P.pi0, P.pi0, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_5})

V_12 = Vertex(name = 'V_12',
              particles = [ P.pim, P.pim, P.pip, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_10})

V_13 = Vertex(name = 'V_13',
              particles = [ P.eta, P.Ka0__tilde__, P.Ka0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_13})

V_14 = Vertex(name = 'V_14',
              particles = [ P.eta, P.Kap__tilde__, P.Kap, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_14})

V_15 = Vertex(name = 'V_15',
              particles = [ P.eta, P.pi0, P.pi0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_16})

V_16 = Vertex(name = 'V_16',
              particles = [ P.eta, P.Ka0, P.Kap__tilde__, P.pim ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_17})

V_17 = Vertex(name = 'V_17',
              particles = [ P.eta, P.Ka0__tilde__, P.Kap, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_18})

V_18 = Vertex(name = 'V_18',
              particles = [ P.eta, P.pi0, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_15})

V_19 = Vertex(name = 'V_19',
              particles = [ P.eta, P.eta, P.Ka0__tilde__, P.Ka0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_19})

V_20 = Vertex(name = 'V_20',
              particles = [ P.eta, P.eta, P.Kap__tilde__, P.Kap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_20})

V_21 = Vertex(name = 'V_21',
              particles = [ P.eta, P.eta, P.pi0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_21})

V_22 = Vertex(name = 'V_22',
              particles = [ P.eta, P.eta, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_22})

V_23 = Vertex(name = 'V_23',
              particles = [ P.eta, P.eta, P.eta, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_23})

V_24 = Vertex(name = 'V_24',
              particles = [ P.eta, P.eta, P.eta, P.eta ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_24})

V_25 = Vertex(name = 'V_25',
              particles = [ P.etap, P.Ka0__tilde__, P.Ka0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_25})

V_26 = Vertex(name = 'V_26',
              particles = [ P.etap, P.Kap__tilde__, P.Kap, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_26})

V_27 = Vertex(name = 'V_27',
              particles = [ P.etap, P.pi0, P.pi0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_28})

V_28 = Vertex(name = 'V_28',
              particles = [ P.etap, P.Ka0, P.Kap__tilde__, P.pim ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_29})

V_29 = Vertex(name = 'V_29',
              particles = [ P.etap, P.Ka0__tilde__, P.Kap, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_30})

V_30 = Vertex(name = 'V_30',
              particles = [ P.etap, P.pi0, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_27})

V_31 = Vertex(name = 'V_31',
              particles = [ P.eta, P.etap, P.Ka0__tilde__, P.Ka0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_31})

V_32 = Vertex(name = 'V_32',
              particles = [ P.eta, P.etap, P.Kap__tilde__, P.Kap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_32})

V_33 = Vertex(name = 'V_33',
              particles = [ P.eta, P.etap, P.pi0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_33})

V_34 = Vertex(name = 'V_34',
              particles = [ P.eta, P.etap, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_34})

V_35 = Vertex(name = 'V_35',
              particles = [ P.eta, P.eta, P.etap, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_35})

V_36 = Vertex(name = 'V_36',
              particles = [ P.eta, P.eta, P.eta, P.etap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_36})

V_37 = Vertex(name = 'V_37',
              particles = [ P.etap, P.etap, P.Ka0__tilde__, P.Ka0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_37})

V_38 = Vertex(name = 'V_38',
              particles = [ P.etap, P.etap, P.Kap__tilde__, P.Kap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_38})

V_39 = Vertex(name = 'V_39',
              particles = [ P.etap, P.etap, P.pi0, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_39})

V_40 = Vertex(name = 'V_40',
              particles = [ P.etap, P.etap, P.pim, P.pip ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_40})

V_41 = Vertex(name = 'V_41',
              particles = [ P.eta, P.etap, P.etap, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_41})

V_42 = Vertex(name = 'V_42',
              particles = [ P.eta, P.eta, P.etap, P.etap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_42})

V_43 = Vertex(name = 'V_43',
              particles = [ P.etap, P.etap, P.etap, P.pi0 ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_43})

V_44 = Vertex(name = 'V_44',
              particles = [ P.eta, P.etap, P.etap, P.etap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_44})

V_45 = Vertex(name = 'V_45',
              particles = [ P.etap, P.etap, P.etap, P.etap ],
              color = [ '1' ],
              lorentz = [ L.SSSS1 ],
              couplings = {(0,0):C.GC_45})


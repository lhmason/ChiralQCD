# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Fri 17 May 2019 08:21:15



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
fp = Parameter(name = 'fp',
               nature = 'external',
               type = 'real',
               value = 0.14,
               texname = '\\text{fp}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

Md = Parameter(name = 'Md',
               nature = 'external',
               type = 'real',
               value = 0.008,
               texname = 'm_d',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

Ms = Parameter(name = 'Ms',
               nature = 'external',
               type = 'real',
               value = 0.125,
               texname = 'm_s',
               lhablock = 'FRBlock',
               lhacode = [ 3 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 80.379,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Mpi = Parameter(name = 'Mpi',
                nature = 'external',
                type = 'real',
                value = 0.14,
                texname = '\\text{Mpi}',
                lhablock = 'MASS',
                lhacode = [ 211 ])

Mpi0 = Parameter(name = 'Mpi0',
                 nature = 'external',
                 type = 'real',
                 value = 0.135,
                 texname = '\\text{Mpi0}',
                 lhablock = 'MASS',
                 lhacode = [ 111 ])

MKa0 = Parameter(name = 'MKa0',
                 nature = 'external',
                 type = 'real',
                 value = 0.498,
                 texname = '\\text{MKa0}',
                 lhablock = 'MASS',
                 lhacode = [ 311 ])

MKap = Parameter(name = 'MKap',
                 nature = 'external',
                 type = 'real',
                 value = 0.494,
                 texname = '\\text{MKap}',
                 lhablock = 'MASS',
                 lhacode = [ 321 ])

Meta = Parameter(name = 'Meta',
                 nature = 'external',
                 type = 'real',
                 value = 0.547,
                 texname = '\\text{Meta}',
                 lhablock = 'MASS',
                 lhacode = [ 221 ])

Metap = Parameter(name = 'Metap',
                  nature = 'external',
                  type = 'real',
                  value = 0.958,
                  texname = '\\text{Metap}',
                  lhablock = 'MASS',
                  lhacode = [ 331 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

Mup = Parameter(name = 'Mup',
                nature = 'internal',
                type = 'real',
                value = '0.004',
                texname = 'm_u')

Th = Parameter(name = 'Th',
               nature = 'internal',
               type = 'real',
               value = '-0.4712',
               texname = '\\theta')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')


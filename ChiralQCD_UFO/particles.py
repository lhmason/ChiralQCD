# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Mac OS X x86 (64-bit) (March 7, 2018)
# Date: Thu 30 May 2019 15:03:40


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0)

Z = Particle(pdg_code = 23,
             name = 'Z',
             antiname = 'Z',
             spin = 3,
             color = 1,
             mass = Param.MZ,
             width = Param.WZ,
             texname = 'Z',
             antitexname = 'Z',
             charge = 0)

W__plus__ = Particle(pdg_code = 24,
                     name = 'W+',
                     antiname = 'W-',
                     spin = 3,
                     color = 1,
                     mass = Param.MW,
                     width = Param.WW,
                     texname = 'W+',
                     antitexname = 'W-',
                     charge = 1)

W__minus__ = W__plus__.anti()

g = Particle(pdg_code = 21,
             name = 'g',
             antiname = 'g',
             spin = 3,
             color = 8,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'g',
             antitexname = 'g',
             charge = 0)

pip = Particle(pdg_code = 211,
               name = 'pip',
               antiname = 'pip~',
               spin = 1,
               color = 1,
               mass = Param.Mpip,
               width = Param.ZERO,
               texname = 'pip',
               antitexname = 'pip~',
               charge = 0)

pip__tilde__ = pip.anti()

pim = Particle(pdg_code = -211,
               name = 'pim',
               antiname = 'pim~',
               spin = 1,
               color = 1,
               mass = Param.Mpim,
               width = Param.ZERO,
               texname = 'pim',
               antitexname = 'pim~',
               charge = 0)

pim__tilde__ = pim.anti()

pi0 = Particle(pdg_code = 111,
               name = 'pi0',
               antiname = 'pi0~',
               spin = 1,
               color = 1,
               mass = Param.Mpi0,
               width = Param.ZERO,
               texname = 'pi0',
               antitexname = 'pi0~',
               charge = 0)

pi0__tilde__ = pi0.anti()

Ka0 = Particle(pdg_code = 311,
               name = 'Ka0',
               antiname = 'Ka0~',
               spin = 1,
               color = 1,
               mass = Param.MKa0,
               width = Param.ZERO,
               texname = 'Ka0',
               antitexname = 'Ka0~',
               charge = 0)

Ka0__tilde__ = Ka0.anti()

Kap = Particle(pdg_code = 321,
               name = 'Kap',
               antiname = 'Kap~',
               spin = 1,
               color = 1,
               mass = Param.MKap,
               width = Param.ZERO,
               texname = 'Kap',
               antitexname = 'Kap~',
               charge = 0)

Kap__tilde__ = Kap.anti()

eta = Particle(pdg_code = 221,
               name = 'eta',
               antiname = 'eta',
               spin = 1,
               color = 1,
               mass = Param.Meta,
               width = Param.ZERO,
               texname = 'eta',
               antitexname = 'eta',
               charge = 0)

etap = Particle(pdg_code = 331,
                name = 'etap',
                antiname = 'etap',
                spin = 1,
                color = 1,
                mass = Param.Metap,
                width = Param.ZERO,
                texname = 'etap',
                antitexname = 'etap',
                charge = 0)


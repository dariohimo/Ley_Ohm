#!/usr/bin/env python
# -*- coding: utf-8 -*-

      
def voltios(I, R):
    """calculo voltaje = A ("I", Amperios) * R(Ohmios);  V = I * R """
    V = I * R
    return V
    
def amperios(V, R):
    """calculo Amperios(I ó A)  = Voltaje(V) / R(Ohmios_Resistencia);  I = V/R """
    I = V / R
    return I

def resistencia(V, I):
    """Resistencia(Ohmios) = Voltios / Amperios(I ó A); R = V / I """ 
    R = V / I
    return R

if __name__ == "__main__":
    voltios()
    amperios()
    resistencia()

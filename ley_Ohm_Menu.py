#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Ley_Ohm_Formulas import *

""" la ley de Ohm, calculo de voltaje, Amperaje y Resistencia; (V = I * R) """

while True:
    print(f"\n#################################################")
    print(f"\tDigite los valores, si no cuenta con valores digite 0 donde correponda")
    print(f"#################################################\n")
    
    Voltios = float(input("voltios (V) : "))
    Amperios = float(input("amperios (I) : "))
    Resistencia = float(input("resistencia (R) Ohm) : "))

    if Voltios == 0:
        print(f"\nResultado: \n\n I={Amperios} * R={Resistencia} son: {voltios(Amperios, Resistencia)} Voltios(V)")
    elif Amperios == 0:
        print(f"\nResultado: \n\n V={Voltios} / R={Resistencia} son: {amperios(Voltios, Resistencia)} Amperios(I)")
    elif Resistencia == 0:
        print(f"\nResultado: \n\n V={Voltios} / I={Amperios} son: {resistencia(Voltios, Amperios)} Ohmios(R)")   
        
        
if __name__ == "__main__":
    voltios()
    amperios()
    resistencia()


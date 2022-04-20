# n'oubliez d'installer les différents packages pour le bon fonctionnement du code.
from sympy import Matrix
import numpy as np
import numpy.matlib
import pandas as pd
from pandas import DataFrame
from fractions import Fraction

								    #################################
							            #         Modèle 1              #
								    #################################

#Fonction de probabilité
########################							
def q(i):
	p=[0,0,1,2,3,4,5,6,5,4,3,2,1]
	if i<0 and 0<=i+40<=12:
		return Fraction(p[i+40],36)
	elif 0<=i<=12:
		return Fraction(p[i],36)
	return Fraction(0,1)

# Fonction de transition vers une case spéciale (chance ou commune) ou une case non-spéciale
############################################################################################
def pd(i,j,proba):
	S=[x for x in range(40)]
	if i in S and i!=30:
		if j==42:
			return proba(30-i) #i->10 ou i->(30)->10
		if j in [2,17,33]:
			return proba(j-i)*Fraction(12,16) # transition vers caisse commune
		if j in [7,22,36]:
			return proba(j-i)*Fraction(9,16)  # transition vers carte chance
		if j not in [30,40,41]:
			return proba(j-i)
	return Fraction(0,1)                         # concerne le cas où i==30

# Fonction transition d'un état à un autre via la caisse commune
################################################################
def pcc(i,j,proba):
	S=[x for x in range(40)]
	if i in S and i!=30:
		if j in [0,1,42]:
			return (proba(2-i)+proba(17-i)+proba(33-i))*Fraction(1,16)
		if j==5:
			return proba(2-i)*Fraction(1,16)
		if j==25:
			return proba(17-i)*Fraction(1,16)
		if j==35:
			return proba(33-i)*Fraction(1,16)
	return Fraction(0,1)

# Fonction transition d'un état à un autre via une carte chance
###############################################################
def pch(i,j,proba):
	S=[x for x in range(40)]
	if i in S and i!=30:
		if j in [0,42,11,15,24,39]:
			return (proba(7-i)+proba(22-i)+proba(36-i))*Fraction(1,16)
		if j==4:
			return proba(7-i)*Fraction(1,16)
		if j==19:
			return proba(22-i)*Fraction(1,16)
		if j==33:
			return proba(36-i)*Fraction(1,16)
	return Fraction(0,1)

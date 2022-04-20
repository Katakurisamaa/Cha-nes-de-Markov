from Modele2 import*

								    #################################
							        #          Modèle 3             #
							        # Introduction des prisons vir- #
							        #            tuelles            #
								    #################################
							        
							        
# Sortir de prison : soit en payant l'amende (a), soit en faisant un double
###########################################################################

# Fonction de transition de la prison vers une case quelconque sans passer par une case spéciale
################################################################################################
def jail_pd(i,j,proba,a):
	p=Fraction(0,1)
	if i==40:
		if j in [12,13,14,15,16,18,19,20,21]:
			p=proba(j-10)
		elif j==17:
			p=proba(7)*Fraction(12,16)
		elif j==22:
			p=proba(12)*Fraction(9,16) # proba(12)=1/36
	if i in [41,42]:
		if j in [12,14,16,18,20]:
			p=Fraction(1-a,36) + Fraction(a,1)*proba(j-10)
		if j==22:
			p=Fraction(a,1)*proba(12)*Fraction(9,16)+Fraction((1-a),36)*Fraction(9,16) #
		if j in [13,15,19,21]:
			p=Fraction(a,1)*proba(j-10)
		if j==17:
			p=Fraction(a,1)*proba(j-10)*Fraction(12,16)
		if i==42 and j==41:
			p=Fraction((1-a),1)*Fraction(5,6)
		if i==41 and j==40:
			p=Fraction((1-a),1)*Fraction(5,6)
	return p

# Fonction de transition de la prison vers une case via la caisse commune
##########################################################################
def jail_cc(i,j,proba,a):
	p=Fraction(0,1)
	if j in [0,42,1,25]:
		if i==40:
			p=proba(17-10)*Fraction(1,16)
		if i in [41,42]:
			p=Fraction(a,1)*proba(17-10)*Fraction(1,16)
	return p

# Fonction de transition de la prison vers une case via une carte chance
#########################################################################
def jail_ch(i,j,proba,a):
	p=Fraction(0,1)
	if j in [0,42,15,11,24,39,19]:
		if i==40:
			p=proba(12)*Fraction(1,16)
		if i in [41,42]:
			p=Fraction(a,1)*proba(12)*Fraction(1,16) + Fraction((1-a),16*36)
	return p
			
def modele3(proba,a):
	monopole=np.zeros([43,43], dtype=Fraction)
	for i in [40,41,42]:
		for j in range(43):
			monopole[i][j]=jail_pd(i,j,proba,a)+jail_cc(i,j,proba,a)+jail_ch(i,j,proba,a)
	return monopole			

def monopoly(proba,a):
	return modele2(proba)+modele3(proba,a)							        
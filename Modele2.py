from Modele1 import*

								    #################################
							        #         Modèle 2              #
								    #################################
							        
# modification de la carte chance
def pch_mod(i,j,proba):
	S=[x for x in range(40)]
	p=pch(i,j,proba)
	if i in S and i!=30:
		if j in [0,1,42,35]:
			p=pch(i,j,proba)+proba(36-i)*Fraction(1,1256)
		if j==33:
			p=pch(i,j,proba)-proba(36-i)*Fraction(4,1256)
	return p

def modele2(proba):
	monopole=np.zeros([43,43],dtype=Fraction)
	for i in range(43):
		for j in range(43):
			monopole[i][j]=pd(i,j,proba)+pcc(i,j,proba)+pch_mod(i,j,proba)
	return monopole
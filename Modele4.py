from Modele3 import*

								    #################################
							            #          Modèle 4             #
							            # Introduction de la règle des  #
							            #   3 doubles consécutifs       #
								    #################################
							        
# Cette fonction modifie les probabilités pour les valeurs paires
##################################################################
def q_2(i):
	p=q(i)
	if q(i) in [q(2),q(4),q(6),q(8),q(10),q(12)]:
		p=q(i)-Fraction(1,1296)
	return p

def pd_double(i,j,proba):
	p=pd(i,j,proba)
	if j==42 and i not in [40,41,30,42]:
		return p+Fraction(1,216)
	return p

def P(q_2):
	monopole=np.zeros([43,43],dtype=Fraction)
	for i in range(43):
		for j in range(43):
			monopole[i][j]=pd_double(i,j,q_2)+pcc(i,j,q_2)+pch_mod(i,j,q_2)
	return monopole

def modele4(proba,a):
	return P(q_2)+modele3(proba,a)

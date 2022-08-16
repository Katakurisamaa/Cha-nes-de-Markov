from Modele4 import*
import matplotlib.pyplot as plt
case=["DÉPART","BOULEVARD DE BELVILLE","CAISSE COMMUNAUTÉ","RUE LE COURBE",
	  "IMPÔT SUR LES REVENUS","GARE MONTPARNASSE","RUE DE VAUGIRARD","CHANCE",
	  "RUE DE COURCELLES","AVENUE DE LA REPUBLIQUE","PRISON EN SIMPLE VISITE",
	  "BOULEVARD DE LA VILLETTE","COMPAGNIE DE DISTRIBUTION D'ÉLECTRICITÉ",
	  "AVENUE DE NEUILLY","RUE DE PARADIS","GARE DE LYON","AVENUE MOZART","CAISSE DE COMMUNAUTÉ",
	  "BOULEVARD SAINT-MICHEL","PLACE PIGALLE","PARC GRATUIT","AVENUE MATIGNON","CHANCE",
	  "BOULEVARD MALSHERBES","AVENUE HENRI-MARTIN","GARE DU NORD","FAUBOURG SAINT-HONORÉ",
	  "PLACE DE LA BOURSE","COMPAGNIE DE DISTRIBUTION DES EAUX","RUE DE LA FAYETTE","AVENUE DE BRETEUIL",
	  "AVENUE FOCH","CAISSE COMMUNAUTÉ","BOULEVARD DES CAPUCINES","GARE SAINT-LAZARE","CHANCE",
	  "AVENUE DES CHAMPS-ÉLYSÉES","TAXE DE LUXE","RUE DE LA PAIX","PRISON","PRISON","PRISON"]


# Cette fonction calcul la somme de chaque ligne de la matrice de transition
def som(matrice):
	somme=[]
	indice=[]
	for i in range(len(matrice)):
		somme.append(sum(matrice[i]))
	return somme
# Prend en argument une matrice et le numéro de la colonne (et ligne) qu'on veut supprimer, puis renvoie un data frame.
def Q(matrice,col):
	monopole=DataFrame(data=matrice)
	monopole=monopole.drop(columns=col)
	monopole=monopole.drop(monopole.index[col])
	return monopole.values
# Prend en argument la matrice M et la renvoie sous forme d'un data frame.
def data(M):
	global case
	name=case[:len(M)]
	return DataFrame(data=M, columns=name)
# Cette fonction convertis la matrice en numpy.
def convert(matrice):
	return np.array(matrice).astype(np.float64)
# Cette fonction calcul la puissance n-iéme de la matrice
def puissance(matrix,n):
	return np.linalg.matrix_power(matrix,n)
## Si a==1 on supprime la case 40,41 qui ne seront jamais atteint
def afficher(P,a):
	if a==Fraction(1,1):
		return Q(P,[30,40,41])
	return Q(P,[30])

								    #################################
							            #       Test  Modèle 2          #
								    #################################
# Afficher la matrice de taille 42x42
#####################################

#print(data(convert(Q(P(q),[30]))))               # Affichage à virgule flottante
#print(data(Q(P(q),[30])))                        # Affichage sous forme de fraction

#Vérification si la somme de chacune des lignes vaut 1 sauf bien-sûr les cases 40,41,42
#######################################################################################

#print(Matrix(som(Q(modele2(q),[30]))))

								    #################################
							            #       Test  Modèle 3          #
								    #################################
# modifiez la valeur de a ici:
##############################

a=Fraction(1,1000)

# Affichage de la matrice
######################################

#print(data(afficher(monopoly(q,a),a)))                            # Affichage sous forme de fraction
#print(data(convert(afficher(monopoly(q,a),a))))                   # Affichage à virgule flottante

#Vérification si la somme de chacune des lignes vaut 1
########################################################

#print(Matrix(som(afficher(monopoly(q,a),a))))



								    #################################
							            #       Test  Modèle 4          #
								    #################################
# Modifiez la valeur de a ici:
################################

a=Fraction(999,1000)

# Afficher la matrice
######################################

#print(data(afficher(modele4(q,a),a)))                                # Affichage sous forme de fraction
#print(data(convert(afficher(modele4(q,a),a))))                       # Affichage à virgule flottante

#Vérification si la somme de chacune des lignes vaut 1
########################################################

#print(Matrix(som(afficher(modele4(q,a),a))))

# Calcul des puissances de la matrice (preuve de l'irréductibilité)
#####################################################################

#print(data(puissance(convert(afficher(modele4(q,a),a)),3)))

A=data(np.transpose(puissance(convert(afficher(modele4(q,a),a)),3)))
P=puissance(convert(afficher(modele4(q,a),a)),20)
alpha=np.zeros([1,len(P)])
alpha[0,0]=1
b=np.matmul(alpha,P)
A=DataFrame(data=np.transpose(b), columns=["proba"])
A["case"]=case
A=A.sort_values(by=["proba"], axis=0, ascending=False)

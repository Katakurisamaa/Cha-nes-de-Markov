from Test_final import*
import matplotlib.pyplot as plt
import dataframe_image as dfi
plt.rcParams.update({'figure.figsize':(7,5), 'figure.dpi':100})

#É
couleurs=["brown","skyblue","pink","orange","red","yellow","green","darkblue","black","white"]

dico_col={1:"brown",3:"brown",6:"skyblue",8:"skyblue",9:"skyblue",11:"pink",13:"pink",14:"pink",16:"orange",
	  18:"orange",19:"orange",21:"red",23:"red",24:"red",26:"yellow",27:"yellow",29:"yellow",31:"green",
	  32:"green",34:"green",37:"darkblue",39:"darkblue", 5:"black",15:"black",25:"black",35:"black",
	  12:"gray",28:"gray"} # couleur 'gray'=Compagnies....

dico_num={couleurs[0]:"1,3",couleurs[1]:"6,8,9",couleurs[2]:"11,13,14",
	  couleurs[3]:"16,18,19",couleurs[4]:"21,23,24",couleurs[5]:"26,27,29",
	 couleurs[6]:"31,32,34",couleurs[7]:"37,39",couleurs[8]:"5,15,25",
	  couleurs[9]:"12,28"}

marron=["BOULEVARD DE BELVILLE", "RUE LE COURBE"]
bleu_ciel=["RUE DE VAUGIRARD","RUE DE COURCELLES","AVENUE DE LA RÉPUBLIQUE"]
rose=["BOULEVARD DE LA VILLETTE","AVENUE DE NEUILLY","RUE DE PARADIS"]
orange=["AVENUE MOZART","BOULEVARD SAINT-MICHEL","PLACE PIGALLE"]
rouge=["AVENUE MATIGNON","BOULEVARD MALSHERBES","AVENUE HENRI-MARTIN"]
jaune=["FAUBOURG SAINT-HONORÉ","PLACE DE LA BOURSE","RUE DE LA FAYETTE"]
vert=["AVENUE DE BRETEUIL","AVENUE FOCH","BOULEVARD DES CAPUCINES"]
bleu=["AVENUE DES CHAMPS-ÉLYSÉES","RUE DE LA PAIX"]
Gare=["GARE MONTPARNASSE","GARE DE LYON","GARE DU NORD","GARE SAINT-LAZARE"]
compagnies=["COMPAGNIE DE DISTRIBUTION DES EAUX","COMPAGNIE DE DISTRIBUTION D'ÉLECTRICITÉ"]
Rue=marron+bleu_ciel+rose+orange+rouge+jaune+vert+bleu+Gare+compagnies
cases=Rue+Gare+["COMPAGNIE DE DISTRIBUTION DES EAUX","COMPAGNIE DE DISTRIBUTION D'ÉLECTRICITÉ"]
loyer={marron[0]:25000,marron[1]:45000,bleu_ciel[0]:55000,bleu_ciel[1]:55000,bleu_ciel[0]:55000,
bleu_ciel[2]:60000,rose[0]:75000,rose[1]:75000,rose[2]:90000,orange[0]:95000,orange[1]:95000,
orange[2]:100000,rouge[0]:105000,rouge[1]:105000,rouge[2]:110000,jaune[0]:115000,jaune[1]:115000,
jaune[2]:120000,vert[0]:127500,vert[1]:127500,vert[2]:140000,bleu[0]:150000,bleu[1]:200000
}

case=["DÉPART","BOULEVARD DE BELVILLE","CAISSE COMMUNAUTÉ","RUE LE COURBE",
	  "IMPÔT SUR LES REVENUS","GARE MONTPARNASSE","RUE DE VAUGIRARD","CHANCE",
	  "RUE DE COURCELLES","AVENUE DE LA RÉPUBLIQUE","PRISON EN SIMPLE VISITE",
	  "BOULEVARD DE LA VILLETTE","COMPAGNIE DE DISTRIBUTION D'ÉLECTRICITÉ",
	  "AVENUE DE NEUILLY","RUE DE PARADIS","GARE DE LYON","AVENUE MOZART","CAISSE DE COMMUNAUTÉ",
	  "BOULEVARD SAINT-MICHEL","PLACE PIGALLE","PARC GRATUIT","AVENUE MATIGNON","CHANCE",
	  "BOULEVARD MALSHERBES","AVENUE HENRI-MARTIN","GARE DU NORD","FAUBOURG SAINT-HONORÉ",
	  "PLACE DE LA BOURSE","COMPAGNIE DE DISTRIBUTION DES EAUX","RUE DE LA FAYETTE","AVENUE DE BRETEUIL",
	  "AVENUE FOCH","CAISSE COMMUNAUTÉ","BOULEVARD DES CAPUCINES","GARE SAINT-LAZARE","CHANCE",
	  "AVENUE DES CHAMPS-ÉLYSÉES","TAXE DE LUXE","RUE DE LA PAIX","PRISON","PRISON","PRISON"]

a=Fraction(1,1000)
###########################################
#Conversion du datat frame en fichier csv #
###########################################

dat=data(convert(afficher(modele4(q,a),a)))
D=data(puissance(convert(afficher(modele4(q,a),a)),3))
data_csv=D.to_csv(r'C:\Users\minko\OneDrive\Bureau\projet fin bac\statio.csv',header=True,sep=";",index=False)
#dfi.export(dat,"mytable.png")

#############################################
# Liste des cases du monopoly et numérotion #
#############################################

monopol=DataFrame(data=np.transpose(np.array([x for x in range(len(dat))])), columns=["Id case"])
monopol["Nom case"]=case[:len(dat)]
#monopoly_csv=monopol.to_csv(r'C:\Users\minko\OneDrive\Bureau\projet fin bac\monopoly.csv',header=True,sep=";",index=False)

#########################################################
#     recherche de la distribution stationnaire         #
#########################################################

P=convert(afficher(modele4(q,a),a))
alpha=np.zeros([1,len(P)])
alpha[0,0]=1
def pi():
	global P, alpha
	a=alpha
	b=np.matmul(a,P)
	i=1
	while np.array_equal(b,a)==0:
		a=b
		b=np.matmul(a,P)
		i+=1
	a_s=b
	return [a_s,i]
print(pi()[1])
print(pi()[0])

###################################################################
# Exportation de la distribution stationnaire dans un fichier.csv #
###################################################################

base=DataFrame(data=np.transpose(pi()[0]),columns=["probability"])
base["Case"]=case[:len(pi()[0][0])]
Index=[i for i in range(30)]+[j for j in range(31,43)] # contient les numéros en temps réel de chaque case.
base["Numéro de la case"]=Index
#base_csv=base.sort_values(by=["probability"], axis=0, ascending=False).to_csv(r'C:\Users\minko\OneDrive\Bureau\projet fin bac\steady_00001.csv',header=True,sep=";",index=False)

########################################
# barplot des différentes probabilités #
########################################
M=base.sort_values(by=["probability"], axis=0, ascending=False)

def prob(couleur):
	n=len(couleur)
	return sum(M[M["Case"].isin(couleur)]["probability"])/n
def mean():
	global couleurs,M,marron,bleu_ciel,rose,orange,rouge,jaune,vert,bleu
	m=np.array([prob(marron),prob(bleu_ciel),prob(rose),prob(orange),
			 prob(rouge),prob(jaune),prob(vert),prob(bleu)])
	m=DataFrame(data=np.transpose(m),columns=["probability"])
	m["couleurs"]=couleurs[:8]     
	return m.sort_values(by=["probability"], axis=0, ascending=False)

## FICHIER CSV CONTENANT LE CLASSEMENT DES COULEURS.
color_csv=mean().to_csv(r'C:\Users\minko\OneDrive\Bureau\projet fin bac\color.csv',header=True,sep=";",index=False)

## Visualiser les proba moyennes de visites de chaque couleur ici.
plt.figure(figsize=(5, 5))
col=[i for i in mean()["couleurs"]] #["orange","red","yellow","green","pink","brown","darkblue","skyblue"]
name=[dico_num[i] for i in mean()["couleurs"]]
#ax = mean()["probability"].plot(kind='bar', color=col)
#ax.set_xlabel('Numéro de la propriété')
#ax.set_ylabel('probabilité')
#ax.set_title("a=0.001")
#ax.set_xticklabels(name)
#plt.show()
		
# Rues et gares et compagnies
x=[i for i in cases]
col1=[dico_col[index] for index in M[M["Case"].isin(x)]["Numéro de la case"]]
state=M[M["Case"].isin(x)]
#ax = state["probability"].plot(kind='bar', color=col1)
#ax.set_xlabel('Numéro de la propriété')
#ax.set_ylabel('probabilité')
#Id=state["Numéro de la case"]
#ax.set_title("a=0.001")
#ax.set_xticklabels(Id)
#plt.show()
# Fichier csv contenant le classement des propriétés par ordre décroissant en fonction du numéro
state_csv=state.to_csv(r'C:\Users\minko\OneDrive\Bureau\projet fin bac\properties.csv',header=True,sep=";",index=False)
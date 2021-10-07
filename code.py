import pandas as pd
import re
from math import sqrt
import numpy as np

##Q1
#definir nos donnees
data=pd.read_csv('dataset.csv')

##Q2
#on cree une fonction qui crée une liste L de tous les mots figurant dans cette base
def listing(data):
    liste=[]
    length=len(data['texte'])
    
    for i in range(length):

        l=re.split(' ', data['texte'][i])

        liste.extend(l)
    mylist = list( dict.fromkeys(liste) )
    return(mylist)

##Q3
#Création de txt2num

def T2V(t,VA):

    VN=[]
    T=t.split()
    for j in range(len(VA)):
        cmpt=0
        for i in range(len(T)):
            if T[i]==VA[j]:
                cmpt=cmpt+1
        VN.append(cmpt)    
    return VN
##Q4
#une liste de mots vides 
MV=['Si', 'la', 'du',  'tous', 'les',  '40', 'ans','de', 'ne', 'pas', 'y',  'Le', 'se',  'donc', 
 'sans',  'ou', 'encore', 'Cristiano', 'Ronaldo',  'à',  'une','Et', 'il', "qu'il", 
'même', 'chez', "jusqu'à", 'Kylian', 'Mbappé', 'a', 'le', 'et', 'dans', 'au', 'son', 'Sergio', 'Ramos', "n'a", 'toujours',
'avec','en', '2019', '2020,', 'Primoz', 'Roglic', 'ça', '2021,',  'devant', 'Enric', 'Mas', 'Jack', 
'Haig.', 'Slovène', 'Jumbo-Visma', 'sur',   'La',  'par',  'sous',  'Après', 'qui', 'sa',  'd’un', 'plus', 'que', 'c’est',  'des', 'bonnes', 'nouvelles', 'En', 'raison', 'difficultés', 'pour', 'consommer', 'pendant', 'pandémie,', 
'ont', 'beaucoup', 'ce', "qu'ils",  'un', 'd’Emmanuel', '22', 'septembre.', 'est', 'vendredi', '10', 'septembre,', 'Elle', 
'Une', 'leurs', 'selon','Les',  "s'en", 'Il', '2022', 'Emmanuel', 'Macron,', '2022,', 'dernier', 'mandat', 
'pour', 'd’autrui',  'Mais', 'alors', 'qu’il', 'octobre', '1554', '1585', 'Un', 'depuis', 'an', 'Pour', 'serait' 
'avant',  'comme', 'trop', 'C’est', ]
#on utilise la pour réduite la dimension de L
def stopword(L,MV):
    L1=L.copy()
    for i in MV:
        if i in L1: 
            L1.remove(i)
   
    L2=L1
    return(L2)
#le taux de réduction
T=1-len(stopword(listing(data),MV))/len(listing(data))
print('alors le taux de réduction est :', T)

##Q5
#on élimine les mots de la liste L ayant figuré dans les 3 classes et garde uniquement ceux qui figurent dans une ou deux classes.
def ELIM(L,data):
    nb=0
    for word in L:
        for i in ['Sport','économie','politique']:
            for j in data[data['label']==i]:
                if word==j:
                    nb+=1
            if nb==3:
                L.remove(word)
                print(L)
    return(L)

#le taux de réduction
T=1-len(ELIM(listing(data),data))/len(listing(data))
print('alors le taux de réduction est :', T)


##Q6
#on calcule la distance euclidienne entre deux vecteurs   
def DIST(X,Y):
    d=0
    for i in range(len(X)):
        d=d+(X[i]-Y[i])**2        
    return sqrt(d)

##Q7
#on propose un texte pour lequel : (en utilisant T2V) Parmi les 15 textes de la base, la DIST minimale correspond à la classe économie.

def minimal(data, L):
    length=len(L)
    
    vec=np.zeros(length)
    ve=np.zeros(length)
    dist={}
    df=data[data['label']=='économie']
    for i in range(5):
        ve=np.array(T2V(df['texte'][i+5], L)) 
        vec=vec+ve
    vec_eco=vec/5
    
    for i in range(15):
        vec=np.empty(length)
        vec=np.array(T2V(data['texte'][i], L))
        dist[i]=DIST(list(vec),list(vec_eco))
        
    mininum = min(dist, key=dist.get)  
    print('Parmi les 15 textes de la base, la DIST minimale correspond à la classe économie c est[',data['texte'][mininum] + '] ') 
    print('par la valeur de ')
    return(dist[mininum])
print(minimal(data,listing(data)))

##Q8
#on propose un texte pour lequel : (en utilisant T2V + MV + ELIM) Parmi les 15 textes de la base, la DIST minimale correspond à la classe sport.

def minimal(data, L,MV):
    L=stopword(L, MV)
    L=ELIM(L,data)
    length=len(L)
    
    vec=np.zeros(length)
    ve=np.zeros(length)
    dist={}
    df=data[data['label']=='Sport']
    for i in range(5):
        ve=np.array(T2V(df['texte'][i], L)) 
        vec=vec+ve
    vec_eco=vec/5
    
    for i in range(15):
        vec=np.empty(length)
        vec=np.array(T2V(data['texte'][i], L))
        dist[i]=DIST(list(vec),list(vec_eco))
        
    mininum = min(dist, key=dist.get)  
    print('Parmi les 15 textes de la base, la DIST minimale correspond à la classe sport c est[',data['texte'][mininum] + '] ') 
    print('par la valeur de ')
    return(dist[mininum])
print(minimal(data,listing(data), MV))

#Q9
#Proposez un texte pour lequel : La classe de la DIST minimale (en utilisant T2V) est différente de la classe de la DIST minimale (en utilisant T2V + MV + ELIM)
def deux(data, L1,MV):
    L=L1.copy()
    length=len(L)
    
    vec=np.zeros(length)
    ve=np.zeros(length)
    dist_eco={}
    dist_spo={}
    dist_pol={}
    df=data[data['label']=='économie']
    for i in range(5):
        ve=np.array(T2V(df['texte'][i+5], L)) 
        vec=vec+ve
    vec_eco=vec/5
    df=data[data['label']=='Sport']
    for i in range(5):
        vec=np.empty(length)
        ve=np.empty(length)
        ve=np.array(T2V(df['texte'][i], L)) 
        vec=vec+ve
    vec_spo=vec/5
    df=data[data['label']=='politique']
    for i in range(5):
        vec=np.empty(length)
        ve=np.empty(length)
        ve=np.array(T2V(df['texte'][i+10], L)) 
        vec=vec+ve
    vec_pol=vec/5
    d={}
    for i in range(15):
        vec=np.empty(length)
        vec=np.array(T2V(data['texte'][i], L))
        dist_eco[i]=DIST(list(vec),list(vec_eco))
        dist_spo[i]=DIST(list(vec),list(vec_spo))
        dist_pol[i]=DIST(list(vec),list(vec_pol))
        d[i]=dist_eco[i]+dist_spo[i]+dist_pol[i]
        
    maxi = max(d, key=d.get) 
    print('le texte pour lequel : La classe de la DIST minimale (en utilisant T2V) est différente de la classe de la DIST minimale (en utilisant T2V + MV + ELIM)')
    print(data['texte'][maxi])
    print('par la valeur de ')
    return (d[maxi])
print(deux(data,listing(data), MV))


##Q10

##le model d’apprentissage artificiel avez-vous utilisé dans les questions 7 à 9 est KNN (K-Nearest Neighbors) (K=3)
##avantage :L’algorithme est polyvalent. Il peut être utilisé pour la classification, la régression et la recherche d’informations (comme nous le verrons dans la section suivante).
##inconvénient:L’algorithme ralentit considérablement à mesure que le nombre d’observations et/ou de variables dépendantes/indépendantes augmente. En effet, l’algorithme parcourt l’ensemble des observations pour calculer chaque distance.
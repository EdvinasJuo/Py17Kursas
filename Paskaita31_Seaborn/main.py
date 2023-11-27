import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


tips = sns.load_dataset('tips')
print(tips.to_string())

#---------------------------------------------------------------------------------------------
#Pasiskirstymo histogramos
# Jų pagalba matysime, koks yra kokio nors vieno rodiklio pasiskirstymas

# sns.distplot(tips['total_bill'], kde =False, bins=20)  #kde=False nuima linija. bins=20 Nurodo stulpeliu skaiciu.
# plt.show()

#---------------------------------------------------------------------------------------------
#.joingplot sujungia du stulpelius
# sns.jointplot(x='total_bill', y='tip', data=tips)
# plt.show()

# # kind='hex' nurodo atvaizdavimo rusi.
# sns.jointplot(x='total_bill', y='tip', data=tips, kind = 'hex')
# plt.show()
#
# # kind='reg' nurodo atvaizdavimo rusi su tiesia.
# sns.jointplot(x='total_bill', y='tip', data=tips, kind = 'reg')
# plt.show()

# # kind='kde' nurodo atvaizdavimo rusi su koncentracija.
# sns.jointplot(x='total_bill', y='tip', data=tips, kind = 'kde')
# plt.show()
#
# #---------------------------------------------scatterplot---------------------------------------------
# # scatterplot grupuoja dalykus pagal hue=' '
# sns.scatterplot(y='tip', x='total_bill', data=tips, hue='day', size='size')
# plt.show()

#--------------------------------------------pairplot----------------------------------------------
# # duoda mums visas įmanomas pasiskirstymo kombinacijas lentelėje:
# sns.pairplot(tips)
# plt.show()
#
# # pridedu grupavima pagal lyti ir pakeiciu spalvas
# sns.pairplot(tips, hue='sex', diag_kind='hist')
# plt.show()

# #--------------------------------------------barplot----------------------------------------------
# #KATEKORIZAVIMO DIAGRAMOS
# # .barplot() išskirsto kategorijas pagal kurį nors rodiklį ir leidžia tam rodikliui taikyi kokią nors funkciją:
# #estimator = sum. grazins tos dienos suma
# #ci="False" panaikina bruksiunuka
# sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum, ci=False)
# plt.show()
#
#
# #--------------------------------------------countplot----------------------------------------------
# sns.countplot(x='smoker', data=tips) # SUSKAICIUOJA KIEK YRA RUKANCIU (KIEK YRA IRASU KIEKI)
# plt.show()


# #--------------------------------------------boxplot----------------------------------------------
# sns.boxplot(x='smoker', y='total_bill', data=tips)
# plt.show()


#--------------------------------------------heatmap----------------------------------------------
# koreliacijos = tips.corr(numeric_only=True)
# print(koreliacijos)
# sns.heatmap(koreliacijos, annot=True)
# plt.show()
#
#
# #--------------------------------------------FaceGrid----------------------------------------------
# #.FacetGrid() leidžia susikurti tinklelį, kurį vėliau reikės užpildytyi diagramomis. Pvz.:
# g = sns.FacetGrid(data=tips, col='time', row ='smoker')
# g.map(sns.scatterplot, 'total_bill', 'tip')
# plt.show()


#--------------------------------------------Stilius ir spalva----------------------------------------------
#Seaborn leidžia nustatyti stilių su .set_style() metodu. Į parametrus reikia įkelti vieną iš šių reikšmių - darkgrid, whitegrid, dark, white, ticks.
sns.set_style('darkgrid')
sns.barplot(x='sex', y='total_bill', data=tips, hue='day', estimator=sum,palette='cividis') #palette = pakeicia spalvu tema
sns.despine() # nustacius backgrouda pasalina jo linijas (ribas)
plt.show()

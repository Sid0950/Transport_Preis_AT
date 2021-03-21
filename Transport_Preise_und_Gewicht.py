#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd


# In[12]:


class Transport_Preise_und_Gewicht:
    def __init__(self, Land, PLZ, Durchmesser, Stutzenlänge, Hohe, Entlüftung, Palette):
        self.Land = Land
        self.PLZ = PLZ
        self.Durchmesser = Durchmesser
        self.Stutzenlänge = Stutzenlänge
        self.Hohe = Hohe
        self.Entlüftung = Entlüftung
        self.Palette = Palette
            
    def Gewicht_Rechner(self, Land, PLZ, Durchmesser, Stutzenlänge, Hohe, Entlüftung, Palette):
        #Variablen
        Land = self.Land
        PLZ = self.PLZ 
        Durchmesser = self.Durchmesser
        Stutzenlänge = self.Stutzenlänge
        Hohe = self.Hohe
        Entlüftung = self.Entlüftung
        Palette = self.Palette
            
    
        # GEWICHT & VOLUMEN RECHNER

        #Breite, in millimeter
        Breite = Durchmesser + 2*Stutzenlänge
        #Packstück Höhe, in millimeter
        Packstuck_Hohe = Hohe + Entlüftung + Palette

        #Volumen, in cubic meter 
        Volumen = (Breite*Breite*Packstuck_Hohe)/10**9

        # Gewicht pro cubic meter, kg/m3
        GPCM = 300

        # Gewicht
        Gewicht = GPCM*Volumen
        return Gewicht
    
    def Preise_Rechner(self,Gewicht):
        
        #Variablen
        Land = self.Land
        PLZ = self.PLZ
        
        if Land == 'Osterreich':
            df = pd.read_excel('TransportPreise.xlsx', sheet_name = 'Osterreich')
        else:
            df = pd.read_excel('TransportPreise.xlsx', sheet_name  = 'Deutschland')
            
        # RUNDUNG UND PREIS
        
        #CONDITION 1
        if 0<Gewicht<=200:
            if 0<Gewicht <=40:
                Gewicht = 40
                if 6800 <= PLZ <=6989:
                    Preise = df["Gruppe 1"].loc[0]

                elif 6700 <= PLZ <=6799:
                    Preise = df["Gruppe 2"].loc[0]

                elif (6000 <= PLZ <=6199) or (6400 <= PLZ <=6699):
                    Preise  = df["Gruppe 3"].loc[0]

                elif (4900 <= PLZ <=5499) or (5600 <= PLZ <=5799) or (6200 <= PLZ <=6399) or (6200 <= PLZ <=6399) or (9600 <= PLZ <=9699) or (9900 <= PLZ <=9999):
                    Preise = df["Gruppe 4"].loc[0]

                else:
                    Preise = df["Gruppe 5"].loc[0]





            else:
                for i in range(0,8,1):
                    if (df["Menge"].loc[i]) <Gewicht<= (df["Menge"].loc[i+1]):
                        Gewicht = df["Menge"].loc[i+1]
                        
                        if 6800 <= PLZ <=6989:
                            Preise = df["Gruppe 1"].loc[i+1]
                        elif 6700 <= PLZ <=6799:
                            Preise = df["Gruppe 2"].loc[i+1]
                        elif (6000 <= PLZ <=6199) or (6400 <= PLZ <=6699):
                            Preise = df["Gruppe 3"].loc[i+1]
                        elif (4900 <= PLZ <=5499) or (5600 <= PLZ <=5799) or (6200 <= PLZ <=6399) or (6200 <= PLZ <=6399) or (9600 <= PLZ <=9699) or (9900 <= PLZ <=9999):
                            Preise = df["Gruppe 4"].loc[i+1]
                        else:
                            Preise = df["Gruppe 5"].loc[i+1]







        #CONDITION 2           
        elif 200< Gewicht<=500:
            for j in range(8,14,1):
                if (df["Menge"].loc[j]) <Gewicht<= (df["Menge"].loc[j+1]):
                    Gewicht = df["Menge"].loc[j+1]

                    if 6800 <= PLZ <=6989:
                        Preise = df["Gruppe 1"].loc[j+1]
                    elif 6700 <= PLZ <=6799:
                        Preise = df["Gruppe 2"].loc[j+1]
                    elif (6000 <= PLZ <=6199) or (6400 <= PLZ <=6699):
                        Preise = df["Gruppe 3"].loc[j+1]
                    elif (4900 <= PLZ <=5499) or (5600 <= PLZ <=5799) or (6200 <= PLZ <=6399) or (6200 <= PLZ <=6399) or (9600 <= PLZ <=9699) or (9900 <= PLZ <=9999):
                        Preise = df["Gruppe 4"].loc[j+1]
                    else:
                        Preise = df["Gruppe 5"].loc[j+1]









        #CONDITION 3                       
        else:
            for k in range(14,16,1):
                Residue = Gewicht%100
                
                if Residue <=50:
                    Gewicht = Gewicht - Residue + 50

                else:
                    Gewicht = Gewicht - Residue + 100

                if 500 < Gewicht <=1000:

                    if 6800 <= PLZ <=6989:
                        Preise = Gewicht*df["Gruppe 1"].loc[k]/100

                    elif 6700 <= PLZ <=6799:
                        Preise = Gewicht*df["Gruppe 2"].loc[k]/100

                    elif (6000 <= PLZ <=6199) or (6400 <= PLZ <=6699):
                        Preise = Gewicht*df["Gruppe 3"].loc[k]/100

                    elif (4900 <= PLZ <=5499) or (5600 <= PLZ <=5799) or (6200 <= PLZ <=6399) or (6200 <= PLZ <=6399) or (9600 <= PLZ <=9699) or (9900 <= PLZ <=9999):
                        Preise = Gewicht*df["Gruppe 4"].loc[k]/100

                    else:
                        Preise = Gewicht*df["Gruppe 5"].loc[k]/100



                else:

                    if 6800 <= PLZ <=6989:
                        Preise = Gewicht*df["Gruppe 1"].loc[k+1]/100

                    elif 6700 <= PLZ <=6799:
                        Preise = Gewicht*df["Gruppe 2"].loc[k+1]/100

                    elif (6000 <= PLZ <=6199) or (6400 <= PLZ <=6699):
                        Preise = Gewicht*df["Gruppe 3"].loc[k+1]/100

                    elif (4900 <= PLZ <=5499) or (5600 <= PLZ <=5799) or (6200 <= PLZ <=6399) or (6200 <= PLZ <=6399) or (9600 <= PLZ <=9699) or (9900 <= PLZ <=9999):
                        Preise = Gewicht*df["Gruppe 4"].loc[k+1]/100

                    else:
                        Preise = Gewicht*df["Gruppe 5"].loc[k+1]/100
                        
                        
        return Preise    
        


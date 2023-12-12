import pandas as pd

# Lee el archivo CSV / Read the file
df = pd.read_csv("table_tableau11.csv")

# Filtra los distritos electorales con población menor a 100000 / Filter all Electoral District with the Population is less than 100000
# Creamos un nuevo DataFrame llamado df_filtered que contiene solo las filas donde la población es menor a 100,000. / 
# Create a DataFrame called df_filtered within ther rows where the Population is less than 100000
df_filtered = df[(df["Population"] < 100000)]

# Encuentra el distrito electoral con el mayor número de votos rechazados en el DataFrame filtrado
# Find the Max Rejected Ballots
max_rejected_district = df_filtered.loc[df_filtered["Rejected Ballots/Bulletins rejetés"].idxmax()]

# Imprime el resultado / show teh resuts
print("Electoral District Name/Nom de circonscription:", max_rejected_district["Electoral District Name/Nom de circonscription"])
print("Rejected Ballots/Bulletins:", max_rejected_district["Rejected Ballots/Bulletins rejetés"])
print("Population:", max_rejected_district["Population"])
#print("Elected Candidate/Candidat élu:", max_rejected_district["Elected Candidate/Candidat élu"])
print("echo", max_rejected_district["Electoral District Name/Nom de circonscription"], "> ~/mysolution")
import pandas as pd
my_path_file='C:\\Users\\deeph\\visual_studio_projects\\pokemon_database\\'
my_csv=my_path_file + "pokemon.csv"
poke = pd.read_csv(my_csv)
# print(poke)

# with open("pokemon_true.csv", "w") as f:
#     f.write("#,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary")

df =poke[poke['Legendary'].isin([True])]
my_csv=my_path_file + "pokemon_true.csv"
df.to_csv(my_csv)
print(df)
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')





df = pd.read_csv("C:\\Users\\deeph\\visual_studio_projects\\pokemon_database\\pokemon_true.csv")
poke_id = df['id'].values.tolist()
# print(poke_id)
idx = random.randint(0, len(poke_id))
#rand_poke = df['id'], df['Name'], df['Attack'], df['Defense'], df['Sp. Atk'], df['Sp. Def'], df['Speed'] 
params =['Attack','Defense','Sp. Atk','Sp. Def','Speed']
rand_poke = df['Attack'][idx], df['Defense'][idx], df['Sp. Atk'][idx], df['Sp. Def'][idx], df['Speed'][idx]
rand_params = list(rand_poke)
rand_label =df['Name'][idx]

angles =np.linspace(0,2*np.pi, len(params), endpoint = False)

angles=np.concatenate((angles,[angles[0]]))
params.append(params[0])
rand_params.append(rand_params[0])

print(rand_label, rand_params)
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
#basic plot
ax.plot(angles,rand_params, '*--', color = 'r', label= rand_label)
#fill plot
ax.fill(angles, rand_params, alpha=0.25, color='r')
#Add labels
ax.set_thetagrids(angles * 180/np.pi, params)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()


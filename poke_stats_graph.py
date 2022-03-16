import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv("C:\\Users\\deeph\\visual_studio_projects\\pokemon_database\\pokemon_true.csv")

params =['Attack','Defense','Sp. Atk','Sp. Def','Speed']
zapdos =[110,90,154,90,130]

angles =np.linspace(0,2*np.pi, len(params), endpoint = False)

angles=np.concatenate((angles,[angles[0]]))
params.append(params[0])
zapdos.append(zapdos[0])

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
#basic plot
ax.plot(angles,zapdos, 'o--', color = 'r', label= 'Zapdos')
#fill plot
ax.fill(angles, zapdos, alpha=0.25, color='r')
#Add labels
ax.set_thetagrids(angles * 180/np.pi, params)
plt.grid(True)
plt.tight_layout()
plt.legend()
plt.show()
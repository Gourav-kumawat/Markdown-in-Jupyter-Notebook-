# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:49:17 2020

@author: SCEA
"""


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

data = np.loadtxt('C:/Users/SCEA/.spyder-py3/My Stuffs/Files/NGC5272.csv')
color = []
index=np.where(data[:,6]>90)

for i in range(1,5):
   color.append( data[index,i] - data[index,i+1])

# plt.style.use('classic')



# ST PARTFIR
fig, axes = plt.subplots(2, 2, sharex='all', sharey='all')


axes[0,0].scatter(color[0].flatten(), data[index,1], s=0.05, color = 'blue', alpha=0.8 )
axes[0,1].scatter(color[1].flatten(), data[index,2], s=0.05, color = 'blue', alpha=0.8)
axes[1,0].scatter(color[2].flatten(), data[index,3], s=0.05, color = 'blue', alpha=0.8 )
axes[1,1].scatter(color[3].flatten(), data[index,4], s=0.05, color = 'blue', alpha=0.8 )


for ax in axes.flat:
    ax.set(xlim=[-2.5,6], ylim=[30,13])
    
axes[0,0].set_title('F275W vs F275W-F336W')
axes[0,1].set_title('F336W vs F336W-F438W')
axes[1,0].set_title('F438W vs F438W-F606W')
axes[1,1].set_title('F606W vs F606W-F814W')

axes[0,0].set_ylabel('Apparent Magnitude')
axes[1,0].set_xlabel('Color')
axes[1,0].set_ylabel('Apparent Magnitude')
axes[1,1].set_xlabel('Color')




#SECOND PART


fig = plt.figure(figsize=(20,8), facecolor='black')
fig.suptitle('HR DIAGRAM', fontsize=22)
plt.style.use('dark_background')
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], ylim= (30,15), xlim=(-2,5), ylabel = 'Apparent Mgnitude in 275 nm', xlabel = 'Color (275-336 nm)')


ax.set_title('Messier 3', style='oblique', fontsize=15)

secax = ax.secondary_yaxis(location='right')
secax.set_ylabel('Luminosity (in Solar units)', fontsize=14)
secax.set_yticklabels(['$1000$','$100$','$10$','$1$','$0.1$','$0.01$'])
secax.set_yticks([16.14,18.64,21.14,23.64,26.14,28.64])


main_seq = patches.Ellipse(xy=(0.9,22), width=0.8, height=5, angle=350, fill= False, color='white')
turn_off = patches.Ellipse(xy=(0.5,19), width=0.5, height=1, angle=350, fill= False, color='white')
sub_giant = patches.Ellipse(xy=(0.95,19.6), width=0.4  , height=0.9  , angle=10, fill=False, color='white')
red_giant = patches.Ellipse(xy=(1.9,18.5), width=2  , height=1  , angle=355, fill=False, color='white')
asy_giant = patches.Ellipse(xy=(0.88,17), width=0.9  , height=0.5  , angle=5, fill=False, color='white')
hor_branch= patches.Ellipse(xy=(0.1,16.12), width=0.8  , height=0.5  , angle=355, fill=False, color='white')


ax.add_patch(main_seq)
ax.add_patch(turn_off)
ax.add_patch(sub_giant)
ax.add_patch(red_giant)
ax.add_patch(asy_giant)
ax.add_patch(hor_branch)


ax.annotate(s='Main Sequence Branch', xy=(0.9, 22), xycoords='data', xytext=(2, 21.7), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))

ax.annotate(s='Turnoff Point', xy=(0.5, 19), xycoords='data', xytext=(-0.44, 18.9), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))

ax.annotate(s='Horizontal Branch', xy=(0.1, 16.12), xycoords='data', xytext=(-0.9,16.2 ), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))

ax.annotate(s='Asymptotic Giant Branch', xy=(0.88, 17), xycoords='data', xytext=(-0.35,17.3 ), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))

ax.annotate(s='Super Giant Branch', xy=(0.95, 19.6), xycoords='data', xytext=(2.05,20.23 ), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))

ax.annotate(s='Red Giant Branch', xy=(1.9, 18.5), xycoords='data', xytext=(3.13,16.86 ), textcoords='data', size=9,
              va='center', ha='center',bbox=dict(fc='k'),
              arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3,rad=-0.2', fc='w'))








ax.scatter(color[0].flatten(), data[index,1], s=0.09, color = 'skyblue' )







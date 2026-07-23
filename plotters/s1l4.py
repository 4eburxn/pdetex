import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches

fig, ax = plt.subplots(figsize=(4, 4))

x = np.linspace(-100, 10, 1000)
y = np.linspace(-100, 10, 1000)
X, Y = np.meshgrid(x, y)

# мега-формула(хз как работает))
W = 0.5*((X - 2 + 0.1*np.cos(X/20))**2 + (Y-0.1 + np.sin(Y/10))**2 - (X**3)/10 + (Y*X**2) + 1.5*np.sin(X*Y * 0.4 * np.pi/2) - 1.5*np.sin((X + Y) * 0.2 * np.pi/2))

levels = [i/100 for i in range(1, 400, 15)]
cs = ax.contour(X, Y, W, levels=levels, colors='black', linewidths=1.2)

# Центр и базовый эллипс
cx, cy = 1.1, 0.7
a, b = 0.8, 0.7
theta = np.linspace(0, 2 * np.pi, 200)

# Радиус идеального эллипса
r_base = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)

# МЕНЕЕ СИММЕТРИЧНАЯ ДЕФОРМАЦИЯ
# Смесь нескольких гармоник с несоизмеримыми частотами и фазами
r_deformed = r_base * (1 + 0.1 * (np.sin(2*theta + 0.5) + 
                                   0.7 * np.cos(3*theta - 0.3) + 
                                   0.5 * np.sin(5*theta + 0.8) + 
                                   0.3 * np.cos(7*theta + 1.2) + 
                                   0.2 * np.sin(theta + 0.1)))

x_deformed = cx + r_deformed * np.cos(theta)
y_deformed = cy + r_deformed * np.sin(theta)

verts = np.column_stack((x_deformed, y_deformed))
path = mpath.Path(verts)
deformed_ellipse = mpatches.PathPatch(path, facecolor='none', edgecolor='black', linewidth=1.5)

ax.add_patch(deformed_ellipse)
cs.set_clip_path(deformed_ellipse)

# Подписи и оси
ax.text(0.8, 1.5, r'$w(x, y) = C$', fontsize=14, rotation=0)
ax.text(0.15, 1.4, r'$G$', fontsize=18, fontweight='bold')
ax.annotate("", xy=(0.62, 1.2), xytext=(0.3, 1.4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=-0.3",
                            color="black", lw=2.3))

ax.arrow(0, 0, 2.3, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.arrow(0, 0, 0, 2.3, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(2.35, -0.2, r'$x$', fontsize=16)
ax.text(-0.15, 2.35, r'$y$', fontsize=16)
ax.text(-0.14, -0.13, r'$O$', fontsize=16)

ax.set_aspect('equal')
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.axis('off')

plt.tight_layout()
# plt.show()
plt.savefig("s1l4.png")

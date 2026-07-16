import matplotlib.pyplot as plt
import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches

# 1. Создание фигуры и осей
fig, ax = plt.subplots(figsize=(4, 4))

# 2. Настройка области построения
x = np.linspace(-0.5, 2.5, 400) 
y = np.linspace(-0.5, 2.5, 400)
X, Y = np.meshgrid(x, y)

# 3. Функция w(x, y)
W = (X - 0.2)**2 + (Y - 0.2)**2 + np.sin(X*0.5*np.pi)

# 4. Рисуем линии уровня
levels = [i/100 for i in range(1, 400, 10)]
cs = ax.contour(X, Y, W, levels=levels, colors='black', linewidths=1.2)

# ==========================================
# 5. СОЗДАЕМ ДЕФОРМИРОВАННЫЙ (ВОЛНИСТЫЙ) ЭЛЛИПС
# ==========================================
cx, cy = 1.1, 0.7         # Центр эллипса
a, b = 0.8, 0.7           # Длина полуосей
theta = np.linspace(0, 2 * np.pi, 200) # Угол от 0 до 2π

# Формула радиуса идеального эллипса в полярных координатах
r_base = (a * b) / np.sqrt((b * np.cos(theta))**2 + (a * np.sin(theta))**2)

# Добавляем волнистость (искривление) к радиусу. 
# ИЗМЕНЕНИЕ: 5 заменено на 7 (будет 7 "лепестков")
r_deformed = r_base * (1 + 0.08 * np.sin(7 * theta)) 

# Переводим полярные координаты обратно в декартовы
x_deformed = cx + r_deformed * np.cos(theta)
y_deformed = cy + r_deformed * np.sin(theta)

# Собираем вершины и создаем патч
verts = np.column_stack((x_deformed, y_deformed))
path = mpath.Path(verts)
deformed_ellipse = mpatches.PathPatch(path, facecolor='none', edgecolor='black', linewidth=1.5)

# Добавляем на график и обрезаем контуры
ax.add_patch(deformed_ellipse)
cs.set_clip_path(deformed_ellipse)
# ==========================================

# 6. Добавляем подпись к линии уровня
ax.text(0.8, 1.5, r'$w(x, y) = C$', fontsize=14, rotation=0)

# 7. Добавляем букву G и стрелку
ax.text(0.2, 1.3, r'$G$', fontsize=18, fontweight='bold')
ax.annotate(
    "",  
    xy=(0.62, 1.2),          
    xytext=(0.3, 1.3),      
    arrowprops=dict(
        arrowstyle="->",           
        connectionstyle="arc3,rad=0.3", 
        color="black",             
        lw=2.3
    )
)

# 8. Рисуем оси координат
ax.arrow(0, 0, 2.3, 0, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.arrow(0, 0, 0, 2.3, head_width=0.05, head_length=0.1, fc='black', ec='black')
ax.text(2.35, -0.1, r'$x$', fontsize=16)
ax.text(-0.1, 2.35, r'$y$', fontsize=16)
ax.text(-0.12, -0.12, r'$O$', fontsize=16)

# 9. Оформление
ax.set_aspect('equal') 
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.axis('off') 

plt.tight_layout()
plt.show()

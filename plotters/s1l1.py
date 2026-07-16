import matplotlib.pyplot as plt

def set_academic_style():
    """
    Устанавливает строгий академический стиль для matplotlib.
    """
    params = {
        # Размеры фигуры (ширина 8", высота 5" — подходит для страницы А4)
        'figure.figsize': (8, 5),
        'figure.dpi': 1000,
        
        # Шрифты (семейство с засечками, размер 11 pt)
        'font.family': 'serif',
        'font.serif': ['Computer Modern', 'Times New Roman', 'DejaVu Serif'],
        'font.size': 24,
        
        # Оси
        'axes.titlesize': 12,
        'axes.labelsize': 11,
        'axes.labelweight': 'normal',
        'axes.linewidth': 0.8,
        'axes.edgecolor': 'black',
        'axes.grid': True,
        'axes.grid.which': 'major',
        'axes.grid.axis': 'both',
        'axes.spines.top': False,
        'axes.spines.right': False,   # убираем верхнюю и правую рамки
        
        # Сетка (тонкая, пунктирная, серого цвета)
        'grid.color': '0.6',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5,
        'grid.alpha': 0.7,
        
        # Деления на осях
        'xtick.direction': 'in',      # засечки внутрь графика
        'ytick.direction': 'in',
        'xtick.major.size': 5,
        'ytick.major.size': 5,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        
        # Линии (толщина, стиль по умолчанию)
        'lines.linewidth': 1.8,
        'lines.markersize': 6,
        'lines.markeredgewidth': 0.5,
        
        # Легенда (без рамки, в углу)
        'legend.frameon': False,
        'legend.fontsize': 10,
        'legend.loc': 'best',
        'legend.handlelength': 1.5,
        
        # Цвета (сдержанная палитра, различимая в оттенках серого)
        'axes.prop_cycle': plt.cycler(
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
                   '#9467bd', '#8c564b', '#e377c2', '#7f7f7f']
        ),
        
        # Сохранение
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
    }
    plt.rcParams.update(params)
set_academic_style()
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.patheffects as path_effects
# ----------------------------------------------------------------------
# Функция для создания 3D-конуса (стрелки)
# ----------------------------------------------------------------------
def add_cone(ax, tip, direction, length=0.2, radius=0.06, color='black', alpha=1.0):
    """
    Рисует 3D-конус с вершиной в точке tip,
    направленный вдоль вектора direction (единичный),
    с заданной длиной и радиусом основания.
    """
    d = np.array(direction) / np.linalg.norm(direction)  # нормализуем
    # Основание конуса смещено назад от вершины
    base_center = tip - d * length
    
    # Строим два ортогональных вектора, перпендикулярных d
    if np.allclose(d, [0, 0, 1]) or np.allclose(d, [0, 0, -1]):
        u = np.array([1, 0, 0])
    else:
        u = np.cross(d, [0, 0, 1])
        u = u / np.linalg.norm(u)
    v = np.cross(d, u)
    
    # Точки окружности основания
    n_points = 20
    angles = np.linspace(0, 2*np.pi, n_points)
    circle = base_center[:, None] + radius * (np.outer(u, np.cos(angles)) + np.outer(v, np.sin(angles)))
    
    # Треугольники (вершина + две соседние точки основания)
    vertices = []
    for i in range(n_points):
        j = (i + 1) % n_points
        vertices.append([tip, circle[:, i], circle[:, j]])
    
    collection = Poly3DCollection(vertices, facecolor=color, edgecolor='none', alpha=alpha)
    ax.add_collection3d(collection)

# ----------------------------------------------------------------------
# 1. Функция, задающая радиус фигуры в зависимости от углов u и v
# ----------------------------------------------------------------------
def get_radius(u, v, amplitude=0.5):
    perturbation = (
        0.6 * np.sin(2 * u) * np.cos(3 * v) +
        0.4 * np.cos(3 * u + 0.5) * np.sin(2 * v + 1.2) +
        0.3 * np.sin(5 * u + 0.7) * np.cos(4 * v + 2.3) +
        0.2 * np.cos(6 * u + 1.1) * np.sin(5 * v + 0.8) +
        0.15 * np.sin(8 * u + 2.5) * np.cos(7 * v + 1.8)
    )
    # Затухание на полюсах (u=0,π) и на осях X, Y (v=0, π/2, π, 3π/2)
    envelope = np.sin(u) ** 2 * np.sin(2 * v) ** 2
    return 1 + amplitude * perturbation * envelope

# ----------------------------------------------------------------------
# 2. Строим поверхность
# ----------------------------------------------------------------------
u = np.linspace(0, np.pi, 150)
v = np.linspace(0, 2 * np.pi, 150)
u, v = np.meshgrid(u, v)

# Координаты базовой сферы (немного уменьшаем масштаб)
scale = 1
x_sphere = np.sin(u) * np.cos(v) / scale
y_sphere = np.sin(u) * np.sin(v) / scale
z_sphere = np.cos(u) / scale

r = get_radius(u, v, amplitude=0.1)   # амплитуда возмущения для поверхности
X = r * x_sphere
Y = r * y_sphere
Z = r * z_sphere

# ----------------------------------------------------------------------
# 3. Визуализация
# ----------------------------------------------------------------------
fig = plt.figure(figsize=(4, 6))
ax = fig.add_subplot(111, projection='3d')

# Рисуем поверхность
surf = ax.plot_surface(X, Y, Z,
                       cmap='Greys',
                       linewidth=0,
                       antialiased=True,
                       shade=True,
                       alpha=0.6,zorder=0)

# ----------------------------------------------------------------------
# 4. Убираем стандартные оси и рамку
# ----------------------------------------------------------------------
ax.set_axis_off()

# ----------------------------------------------------------------------
# 5. Вычисляем радиусы фигуры в направлениях осей
# ----------------------------------------------------------------------
rx = get_radius(np.pi/2, 0, amplitude=0.5)
ry = get_radius(np.pi/2, np.pi/2, amplitude=0.5)
rz = get_radius(0, 0, amplitude=0.5)

margin = 1.4
x_max = max(np.max(X), rx) * margin
y_max = max(np.max(Y), ry) * margin
z_max = max(np.max(Z), rz) * margin

# ----------------------------------------------------------------------
# 6. Функция для рисования одной оси с пунктиром внутри фигуры
#    и объёмной стрелкой-конусом на конце
# ----------------------------------------------------------------------
def draw_axis(ax, direction, radius, limit, color='black', linewidth=1.5):
    if direction == 'x':
        p_start = (-limit, 0, 0)
        p_neg   = (-radius, 0, 0)
        p_pos   = ( radius, 0, 0)
        p_end   = ( limit, 0, 0)
        arrow_dir = np.array((1, 0, 0))
        label = r'$X_1$'
    elif direction == 'y':
        p_start = (0,  limit, 0)
        p_neg   = (0,  radius, 0)
        p_pos   = (0, -radius, 0)
        p_end   = (0, -limit, 0)
        arrow_dir = np.array((0, -1, 0))
        label = r'$X_2$'
    else:
        p_start = (0, 0, -limit)
        p_neg   = (0, 0, -radius)
        p_pos   = (0, 0,  radius)
        p_end   = (0, 0,  limit)
        arrow_dir = np.array((0, 0, 1))
        label = r'$X_n$'

    # Оси (оставляем как есть)
    ax.plot([p_start[0], p_neg[0]], [p_start[1], p_neg[1]], [p_start[2], p_neg[2]],
            color=color, linewidth=linewidth, linestyle='-')
    ax.plot([p_neg[0], p_pos[0]], [p_neg[1], p_pos[1]], [p_neg[2], p_pos[2]],
            color=color, linewidth=linewidth, linestyle='--', dashes=(2, 2))
    ax.plot([p_pos[0], p_end[0]], [p_pos[1], p_end[1]], [p_pos[2], p_end[2]],
            color=color, linewidth=linewidth, linestyle='-', zorder=10)

    # ---- НОВЫЕ ТОЧКИ (гарантированно поверх) ----
    # Используем plot с маркерами, а не scatter
    ax.scatter([p_neg[0], p_pos[0]],
               [p_neg[1], p_pos[1]],
               [p_neg[2], p_pos[2]],
               color=color, s=50, zorder=10,linewidth=0.8)
    ax.plot([p_pos[0]], [p_pos[1]], [p_pos[2]], 'o',
            color='black', markersize=6,
            markeredgecolor='black', markeredgewidth=1.5,
            zorder=100)

    # Остальное без изменений
    offset = 0.01
    p_neg_out = np.array(p_neg) - arrow_dir * offset
    p_pos_out = np.array(p_pos) + arrow_dir * offset
    # (эти точки больше не нужны, но если оставить, они дублируют)
    # add_cone и текст ...
    add_cone(ax, tip=p_end+arrow_dir*0.1, direction=arrow_dir,
             length=0.15, radius=0.06, color=color, alpha=1.0)
    text_pos = np.array(p_end) + 0.4 * np.array(arrow_dir)
    ax.text(text_pos[0], text_pos[1], text_pos[2],
            label, color=color, fontsize=14, fontweight='bold')

# Рисуем три оси
draw_axis(ax, 'x', rx, x_max, color='black', linewidth=2.5)
draw_axis(ax, 'y', ry, y_max, color='black', linewidth=2.5)
draw_axis(ax, 'z', rz, z_max, color='black', linewidth=2.5)

# Выбор точки на поверхности для обозначения области
u0 = np.pi/3
v0 = np.pi/4
r0 = get_radius(u0, v0, amplitude=0.1)
X_s = r0 * np.sin(u0) * np.cos(v0)
Y_s = r0 * np.sin(u0) * np.sin(v0)
Z_s = r0 * np.cos(u0)

# Точка внутри для подписи 'x'
factor = -0.7
X_in = factor * X_s
Y_in = factor * Y_s
Z_in = factor * Z_s

# Рисуем внутреннюю точку
ax.plot([X_in], [Y_in], [Z_in+0.3], 'o', 
        color='brown', markersize=6, 
        markeredgecolor='brown', markeredgewidth=2,
        zorder=100)
# Подпись 'x' рядом

txt = ax.text(X_in + 0.03, Y_in + 0.06, Z_in + 0.03+0.3, 'x', color='brown', fontsize=16, fontweight='bold',zorder=20)
# Буква G, указывающая на область (точка на поверхности)
# Размещаем G снаружи, немного дальше от центра
G_pos = np.array([X_s, Y_s, Z_s]) * 1.8  # снаружи
# Линия от G_pos к точке на поверхности
ax.plot([G_pos[0], X_s], [G_pos[1], Y_s], [G_pos[2], Z_s], color='blue', linewidth=1.5, linestyle='--')
# Добавляем стрелку (конус) в точке поверхности, указывающую на область
dir_vec = np.array([X_s, Y_s, Z_s]) - G_pos
dir_len = np.linalg.norm(dir_vec)
if dir_len > 0:
    dir_vec = dir_vec / dir_len
    # Ставим конус в точке поверхности, направленный по dir_vec (от G к поверхности)
    # Но если мы хотим, чтобы конус указывал на область, то вершина конуса должна быть в области, а основание на линии.
    # Мы можем нарисовать конус с вершиной в (X_s, Y_s, Z_s) и направлением dir_vec, но тогда он будет "вонзаться" в поверхность.
    # Лучше нарисовать конус с вершиной в (X_s, Y_s, Z_s) и направлением -dir_vec (чтобы он торчал наружу?) 
    # Или просто поставить конус на линии перед точкой.
    # Я сделаю так: вершина конуса в (X_s, Y_s, Z_s), а направление указывает от G к поверхности, т.е. конус входит в поверхность?
    # Это некрасиво. Обычно стрелка указывает на объект, так что конец стрелки (остриё) находится в объекте.
    # Поэтому мы рисуем конус с вершиной в (X_s, Y_s, Z_s) и направлением от G к поверхности (т.е. остриё в объекте).
    add_cone(ax, tip=np.array([X_s, Y_s, Z_s]), direction=dir_vec, length=0.15, radius=0.06, color='navy', alpha=1.0)
    # Также рисуем текст G в позиции G_pos
    ax.text(G_pos[0], G_pos[1], G_pos[2], 'G', color='blue', fontsize=16, fontweight='bold')

# ----------------------------------------------------------------------
# 7. Настройка масштаба
# ----------------------------------------------------------------------
scale = 0.8
ax.set_xlim(-x_max*scale, x_max*scale)
ax.set_ylim(-y_max*scale, y_max*scale)
ax.set_zlim(-z_max*scale, z_max*scale)
ax.set_box_aspect([1, 1, 1])

plt.tight_layout()
plt.savefig("s1l1.png")

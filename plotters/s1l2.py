"""Сферические и цилиндрические координаты — читаемая версия конспекта."""
import numpy as np
import matplotlib.pyplot as plt

def set_academic_style():
    """
    Устанавливает строгий академический стиль для matplotlib.
    """
    params = {
        # Размеры фигуры (ширина 8", высота 5" — подходит для страницы А4)
        'figure.figsize': (8, 5),
        'figure.dpi': 100,
        
        # Шрифты (семейство с засечками, размер 11 pt)
        'font.family': 'serif',
        'font.serif': ['Computer Modern', 'Times New Roman', 'DejaVu Serif'],
        'font.size': 11,
        
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

INK = "#1f2430"        # основной цвет "чернил"
MUTED = "#8a8f98"      # вспомогательные штриховые линии
ACCENT = "#2f6fb7"     # дуги углов
ACCENT2 = "#b7532f"    # радиус / образующая

# косоугольная проекция: (x1, x2, x3) -> 2D
# x2 -> вправо, x3 -> вверх, x1 -> к зрителю (влево-вниз)
E1 = np.array([-0.62, -0.45])
E2 = np.array([1.0, 0.0])
E3 = np.array([0.0, 1.0])

def P(v):
    v = np.atleast_2d(v)
    out = v[:, [0]] * E1 + v[:, [1]] * E2 + v[:, [2]] * E3
    return out if out.shape[0] > 1 else out[0]

def arrow(ax, a, b, color=INK, lw=1.6, z=3):
    ax.annotate("", xy=tuple(b), xytext=tuple(a), zorder=z,
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                shrinkA=0, shrinkB=0, mutation_scale=16))

def dashed(ax, a3, b3, color=MUTED, lw=1.1):
    a, b = P(np.array(a3, float)), P(np.array(b3, float))
    ax.plot([a[0], b[0]], [a[1], b[1]], ls=(0, (5, 4)), color=color, lw=lw, zorder=1)

def axes3d(ax):
    O = np.zeros(3)
    arrow(ax, P(O), P([3.5, 0, 0]))
    arrow(ax, P(O), P([0, 3.5, 0]))
    arrow(ax, P(O), P([0, 0, 3.1]))
    ax.text(*(P([3.7, 0, 0]) + [-0.05, -0.18]), "$x_1$", fontsize=15, ha="center", color=INK)
    ax.text(*(P([0, 3.62, 0]) + [0, -0.05]), "$x_2$", fontsize=15, va="center", color=INK)
    ax.text(*(P([0, 0, 3.22]) + [0.14, 0]), "$x_3$", fontsize=15, color=INK)

def angle_arc(ax, pts3d, label, lab_xy, color=ACCENT):
    q = np.array([P(p) for p in pts3d])
    ax.plot(q[:, 0], q[:, 1], color=color, lw=1.6, zorder=4)
    ax.text(*lab_xy, label, fontsize=15, color=color, ha="center", va="center", zorder=5)

fig, (axs, axc) = plt.subplots(1, 2, figsize=(13.2, 5.6))
for ax in (axs, axc):
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-2.8, 5.3)
    ax.set_ylim(-2.25, 3.7)

# ---------------- сферические ----------------
axes3d(axs)
r, th, ph = 2.6, np.deg2rad(35), np.deg2rad(55)
M3 = np.array([r*np.sin(th)*np.cos(ph), r*np.sin(th)*np.sin(ph), r*np.cos(th)])
Q3 = np.array([M3[0], M3[1], 0.0])          # проекция M на плоскость x1x2
M, Q = P(M3), P(Q3)

arrow(axs, (0, 0), M, color=ACCENT2, lw=1.8)              # радиус r
axs.plot(*M, "o", ms=5, color=INK, zorder=5)
axs.text(M[0] + 0.12, M[1] + 0.14, "$M$", fontsize=15, color=INK)
axs.text(0.28, 1.52, "$r$", fontsize=15, color=ACCENT2)

dashed(axs, M3, Q3)                                        # вертикаль вниз
dashed(axs, (0, 0, 0), Q3)                                 # след в плоскости
dashed(axs, M3, (0, 0, M3[2]))                             # до оси x3
dashed(axs, Q3, (M3[0], 0, 0))                             # параллелограмм следа
dashed(axs, Q3, (0, M3[1], 0))

t = np.linspace(0, th, 40)                                 # дуга θ (в плоскости x3–OM)
arc_th = [(0.8*np.sin(s)*np.cos(ph), 0.8*np.sin(s)*np.sin(ph), 0.8*np.cos(s)) for s in t]
angle_arc(axs, arc_th, r"$\theta$", (0.19, 0.99))

t = np.linspace(0, ph, 40)                                 # дуга φ (в плоскости x1x2)
arc_ph = [(0.85*np.cos(s), 0.85*np.sin(s), 0) for s in t]
angle_arc(axs, arc_ph, r"$\varphi$", (-0.10, -0.68))

axs.set_title("Сферические координаты", fontsize=14, color=INK, pad=10)
axs.text(2.35, 2.9,
         "$x_1 = r\\,\\sin\\theta\\,\\cos\\varphi$\n"
         "$x_2 = r\\,\\sin\\theta\\,\\sin\\varphi$\n"
         "$x_3 = r\\,\\cos\\theta$",
         fontsize=15, color=INK, va="top", linespacing=2.0)

# ---------------- цилиндрические ----------------
axes3d(axc)
R, ph2, h = 1.9, np.deg2rad(55), 2.1
Q3 = np.array([R*np.cos(ph2), R*np.sin(ph2), 0.0])
M3 = np.array([Q3[0], Q3[1], h])
M, Q = P(M3), P(Q3)

arrow(axc, (0, 0), Q, color=ACCENT2, lw=1.8)               # радиус R в плоскости
axc.plot([Q[0], M[0]], [Q[1], M[1]], color=INK, lw=1.8, zorder=3)   # высота h
axc.plot(*M, "o", ms=5, color=INK, zorder=5)
axc.text(M[0] + 0.12, M[1] + 0.14, "$M$", fontsize=15, color=INK)
axc.text(0.55, -0.72, "$R$", fontsize=15, color=ACCENT2, ha="center")
axc.text(Q[0] + 0.16, (Q[1] + M[1])/2, "$h$", fontsize=15, color=INK)

dashed(axc, M3, (0, 0, h))                                 # до оси x3

t = np.linspace(0, ph2, 40)
arc_ph2 = [(0.7*np.cos(s), 0.7*np.sin(s), 0) for s in t]
angle_arc(axc, arc_ph2, r"$\varphi$", (-0.10, -0.60))

axc.set_title("Цилиндрические координаты", fontsize=14, color=INK, pad=10)
axc.text(2.35, 2.9,
         "$x_1 = R\\,\\cos\\varphi$\n"
         "$x_2 = R\\,\\sin\\varphi$\n"
         "$x_3 = h$",
         fontsize=15, color=INK, va="top", linespacing=2.0)

plt.savefig("s1l2.png")

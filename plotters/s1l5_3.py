import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

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

def draw_structure_graph():
    # 1. Создаем фигуру и оси
    fig, ax = plt.subplots(figsize=(5, 3))
    
    # Убираем стандартные границы
    # ax.set_xlim(-0.5, 4.5)
    # ax.set_ylim(-0.5, 4.0)
    ax.axis('off')

    # 2. Рисуем тетрадную сетку (по желанию, для имитации клетки)
    ax.set_axisbelow(True)
    ax.grid(True, which='both', linestyle='--', color='lightgray', alpha=0.6)
    ax.set_xticks(np.arange(-0.5, 5, 0.5))
    ax.set_yticks(np.arange(-0.5, 4.5, 0.5))
    
    # 3. Рисуем оси координат со стрелками
    # Ось X
    ax.arrow(-0.5, 0, 4.2-0.8, 0, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(3.7-0.8, -0.23, '$x$', fontsize=20)
    # Ось U
    ax.arrow(0, -0.4, 0, 2, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(-0.2, 3.15-1.5, '$u$', fontsize=20)
    # Точка O
    ax.text(-0.2, -0.25, '$O$', fontsize=20)
    # Точка l
    ax.text(2.5, -0.3, '$l$', fontsize=20, color='navy')
    # Засечка га Оси X
    l = 2.5
    ax.vlines(x=[l, l], ymin=-0.08, ymax=0.08, colors='black', linewidth=2)


    # 4. Задаем функцию для кривой (парабола)
    extremum = 1.5
    def u_func(x):
        return -0.4 * (x)**2 + x

    # Генерируем точки для отрисовки плавной кривой
    x_vals = np.linspace(0, l, 200)
    u_vals = u_func(x_vals)
    
    # Рисуем саму кривую (струну)
    ax.plot(x_vals, u_vals, color='navy', linewidth=2.5)

    # Показываем результат
    plt.tight_layout()
    # plt.show()
    plt.savefig("s1l5_3.png", bbox_inches='tight',dpi=300)

if __name__ == '__main__':
    draw_structure_graph()

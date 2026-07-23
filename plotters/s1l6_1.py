import matplotlib.pyplot as plt
import numpy as np


def set_academic_style():
    """
    Устанавливает строгий академический стиль для matplotlib.
    """
    params = {
        # Размеры фигуры (ширина 8", высота 5" — подходит для страницы А4)
        'figure.figsize': (4, 3),
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
        'axes.grid': False,
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


def draw_coordinate_systems():
    # Создаем фигуру с белым фоном (для вставки в учебник)
    fig, ax = plt.subplots(figsize=(4, 3), facecolor='white')
    ax.set_facecolor('white')

    # 1. Настраиваем область отображения
    # ax.set_xlim(-1.0, 7.5)
    # ax.set_ylim(-1.0, 6.0)

    # 2. Рисуем сетку (имитация тетради)
    # Задаем шаг сетки 0.5
    # x_ticks = np.arange(-1.0, 8.0, 0.5)
    # y_ticks = np.arange(-1.0, 6.5, 0.5)
    
    # ax.set_xticks(x_ticks)
    # ax.set_yticks(y_ticks)
    ax.set_xticklabels([])  # Убираем числовые подписи
    ax.set_yticklabels([])
    
    # Убираем рамку (спайны) и тики
    ax.tick_params(axis='both', which='both', length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    #
    # # Сетка должна быть позади осей
    # ax.set_axisbelow(True)
    # ax.grid(True, which='both', linestyle='--', color='#D3D3D3', linewidth=0.8, alpha=0.7)

    # 3. Рисуем оси координат для системы O, x, t
    arrow_args = {'head_width': 0.15, 'head_length': 0.3, 'fc': 'black', 'ec': 'black', 'linewidth': 1.5}

    # Ось x
    ax.arrow(-0.6, 0, 6.8, 0, **arrow_args)
    ax.text(6.2, -0.8, r"$x$",  color='black')

    # Ось t
    ax.arrow(0, -0.6, 0, 6.1, **arrow_args)
    ax.text(-0.5, 5.5, r"$t$",  color='black')

    # Начало координат O
    ax.text(-0.8, -1., r"$O$",  color='black')

    # 4. Рисуем оси координат для системы O', x', t'
    # Координаты начала O' выбираем так, чтобы было визуально похоже на картинку
    x_o, y_o = 2.5, 2. 

    # Ось x'
    ax.arrow(x_o, y_o, 4.8, 0, **arrow_args)
    ax.text(7.3, y_o - 0.8, r"$x'$",  color='black')

    # Ось t'
    ax.arrow(x_o, y_o, 0, 3.8, **arrow_args)
    ax.text(x_o - 0.5, 5.8, r"$t'$",  color='black')

    # Начало координат O'
    ax.text(x_o -0.8, y_o - 1, r"$O'$", color='black')

    # 5. Сохраняем результат с высоким разрешением
    plt.tight_layout()
    plt.savefig("s1l6_1.png", dpi=300, bbox_inches='tight')
    # plt.show() # Раскомментируйте, если нужно посмотреть в окне

if __name__ == '__main__':
    draw_coordinate_systems()

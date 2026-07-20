import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

def draw_vector_with_dashed_extension(ax, x0, y0, dx, dy, label,
                                      color='navy', extra=0.5,
                                      arrow_kw=None, text_kw=None,
                                      draw_angle=False, angle_label=None,
                                      arc_radius=0.5, arc_color=None,
                                      arc_kw=None, label_offset=0.3):
    """
    Рисует вектор-стрелку из (x0,y0) с компонентами (dx,dy),
    пунктирное продолжение за концом стрелки на длину extra,
    и подпись label у конца стрелки.

    Параметры для дуги угла:
        draw_angle : bool          - рисовать ли дугу
        angle_label : str          - текст метки угла (например, r'$\theta$')
        arc_radius : float         - радиус дуги
        arc_color : str            - цвет дуги и метки (по умолчанию равен color)
        arc_kw : dict              - дополнительные параметры для Arc
        label_offset : float       - смещение метки вдоль биссектрисы (в долях радиуса)
    """
    if arrow_kw is None:
        arrow_kw = dict(head_width=0.1, head_length=0.15, fc=color, ec=color, lw=2)
    if text_kw is None:
        text_kw = dict(fontsize=16, color=color)
    if arc_color is None:
        arc_color = color
    if arc_kw is None:
        arc_kw = dict(lw=1.5)

    # Стрелка
    ax.arrow(x0, y0, dx, dy, **arrow_kw)

    # Подпись у конца стрелки (автоматическое смещение)
    offset_x = -0.15 if dx >= 0 else -0.15 - len(label) * 0.1
    offset_y = 0.15 if dy >= 0 else -0.2
    ax.text(x0 + dx + offset_x, y0 + dy + offset_y, label, **text_kw)

    # Дуга угла между вектором и положительной осью X
    if draw_angle:
        angle_deg = np.degrees(np.arctan2(dy, dx))   # угол от +x, в градусах
        # Если угол отрицательный, дуга идёт по часовой стрелке (вниз)
        # Arc принимает theta1 и theta2 как углы от горизонтали (в градусах)
        arc = Arc((x0, y0), width=2.6*arc_radius, height=2.6*arc_radius,
                  angle=0, theta1=0, theta2=angle_deg,
                  color=arc_color, **arc_kw,zorder=100)
        ax.add_patch(arc)

        # Метка угла на биссектрисе
        mid_angle = np.radians(angle_deg / 2)-0.1
        r = arc_radius * (1 + label_offset)   # смещение за пределы дуги
        ax.text(x0 + r * np.cos(mid_angle),
                y0 + r * np.sin(mid_angle),
                angle_label, fontsize=16, color=arc_color)
    

def draw_structure_graph():
    # 1. Создаем фигуру и оси
    fig, ax = plt.subplots(figsize=(4, 3))
    
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
    ax.arrow(-0.5, 0, 4.2-1, 0, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(3.7-1, -0.25, '$x$', fontsize=20)
    # Ось U
    ax.arrow(0, -0.4, 0, 3.5-1, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(-0.2, 3.15-1, '$u$', fontsize=20)
    # Точка O
    ax.text(-0.25, -0.28, '$O$', fontsize=20)

    # 4. Задаем функцию для кривой (парабола)
    extremum = 1.5
    def u_func(x):
        return -0.3 * (x)**2 + 1.4*x

    # Генерируем точки для отрисовки плавной кривой
    x_vals = np.linspace(extremum - 1.1, extremum + 1.1, 200)
    u_vals = u_func(x_vals)
    
    # Рисуем саму кривую (струну)
    ax.plot(x_vals, u_vals, color='navy', linewidth=2.5)

    # 5. Определяем точки x1 и x2
    x1, x2 = 0.7, 1.5
    u1, u2 = u_func(x1), u_func(x2)

    # Рисуем пунктирные линии от x1 и x2 до кривой и ставим точки на оси X
    ax.vlines(x=x1, ymin=0, ymax=u1, colors='gray', linestyles='dashed')
    ax.vlines(x=x2, ymin=0, ymax=u2, colors='gray', linestyles='dashed')
    
    ax.text(x1 - 0.05, -0.3, '$x$', fontsize=14)
    ax.text(x2 - 0.05, -0.3, '$x + \Delta x$', fontsize=14)

    # --- ДОБАВЛЯЕМ ГОРИЗОНТАЛЬНУЮ ЛИНИЮ ИЗ ТОЧКИ x2 ---
    # Горизонтальная пунктирная линия от (x2, u2) до оси u (x=0)
    ax.hlines(y=u2, xmin=x2, xmax=2.5, colors='blue', linestyles='dashed', linewidth=2)
    ax.hlines(y=u1, xmin=x1, xmax=2, colors='blue', linestyles='dashed', linewidth=2)

    # 6. Рисуем векторы T (касательные)
    # Находим производную в точках: u'(x) = -0.6 * (x - 1.5)
    # Производные
    slope1 = -0.6 * x1 + 1.4
    slope2 = -0.6 * x2 + 1.4

    # Вектор T в x1 (вверх-вправо)
    dx1, dy1 = 0.5, 0.5 * slope1

    draw_vector_with_dashed_extension(
        ax, x1, u1, dx1, dy1, r"$\vec{T_1}$",
        color='navy', extra=0.5,
        draw_angle=True, angle_label=r'$\alpha_x$',
        arc_radius=0.3, arc_color='red', label_offset=0.4,
        arc_kw=dict(lw=2)
    )

    dx2, dy2 = 0.5, 0.5 * abs(slope2)
    draw_vector_with_dashed_extension(
        ax, x2, u2, dx2, dy2, r"$\vec{T_2}$",
        color='navy', extra=0.5,
        draw_angle=True, angle_label=r'$\alpha_{x + \Delta x}$',
        arc_radius=0.3, arc_color='red', label_offset=0.5,
        arc_kw=dict(lw=2)
    )

    # Показываем результат
    plt.tight_layout()
    plt.savefig("s1l5_2.png", bbox_inches='tight',dpi=300)
    # plt.show()

if __name__ == '__main__':
    draw_structure_graph()

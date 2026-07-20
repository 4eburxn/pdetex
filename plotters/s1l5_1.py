import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

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
    ax.arrow(-0.5, 0, 4.2, 0, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(3.75, -0.32, '$x$', fontsize=20)
    # Ось U
    ax.arrow(0, -0.4, 0, 3.5, head_width=0.08, head_length=0.15, fc='black', ec='black')
    ax.text(-0.25, 3.15, '$u$', fontsize=20)
    # Точка O
    ax.text(-0.35, -0.4, '$O$', fontsize=20)

    # 4. Задаем функцию для кривой (парабола)
    # u(x) = -0.3 * (x - 1.5)^2 + 2
    extremum = 1.5
    def u_func(x):
        return -0.3 * (x - extremum)**2 + 2

    # Генерируем точки для отрисовки плавной кривой
    x_vals = np.linspace(extremum - 1.7, extremum + 1.7, 200)
    u_vals = u_func(x_vals)
    
    # Рисуем саму кривую (струну)
    ax.plot(x_vals, u_vals, color='navy', linewidth=2.5)

    # 5. Определяем точки x1 и x2
    x1, x2 = 0.4, 1.0
    u1, u2 = u_func(x1), u_func(x2)

    # Рисуем пунктирные линии от x1 и x2 до кривой и ставим точки на оси X
    ax.vlines(x=x1, ymin=0, ymax=u1, colors='gray', linestyles='dashed')
    ax.vlines(x=x2, ymin=0, ymax=u2, colors='gray', linestyles='dashed')
    
    ax.text(x1 - 0.05, -0.3, '$x_1$', fontsize=18)
    ax.text(x2 - 0.05, -0.3, '$x_2$', fontsize=18)

    # --- ДОБАВЛЯЕМ ГОРИЗОНТАЛЬНУЮ ЛИНИЮ ИЗ ТОЧКИ x2 ---
    # Горизонтальная пунктирная линия от (x2, u2) до оси u (x=0)
    ax.hlines(y=u2, xmin=x2, xmax=2.5, colors='blue', linestyles='dashed', linewidth=1.5)

    # 6. Рисуем векторы T (касательные)
    # Находим производную в точках: u'(x) = -0.6 * (x - 1.5)
    slope1 = -0.6 * (x1 - 1.5)   # = 0.96
    slope2 = -0.6 * (x2 - 1.5)   # = -0.96

    # Пунктирное продолжение вектора T (недлинное, в том же направлении)
    extra = 0.5  # дополнительная длина (в единицах координат)
    # единичный вектор направления
    dx2, dy2 = 0.9, 0.9 * abs(slope2)

    len_vec = np.sqrt(dx2**2 + dy2**2)
    dx_unit = dx2 / len_vec
    dy_unit = dy2 / len_vec
    # конечная точка продолжения
    end_x = x2 + dx2 + extra * dx_unit
    end_y = u2 + dy2 + extra * dy_unit
    ax.plot([x2 + dx2, end_x], [u2 + dy2, end_y],
            color='navy', linestyle='dashed', linewidth=1.5)

    # Для вектора T' в точке x2 (вверх-влево)
    ax.arrow(x2, u2, dx2, dy2, head_width=0.1, head_length=0.15, fc='navy', ec='navy', lw=2)
    ax.text(x2 + dx2 - 0.4, u2 + dy2, r"$\vec{T}$", fontsize=25, color='navy')

    # 7. Рисуем маленькую дугу для угла между горизонталью и вектором T
    # Угол наклона вектора T к горизонтали (в градусах)
    angle_deg = np.degrees(np.arctan(slope2))
    # Рисуем дугу от горизонтали (0°) до направления вектора
    arc = Arc((x2, u2), width=2.5, height=2.5, angle=0,
              theta1=0, theta2=angle_deg, color='red', lw=2)
    ax.add_patch(arc)
    # Подпись угла (чуть смещена внутрь дуги)
    mid_angle = np.radians(angle_deg / 2)
    label_r = .6
    ax.text(x2 + 2.23*label_r * np.cos(mid_angle),
            u2 + 1.5 * label_r * np.sin(mid_angle),
            r'$\alpha$', fontsize=20, color='red')

    # Показываем результат
    plt.tight_layout()
    plt.savefig("s1l5_1.png",bbox_inches='tight',dpi=300)
    # plt.show()

if __name__ == '__main__':
    draw_structure_graph()

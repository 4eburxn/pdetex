import matplotlib.pyplot as plt

def draw_characteristic_triangle():
    # Настраиваем фигуру: строго белый фон, большой размер для учебника
    fig, ax = plt.subplots(figsize=(5, 4), facecolor='white')
    ax.set_facecolor('white')

    # Устанавливаем границы отображения
    # ax.set_xlim(-2, 8)
    # ax.set_ylim(-2, 5)

    # Полностью убираем стандартные оси и сетку
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    # Задаем настройки для стрелок
    arrow_params = {
        'head_width': 0.1,
        'head_length': 0.3,
        'fc': 'black',
        'ec': 'black',
        'linewidth': 1.5
    }

    # 1. Рисуем координатные оси (Ox и Ot)
    # Ось x
    ax.arrow(-1, 0, 8, 0, **arrow_params)
    ax.text(7.1, -0.4, r'$x$', fontsize=22, color='black')
    arrow_params = {
        'head_width': 0.17,
        'head_length': 0.18,
        'fc': 'black',
        'ec': 'black',
        'linewidth': 1.5
    }
    # Ось t
    ax.arrow(0, -1, 0, 3.5, **arrow_params)
    ax.text(-0.4, 2.6, r'$t$', fontsize=22, color='black')

    # Начало координат O (немного подняли относительно оси x)
    ax.text(-0.6, -0.6, r'$O$', fontsize=22, color='black')

    # 2. Задаем координаты вершин треугольника (при параметре a=1)
    x1, x2 = 1.0, 5.0
    x0, t0 = 3.0, 2.0
    P, Q, M = (1, 0), (5, 0), (3, 2)

    # 3. Рисуем заливку треугольника (светло-серая)
    ax.fill([P[0], M[0], Q[0]], [P[1], M[1], Q[1]], color='#d9d9d9', alpha=0.4)

    # 4. Рисуем линии самого треугольника (характеристики)
    # Левая ветвь: x - at = x1 => при a=1, t = x - 1
    ax.plot([P[0], M[0]], [P[1], M[1]], color='#005f73', linewidth=2.5)
    
    # Правая ветвь: x + at = x2 => при a=1, t = 5 - x
    ax.plot([M[0], Q[0]], [M[1], Q[1]], color='#005f73', linewidth=2.5)
    
    # Основание (на оси x)
    ax.plot([P[0], Q[0]], [P[1], Q[1]], color='black', linewidth=2.5)

    # 5. Добавляем текстовые подписи и формулы
    # Точки P, Q (над осью Ox)
    ax.text(P[0] - 0.3, 0.08, r'$P$', fontsize=20, color='black')
    ax.text(Q[0] +0.05, 0.08, r'$Q$', fontsize=20, color='black')

    # Координаты x1, x2 (под осью Ox)
    ax.text(P[0] - 0.3, -0.4, r'$x_1$', fontsize=20, color='black')
    ax.text(Q[0] - 0.3, -0.4, r'$x_2$', fontsize=20, color='black')

    # Точка M
    ax.text(M[0] -0.6, M[1] + 0.2, r'$M(x_0, t_0)$', fontsize=20, color='black')

    # Формулы характеристик (под углом 45 и -45 градусов)
    ax.text(1.75, 1.1, r'$x - at = x_1$', fontsize=18, ha='center', va='center', rotation=60.3, color='darkgreen')
    ax.text(4.25, 1.1, r'$x + at = x_2$', fontsize=18, ha='center', va='center', rotation=-60.3, color='darkgreen')
    ax.scatter([x1, x2, x0], [0, 0, t0], color='black', zorder=5)
    # Сохраняем результат
    plt.tight_layout()
    plt.savefig("s1l6_2.png", dpi=300, bbox_inches='tight')
    # plt.show() # Раскомментируйте для просмотра в окне

if __name__ == '__main__':
    draw_characteristic_triangle()

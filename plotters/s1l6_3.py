import matplotlib.pyplot as plt

# Настройка размера фигуры (4x3 дюйма) и строгого стиля
fig, ax = plt.subplots(figsize=(4, 3))

# --- 1. Убираем стандартные рамки, сетку и метки (строгий стиль) ---
# ax.set_xlim(0, 6.5)
# ax.set_ylim(0, 4.5)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)

for spine in ax.spines.values():
    spine.set_visible(False)

# --- 2. Рисуем свои оси (стрелки) ---
# Ось X
ax.arrow(-0.4, 0, 6.2, 0, head_width=0.1, head_length=0.2, fc='black', ec='black', linewidth=1.)
# Ось Y (подпись t)
ax.arrow(0, -0.4, 0, 4.2, head_width=0.1, head_length=0.2, fc='black', ec='black', linewidth=1.)

# --- 3. Подписи осей и начала координат ---
ax.text(6.2, -0.2, '$x$', ha='center', va='top', fontsize='x-large')
ax.text(-0.2, 4.2, '$t$', ha='center', va='top', fontsize='x-large')
ax.text(-0.1, -0.1, '$O$', ha='right', va='top', fontsize='x-large')

# --- 4. Задаём точки x1 и x2 (одинаковый наклон линий) ---
x1 = .5
x2 = 2.5

# Рисуем точки на оси X
ax.scatter(x1, 0, color='red', s=40, zorder=10)
ax.scatter(x2, 0, color='green', s=40, zorder=10)

# Подписи для x1 и x2 (цветные, крупный шрифт)
ax.text(x1, -0.3, '$x_1$', ha='center', va='top', fontsize='x-large', color='red')
ax.text(x2, -0.3, '$x_2$', ha='center', va='top', fontsize='x-large', color='green')

# --- 5. Рисуем линии с ОДИНАКОВЫМ наклоном ---
# Красная линия (ЗСР) - наклон 1 (y = x - 1)
ax.plot([x1, 3.5], [0, 3.0], color='red', linewidth=1.5)
ax.text(3.5, 3, 'ЗФ', ha='center', va='bottom', fontsize='x-large', color='red')

# Зелёная линия (ПФ) - наклон 1 (y = x - 2.5)
ax.plot([x2, 5.5], [0, 3.0], color='green', linewidth=1.5)
ax.text(5.5, 3., 'ПФ', ha='center', va='bottom', fontsize='x-large', color='green')

# --- 6. Расставляем области (Римские цифры строго внутри областей) ---
# Область I (слева от красной линии)
ax.text(1.45, 1.6, 'I', ha='center', va='center', fontsize='xx-large', color='black')

# Область II (между красной и зелёной линиями)
ax.text(2.725, 1.2, 'II', ha='center', va='center', fontsize='xx-large', color='black')

# Область III (справа от зелёной линии)
ax.text(4.1, 0.7, 'III', ha='center', va='center', fontsize='xx-large', color='black')

# --- 7. Отображение ---
plt.tight_layout()
plt.savefig("s1l6_3.png", dpi=300, bbox_inches='tight')

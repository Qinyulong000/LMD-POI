import matplotlib.pyplot as plt

# 1. 准备数据 (根据图像估算)
k_values = [5, 10, 15, 20, 25]

# 左侧 Y 轴数据 (NDCG@20) - 蓝色实线
ndcg_values = [45.4, 47.3, 48.95, 47.7, 47.1]

# 右侧 Y 轴数据 (Acc@20) - 红色虚线
acc_values = [73.6, 75.6, 76.3, 75.8, 74.4]

# 2. 创建画布和子图
fig, ax1 = plt.subplots(figsize=(8, 6), dpi=100)

# 设置全局字体大小参数 (以便与原图的大字体匹配)
plt.rcParams.update({'font.size': 18})

# --- 绘制左侧 Y 轴 (NDCG) ---
color_left = 'blue'
# 绘制线条：蓝色，圆点标记，实线
line1, = ax1.plot(k_values, ndcg_values, color=color_left, marker='o', 
                  linestyle='-', linewidth=2, markersize=8, label='NDCG@20')

# 设置左轴标签和刻度样式
ax1.set_xlabel('Values of k', fontsize=24, color='black')
ax1.set_ylabel('Values of NDCG@20 (%)', color=color_left, fontsize=24)
ax1.tick_params(axis='y', labelcolor=color_left, labelsize=20)
ax1.tick_params(axis='x', labelsize=20)
ax1.set_ylim(44, 50)  # 设置左轴范围

# 强制设置 X 轴刻度为 5, 10, 15, 20, 25
ax1.set_xticks(k_values)

# --- 绘制右侧 Y 轴 (Acc) ---
ax2 = ax1.twinx()  # 实例化共享 x 轴的第二个轴

color_right = 'red'
# 绘制线条：红色，三角形标记，虚线
line2, = ax2.plot(k_values, acc_values, color=color_right, marker='^', 
                  linestyle='--', linewidth=2, markersize=8, label='Acc@20')

# 设置右轴标签和刻度样式
ax2.set_ylabel('Values of Acc@20 (%)', color=color_right, fontsize=24)
ax2.tick_params(axis='y', labelcolor=color_right, labelsize=20)
ax2.set_ylim(73, 78)  # 设置右轴范围

# --- 设置图例 ---
# 将两个轴的图例合并在一起
lines = [line1, line2]
labels = [l.get_label() for l in lines]
# loc='lower right' 放在右下角，bbox_to_anchor 微调位置
ax1.legend(lines, labels, loc='lower right', fontsize=20, 
           bbox_to_anchor=(0.98, 0.02), frameon=True)

# 调整布局以防止标签被截断
plt.tight_layout()

# 显示图表
plt.show()
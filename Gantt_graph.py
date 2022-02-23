import matplotlib.pyplot as plt
import numpy as np

#注：此处的Machine和AGV分别表示Machine类列表和AGV类列表
def Gantt(Task):
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 如果要显示中文字体,则在此处设为：SimHei
    plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    M = ['red', 'blue', 'yellow', 'orange', 'green', 'palegoldenrod', 'purple', 'pink', 'Thistle', 'Magenta',
         'SlateBlue', 'RoyalBlue', 'Cyan', 'Aqua', 'floralwhite', 'ghostwhite', 'goldenrod', 'mediumslateblue',
         'navajowhite','navy', 'sandybrown', 'moccasin']
    Job_text=['J'+str(i+1) for i in range(np.shape(Task)[0])]
    #Job_text=np.array(Job_text)
    #0-id	1-所属大任务  2-内部编号  3-允许执行的机器类型编号	4-开始时间 5-结束时间 6-机器编号
    t = 0

    for i in range(np.shape(Task)[0]):
        if Task[i][5] - Task[i][4] != 0:
            plt.barh(Task[i][6], width=np.int(Task[i][5] - Task[i][4]),
                     height=0.8, left=Task[i][4],
                     color=M[np.int(Task[i][1]%22-1)],
                     edgecolor='black')
            plt.text(x=np.float(Task[i][4]+(Task[i][5] - Task[i][4])/2 - 0.1),
                     y=Task[i][6],
                     s="J{}-O{}".format(np.int(Task[i][1]),np.int(Task[i][0])),
                     fontsize=12)
        if Task[i][5]>t:
            t=Task[i][5]
    plt.show()



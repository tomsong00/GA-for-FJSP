import numpy as np
import Machine
import Task
import Parameters
import Optimization
from Gantt_graph import Gantt
class GA_main(object):
    #初始化参数
    parameters=Parameters.Parameters()
    max_generation,population_size, alpha, beta, gobal_best_fitness,length=parameters.parameter_setting()
    #读取数据
    machine = Machine.Machine()
    task=Task.Task()
    task_set=task.load_task(1,1)
    machine_set=machine.load_machine(1,1)
    #print(task_set)
    #print(machine_set)
    print("数据读取完成")
    #print(task_set.shape[0])
    #初始化种群
    optimization=Optimization.Optimization()
    ini_population=optimization.initialization(population_size, task_set)
   # print(ini_population)
   #开始迭代搜索
    gobal_best_fitness, gobal_best_individual= optimization.search_by_iteration(ini_population,max_generation,task_set,machine_set,alpha,beta,length,gobal_best_fitness)
    print("已搜索完毕")
    gobal_best_individual=np.array(gobal_best_individual)
    Gantt(gobal_best_individual)

if __name__ == '__main__':
    ga=GA_main()




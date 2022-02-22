import numpy as np
class Scheudling:
    def __init__(self):
        self
    #给设备安排任务
    def arrange_task_to_machine(self, population, task_set, machine_set):
        population_size = np.shape(population)[0]
        task_size = np.shape(task_set)[0]
        #存储结果
        pop_result=np.zeros([population_size,int(task_size),np.shape(task_set)[1]+1])
        #依次读取种群每一行
        for i in range(population_size):
            #需要分割时间窗，所以增加一个新的机器表，在此操作
            arrange_number = 0
            temp_machine_set=np.array(machine_set)
            machine_size = np.shape(temp_machine_set)[0]
            #初始化一个记录前序任务的表,第一个值记录前序编号
            indi_result = np.zeros([1, int(np.shape(task_set)[1] + 1)])
            processor=np.zeros([task_set[task_size-1][1],2])
            #依次读取每行中的每一列
            for j in range(task_size):
                task_id=np.int(population[i][j])
                #需要根据前序完成转到对应后序任务
                job_id=task_set[int(task_id-1)][1]
                if np.int(processor[job_id-1][0])==0:
                    #找到每一个第一个子任务
                    col_job=task_set[:,1]
                    subtask=np.where(col_job==job_id)
                    subtask=np.array(subtask)
                    task_id=np.int(task_set[subtask[0][0]][0])
                if np.int(processor[job_id-1][0])!=0:
                    task_id=np.int(processor[job_id-1][0]+1)
                #遍历机器表
                for k in range(machine_size):
                    #任务要求类型与机器类型相同
                    if task_set[int(task_id-1)][3]==temp_machine_set[k][1]:
                        #判断时间窗大小
                        duration=np.int(temp_machine_set[k][3]-max(temp_machine_set[k][2],processor[job_id-1][1]))
                        if np.int(task_set[int(task_id-1)][4]+task_set[int(task_id-1)][5])<=duration:
                            #根据前序任务分为两种情况
                            #直接安排
                            if (np.int(processor[job_id-1][1])<=np.int(temp_machine_set[k][2]) and
                                np.int(processor[job_id-1][1]+task_set[int(task_id-1)][4]+task_set[int(task_id-1)][5])<=np.int(temp_machine_set[k][3])):
                                if arrange_number==0:
                                    #创建一个array
                                    temp_indi_result=np.hstack((task_set[int(task_id-1)][:],temp_machine_set[k][0]))
                                    end_time=temp_machine_set[k][2]+temp_indi_result[4]+temp_indi_result[5]
                                    temp_indi_result[5]=end_time
                                    temp_indi_result[4]=temp_machine_set[k][2]
                                    indi_result[0][:]=temp_indi_result
                                    #添加前序记录表
                                    processor[job_id-1][0]=temp_indi_result[0]
                                    processor[job_id-1][1]=temp_indi_result[5]
                                    # 修改机器表
                                    temp_machine_set[k][2]=temp_indi_result[5]
                                else:
                                    #直接在array中继续添加
                                    temp_indi_result=np.hstack((task_set[int(task_id-1),:],temp_machine_set[k][0]))
                                    end_time=temp_machine_set[k][2]+temp_indi_result[4]+temp_indi_result[5]
                                    temp_indi_result[5]=end_time
                                    temp_indi_result[4]=temp_machine_set[k][2]
                                    indi_result=np.vstack((indi_result,temp_indi_result))
                                    #添加前序记录表
                                    processor[job_id-1][0]=temp_indi_result[0]
                                    processor[job_id-1][1]=temp_indi_result[5]
                                    #修改机器表
                                    temp_machine_set[k][2] = temp_indi_result[5]
                                arrange_number = arrange_number + 1
                                break
                            #切割时间窗
                            if [np.int(processor[job_id-1][1])>np.int(temp_machine_set[k][2]) and (np.int(processor[job_id-1][1]+task_set[int(task_id-1)][4]+task_set[int(task_id-1)][5])<=np.int(temp_machine_set[k][3])) and np.int(task_set[int(task_id - 1)][4] + task_set[int(task_id - 1)][5])<=np.int(temp_machine_set[k][3]-processor[job_id-1][1])]:
                                if arrange_number==0:
                                    #创建一个array
                                    temp_indi_result=np.hstack((task_set[int(task_id-1),:],temp_machine_set[k][0]))
                                    end_time=processor[job_id-1][1]+task_set[int(task_id-1)][4]+task_set[int(task_id-1)][5]
                                    temp_indi_result[5]=end_time
                                    temp_indi_result[4]=processor[job_id-1][1]
                                    indi_result[0][:]=temp_indi_result
                                    #添加前序记录表
                                    processor[job_id-1][0]=temp_indi_result[0]
                                    processor[job_id-1][1]=temp_indi_result[5]
                                    #添加新的机器
                                    temp_machine_set=np.vstack((temp_machine_set,temp_machine_set[k,:]))
                                    machine_size = np.shape(temp_machine_set)[0]
                                    temp_machine_set[k][3] = temp_indi_result[4]
                                  #  print(temp_indi_result[4]); print(temp_indi_result[5])
                                    temp_machine_set[machine_size-1][2] = temp_indi_result[5]
                                else:
                                    #直接在array中继续添加
                                    temp_indi_result=np.hstack((task_set[int(task_id-1),:],temp_machine_set[k][0]))
                                    end_time=processor[job_id-1][1]+task_set[int(task_id-1)][4]+task_set[int(task_id-1)][5]
                                    temp_indi_result[5]=end_time
                                    temp_indi_result[4]=processor[job_id-1][1]
                                    indi_result=np.vstack((indi_result,temp_indi_result))
                                    #添加前序记录表
                                    processor[job_id-1][0]=temp_indi_result[0]
                                    processor[job_id-1][1]=temp_indi_result[5]
                                    #添加新的机器
                                    temp_machine_set=np.vstack((temp_machine_set,temp_machine_set[k,:]))
                                    machine_size = np.shape(temp_machine_set)[0]
                                    temp_machine_set[k][3] = temp_indi_result[4]
                                    temp_machine_set[machine_size-1][2] = temp_indi_result[5]
                                  #  print(temp_indi_result[4]);print(temp_indi_result[5])
                                arrange_number = arrange_number + 1
                                break
            pop_result[i][0:np.shape(indi_result)[0]]=indi_result
        return pop_result

    # 计算适应度函数值
    def fitness_calculation(self, scehduling_result, populaiton):
        population_size = np.shape(populaiton)[0]
        fitness = np.zeros(population_size)
        for i in range(population_size):
            comlete_time = scehduling_result[i, :, 5]
            fitness[i] = max(comlete_time)
        return fitness
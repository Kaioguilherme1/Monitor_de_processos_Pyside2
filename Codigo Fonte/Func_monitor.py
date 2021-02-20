import psutil  



def cpu(locacao):
    cpu_freq = psutil.cpu_freq()                       # 0-Freq atual 1-min 2-max
    cpu_percent = psutil.cpu_percent(interval=0.1)     # porcentagem de uso do processador
    cpu_status = (str(int(cpu_freq[0]))+ ' Ghz' , str(int(cpu_freq[1]))+ ' Ghz', str(int(cpu_freq[2]))+ ' Ghz', int(cpu_percent))
    return cpu_status[locacao]
    
def memoria(Locacao):
    memory = psutil.virtual_memory()                   # 0-total bit 1-usavel 2-porcentagem de uso 3-usado 4-livre 
    ram_memory = (memory[0]/1000000,memory[1]/1000000,memory[2],memory[3]/1000000,memory[4]/1000000)
    memo = (str(int(ram_memory[0])) + ' Mb',str(int(ram_memory[1])) + ' Mb',int(ram_memory[2]),str(int(ram_memory[3])) + ' Mb',str(int(ram_memory[4])) + ' Mb')
    return memo[Locacao]
        
    
def disco(Locacao):
    disk_partitions = psutil.disk_partitions()         # 0-local 1-ponto de montagem 2-type 3-opts 4-tamanho max de nome 
    disk_usage = psutil.disk_usage("C://")             # 0-tamanho total byte 1-usado 2-vazio 3-porcentagem de de alocação
    disk_user = (disk_usage[0]/1000000000,disk_usage[1]/1000000000,disk_usage[2]/1000000000,disk_usage[3])
    disk_status = ('%.2f GB' % float(disk_user[0]), '%.2f GB' % float(disk_user[1]), '%.2f GB' % float(disk_user[2]), int(disk_user[3]))
    return disk_status[Locacao]





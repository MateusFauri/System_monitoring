from prettytable import PrettyTable
import psutil

print("----Networks----")

network_table = PrettyTable(["NETWORK","STATUS","SPEED"])

for key in  psutil.net_if_stats().keys():
    name = key
    up = "UP" if psutil.net_if_stats()[key].isup else "DOWN"
    speed = psutil.net_if_stats()[key].speed
    network_table.add_row([name,up,speed])

print(network_table)

print("----Memory----")

memory_table = PrettyTable(["TOTAL","USED","AVAILABLE","PERCETAGE"])

vm = psutil.virtual_memory()
memory_table.add_row([
    vm.total,
    vm.used,
    vm.available,
    vm.percent 
])
print(memory_table)

print("----Processes----")

process_table =  PrettyTable(["PID","PNAME","STATUS","CPU","NUM THREADS"])

for process in psutil.pids():

    try:
        p = psutil.Process(process)
        process_table.add_row([
            str(process),
            p.name(),
            p.status(),
            str(p.cpu_percent()) + "%",
            p.num_threads()
        ])

    except Exception as e:
        pass

print(process_table)

# Simulates a 2-thread SMT, 4-wide issue superscalar processor.

import m5
from m5.objects import *
from m5.util import fatal

# Set up the system
system = System()
system.clk_domain = SrcClockDomain(clock='1GHz', voltage_domain=VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Configure the O3CPU for 2-way SMT
system.cpu = O3CPU(cpu_id=0, width=4, numThreads=2)

# Create a simple cache hierarchy (shared by the threads)
system.cpu.icache = L1_ICache(size='32kB')
system.cpu.dcache = L1_DCache(size='32kB')
system.cpu.icache.connectCPU(system.cpu)
system.cpu.dcache.connectCPU(system.cpu)
system.l2bus = L2XBar()
system.cpu.icache.connectBus(system.l2bus)
system.cpu.dcache.connectBus(system.l2bus)
system.l2cache = L2Cache(size='256kB')
system.l2cache.connectCPUSideBus(system.l2bus)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus)

# Create a memory controller
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.port = system.membus.mem_side_ports
system.system_port = system.membus.cpu_side_ports

# Define the two processes to run concurrently
process1 = Process(pid=100)
process1.cmd = ['workload']
process2 = Process(pid=101)
process2.cmd = ['workload2']

system.cpu.workload = [process1, process2]
system.cpu.createThreads()

# Instantiate and run the simulation
root = Root(full_system=False, system=system)
m5.instantiate()

print("**** REAL SIMULATION ****")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")

# Simulates a 4-wide issue, out-of-order superscalar processor.

import m5
from m5.objects import *
from m5.util import fatal
import argparse

# Set up the system
system = System()
system.clk_domain = SrcClockDomain(clock='1GHz', voltage_domain=VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Use O3CPU for an out-of-order, superscalar model
# Configure the issue width to 4
system.cpu = O3CPU(cpu_id=0, width=4)

# Create a simple cache hierarchy
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

# Set up the process to run
parser = argparse.ArgumentParser()
parser.add_argument("--cmd", type=str, required=True)
options = parser.parse_args()

process = Process()
process.cmd = [options.cmd]
system.cpu.workload = process
system.cpu.createThreads()

# Instantiate and run the simulation
root = Root(full_system=False, system=system)
m5.instantiate()

print("**** REAL SIMULATION ****")
exit_event = m5.simulate()
print(f"Exiting @ tick {m5.curTick()} because {exit_event.getCause()}")

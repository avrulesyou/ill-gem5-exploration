# Extends the simple pipeline with a branch predictor.

import m5
from m5.objects import *
from m5.util import fatal
import argparse

# Set up the system
system = System()
system.clk_domain = SrcClockDomain(clock='1GHz', voltage_domain=VoltageDomain())
system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')]

# Use the MinorCPU for an in-order pipeline model
system.cpu = MinorCPU(cpu_id=0)

# ADD A BRANCH PREDICTOR
system.cpu.branchPred = BiModeBP()

# Create a memory bus and controller
system.membus = SystemXBar()
system.mem_ctrl = MemCtrl()
system.mem_ctrl.dram = DDR3_1600_8x8()
system.mem_ctrl.port = system.membus.mem_side_ports

# Connect CPU ports to the memory bus
system.cpu.icache_port = system.membus.cpu_side_ports
system.cpu.dcache_port = system.membus.cpu_side_ports
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

Gem5 Scripts for Exploring Instruction-Level Parallelism (ILP)
Author: Abhishek Vishwakarma

Overview
This repository contains the source code and gem5 simulation scripts used for the practical exploration section of "Assignment 4: Exploring Instruction-Level Parallelism (ILP) in Modern Processors". The scripts are designed to demonstrate the performance impact of fundamental ILP techniques, including pipelining, branch prediction, superscalar execution, and Simultaneous Multithreading (SMT).

Contents
This repository includes the following files:

workload.c: A simple C program with a loop used as the primary benchmark for single-threaded simulations.

workload2.c: A slightly modified C program used as the second benchmark for the SMT simulation.

simple_pipeline.py: A gem5 script to simulate a basic in-order, pipelined processor using the MinorCPU model.

pipeline_with_bp.py: A gem5 script that adds a BiModeBP branch predictor to the in-order pipeline.

superscalar.py: A gem5 script to simulate a 4-wide issue, out-of-order superscalar processor using the O3CPU model.

smt.py: A gem5 script that configures the O3CPU for 2-way SMT and runs two workloads concurrently.

How to Use
1. Prerequisites
A working gem5 development environment, compiled for the X86 architecture (build/X86/gem5.opt).

A C compiler, such as gcc, to compile the workloads.

2. Compile the Workloads
Before running the simulations, you must compile the C programs into static executables.

gcc -static workload.c -o workload
gcc -static workload2.c -o workload2

3. Run the Simulations
Execute the desired simulation using the gem5 executable. The scripts are written to accept the workload binary as a command-line argument.

Example Commands:

# Run the simple in-order pipeline simulation
./build/X86/gem5.opt simple_pipeline.py --cmd=workload

# Run the pipeline with branch prediction
./build/X86/gem5.opt pipeline_with_bp.py --cmd=workload

# Run the superscalar simulation
./build/X86/gem5.opt superscalar.py --cmd=workload

# Run the SMT simulation (loads both workloads automatically)
./build/X86/gem5.opt smt.py

After each run, performance statistics can be found in the m5out/stats.txt file.

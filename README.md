# 🚀 Gem5 Scripts for Exploring Instruction-Level Parallelism (ILP)

[![Gem5](https://img.shields.io/badge/Gem5-Simulation-blue?style=for-the-badge&logo=gem5)](https://www.gem5.org/)
[![X86](https://img.shields.io/badge/Architecture-X86-red?style=for-the-badge&logo=intel)](https://www.intel.com/)
[![C](https://img.shields.io/badge/Language-C-green?style=for-the-badge&logo=c)](<https://en.wikipedia.org/wiki/C_(programming_language)>)
[![Python](https://img.shields.io/badge/Scripting-Python-yellow?style=for-the-badge&logo=python)](https://python.org/)

> **Author:** [Abhishek Vishwakarma](https://github.com/abhishekvishwakarma)  
> **Assignment:** Exploring Instruction-Level Parallelism (ILP) in Modern Processors

---

## 📋 Table of Contents

- [📝 Overview](#-overview)
- [🎯 Features](#-features)
- [📁 Repository Contents](#-repository-contents)
- [🚀 Quick Start](#-quick-start)
- [📊 Performance Analysis](#-performance-analysis)
- [🔧 Prerequisites](#-prerequisites)
- [📖 Usage Guide](#-usage-guide)
- [📈 Expected Results](#-expected-results)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📝 Overview

This repository contains comprehensive Gem5 simulation scripts designed to explore and demonstrate the performance impact of fundamental **Instruction-Level Parallelism (ILP)** techniques in modern processors. The project serves as a practical implementation for understanding how different architectural features affect processor performance.

### 🎯 Key Learning Objectives

- Understanding the impact of **pipelining** on processor performance
- Analyzing the effectiveness of **branch prediction** mechanisms
- Exploring **superscalar execution** capabilities
- Investigating **Simultaneous Multithreading (SMT)** performance benefits

---

## 🎯 Features

- 🔄 **Progressive Complexity**: Scripts range from basic in-order pipelines to advanced out-of-order superscalar processors
- 📊 **Comprehensive Analysis**: Detailed performance metrics and statistics
- 🎛️ **Configurable Parameters**: Easy-to-modify simulation parameters
- 📈 **Comparative Studies**: Side-by-side performance comparisons
- 🧪 **Multiple Workloads**: Different benchmark programs for varied analysis

---

## 📁 Repository Contents

| File                                           | Description                                        | CPU Model           | Key Features                 |
| ---------------------------------------------- | -------------------------------------------------- | ------------------- | ---------------------------- |
| [`workload.c`](./workload.c)                   | Primary benchmark program with computational loops | -                   | Single-threaded workload     |
| [`workload2.c`](./workload2.c)                 | Secondary benchmark for SMT analysis               | -                   | Alternative workload pattern |
| [`simple_pipeline.py`](./simple_pipeline.py)   | Basic in-order pipelined processor                 | MinorCPU            | 5-stage pipeline             |
| [`pipeline_with_bp.py`](./pipeline_with_bp.py) | Pipeline with branch prediction                    | MinorCPU + BiModeBP | Enhanced branch handling     |
| [`superscalar.py`](./superscalar.py)           | 4-wide issue out-of-order processor                | O3CPU               | Superscalar execution        |
| [`smt.py`](./smt.py)                           | 2-way SMT configuration                            | O3CPU               | Simultaneous multithreading  |

---

## 🚀 Quick Start

### 1. 🔧 Prerequisites

Ensure you have the following installed:

- **Gem5 Development Environment** (compiled for X86 architecture)
- **GCC Compiler** for building workloads
- **Python 3.x** for running simulation scripts

```bash
# Verify Gem5 installation
ls build/X86/gem5.opt

# Check GCC version
gcc --version

# Verify Python installation
python3 --version
```

### 2. 📦 Compile Workloads

```bash
# Compile primary workload
gcc -static workload.c -o workload

# Compile secondary workload
gcc -static workload2.c -o workload2

# Verify compilation
ls -la workload*
```

### 3. 🏃‍♂️ Run Simulations

```bash
# Basic pipeline simulation
./build/X86/gem5.opt simple_pipeline.py --cmd=workload

# Pipeline with branch prediction
./build/X86/gem5.opt pipeline_with_bp.py --cmd=workload

# Superscalar execution
./build/X86/gem5.opt superscalar.py --cmd=workload

# Simultaneous Multithreading
./build/X86/gem5.opt smt.py
```

---

## 📊 Performance Analysis

### 📈 Key Metrics

After each simulation, analyze the following metrics in `m5out/stats.txt`:

- **Cycles per Instruction (CPI)**
- **Branch Prediction Accuracy**
- **Cache Hit Rates**
- **Instruction Throughput**
- **Memory Bandwidth Utilization**

### 📊 Expected Performance Trends

| Configuration          | Expected CPI | Branch Accuracy | Notes                    |
| ---------------------- | ------------ | --------------- | ------------------------ |
| Simple Pipeline        | ~1.2-1.5     | N/A             | Baseline performance     |
| With Branch Prediction | ~1.0-1.2     | >90%            | Improved branch handling |
| Superscalar            | ~0.3-0.8     | >95%            | Out-of-order execution   |
| SMT                    | ~0.4-1.0     | >95%            | Thread-level parallelism |

---

## 📖 Usage Guide

### 🔍 Detailed Analysis Steps

1. **Run Baseline Simulation**

   ```bash
   ./build/X86/gem5.opt simple_pipeline.py --cmd=workload
   ```

2. **Compare with Branch Prediction**

   ```bash
   ./build/X86/gem5.opt pipeline_with_bp.py --cmd=workload
   ```

3. **Analyze Superscalar Benefits**

   ```bash
   ./build/X86/gem5.opt superscalar.py --cmd=workload
   ```

4. **Evaluate SMT Performance**
   ```bash
   ./build/X86/gem5.opt smt.py
   ```

### 📋 Analysis Checklist

- [ ] Compare CPI across different configurations
- [ ] Analyze branch prediction effectiveness
- [ ] Evaluate superscalar speedup
- [ ] Measure SMT performance gains
- [ ] Document performance bottlenecks

---

## 📈 Expected Results

### 🎯 Performance Improvements

- **Pipeline**: 20-30% improvement over non-pipelined
- **Branch Prediction**: 10-20% additional improvement
- **Superscalar**: 2-4x speedup depending on workload
- **SMT**: 1.5-2x improvement with 2 threads

### 📊 Sample Output

```
Simulation Statistics:
- Total Cycles: 1,234,567
- Instructions: 987,654
- CPI: 1.25
- Branch Prediction Accuracy: 94.2%
- Cache Hit Rate: 89.7%
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### 🔧 Development Setup

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

This project is part of academic coursework and is intended for educational purposes. Please ensure compliance with your institution's academic integrity policies.

---

<div align="center">

**Made with ❤️ by [Abhishek Vishwakarma](https://github.com/abhishekvishwakarma)**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github)](https://github.com/abhishekvishwakarma)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/abhishekvishwakarma)

</div>

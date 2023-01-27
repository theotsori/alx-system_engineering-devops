<h1>Processes and signals</h1>
<img src="https://www.cyberciti.biz/media/new/faq/2007/08/Linux-and-UNIX-Find-out-or-determine-if-process-PID-is-running-command.png">
<h2>What is a PID</h2>
<p>In Linux, a Process ID (PID) is a unique numerical identifier assigned to every process that is running on the system. Each process has a unique PID, which is used to identify and control the process.</p>
<p>PIDs are assigned by the kernel when a process is created and can be used to track, monitor, and manage processes. For example, the ps command can be used to display information about running processes and their corresponding PIDs, and the kill command can be used to send signals to processes based on their PIDs.</p>
You can also use the built-in variable $$ in a shell script to get the PID of the script itself.

The operating system uses the PID to track a process, it uses the same number to identify the process in memory, in the process table and also in system calls to refer to the process. The kernel uses the PID to keep track of the process's state, its memory usage, and its resources.

In summary, PID is a unique identification number that is assigned to every process running on a Linux system, and it is used to track, monitor and manage processes.
<h2>What is a process</h2>
<p>A process is a series of actions or steps taken in order to achieve a specific result or outcome. It can refer to a variety of different things, depending on the context. In general, a process is a systematic and organized way of achieving a specific goal or objective.
In terms of industrial control systems, a process refers to a specific industrial operation or production process that is being controlled or monitored by a process control system. It could be anything from a manufacturing process to a chemical reaction, a physical change, or a biological process. The process variable is the measured output of the process which can be temperature, pressure, flow, level, etc. The goal of the process control system is to control the process variable to match a desired setpoint or target.</p>

# Day 4 Task: Basic Linux Shell Scripting for DevOps Engineers.

## What is Kernel

The kernel is a computer program that is the core of a computer’s operating system, with complete control over everything in the system.

## What is Shell

A shell is special user program which provide an interface to user to use operating system services. Shell accept human readable commands from user and convert them into something which kernel can understand. It is a command language interpreter that execute commands read from input devices such as keyboards or from files. The shell gets started when the user logs in or start the terminal.

## What is Linux Shell Scripting?

A shell script is a computer program designed to be run by a linux shell, a command-line interpreter. The various dialects of shell scripts are considered to be scripting languages. Typical operations performed by shell scripts include file manipulation, program execution, and printing text.

**Tasks**

- Explain in your own words and examples, what is Shell Scripting for DevOps.
    Shell scripting for DevOps means writing a set of command-line instructions inside a script file to automate tasks.
    In DevOps, many tasks are repeated often, such as creating files, checking system information, installing packages, running tests, building applications, deploying code, checking logs, or restarting services. Instead of typing the same commands manually every time, we can write them once in a shell script and execute the script whenever needed.
    Shell scripts are useful because they save time, reduce manual errors, and make processes more consistent.

- What is `#!/bin/bash?` can we write `#!/bin/sh` as well?
    `#!/bin/bash` is called a shebang (#!). It tells the operating system to run the script using the Bash shell.
    Yes, we can also use `#!/bin/sh`, but `/bin/sh` may use a different and simpler shell depending on the system.
    For simple scripts, both can work. If we use Bash-spe1cific features, `#!/bin/bash` is the better option.

- Write a Shell Script which prints `I will complete #90DaysOofDevOps challenge`
    challenge1.sh
- Write a Shell Script to take user input, input from arguments and print the variables.
    challenge2.sh
- Write an Example of If else in Shell Scripting by comparing 2 numbers
    challenge3.sh
Was it difficult?

- Post about it on LinkedIn and Let me know :)

Article Reference: [Click here to read basic Linux Shell Scripting](https://devopscube.com/linux-shell-scripting-for-devops/)

YouTube Video: [EASIEST Shell Scripting Tutorial for DevOps Engineers](https://www.youtube.com/watch?v=_-D6gkRj7xc&list=PLlfy9GnSVerQr-Se9JRE_tZJk3OUoHCkh&index=3)

[← Previous Day](../day03/README.md) | [Next Day →](../day05/README.md)

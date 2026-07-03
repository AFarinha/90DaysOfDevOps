#!/bin/bash

check_disk() {
    df -h /
}

check_memory() {
    free -h
}

check_disk
check_memory


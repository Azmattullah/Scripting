#!/bin/bash


# Conditional Statements

# 1. if, else, elif:

num=100

if [ $num -gt 10 ]; then
    echo "Number is greater than 10"
elif [ $num -eq 10 ]; then
    echo "Number is equal to 10"
else
    echo "Number is less than 10"
fi
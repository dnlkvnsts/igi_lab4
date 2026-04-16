"""
The main program

Lab 4. Working with files, classes, serializers, regular expressions, and
standard libraries

Version: 1

Developer: Danilkova Anastasia Alexandrovna

Date: 13.04.2026
"""

import tasks.Task1.task1 as t1
import tasks.Task2.task2 as t2
import tasks.Task3.task3 as t3
import tasks.Task4.task4 as t4
import tasks.Task5.task5 as t5
import tasks.Task6.task6A as t6A
import tasks.Task6.task6B as t6B

def main():
    print("Program\n")
    while True: 
        print("\nMenu")
        print("1. Task 1")
        print("2. Task 2")
        print("3. Task 3")
        print("4. Task 4")
        print("5. Task 5")
        print("6A. Task 6A")
        print("6B. Task 6B")
        print("0. Exit\n")
    
        choice = input("Choose one option\n")
        
        if choice == "1":
            t1.run_task1()
        elif choice == "2":
            t2.run_task2()
        elif choice == "3":
            t3.run_task3()
        elif choice == "4":
            t4.run_task4()
        elif choice == "5":
            t5.run_task5()
        elif choice == "6A":
            t6A.run_task6A()
        elif choice == "6B":
            t6B.run_task6B()
        elif choice == "0":
            break
        else:
            print("Invalid input.Choose right option from menu")
    
    

if __name__ == "__main__":
    main()
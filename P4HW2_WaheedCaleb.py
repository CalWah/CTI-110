#Caleb Waheed
#4/10/2024
#P4HW2
#Make a code for employee's job hours/pay
Total_emp = 0
Total_over = 0
Total_reg = 0 
Total_gros = 0


name_1 = input("Enter employee's name or 'Done' to terminate: ")
while name_1 != "Done":
    num_1 = float(input(f"How many hours did of {name_1} work?: "))
    pay_1 = float(input(f"What is {name_1} pay rate: "))

    if num_1 > 40:
        Norm_hours = (40)
        Overtime_hours = (num_1-40)
    else:
        Norm_hours = (num_1)
        Overtime_hours = (0)
    reg_pay = (pay_1 * Norm_hours)
    ot_pay = (Overtime_hours  * pay_1 * 1.5)
    gros_pay = (reg_pay + ot_pay)

    print("----------------------------------------------")

    print(f"{'Employee name':^20}{name_1}")

    print("Hours Worked    Pay Rate    Overtime   OverTime Pay     RegHour Pay     Gross Pay")
    print("------------------------------------------------------------------------------")
    print(f"{num_1}           ${pay_1:.2f}         {Overtime_hours}        ${ot_pay:.2f}          ${reg_pay:.2f}           ${gros_pay:.2f}")
    name_1 = input("Enter employee's name or 'Done' to terminate: ")
    Total_emp += 1
    Total_over += ot_pay
    Total_reg += reg_pay
    Total_gros += gros_pay
print(f"Total number of employees entred:{Total_emp}")
print(f"Total amount paid for overtime:{Total_over}")
print(f"Total amount paid for regular hours:{Total_reg}")
print(f"Total amount paid in gross:{Total_gros}")

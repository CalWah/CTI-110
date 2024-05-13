#Caleb Waheed
#3/21/2024
#P3HW2
#Make a code for employee's job hours/pay

name_1 = input("Enter employee's name: ")
num_1 = float(input("Enter number of hours worked: "))
pay_1 = float(input("Enter employee's pay rate: "))

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

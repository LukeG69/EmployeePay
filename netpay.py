import employeeclass as m
import payrolldedectionclass as d

def main():
    name = 'Jimmy Smith'
    idnum = '58475'
    dep = 'Information Systems'
    title = 'Developer'
    month_salary = 6800

    emp = m.Employee(name, idnum, dep, title, month_salary)
    return emp

def enter_deductions():
    deduction1 = d.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
    deduction2 = d.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
    deduction3 = d.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
    deduction4 = d.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
    deduction5 = d.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58745)
    deductions = [deduction1, deduction2, deduction3, deduction4, deduction5]

    return deductions

def show_NetPay(employee):

    if m.Employee.get_num == d.PayrollDeduction.get_num:
        deduct = sum(d.__amt)
        print('*** Employee Pay ***')
        print('Name: ', m.get_name())
        print('ID Number: ', m.get_id())
        print('Department: ', m.get_dep())
        print('Gross Pay: $', m.get_salary())
        print('Net Pay: $', format(m.get_salary() - enter_deductions()))

main()
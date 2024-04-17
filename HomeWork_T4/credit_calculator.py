import tkinter as tk


def calculate_payment():
    principal = float(entry_principal.get())
    interest_rate = float(entry_interest.get()) / 100
    months = int(entry_months.get())

    monthly_interest = interest_rate / 12
    monthly_payment = principal * (monthly_interest * (1 + monthly_interest) ** months) / (
                (1 + monthly_interest) ** months - 1)
    total_payment = monthly_payment * months
    total_interest = total_payment - principal

    label_monthly_payment.config(text=f"Ежемесячный платеж: {monthly_payment:.2f}")
    label_total_payment.config(text=f"Общая сумма выплат: {total_payment:.2f}")
    label_total_interest.config(text=f"Переплата: {total_interest:.2f}")


root = tk.Tk()
root.title("Кредитный калькулятор")
root.geometry("500x500+500+300") #размер окна м его положение
root.resizable(False, False) #растягивание окна по оси х/у

label_principal = tk.Label(root, text="Общая сумма кредита:")
label_principal.pack()

entry_principal = tk.Entry(root)
entry_principal.pack()

label_interest = tk.Label(root, text="Процентная ставка (%):")
label_interest.pack()

entry_interest = tk.Entry(root)
entry_interest.pack()

label_months = tk.Label(root, text="Срок кредита (месяцы):")
label_months.pack()

entry_months = tk.Entry(root)
entry_months.pack()

button_calculate = tk.Button(root, text="Рассчитать", command=calculate_payment)
button_calculate.pack(padx=30, pady=30, ipadx=10, ipady=10)


label_monthly_payment = tk.Label(root, text="")
label_monthly_payment.pack()

label_total_payment = tk.Label(root, text="")
label_total_payment.pack()

label_total_interest = tk.Label(root, text="")
label_total_interest.pack()

root.mainloop()
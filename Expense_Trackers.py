from ex import Expense
import calendar
import datetime


def main():
    print("run🏃 ho rha h ki nhi ")
    expense_file_path = "expense.csv"
    budget = 3000000



    expense =expense_kitna_hua()


    file_m_save_kro(expense ,expense_file_path)


    summarize_expenses(expense_file_path,budget)








def expense_kitna_hua():
    print("kitna kharcha kiya h")
    expense_name =input("khha krhcha kiya bolo  : ")
    expense_amount =float(input("kitne paise yaha p udaye h "))
    print(f"expense name is {expense_name}, {expense_amount}")


    expense_categories = [
        "🌮 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]


    while True:
        print("kis category m kharcha kr rhe ho batao :   ")
        for i , category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")

        value_range= f"[1-{len(expense_categories)}]"
        selcetd_index =int(input(f"bhai catergory bata do:: {value_range}"))-1

        if selcetd_index in range(len(expense_categories)):
            selcetd_catergory=expense_categories[selcetd_index]
            print(selcetd_catergory)

            
            new_expense=Expense(name =expense_name,category=selcetd_catergory,amount=expense_amount) 

            return new_expense


        else:
            print("invalid category")
        break

def file_m_save_kro(expense :Expense,expense_file_path):

    print(f"khrach file m save krna h : {expense} to {expense_file_path}")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path,budget):
    print("summary of user expenses:")
    expenses =[]
    with open(expense_file_path,'r') as f:
        lines =f.readlines()
        for line in lines:
            #print(line)
            expense_name ,expense_amount ,expense_category =line.strip().split(",")
            print(f"{expense_name} {expense_amount} {expense_category}")
            line_expense=Expense(name=expense_name,amount=float(expense_amount),category=expense_category)
            #print(line_expense)
            expenses.append(line_expense)
            #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key=expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    #print(amount_by_category)
    print("y apka category wise khracha h ")
    for key ,amount in amount_by_category.items():
        print(f"{key} : {amount}")


    total_spent = sum([x.amount for x in expenses])
    print(f"itna khracha kr leye ho bhai : {total_spent:.2f}")


    remaining_budget = budget - (total_spent)
    print(f"remaining budget : {remaining_budget:2f}")


    now=datetime.datetime.now()
    days_in_month=calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print("reaming days is month m bache h :",remaining_days)


    daily_budget = remaining_budget/remaining_days
    print("daily budget : ",daily_budget)
   

   













    















if __name__ == "__main__":
    main()
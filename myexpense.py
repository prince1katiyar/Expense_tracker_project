from expense import Expense
import calendar
import time
import datetime 


def main():
    print("it is runnig🚐  or not ")
    expense_file_path = "expenses.csv"
    budget = 20000
    

    # get user input
    #expense = get_user_expense()
    expense = expense_kitna_hua()
    #print(expense)



    # write expenses to the file 
    file_m_save_kro(expense,expense_file_path)



    summarize_expenses(expense_file_path,budget)



# read file and summarize expenses
#def get_user_expense():
def expense_kitna_hua():
    print("kitna khracha kiya h")
    expense_name = input("khha krhcha kiya bolo  : ")
    expense_amount  = float(input("kitna paise udhaya batao : "))
    print(f"expense name is {expense_name}, {expense_amount}")

    expense_categories = [
        "🌮 Food",
        "🏠 Home",
        "💼 Work",
        "🎉 Fun",
        "✨ Misc",
    ]
    while True:
        print("kis category m khracha kiya bolo  :")
        for i ,category_name in enumerate(expense_categories):
            print(f"{i+1}. {category_name}")
        # break
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f" category ka number to batao bhai  {value_range} :")) - 1
        # break

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            print(selected_category)
            new_expense = Expense(name=expense_name , category=selected_category,
                                   amount=expense_amount)
                                  
    
            return new_expense
        else:
            print("invalid category")

        #break 

        
        

def file_m_save_kro(expense:Expense,expense_file_path):
    print(f"khrcha save krta h :{expense} to {expense_file_path} ")
    with open(expense_file_path,"a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


    

def summarize_expenses(expense_file_path ,budget):
    print("summarizing user expenses")
    expenses :list[Expense]= []
    with open(expense_file_path,'r') as f:
        lines = f.readlines()
        for line in lines:
            #print(line)
            #stripped_line = line.strip()
            expense_name,expense_amount ,expense_category = line.strip().split(",")
            print(expense_name,expense_amount,expense_category)
            line_expense = Expense( name =expense_name ,amount =float(expense_amount) ,category=expense_category)
           # print(line_expense)
            expenses.append(line_expense)
        #print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key] +=expense.amount
        else:
            amount_by_category[key] = expense.amount  
    #print(amount_by_category) 
    print("Expense by category :")
    for key , amount in amount_by_category.items():
        print(f"{key} : ${amount:.2f}") 


    total_spent =sum([ x.amount for x in expenses])  
    print(f"you have spent : ${total_spent:.2f}")

#     remaining_budget = budget - total_spent
#     print(f"your remaining budget : ${remaining_budget:.2f}")
    remaining_budget = budget- total_spent
    print(f" budget left :${remaining_budget:.2f}")


    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year,now.month)[1]
    remaining_days = days_in_month - now.day
    print("remaining days in current month : ",remaining_days)

    daily_budget = remaining_budget/remaining_days
    print(red(f"your daily budget : ${daily_budget:.2f}"))


# def green(text):
#     return f"\033[92m{text}\033[0m"
def red(text):
    return f"\033[91m{text}\033[0m"

    





            

 









if __name__ == "__main__":
    main()



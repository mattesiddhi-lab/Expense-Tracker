# Create a personal finance tracking application that allows users to record, categorize, and analyze their expenses. The application should provide insights into spending habits through charts and summaries.
# Requirements
# • Add/edit/delete expenses
# • Categories
# • Monthly summaries
# • Expense visualizations
# • Budget limits

import pandas as pd
import matplotlib.pyplot as plt

material_list = []
material_expense = []
category_choosed = []
categories = ["Food" , "Entertainment" , "Travelling" , "Subscription" , "Maintenance" , "Investment"]
bgt = 50000


def material_add(choose): # Purchased item to add in the list
    item = input("Enter the item name: ")
    price = int(input("Enter the price of the item:"))
    material_list.append(item)
    material_expense.append(price)
    category_choosed.append(choose)
    return material_list , material_expense , category_choosed

def delete():      # Deleting characters
    delete_item = input("Delete item name: ")
    for i , j , k in zip(material_list, material_expense , category_choosed):
        if i == delete_item:
            material_list.remove(delete_item)
            material_expense.remove(j)
            category_choosed.remove(k)
    return material_list, material_expense , category_choosed

def edit(choose):
    editing = input("Replacing item name: ")
    new_item = input("Enter new item: ")
    new_price = int(input("Enter New value: "))
    idx = material_list.index(editing)
    for i , j , k  in zip(material_list, material_expense , category_choosed):
        if i == editing:
            material_list.remove(i)
            material_expense.remove(j)
            category_choosed.remove(k)
            
            material_list.insert(idx , new_item)
            material_expense.insert(idx, new_price )
            category_choosed.insert(idx,choose)
            return material_list, material_expense , category_choosed

def call():
    print ("1. Food\n2. Entertainment\n3. Travelling\n4. Subscription\n5. Maintenance\n6. Investment")
    num = int(input("Enter the number: ")) - 1
    choose = categories[num]
    # category_choosed.append(choose)
    print (f"*"*10,{choose},"*"*10)
    return choose
    
while True:
    print ("Do u want to...")
    print ("1. Add\n2. Edit\n3. Delete\n4. Save\n5. Return\n6. Exit")
    number = int(input("Enter the number: "))
    try:
        
        if number == 1:
            print (material_add(call()))
        elif number == 2:
            print (edit(call()))
        elif number == 3:
            print (delete())
        elif number == 5:
            call()
        elif number == 4:
            try:
                df = pd.DataFrame({
                    "Category":category_choosed,
                    "Item Name" : material_list,
                    "Price" : material_expense
                })
                df.to_csv("expense_tracker.csv",index=False)
                print ("Saved Sucessfully!!!")
            except Exception as e:
                print (e)
        elif number == 6:
            break
    except Exception as e:
        print ("\n",e,"\n")
        continue


def budget():
    total_fo_ex = 0
    total_ent_ex = 0
    total_tr_ex = 0
    total_ma_ex = 0
    total_sub_ex = 0
    total_in_ex = 0

    read = pd.read_csv("expense_tracker.csv")
    column = read["Category"]
    price = read["Price"]
    n = 0
    for i in column:
        if i == "Food":
            total_fo_ex += price[n]  

        elif i == "Entertainment":
            total_ent_ex += price 
            
        elif i == "Travelling":
            total_tr_ex += price 
            
        elif i == "Maintenance":
            total_ma_ex += price 
            
        elif i == "Subscription":
            total_sub_ex += price 
            
        elif i == "Investment":
            total_in_ex += price 
            
        else:
            pass
        n += 1
    print (f"Total expense of Food :{total_fo_ex}")
    print (f"Total expense of Entertainment:{total_ent_ex}")
    print (f"Total expense of Travelling:{total_tr_ex}")
    print (f"Total expense of Maintenance:{total_ma_ex}")
    print (f"Total expense of Maintenance:{total_ma_ex}")
    print (f"Total expense of Subscription:{total_sub_ex}")
    print (f"Total expense of Investment:{total_in_ex}")

    calculate = read.groupby("Price").sum()
    print (f"Total Expense:{calculate}")

    # 1. Correct Grouping: Group by Category and sum up the Prices
    calculate = read.groupby("Category")["Price"].sum()
    
    # 2. Get the Grand Total as a single number for the bar chart
    grand_total = read["Price"].sum()

    print(f"\nCategorical Breakdown:\n{calculate}")
    print(f"Total Expense: {grand_total}")
    
    fig , (ax1 , ax2) = plt.subplots(1 , 2 , figsize=(12 , 5))

    calculate.plot(kind='pie',autopct='%1.1f%%' , ax=ax1 , title="spending Layout by Category")
    ax1.set_ylabel('')

    ax2.bar(['Total Spent','Budget Limit'], [grand_total , bgt], color=['red','green'])
    ax2.set_title("Overall Expenditut\res vs Threshold")
    ax2.set_ylabel("Amount")

    plt.tight_layout()
    plt.show()
budget()
# py expense_tracker.py

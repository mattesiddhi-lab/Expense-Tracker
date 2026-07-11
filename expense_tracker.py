import pandas as pd
import matplotlib.pyplot as plt

material_list = []
material_expense = []
category_choosed = []
categories = ["Food" , "Entertainment" , "Travelling" , "Subscription" , "Maintenance" , "Investment"]
bgt = 50000

def material_add(choose):
    item = input("Enter the item name: ")
    price = int(input("Enter the price of the item: "))
    material_list.append(item)
    material_expense.append(price)
    category_choosed.append(choose)
    return material_list, material_expense, category_choosed

def delete():
    delete_item = input("Delete item name: ")
    # Find all indexes matching the item name
    indices = [i for i, x in enumerate(material_list) if x == delete_item]
    
    if not indices:
        print("Item not found.")
        return material_list, material_expense, category_choosed
        
    # Delete backwards so indices don't shift during removal
    for idx in reversed(indices):
        material_list.pop(idx)
        material_expense.pop(idx)
        category_choosed.pop(idx)
    print(f"Deleted all occurrences of {delete_item}.")
    return material_list, material_expense, category_choosed

def edit(choose):
    editing = input("Replacing item name: ")
    if editing not in material_list:
        print("Item not found.")
        return material_list, material_expense, category_choosed
        
    new_item = input("Enter new item: ")
    new_price = int(input("Enter New value: "))
    
    # Track the exact position to update
    idx = material_list.index(editing)
    material_list[idx] = new_item
    material_expense[idx] = new_price
    category_choosed[idx] = choose
    
    return material_list, material_expense, category_choosed

def call():
    print ("1. Food\n2. Entertainment\n3. Travelling\n4. Subscription\n5. Maintenance\n6. Investment")
    num = int(input("Enter the number: ")) - 1
    choose = categories[num]
    print (f"*"*10, {choose}, f"*"*10)
    return choose
    
while True:
    print ("\nDo u want to...")
    print ("1. Add\n2. Edit\n3. Delete\n4. Save\n5. View Categories\n6. Exit Tracker & View Visuals")
    try:
        number = int(input("Enter the number: "))
        if number == 1:
            material_add(call())
        elif number == 2:
            edit(call())
        elif number == 3:
            delete()
        elif number == 5:
            call()
        elif number == 4:
            df = pd.DataFrame({
                "Category": category_choosed,
                "Item Name": material_list,
                "Price": material_expense
            })
            df.to_csv("expense_tracker.csv", index=False)
            print ("Saved Successfully!!!")
        elif number == 6:
            break
    except Exception as e:
        print ("\nAn error occurred:", e, "\n")
        continue

def budget():
    try:
        read = pd.read_csv("expense_tracker.csv")
    except FileNotFoundError:
        print("No saved data found. Please add and save expenses first.")
        return

    # Clean Pandas aggregation (Replaces the broken loop logic)
    calculate = read.groupby("Category")["Price"].sum()
    grand_total = read["Price"].sum()

    print("\n" + "="*30)
    print("   CATEGORICAL BREAKDOWN")
    print("="*30)
    for cat in categories:
        amt = calculate.get(cat, 0)
        print(f"Total expense of {cat}: {amt}")
        
    print("-"*30)
    print(f"Total Expense: {grand_total}")
    print(f"Remaining Budget: {bgt - grand_total}")
    print("="*30)
    
    # Matplotlib plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    if grand_total > 0:
        calculate.plot(kind='pie', autopct='%1.1f%%', ax=ax1, title="Spending Layout by Category")
    else:
        ax1.text(0.5, 0.5, 'No Data', ha='center', va='center')
    ax1.set_ylabel('')

    ax2.bar(['Total Spent', 'Budget Limit'], [grand_total, bgt], color=['red', 'green'])
    ax2.set_title("Overall Expenditures vs Threshold")
    ax2.set_ylabel("Amount")

    plt.tight_layout()
    plt.show()

budget()

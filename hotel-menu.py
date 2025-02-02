#define the menu of hotel
menu = {
    'Pizza':100,
    'Pasta':60,
    'Burger':80,
    'Momo':60,
    'Coffee':40
}
#Greet
print("Wellcome To Python Resturant")
print(" Pizza: Rs100\n Pasta: Rs60\n Burger: Rs80\n Momo: Rs60\n Coffee: Rs40")

order_total=0

item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order...")
else:
    print(f"Sorry Ordered item {item_1} is not available yet")

anotherOrder=input("Do you want to add another item? (yes/no)")
if anotherOrder=="yes":
    item_2=input("Enter The Name Of Second Item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to Order...")
    else:
        print(f"Sorry Item {item_2} is not available yet")
        
else:
    print(f"Thank you for visiting....")
        
        
print(f"The Total amount to items to pay is : {order_total}")

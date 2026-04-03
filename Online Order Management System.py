orders = {
    "O1": {
        "customer": "Ali",
        "items": [("Pen",2), ("Book",1)]
    },
    "O2": {
        "customer": "Sara",
        "items": [("Book",3), ("Pencil",5)]
    }
}

def find_orders_by_item(orders, target):
    order_name=[]
    for key,value in orders.items():
        for i in orders[key]['items']:
            if i[0].lower()== target.lower():
                order_name.append(orders[key]['customer'])
    return order_name


target=input("enter the order item name")
process =find_orders_by_item(orders, target)
print(process)
#assuming that only pen,pencil and book  is available
total_quantity={'Book':0,'Pencil':0,'Pen':0}
for key,value in orders.items():
    for i in orders[key]['items']:
        if i[0]== 'Book':
            total_quantity['Book']=int(total_quantity['Book'])+int(i[1])
        elif i[0]== 'Pen':
            total_quantity['Pen']=int(total_quantity['Pen'])+int(i[1])
        elif i[0]== 'Pencil':
            total_quantity['Pencil']=int(total_quantity['Pencil'])+int(i[1])
print(total_quantity)


def get_bulk_customers(orders):
    for key,value in orders.items():
        if len(orders[key]['items']) > 3:
            print(orders[key]['customer'])

get_bulk_customers(orders)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import House, Worker, Tool, License
from tabulate import tabulate


engine = create_engine('sqlite:///house.db')
Session = sessionmaker(bind=engine)
session = Session()


print('1. Add worker\n')
print('2. Add tool\n')
print('3. Delete worker\n')
print('4. Delete tool\n')
print('5. View all workers\n')


choice = input('Enter option: ')

if choice == '1':
    worker_name = input("Enter the name of the worker: ")
    worker_age = int(input("Enter the age of the worker: "))
    worker_phone = int(input("Enter the phone number of the worker: "))
    worker_role = input("Enter the role of the worker: ")
    worker_pay = float(input("Enter the pay of the worker: "))
    worker = Worker(name_of_worker=worker_name, age=worker_age, phone_number=worker_phone, role=worker_role, pay=worker_pay)
    session.add(worker)
    session.commit()

elif choice == '2':
    tool_1 = input('Enter the name of tool: ') 
    tool_2 = int(input('Enter the cost of the tool: '))
    tool = Tool(name_of_tool = tool_1, cost= tool_2)
    session.add(tool)
    session.commit()

elif choice == '3':
    out =input('Enter worker id to delete: ')
    out_2 = session.query(Worker).filter(Worker.id == out).first()
    if out_2:
        session.delete(out_2)
        session.commit()
        print('Worker Deleted Successfully')
    else:
        print('Worker Not Found')

elif choice == '4':
    out_3 =input('Enter tool id to delete: ')
    out_4 = session.query(Tool).filter(Tool.id == out_3).first()
    if out_4:
        session.delete(out_4)
        session.commit()
        print('Tool Deleted Successfully')
    else:
        print('Worker Not Found')

elif choice == '5':
    wafanyikazi = session.query(Worker).all()
    if wafanyikazi:
        wafanyikazi_1 = []
        for i in wafanyikazi:
            wafanyikazi_1.append([i.id, i.name_of_worker, i.age, i.phone_number, i.role, i.pay])
            headers = ['id', 'name', 'age', 'phone_number', 'role', 'pay']
            print(tabulate(wafanyikazi_1, headers = headers, tablefmt = 'double_grid'))
    else:
        print('Worker Not Found')
        
else:
    print('Invalid Input')


session.commit()
session.close()
















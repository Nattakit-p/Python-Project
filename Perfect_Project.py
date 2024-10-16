import datetime,pandas

def Project():
  storage = []
  data_display = {"ID":[],
                  "NAME":[],
                  "BRAND":[],
                  "QTY":[],
                  "PRICE":[],
                  "Warranty_Expiry":[]
                  }
  Search_for =  {"ID":[],
                  "NAME":[],
                  "BRAND":[],
                  "QTY":[],
                  "PRICE":[],
                  "Warranty_Expiry":[]
                  }
  while True:
    menu = "*****_ Choose Opption _*****"
    print("-"*(len(menu)))
    print(menu)
    print("-"*(len(menu)))
    print('''  1. Add Phone
  2. Display All Phones
  3. Search by ID
  4. Update Phone
  5. Delete Phone
  6. Generate Report
  7. Exit''')
    print("-"*(len(menu)))
    opption = input()
    match opption:
      case '1':
        while True:
          add_storage = []
          print("-"*(len(menu)))
          print('         Add Phone      ')
          print("-"*(len(menu)))
          ID = input('ID : ')
          Name = input('NAME : ')
          Brand = input('BRAND : ')
          while True:
            try :
              Qty = int(input('QTY : '))
              if type(Qty) == int:
                break
            except :
              print("Please for number")
              continue
          while True:
            try:
              Price = float(input('Price : '))
              if type(Price) == float:
                break
            except:
              print("Please for number")
              continue
          while True:
            date_example = str(datetime.datetime.now())
            print(f"Example :{date_example[0:10]}")
            Warranty_Expiry = input("Warranty_Expiry (YYYY-MM-DD) :").strip()
            try :
              datetime.datetime.strptime(Warranty_Expiry, "%Y-%m-%d")
              break
            except:
              print("Please try again it's not calendar.")
          value = Qty*Price
          add_storage.append(ID)
          add_storage.append(Name)
          add_storage.append(Brand)
          add_storage.append(Qty)
          add_storage.append(Price)
          add_storage.append(Warranty_Expiry)
          # add_storage.append(value)
          print(add_storage)
          scaner = False
          for record in storage:
            if record[0] == add_storage[0]:
              scaner = True
              print("Retry Agian. ID is Same.")
              break
          if scaner == False:
            storage.append(add_storage)
            print("Completed")
            break
          else:
            print("No Completed")
            break
      case '2':
        print("-"*(len(menu)))
        print('     Display All Phones      ')
        print("-"*(len(menu)))
        for x in storage:
          data_display["ID"].append(x[0])
          data_display["NAME"].append(x[1])
          data_display["BRAND"].append(x[2])
          data_display["QTY"].append(x[3])
          data_display["PRICE"].append(x[4])
          data_display["Warranty_Expiry"].append(x[5])
        print(pandas.DataFrame(data_display).to_string(index=False))
        data_display = {"ID":[],
                  "NAME":[],
                  "BRAND":[],
                  "QTY":[],
                  "PRICE":[],
                  "Warranty_Expiry":[]
                  }
      case '3':
        print("-"*(len(menu)))
        print('       Search by ID      ')
        print("-"*(len(menu)))
        search_id = input("Enter the ID of the phone: ")
        found = False
        for phone in storage:
          if phone[0] == search_id:
              Search_for["ID"].append(phone[0])
              Search_for["NAME"].append(phone[1])
              Search_for["BRAND"].append(phone[2])
              Search_for["QTY"].append(phone[3])
              Search_for["PRICE"].append(phone[4])
              Search_for["Warranty_Expiry"].append(phone[5])
              print(pandas.DataFrame(Search_for).to_string(index=False))
              found = True
              break
        if not found:  
          print("No phone found with that ID.")
        print("-"*(len(menu)))
      case '4':
        print("-"*(len(menu)))
        print('       Update Phone      ')
        print("-"*(len(menu)))
        Data_Update_ID = input("Enter the ID of the phone:")
        for lol,phone in enumerate(storage):
          if phone[0] == Data_Update_ID:
              Name = input('New NAME : ')
              if Name == " " or Name == "":
                 Name = phone[1]
              Brand = input('New BRAND : ')
              if Brand == " " or Brand == "":
                 Brand = phone[2]
              try:
                Qty = int(input('New QTY : '))
              except:
                 Qty = phone[3]
              try:
                Price = float(input('New Price : '))
              except:
                Price = phone[4]
              Warranty_Expiry_New = input("New Warranty_Expiry (YYYY-MM-DD) : ")
              value = Qty*Price
              try:
                datetime.datetime.strptime(Warranty_Expiry_New,"%Y-%m-%d")
                Warranty_Expiry_New = input("Warranty_Expiry (YYYY-MM-DD) :").strip()
              except:
                Warranty_Expiry = phone[5]
              storage[lol] = [Data_Update_ID,Name,Brand,Qty,Price,Warranty_Expiry,value]
              
      case '5':
        print("-"*(len(menu)))
        print('       Delete Phone      ')
        print("-"*(len(menu)))
        delete_id = input("Enter the ID of the phone you want to delete: ")
    
        found = False  
        for phone in storage:
          if phone[0] == delete_id:  
            storage.remove(phone) 
            found = True
            print(f"Phone with ID {delete_id} has been deleted.")
            break
    
          if not found:  
            print("No phone found with that ID.")
          print("-"*(len(menu)))

      case '6':
        print("-" * (len(menu)))
        print('       Generate Report      ')
        print("-" * (len(menu)))

        def generate_report():
            if len(storage) == 0:
                print("No phones available to generate a report.")
                return

            total_value_all = 0
            total_qty_all = 0
            report_lines = []
            report_lines.append("=" * 90)
            report_lines.append(" " * 35 + "Inet Phone Store Report" + " " * 35)
            report_lines.append("=" * 90)
            report_lines.append(f"{'ID':<6} {'Name':<20} {'Brand':<10} {'Qty':<5} {'Price':<10} {'Value':<10} {'Warranty Expiry':<15}")
            report_lines.append("-" * 90)

            phone_past = None
            total_Qty_Brand = 0
            total_Value_Brand = 0

            for phone in storage:
                value = phone[3] * phone[4]

                if phone_past is not None and phone[2]!= phone_past[2]:
                    report_lines.append("-" * 90)
                    report_lines.append(f"Total items of {phone_past[2]}: {total_Qty_Brand}")
                    report_lines.append(f"Total value of {phone_past[2]}: {total_Value_Brand:.2f}")
                    report_lines.append("-" * 90)

                    total_Qty_Brand = 0
                    total_Value_Brand = 0

                report_lines.append(f"{phone[0]:<6} {phone[1]:<20} {phone[2]:<10} {phone[3]:<5} {phone[4]:<10} {value:<10} {phone[5]:<15}")

                total_Qty_Brand += phone[3]
                total_Value_Brand += value

                total_value_all += value
                total_qty_all += phone[3]

                phone_past = phone

            
            if phone_past is not None:
                report_lines.append("-" * 90)
                report_lines.append(f"Total items of {phone_past[2]}: {total_Qty_Brand}")
                report_lines.append(f"Total value of {phone_past[2]}: {total_Value_Brand:.2f}")
                report_lines.append("-" * 90)

            report_lines.append(f"\nTotal items All product: {total_qty_all}")
            report_lines.append(f"Total value All product: {total_value_all:.2f}")
            report_lines.append("=" * 90)

            with open("report.txt", "w") as file:
                file.write("\n".join(report_lines))
            print("\n".join(report_lines))

        generate_report()



        print("-" * (len(menu)))
        print('       Generate Report      ')
        print("-" * (len(menu)))
        generate_report()
                
      case '7':
          print("-"*(len(menu)))
          print('       Exite Completed      ')
          print("-"*(len(menu)))
          break
Project()

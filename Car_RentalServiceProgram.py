_dataSource ="/Users/htooauntshein/Documents/_cardatawereHouseFinalAssignment.csv"

#show data with Formated table
def format_table_output(header, rows):

    col_widths = [max(len(str(row[i])) for row in [header] + rows) for i in range(len(header))]
    
    formatted_header = "  ".join(header[i].ljust(col_widths[i]) for i in range(len(header)))
    print(formatted_header)
    print("-" * len(formatted_header))  
    for row in rows:
        formatted_row = "  ".join(row[i].ljust(col_widths[i]) if i < len(row) else "".ljust(col_widths[i]) for i in range(len(header)))
        print(formatted_row)

# generate new ID
def generate_newItems_ID(_dataSource):
    try:
        with open(_dataSource,mode='r')as f:
            lines = f.readlines()
            if len(lines) > 1 :
                last_line = lines[-1].strip()
                last_id = int(last_line.split(',')[0])
                return last_id + 1
            else :
                return 1
    except FileNotFoundError:
        print(f"Error : File {_dataSource} not found.")


def display_items():
    try:
        with open(_dataSource) as f:
            lines = f.readlines()  

        if len(lines) == 0:
            print("No data available.")
            return

        header = lines[0].strip().split(",")
        data_lines = [line.strip().split(",") for line in lines[1:]]
        
        format_table_output(header, data_lines)

    except FileNotFoundError:
        print(f"Error: File {_dataSource} not found.")

def display_totalItems_count():
    try:
        with open(_dataSource) as f:
            lines = f.readlines()
            _dataCarcount = list(lines)
            total_cars = len(_dataCarcount) - 1 
        print(f"Total Cars : {total_cars}")
    except FileNotFoundError:
        print("File Not Found")
        return 1

def search_items(column_name):
    try:
        with open(_dataSource) as f:
            lines = f.readlines()
    
        if len(lines) == 0:
            print("No data available.")
            return

        header = lines[0].strip().split(",")
        data_lines = [line.strip().split(",") for line in lines[1:]]

        column_name = column_name.lower()
        
        if column_name not in ["name", "group", "type"]:
            print("Invalid column name. Please choose 'Name', 'Group', or 'Type'.")
            return

        if column_name == "name":
            col_index = header.index("CarName")
        elif column_name == "group":
            col_index = header.index("Group")
        elif column_name == "type":
            col_index = header.index("Type")


        search_term = input(f"Enter search term for {column_name}: ")
        search_term = search_term.lower()
        results = [line for line in data_lines if search_term in line[col_index].lower()]
        
        if results:
            format_table_output(header, results)
        else:
            print(f"No results found for '{search_term}'.")

    except FileNotFoundError:
        print(f"Error: File {_dataSource} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_items():
    print("Enter Add Details for Cars")
    new_id = generate_newItems_ID(_dataSource)

    new_carName = input("Enter Car Name : ")
    new_carGroup = input("Enter Car Group : ")
    new_carType = input("Enter Car Type : ")
    new_carModel = input("Enter Car Model Year : ")
    new_carCount = input("Enter Car Count : ")


    new_carItem =[str(new_id), new_carName, new_carGroup, new_carType, new_carModel, new_carCount]
    try:
        with open(_dataSource,mode='a') as f:
            f.write("\n" +','.join(new_carItem))
            print (f"Successfully added with Id {new_id}")
        
    except FileNotFoundError:
        print("Error : with file not found")


def main():
    while True:
        print("\nCar Rental Service Menu")
        print("1 - Display Show Cars")
        print("2 - Display Cars Count Result")
        print("3 - Display Search Item")
        print("4 - Add New Car")
        print("7 - Exit the program")

        choice = input("Choose an option - ")
        if choice == "1":
            display_items()
        elif choice == "2":
            display_totalItems_count()
        elif choice == "3":
            column_name = input("Search by (Name, Group, Type): ")
            search_items(column_name)
        elif choice == "4":
            add_items()
        elif choice == "7":
            break
        else:
            print("Invalid Option Please Choose again")

if __name__ == "__main__":
    main()




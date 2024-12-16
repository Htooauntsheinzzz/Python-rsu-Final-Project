_dataSource ="/Users/htooauntshein/Shein'sWorkspace/RSU_Python(DIT-101)/Final_Assignment/_cardatawereHouseFinalAssignment.csv"

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
        print(f"Total Cars in our service: {total_cars}")
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

def update_items():
    """Update Cars Items List"""

    display_items()

    try:
        with open(_dataSource,'r',encoding='utf-8-sig') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f'Your Data Not found in your directory {_dataSource}')
    
    headers = lines[0].strip().split(',')

    car_id = input("Enter the ID that you want to update: ").strip()
    

    matching_carId = None
    row_index = -1
    for i, line in enumerate(lines[1:], start=1):
        row = line.strip().split(',')
        if row[0] == car_id: 
            matching_carId = row
            row_index = i
            break


    if matching_carId:
        print(f"Data for ID {car_id}:")
        format_table_output(headers, [matching_carId])

        column_name = input("Enter Field Name that want to update you want to update: ").strip()
        normalized_headers = [header.lower() for header in headers]
        normalized_column_name = column_name.lower()

        if normalized_column_name not in normalized_headers:
            print(f"Error: Column '{column_name}' does not exist.")
            return

        column_index = normalized_headers.index(normalized_column_name) 
        if normalized_column_name == 'id':
            format_table_output(headers, [matching_carId])
            print("Error: The 'ID' field cannot be updated.")
        return

        new_value = input(f"Enter the new value for '{column_name}': ").strip()
        matching_carId[column_index] = new_value
        lines[row_index] = ','.join(matching_carId) + '\n'

        with open(_dataSource, 'w', encoding='utf-8-sig') as f:
            f.writelines(lines)

        print(f"Successfully updated '{headers[column_index]}' to '{new_value}' for ID {car_id}.")
        format_table_output(headers, [matching_carId])
    else:
        print(f"Error: No data found for ID {car_id}.")

    
def delete_items():
    try:
        with open(_dataSource, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

        if len(lines) <= 1:
            print("No data available to delete.")
            return

        header = lines[0].strip().split(",")
        data_lines = [line.strip().split(",") for line in lines[1:]]
        print("Available Records:")
        format_table_output(header, data_lines)

        header_lower = [col.lower() for col in header]

        column_name = input(f"Enter the column to search for deletion (ID, CarName, Group, Type): ").strip().lower()
        if column_name not in header_lower:
            print(f"Invalid column name '{column_name}'. Please choose from {', '.join(header)}.")
            return

        col_index = header_lower.index(column_name)

        search_term = input(f"Enter the value to search for in column '{column_name}': ").strip().lower()

        matching_records = [line for line in data_lines if line[col_index].lower() == search_term]

        if not matching_records:
            print(f"No records found matching '{search_term}' in column '{column_name}'.")
            return

        print("\nMatching Records:")
        format_table_output(header, matching_records)

        if input(f"Do you want to delete these records? (yes/no): ").strip().lower() != 'yes':
            print("Deletion cancelled.")
            return

        new_data_lines = [line for line in data_lines if line[col_index].lower() != search_term]
        with open(_dataSource, 'w') as f:
            f.write(",".join(header) + "\n")
            for line in new_data_lines:
                f.write(",".join(line) + "\n")

        print(f"Records matching '{search_term}' in column '{column_name}' have been deleted.")

    except FileNotFoundError:
        print(f"Error: File '{_dataSource}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\n\t\tCar Rental Service Menu")
        print("1 - Display Show Cars")
        print("2 - Display Cars Count Result")
        print("3 - Display Search Item")
        print("4 - Add New Car")
        print("5 - Update Car Items")
        print("6 - Delete Car Items")
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
        elif choice == "5":
            update_items()
        elif choice == "6":
            delete_items()
        elif choice == "7":
            break
        else:
            print("Invalid Option Please Choose again")

if __name__ == "__main__":
    main()




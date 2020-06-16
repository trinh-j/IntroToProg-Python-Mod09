# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# JTrinh,6.8.2020,Modified code to complete assignment 9
# JTrinh,6.12.2020, Added code to script to access modules
# JTrinh,6.14.2020, Refined while loop in Main.py to catch all possible menu inputs
# ------------------------------------------------------------------------ #
# Importing modules and classes from modules
if __name__ == "__main__":
    import DataClasses as D  # data classes
    import ProcessingClasses as P # processing classes
    from DataClasses import Employee as Emp  # Employee class only!
    from IOClasses import EmployeeIO as Eio # EmployeeIO class
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
try:
    lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt") #find text file by this name
    lstTable = [] #create an empty table to read out text file data
    lstTable.clear() #make sure list is cleared
    for line in lstFileData:
        lstTable.append(Emp(line[0], line[1], line[2].strip())) #reformatting data
    print("Data read in from text file: ")
    for row in lstTable:
        print("\t" + row.to_string(), type(row))


# Show user a menu of options
    while(True):
        Eio.print_menu_items()
    # Get user's menu option choice
        strChoice = Eio.input_menu_options()
        # Show user current data in the list of employee objects
        if strChoice == "1":
            Eio.print_current_list_items(lstTable)
        # Let user add data to the list of employee objects
        elif strChoice == "2":
            newEmp = Eio.input_employee_data()
            lstTable.append(newEmp)
    # let user save current data to file
        elif strChoice == "3":
            P.FileProcessor.save_data_to_file("EmployeeData.txt",lstTable)
            print("Data Saved!")
    # Let user exit program
        elif strChoice == "4":
            yn = input("Are you sure you would like to exit the program? [y/n]") #double checks if user wants to leave program
            if yn.lower() == "y":
                print("Exiting Program. Goodbye.")
                break #Exit program
            elif yn.lower() == "n":
                continue #choose another menu item
    # Invalid menu input
        else:
            print("You have not chosen a valid menu option. Please try again")
            continue

except FileNotFoundError as e: #raise error if name of text file note found
    print("Check the name of your file. If it does not exist, create one!")
    print(e, e.__str__(), e.__doc__, sep="\n")

except Exception as e:
    print(e, e.__str__(), e.__doc__, sep="\n")
# Main Body of Script  ---------------------------------------------------- #

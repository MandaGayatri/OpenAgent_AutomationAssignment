def write_list_to_file(file_path, my_list):
    try:
        with open(file_path, 'a') as file:  # Change 'w' to 'a' for append mode
            file.writelines(item + '\n' for item in my_list)  # Use writelines to write the entire list
        print("List appended to file successfully.")
    except Exception as e:
        print("An error occurred:", str(e))


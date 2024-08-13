"""
Created on Fri Aug  2 13:23:44 2024

@author: ryand
"""

import time
import os

file_path = "input_data.txt"
check_interval = .2

def read_list_from_file(file_path):
    with open(file_path, 'r') as file:
        return [float(line.strip()) for line in file.readlines()]

def write_list_to_file(file_path, data_list):
    with open(file_path, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n")

def process_list_in_place(file_path):
    # Read the list from the file
    data_list = read_list_from_file(file_path)

    # Compute sums
    for i in range(len(data_list)):
        data_list[i] += data_list[i]

    # Overwrite the file with the processed list
    write_list_to_file(file_path, data_list)

def main():
    last_modified_time = None

    while True:
        try:
            # Get the last modified time of the file
            current_modified_time = os.path.getmtime(file_path)
            
            # Check if the file has been modified since the last check
            if last_modified_time is None or current_modified_time != last_modified_time:
                print(f"Processing file: {file_path}")
                process_list_in_place(file_path)
                last_modified_time = os.path.getmtime(file_path)

            # Wait for the next check
            time.sleep(check_interval)
        
        except FileNotFoundError:
            print(f"File {file_path} not found. Waiting for the file to be created.")
            time.sleep(check_interval)

if __name__ == "__main__":
    main()

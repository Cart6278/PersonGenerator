# Pandas is used to import and export csv files, this will need to be documented in the README
# import Tkinter
import tkinter as tk
import pandas as panda
import random
import sys


def state_abbv(find_state):
    if find_state == "alaska":
        find_state = "ak"
    elif find_state == "arizona":
        find_state = "az"
    elif find_state == "california":
        find_state = "ca"
    elif find_state == "colorado":
        find_state = "co"
    elif find_state == "hawaii":
        find_state = "hi"
    elif find_state == "idaho":
        find_state = "id"
    elif find_state == "montana":
        find_state = "mt"
    elif find_state == "new mexico":
        find_state = "nm"
    elif find_state == "nevada":
        find_state = "nv"
    elif find_state == "oregon":
        find_state = "or"
    elif find_state == "utah":
        find_state = "ut"
    elif find_state == "washington":
        find_state = "wa"
    elif find_state == "wyoming":
        find_state = "wy"

    return find_state


def main(state, num_gen, out_csv):
    # csv_to_import = 0
    csv_append = ".csv"  # for later to append to the end of the abbreviated state name
    if sys.argv[1]:
        csv_to_import = sys.argv[1]
        csv_import_file = panda.read_csv(csv_to_import, header=0)
        csv_import_data = csv_import_file.values.tolist()
        find_state = csv_import_data[0].lower()
        num_gen = csv_import_data[1]
        out_csv = 1
    else:
        find_state = state.lower()  # make sure submitted state name is in lower case
    # rand_nums_gen = []
    rand_addr = []

    # if state name is longer than two characters send to state_abbv() to find the appropriate state abbreviation
    if len(find_state) != 2:
        find_state = state_abbv(find_state)

    # save the file name of the state to find the random addresses from
    state_import = find_state + csv_append

    # New Mexico apparently has no zip code info... Code now has different parsing for New Mexico!
    if find_state == "nm":
        # adapted from Real Python article about reading a .csv file with Pandas:
        # https://realpython.com/working-with-large-excel-files-in-pandas/
        state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 4, 5, 6, 7], low_memory=False)
        # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
        # state_addr = state_data.DataFrame(state_data, columns=['NUMBER', 'STREET', 'CITY'])
        # do I get rid of NaN spaces? https://realpython.com/analyzing-obesity-in-england-with-python/
        state_data.dropna(inplace=True)
        valid_addr = state_data.values.tolist()
        # state_number = int(format(len(state_data)))
    else:
        # adapted from Real Python article about reading a .csv file with Pandas:
        # https://realpython.com/working-with-large-excel-files-in-pandas/
        state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 4, 5, 6, 7, 8],
                                    low_memory=False)
        # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
        # do I get rid of NaN spaces? https://realpython.com/analyzing-obesity-in-england-with-python/
        state_data.dropna(inplace=True)
        valid_addr = state_data.values.tolist()
        # state_number = int(format(len(state_data)))

    # generate random numbers to correspond with lines from csv data from the given state. Store the random number
    # take random numbers found, find the line from the data, print to .csv and GUI (or save data to list)
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(state_data))])

    # if out_csv is true OR input came from a .csv file then print results to .csv file, else print to GUI
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    if out_csv == 1:
        # fields_out = ['input_state', 'input_number_to_generate', 'output_content_type', 'output_content_value']
        # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
        for z in range(num_gen):
            output_state.append(find_state)
            output_num.append(num_gen)
            output_type.append('Street Address')
            output_data.append(rand_addr[z])  # change so that this prints to output.csv

        dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                    'output_content_type': output_type,
                    'output_content_value': output_data}
        ting = panda.DataFrame(dict_out)
        ting.to_csv('output.csv')

    else:
        for z in range(num_gen):
            print_to_gui = tk.Label(window, text=str(find_state + ", " + num_gen + ", " + rand_addr[z]))
            print_to_gui.pack()
            # print(find_state, ", ", num_gen, ", ", rand_addr[z])  # change so that this prints to the GUI


# loading Tkinter adapted from: https://stackoverflow.com/questions/53797598/how-to-install-tkinter-with-pycharm

window = tk.Tk()

title = tk.Label(text="Welcome to Person Generator")
    # widget code
window.mainloop()
# for GUI
arr_states = [
    'Alaska',
    'Arizona',
    'California',
    'Colorado',
    'Hawaii',
    'Idaho',
    'Montana',
    'New Mexico',
    'Nevada',
    'Oregon',
    'Utah',
    'Washington',
    'Wyoming'
]

# https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
state_choice = tk.StringVar(window)
state_choice.set(arr_states[0])
which_state = tk.OptionMenu(window, state_choice, *arr_states)
which_state.config(width=50, font=('Arial', 12))

# adapted from: https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets
num_label = tk.Label(text='Enter Amount to Generate')
to_gen = tk.Entry(width=10)
num_to_gen = to_gen.get()

# adapted from: https://www.askpython.com/python-modules/tkinter/tkinter-checkbox-and-checkbutton
output_bool = tk.IntVar()
output_box = tk.Checkbutton(window, text='Output to .CSV', variable=output_bool)

# code for submit button adapted from
# https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
submit = tk.Button(
    text="Submit",
    width=12,
    height=5,
    bg='DarkGray',
    fg='White',
)

submit.bind("<Button-1>", main)
submit.pack()
submit['command'] = lambda: main(state_choice.get(), num_to_gen.get(), output_bool.get())

# num_label.pack()
# to_gen.pack()
# which_state.pack() # choose location in GUI

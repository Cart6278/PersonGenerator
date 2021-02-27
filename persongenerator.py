# Kirsten Carter
# Person Generator
# CS 361 - 400 Winter 2021
from flask import Flask, json
from flask import jsonify
import tkinter as tk
import pandas as panda
import random
import sys
import urllib.request


# this function takes full state names and converts them to their lower case abbreviations
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


def csv_wy(find_state, num_gen, rand_addr):
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
    for z in range(num_gen):
        output_state.append(find_state.upper())
        output_num.append(num_gen)
        output_type.append('Street Address')
        output_data.append(
            str(rand_addr[z][0]) + ' ' + str(rand_addr[z][1]) + ', ' + str(rand_addr[z][2]))

    dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                'output_content_type': output_type,
                'output_content_value': output_data}
    ting = panda.DataFrame(dict_out)
    ting.to_csv('output.csv', index=False)
    return "Output to output.csv is complete"


# processing and output for the state of Wyoming due to data lacking important data that breaks .csv input
def output_wy(state, num_gen, out_csv, state_import):
    find_state = state
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # removal of NaN spaces: https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])
    if out_csv == 1:
        return csv_wy(state, num_gen, rand_addr)
    # adapted from: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/
    else:
        new_string = ''
        for z in range(num_gen):
            new_string += find_state.upper()
            new_string += ', '
            new_string += str(num_gen)
            new_string += ', '
            new_string += str(int(rand_addr[z][0]))
            new_string += ' '
            new_string += str(rand_addr[z][1])
            new_string += '\n'

    return new_string


def csv_nm(find_state, num_gen, rand_addr):
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
    for z in range(num_gen):
        output_state.append(find_state.upper())
        output_num.append(num_gen)
        output_type.append('Street Address')
        output_data.append(
            str(rand_addr[z][0]) + ' ' + str(rand_addr[z][1]) + ', ' + str(rand_addr[z][2]) + ', '
            + str(rand_addr[z][3]))  # change so that this prints to output.csv

    dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                'output_content_type': output_type,
                'output_content_value': output_data}
    ting = panda.DataFrame(dict_out)
    ting.to_csv('output.csv', index=False)
    return "Output to output.csv is complete"


# processing and output for the state of New Mexico due to data lacking important data that breaks .csv input
def output_nm(state, num_gen, out_csv, state_import):
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 5], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # removal of NaN spaces: https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])
    if out_csv == 1:
        return csv_nm(state, num_gen, rand_addr)
    # adapted from: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/
    else:
        new_string = ''
        for z in range(num_gen):
            new_string += state.upper()
            new_string += ', '
            new_string += str(num_gen)
            new_string += ', '
            new_string += str(rand_addr[z][0])
            new_string += ' '
            new_string += str(rand_addr[z][1])
            new_string += ', '
            new_string += str(rand_addr[z][2])
            new_string += '\n'
    return new_string


def json_states(find_state, num_gen, rand_addr):
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
    for z in range(num_gen):
        # set data fields in lists with given and generated data
        output_state.append(find_state.upper().rstrip())
        output_num.append(num_gen)
        output_type.append('Street Address'.rstrip())
        # strange concatenation due to [] appearing on output in output.csv
        output_data.append(str(rand_addr[z][0]).rstrip() + ' ' + str(rand_addr[z][1]).rstrip() + ' ' +
                           str(rand_addr[z][2]).rstrip())
    # create dictionary to hold data, necessary for Pandas to output to csv, see reference above
    dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                'output_content_type': output_type,
                'output_content_value': output_data}
    # convert dictionary to json: https://www.geeksforgeeks.org/how-to-convert-python-dictionary-to-json/
    ting = panda.DataFrame(dict_out)
    for_json = [ting.columns.values.tolist()] + ting.values.tolist()
    return for_json


def csv_states(find_state, num_gen, rand_addr):
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
    for z in range(num_gen):
        # set data fields in lists with given and generated data
        output_state.append(find_state.upper())
        output_num.append(num_gen)
        output_type.append('Street Address')
        # strange concatenation due to [] appearing on output in output.csv
        output_data.append(str(rand_addr[z][0]) + ' ' + str(rand_addr[z][1]) + ' ' +
                           str(rand_addr[z][2]))
    # create dictionary to hold data, necessary for Pandas to output to csv, see reference above
    dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                'output_content_type': output_type,
                'output_content_value': output_data}
    ting = panda.DataFrame(dict_out)
    ting.to_csv('output.csv', index=False)
    return "Output to output.csv is complete"  # return text for GUI


# processing and output for every other state but New Mexico and Wyoming
def output_states(state, num_gen, out_csv, state_import):
    find_state = state
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 5, 8], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # removal of NaN spaces: https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    state_number = int(format(len(state_data)))
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])
    if out_csv == 1:
        return csv_states(state, num_gen, rand_addr)
    # adapted from: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/
    elif out_csv == 2:
        # in order for GUI output to work results must be in a string.
        new_string = ''
        for z in range(num_gen):
            new_string += find_state.upper()
            new_string += ', '
            new_string += str(num_gen)
            new_string += ', '
            new_string += str(rand_addr[z][0])
            new_string += ', '
            new_string += str(rand_addr[z][1])
            new_string += ', '
            new_string += str(rand_addr[z][2])
            new_string += '\n'
        return new_string
    else:
        return json_states(state, num_gen, rand_addr)


# returning the data from the connected microservice to my microservice, called in output states
def get_microservice(state, year):
    # adapted from: https://docs.python.org/3/howto/urllib2.html
    state = state.lower()
    str_year = str(year)
    abbv_state = state_abbv(state)
    cur_url = 'http://127.0.0.1:5005/?year='
    cur_url += str_year
    cur_url += '&state='
    cur_url += abbv_state.upper()
    open_url = urllib.request.urlopen(cur_url)
    micro_output = open_url.read()
    # micro_response = json.loads(micro_output)
    return json.loads(micro_output)


def main(state, num_gen, out_csv):
    csv_append = ".csv"
    num_gen = int(num_gen)
    find_state = state.lower()
    if len(find_state) != 2:
        find_state = state_abbv(find_state)
    state_import = find_state + csv_append
    # New Mexico apparently has no zip code info... Code now has different parsing for New Mexico!
    if find_state == "nm":
        return output_nm(find_state, num_gen, out_csv, state_import)
    # special processing for WY because none of the addresses have cities associated with them
    elif find_state == "wy":
        return output_wy(find_state, num_gen, out_csv, state_import)
    else:
        return output_states(find_state, num_gen, out_csv, state_import)


# takes .csv file from command line, processes it and then passes on necessary info to main()
# adapted: https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
# and https://realpython.com/working-with-large-excel-files-in-pandas/
def from_csv():
    csv_to_import = sys.argv[1]
    csv_import_file = panda.read_csv(csv_to_import, header=0)
    csv_import_data = csv_import_file.values.tolist()  # NOTE: this creates a "lists of lists"
    find_state = csv_import_data[0][0].lower()
    num_gen = csv_import_data[0][1]
    out_csv = 1
    main(find_state, num_gen, out_csv)


# if input from command line is received go to from_csv to process else run GUI
if len(sys.argv) == 2:
    from_csv()
else:
    # ------------------ GUI BEGINS HERE -------------------
    # loading Tkinter adapted from: https://stackoverflow.com/questions/53797598/how-to-install-tkinter-with-pycharm
    window = tk.Tk()
    window.title("Welcome to Person Generator")
    window.resizable(width=True, height=True)
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

    input_frame = tk.Frame(master=window)
    state_choice = tk.StringVar(master=input_frame)

    # drop down adapted from: https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/
    state_choice.set(arr_states[0])
    which_state = tk.OptionMenu(input_frame, state_choice, *arr_states)
    which_state.config(width=25, font=('Arial', 12))

    # entry widget adapted from: https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets
    num_label = tk.Label(master=input_frame, text='Enter Number to Generate')
    to_gen = tk.Entry(master=input_frame, width=7)

    # check box adapted from: https://www.askpython.com/python-modules/tkinter/tkinter-checkbox-and-checkbutton
    output_bool = tk.IntVar()
    output_box = tk.Checkbutton(master=input_frame, text='Output to .CSV', variable=output_bool)

    # code for submit button adapted from
    # https://realpython.com/python-gui-tkinter/#building-your-first-python-gui-application-with-tkinter
    submit = tk.Button(
        text="Submit",
        width=5,
        height=2,
        bg='DarkBlue',
        fg='White',
    )
    # https://stackoverflow.com/questions/55343738/how-do-you-use-tkinter-to-display-the-output-of-a-function-call
    submit.bind("<Button-1>", main)
    submit['command'] = lambda: display_out.config(text=main(state_choice.get(), int(to_gen.get()), output_bool.get()))

    display_title = tk.Label(master=input_frame, text='Generated Addresses:')
    display_out = tk.Label(input_frame, bg='White', text='')

    # for data from microservice
    year_label = tk.Label(master=input_frame, text='Enter Year for Population')
    year_gen = tk.Entry(master=input_frame, width=7)
    display_micro_title = tk.Label(master=input_frame, text='From Microservice:')
    display_micro_out = tk.Label(input_frame, bg='White', text='')
    retrieve = tk.Button(
        text="Retrieve",
        width=7,
        height=2,
        bg='Purple',
        fg='White',
    )
    # https://stackoverflow.com/questions/55343738/how-do-you-use-tkinter-to-display-the-output-of-a-function-call
    retrieve.bind("<Button-2>", get_microservice)
    retrieve['command'] = lambda: display_micro_out.config(text=get_microservice(state_choice.get(), int(year_gen.get())))

    # position of elements in window
    input_frame.pack()
    which_state.pack()
    num_label.pack(pady=5)
    to_gen.pack(pady=5)
    output_box.pack()
    submit.pack(pady=5)
    display_title.pack(pady=7)
    display_out.pack()
    display_micro_title.pack(pady=7)
    display_micro_out.pack()
    year_label.pack()
    year_gen.pack()
    retrieve.pack(pady=5)

    # end widget code
    window.mainloop()

# Pandas is used to import and export csv files, this will need to be documented in the README
# import Tkinter
import tkinter as tk
import pandas as panda
import random
import sys


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


# processing and output for the state of Wyoming due to data lacking important data that breaks .csv input
# INCLUDING CITIES, the vast majority of the addresses have no city data
def output_wy(state, num_gen, out_csv, state_import):
    find_state = state
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # do I get rid of NaN spaces? - Yes https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])
        # if out_csv is true OR input came from a .csv file then print results to .csv file, else print to GUI
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    if out_csv == 1:
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


# processing and output for the state of New Mexico due to data lacking important data that breaks .csv input
def output_nm(state, num_gen, out_csv, state_import):
    find_state = state
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 5], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # do I get rid of NaN spaces? - Yes https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])
    # if out_csv is true OR input came from a .csv file then print results to .csv file, else print to GUI
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    if out_csv == 1:
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
    # adapted from: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/
    else:
        new_string = ''
        for z in range(num_gen):
            new_string += find_state.upper()
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


# processing and output for every other state but New Mexico (and maybe Wyoming)
def output_states(state, num_gen, out_csv, state_import):
    find_state = state
    rand_addr = []
    # adapted from Real Python article about reading a .csv file with Pandas:
    # https://realpython.com/working-with-large-excel-files-in-pandas/
    state_data = panda.read_csv("archive/%s" % state_import, header=0, usecols=[2, 3, 5, 8], low_memory=False)
    # adapted from: https://datatofish.com/import-csv-file-python-using-pandas/
    # do I get rid of NaN spaces? https://realpython.com/analyzing-obesity-in-england-with-python/
    state_data.dropna(inplace=True)
    valid_addr = state_data.values.tolist()
    state_number = int(format(len(state_data)))

    # generate random numbers to correspond with lines from csv data from the given state. Store the random number
    # take random numbers found, find the line from the data, print to .csv and GUI (or save data to list)
    for x in range(num_gen):
        rand_addr.append(valid_addr[random.randrange(len(valid_addr))])

    # if out_csv is true OR input came from a .csv file then print results to .csv file, else print to GUI
    output_data = []
    output_state = []
    output_num = []
    output_type = []
    # if output to CSV is selected start this section of code
    if out_csv == 1:
        # adapted from: https://www.geeksforgeeks.org/saving-a-pandas-dataframe-as-a-csv/
        for z in range(num_gen):
            # set data fields in lists with given and generated data
            output_state.append(find_state.upper())
            output_num.append(num_gen)
            output_type.append('Street Address')
            # strange concatenation due to [] appearing on output in output.csv
            output_data.append(str(rand_addr[z][0]) + ' ' + str(rand_addr[z][1]) + ', ' + str(rand_addr[z][2]))
        # create dictionary to hold data, necessary for Pandas to output to csv, see reference above
        dict_out = {'input_state': output_state, 'input_number_to_generate': output_num,
                    'output_content_type': output_type,
                    'output_content_value': output_data}
        ting = panda.DataFrame(dict_out)
        ting.to_csv('output.csv', index=False)
        return "Output to output.csv is complete"  # return text for GUI
    # adapted from: https://yagisanatode.com/2018/02/26/how-to-display-and-entry-in-a-label-tkinter-python-3/
    else:
        # make a string of all the generated addresses. It is necessary to concatenate to make Tkinter happy and this is
        # how I did it. I suspect there is a better way, will need to research
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


def main(state, num_gen, out_csv):
    # csv_to_import = 0
    csv_append = ".csv"  # for later to append to the end of the abbreviated state name
    num_gen = int(num_gen)

    find_state = state.lower()  # make sure submitted state name is in lower case
    # if state name is longer than two characters send to state_abbv() to find the appropriate state abbreviation
    if len(find_state) != 2:
        find_state = state_abbv(find_state)

    # save the file name of the state to find the random addresses from
    state_import = find_state + csv_append

    # New Mexico apparently has no zip code info... Code now has different parsing for New Mexico!
    if find_state == "nm":
        # CALL FUNCTION FOR ONLY NM - shortens main code, fewer if statements. New Mexico data has no zipcodes,
        # needs different processing
        return output_nm(find_state, num_gen, out_csv, state_import)
    elif find_state == "wy":
        # special processing for WY because none of the addresses have cities associated with them
        return output_wy(find_state, num_gen, out_csv, state_import)
    else:
        # FUNCTION FOR ALL OTHER STATES - WY causes error. I suspect there is a necessary data field missing like NM
        return output_states(find_state, num_gen, out_csv, state_import)


# takes .csv file from command line, processes it and then passes on necessary info to main()
# adapted: https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
# and https://realpython.com/working-with-large-excel-files-in-pandas/
def from_csv():
    # get file name
    csv_to_import = sys.argv[1]
    # import file with pandas, remove header
    csv_import_file = panda.read_csv(csv_to_import, header=0)
    # save the imported data as a list, NOTE: this creates a "lists of lists"
    # with 0 0 being the state and 01 being the number to gen
    csv_import_data = csv_import_file.values.tolist()
    # make state name all lower case and save
    find_state = csv_import_data[0][0].lower()
    # save number to generate
    num_gen = csv_import_data[0][1]
    # set output to csv to TRUE (bing 1 in this case)
    out_csv = 1
    # call main function passing info parsed from file
    main(find_state, num_gen, out_csv)


# if input from command line is received go to from_csv to process else run GUI
if len(sys.argv) >= 2:
    from_csv()
else:
    # ------------------ GUI BEGINS HERE -------------------
    # loading Tkinter adapted from: https://stackoverflow.com/questions/53797598/how-to-install-tkinter-with-pycharm
    # for GUI
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

    # https://www.delftstack.com/howto/python-tkinter/how-to-create-dropdown-menu-in-tkinter/

    state_choice.set(arr_states[0])
    which_state = tk.OptionMenu(input_frame, state_choice, *arr_states)
    which_state.config(width=25, font=('Arial', 12))

    # adapted from: https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets
    num_label = tk.Label(master=input_frame, text='Enter Number to Generate')
    to_gen = tk.Entry(master=input_frame, width=7)
    # num_to_gen = to_gen.get()

    # adapted from: https://www.askpython.com/python-modules/tkinter/tkinter-checkbox-and-checkbutton
    output_bool = tk.IntVar()
    # output_bool.set(0)
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
    # a_state=state_choice.get(), nums=to_gen.get(), out_bool=output_bool.get(): main(a_state, nums, out_bool)

    display_title = tk.Label(master=input_frame, text='Generated Addresses:')
    display_out = tk.Label(input_frame, bg='White', text='')

    input_frame.pack()
    which_state.pack()
    num_label.pack(pady=5)
    to_gen.pack(pady=5)
    output_box.pack()
    submit.pack(pady=5)
    display_title.pack(pady=7)
    display_out.pack()

    # widget code
    window.mainloop()

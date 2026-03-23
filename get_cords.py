import pandas


def get_cords():
    states = {
              }

    data = pandas.read_csv('50_states.csv')
    for row in data.iterrows():

        states[row[1]["state"]] = (row[1]["x"], (row[1]["y"]))
    return states


get_cords()

import pandas

original_data = pandas.read_excel("Nodes_Test.xlsx")
origianal_data_frame = pandas.DataFrame(original_data)


unique_key_combination = origianal_data_frame[["External Node Id", "Level ID"]]
duplicate_data = origianal_data_frame[unique_key_combination.duplicated()]
plain_data = origianal_data_frame[~unique_key_combination.duplicated()]


for record1 in duplicate_data:
    for record2 in plain_data:
        pass

import os
import datetime

item_filename = "items.json"
countries_filename = (
    "countries" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".json"
)

# check if countries.json exists and is not empty
if os.path.isfile(countries_filename) and os.stat(countries_filename).st_size != 0:
    raise Exception("countries.json is not empty")

# open countries.json
with open(countries_filename, "a") as countries_file:
    # open items2.json
    with open(item_filename, "r") as f:
        for line in f:
            # eval the line as a dict
            item:dict = eval(line)
            instance_of = item["instance_of"]
            # check if the current line is a country
            if "country" in instance_of or "sovereign state" in instance_of or "nation" in instance_of:
                # write the country to countries.json
                countries_file.write(line)

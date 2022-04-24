import pandas as pd

# read each label sas file
# separate the variable and its label
# add its year
# convert to a dataframe
# write to a csv file


# Parses through label text file and separates the variable and its label.
# Returns a list of lists.
def parse_text(year):
    data = []
    with open(f"data/chis/{year}/ADULT_LABEL.SAS") as f:
        lines = f.readlines()
        # iterate through each line except the first and last line
        for line in lines[1:-1]:
            # remove whitespace and then split on "="
            l = line.strip().split("=")
            l[0] = l[0].strip()

            # Does not include columns that start with RAKED
            if l[0].startswith("RAKED") == False:
                # remove whitespace and then the double quotes
                l[1] = l[1].strip().strip('\"')
                data.append(l)

    return data


# Creates the list of lists to a dataframe and adds the year
# Returns the dataframe
def convert_to_dataframe(data, year):
    df = pd.DataFrame(data, columns=["Variable", "Label"])
    df["Year"] = year

    return df


if __name__ == "__main__":
    # Creates new empty dataframe with 3 columns: Variable, Label, and Year
    df = pd.DataFrame(columns=["Variable", "Label", "Year"])

    # List of years that we want
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]

    # Iterate through the years and parse each years ADULT_LABEL.SAS
    # Convert to another dataframe and then concatenate both into one
    for year in years:
        data = parse_text(year)
        df2 = convert_to_dataframe(data, year)
        df = pd.concat([df, df2])

    # Write to csv file
    df.to_csv("data/variables12to20.csv", index=False)

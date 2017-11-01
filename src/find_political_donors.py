import argparse

### Reads in data ###
def read(path="input/tests1/itcont.txt"):
    data = list()
    with open(path) as f:
        lines = f.readlines()
        for ind, l in enumerate(lines):
            l = l.split('|')

            ### Assumes IND KEY DICTIONARY ordering ###
            CMTE_ID = l[0]
            TRANSACTION_AMT = l[14]

            ### If Other is not empty or no ID or no AMT, skip ###
            if l[15] != '' or CMTE_ID == '' or TRANSACTION_AMT == '':
                continue
            ZIP = l[10]

            TRANSACTION_DT = l[13]

            ### Assures at least ZIP or Date is present ###
            if len(ZIP) >= 5 or len(TRANSACTION_DT) != "":
                data.append([CMTE_ID, ZIP[:5], TRANSACTION_AMT, TRANSACTION_DT])
    return data


def analyse(data=None, outpath1=None, outpath2=None):
    with open(outpath1, "w") as wf:
        ### Stores Zip and Date data as a dictionary where keys are (ID, ZIP) and (ID, DATE) respectively ###
        zip_data = dict()
        date_data = dict()

        ### For each donation, check if it is in the zip dictionary, if yes, update the count, median, and the total amount ###
        for donation in data:
            recip, zip, amt, date = donation[0], donation[1], donation[2], donation[3]
            # print donation
            if len(zip) >= 5:
                if (recip, zip) not in zip_data:
                    zip_data[(recip, zip)] = (int(amt), int(amt), 1)
                else:
                    new_count = zip_data[(recip, zip)][2] + 1
                    zip_data[(recip, zip)] = (int(round((int(amt)+zip_data[(recip, zip)][0])/2)), int(amt)+zip_data[(recip, zip)][1], new_count)


                ### Updates zip file ###
                wf.write('|'.join([recip, zip]+map(str, [zip_data[(recip, zip)][0], zip_data[(recip, zip)][2], zip_data[(recip, zip)][1]])))
                wf.write('\n')

            ### Adds the date file in a similar fashion ###
            if len(date) >= 5:
                if (recip, date) not in date_data:
                    date_data[(recip, date)] = (int(amt), int(amt), 1)
                else:
                    new_count = date_data[(recip, date)][2] + 1
                    date_data[(recip, date)] = (int(round((int(amt)+date_data[(recip, date)][0])/2)), int(amt)+date_data[(recip, date)][1], new_count)

    ### Write to the date file ###
    with open(outpath2, "w") as wf2:
        for key, val in date_data.iteritems():
            recip, date = key[0], key[1]
            wf2.write('|'.join([recip, date] + map(str, [val[0], val[2], val[1]])))
            wf2.write('\n')

if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required=True, type=str,
                    help="Input file path")
    ap.add_argument("-oz", "--out_zip", required=True, type=str,
                    help="Zip file output")
    ap.add_argument("-od", "--out_date", required=True, type=str,
                    help="Date file output")
    args = vars(ap.parse_args())

    data = read(args["input"])
    analyse(data, args["out_zip"], args["out_date"])
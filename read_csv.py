import pandas as pd
import config
#READ TABLES
com_el = pd.read_csv("com_el.csv")
srv_area = pd.read_csv("srv_area.csv")
freq = pd.read_csv("freq.csv")

#TO DO
#check if there is an asssociated space station

#merged_0 = adm_assoc.merge(freq)
merged_1 = freq.merge(srv_area, how='left', on='grp_id')
merged_2 = com_el.merge(merged_1, how='left', on='ntc_id')

f_11 = str(config.freq_mhz_1_min)
f_12 = str(config.freq_mhz_1_max)
f_1 = "(freq_mhz > " + f_11 +  " & freq_mhz < " + f_12 + ")"

f_21 = str(config.freq_mhz_2_min)
f_22 = str(config.freq_mhz_2_max)
f_2 = "(freq_mhz > " + f_21 +  " & freq_mhz < " + f_22 + ")"

f_31 = str(config.freq_mhz_3_min)
f_32 = str(config.freq_mhz_3_max)
f_3 = "(freq_mhz > " + f_31 +  " & freq_mhz < " + f_32 + ")"

f_41 = str(config.freq_mhz_4_min)
f_42 = str(config.freq_mhz_4_max)
f_4 = "(freq_mhz > " + f_41 +  " & freq_mhz < " + f_42 + ")"

f_51 = str(config.freq_mhz_5_min)
f_52 = str(config.freq_mhz_5_max)
f_5 = "(freq_mhz > " + f_51 +  " & freq_mhz < " + f_52 + ")"

f_61 = str(config.freq_mhz_6_min)
f_62 = str(config.freq_mhz_6_max)
f_6 = "(freq_mhz > " + f_61 +  " & freq_mhz < " + f_62 + ")"


def get_row(df, fr):
    group = df.query("(ntc_id != 118590034) & (sat_name == '"+ satellite_name +"') & (ntf_rsn == 'N') & ( "+ fr + ")")
    row = group[["sat_name" ,"beam_name", "stn_name", "freq_mhz"]]
    row = row.drop_duplicates()
    print(row)
    return row

def write_to_csv(array_dfs, f):
    for df in array_dfs:
        df.to_csv(f, index=False, header=False, mode="a")
    return 1

satellite_num = 0
f = "results.csv"
for satellite_name in config.satellite_names:
    print(satellite_name)
    row_1 = get_row(merged_2, f_1)
    row_2 = get_row(merged_2, f_2)
    row_3 = get_row(merged_2, f_3)
    row_4 = get_row(merged_2, f_4)
    row_5 = get_row(merged_2, f_5)
    row_6 = get_row(merged_2, f_6)
    print(row_2)
    if (satellite_num == 0 ):
        row_1.to_csv(f, index=False, header=True, mode="a")
        write_to_csv([row_2, row_3, row_4, row_5, row_6], f)
    else:
        write_to_csv([row_1, row_2, row_3, row_4, row_5, row_6], f)
    satellite_num = satellite_num + 1

import pandas as pd
import config
#READ TABLES
com_el = pd.read_csv("com_el.csv")
grp = pd.read_csv("grp.csv")
srv_area = pd.read_csv("srv_area.csv")

adm_assoc = pd.read_csv("adm_assoc.csv")
freq = pd.read_csv("freq.csv")

#TEST TABLES

#SELECT DISTINCT grp_id, freq_mhz, beam_name, sat_name, stn_name, ctry FROM freq, com_el WHERE (sat_name = "PAKTES-1") AND ((freq_mhz > 2070 AND freq_mhz < 2071) OR (freq_mhz > 2200 AND freq_mhz < 2290) OR (freq_mhz > 8025 AND freq_mhz < 8400) OR (freq_mhz > 24450 AND freq_mhz < 24650) OR (freq_mhz > 25250 AND freq_mhz < 27000) OR (freq_mhz > 32300 AND freq_mhz < 33000)) 


#TO DO
#check if there is an asssociated space station
print(grp.columns)
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

satellite_num = 0
f = "results.csv"
for satellite_name in config.satellite_names:
    print(satellite_name)
    query_results = merged_2.query("(ntc_id != 118590034) & (sat_name == '"+ satellite_name +"') & (ntf_rsn == 'N') & ( "+ f_1 + "|" + f_2 + "|" + f_3 +"|" + f_4 + "|" + f_5 + "|" + f_6 + ")")
    if (satellite_num == 0):
        query_results.to_csv(f, index=False, mode="w")
    else:
        query_results.to_csv(f, index=False, header=False, mode="a")     
    satellite_num = satellite_num + 1

import pandas as pd

#READ TABLES
com_el = pd.read_csv("com_el.csv")
grp = pd.read_csv("grp.csv")
srv_area = pd.read_csv("srv_area.csv")

adm_assoc = pd.read_csv("adm_assoc.csv")
freq = pd.read_csv("freq.csv")

#TEST TABLES
# tmp_results = com_el.query("sat_name == 'PAKTES-1'")
# print(tmp_results)
com_el = freq.query("ntc_id == 112541377 and wic_no > 0")
print(tmp_freq)

#MERGE TABLES
merged = pd.concat([grp, com_el, srv_area, adm_assoc, freq])

# SELECT DISTINCT com_el.ntc_id, adm, sat_name, emi_rcp, beam_name, grp.grp_id, ntf_rsn, freq_max, freq_min, srv_area.ctry FROM com_el, grp, srv_area WHERE ((com_el.ntc_id <> 118590034) AND (sat_name =  "PAKTES-1") AND (ntf_rsn = 'N') AND (com_el.ntc_id=grp.ntc_id)

#MAKE A QUERY
#results = com_el.query("sat_name == 'PAKTES-1'")

#PRINT TO CSV
tmp_freq.to_csv('results.csv', index=False)
#print(results)

# print(com_el.head())
# print(grp.head())

# print(merged.info(verbose=True))


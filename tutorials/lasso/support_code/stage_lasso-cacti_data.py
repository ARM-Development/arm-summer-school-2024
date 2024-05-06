"""
This code stages LASSO-CACTI data files on Cumulus's wolf2 that are needed for the LASSO tutorial portion of the 2024 ARM Summer School.
It is assumed the source of files is the master copy of pre-staged LASSO-CACTI data in cli120's world share area.

Author: William.Gustafson@pnnl.gov
Date: 6-May-2024
"""

import os
import shutil


#-----------------------------------------------------------------------
def copy_soundings(path_tutorial_stage):
    """
    Copy the CACTI sounding files into the tutorial staging folder.
    """
    path_lasso_soundings = "/gpfs/wolf2/arm/cli120/proj-shared/sey/cacti/obs/sonde/arm"
    path_staged_for_turorial = f"{path_tutorial_stage}/corsondewnpn"

    shutil.copytree(path_lasso_soundings, path_staged_for_turorial)
# end copy_soundings()


#-----------------------------------------------------------------------
def copy_taranis(path_tutorial_stage):
    """
    Copy the Taranis radar files into the tutorial staging folder.
    """
    path_taranis = "/gpfs/wolf2/arm/cli120/proj-shared/d3m088/cacti/data/taranis/merged_radar+sat_asof20210826"
    path_staged_for_turorial = f"{path_tutorial_stage}/taranis"

    shutil.copytree(path_taranis, path_staged_for_turorial)
# end copy_taranis()


#-----------------------------------------------------------------------
def copy_subset(sub_types, domains, dates, ens_members, config_label, path_lasso_stage, path_tutorial_stage):
    """
    Copy the requested CACTI subset files into the tutorial staging folder for the specified combinations.
    
    NOTE: All the simulation selection parameters are sent as lists EXCEPT for config_label.
    """
    dir_orig = os.getcwd()
    os.chdir(path_lasso_stage)

    for domain in domains:
        scale = "meso" if domain < 3 else "les"
        for date in dates:
            for ens_member in ens_members:
                for sub_type in sub_types:
                    src = f"{date}/{ens_member}/{config_label}/{scale}/subset_d{domain}/corlasso_{sub_type}_*"
                    dst = f"{path_tutorial_stage}/lasso-cacti/"
                    cmd = f"rsync --relative {src} {dst}"
                    os.system(cmd)

    os.chdir(dir_orig)
# end copy_subset()


#-----------------------------------------------------------------------
def main():
    path_lasso_stage = "/gpfs/wolf2/arm/cli120/world-shared/d3m088/cacti/staged_runs"
    path_tutorial_stage = "/gpfs/wolf2/arm/atm124/world-shared/arm-summer-school-2024/lasso_tutorial/cacti"

    ### --- sections that are already copied have been commented out --- ###

    # Observation files...
    # copy_soundings(path_tutorial_stage)
    # copy_taranis(path_tutorial_stage)

    # Simulation files...
    # First, copy all the domain 2 subset files for stat, met, cld, cldhamsl
    dates = [
        "20181026", 
        "20181104",
        "20181105",
        "20181106",
        "20181110",
        "20181121",
        "20181129",
        "20181130",
        "20181204",
        "20181205",
        "20181219",
        "20190122",
        "20190123",
        "20190125",
        "20190129",
        "20190131",
        "20190208",
        "20190223",
        "20190314",
        "20190315",
    ]
    ens_members = [
        "eda00",
        "eda01",
        "eda02",
        "eda03",
        "eda04",
        "eda05",
        "eda06",
        "eda07",
        "eda08",
        "eda09",
        "era5",
        "fnl",
        "gefs00",
        "gefs01",
        "gefs02",
        "gefs03",
        "gefs04",
        "gefs05",
        "gefs06",
        "gefs07",
        "gefs08",
        "gefs09",
        "gefs10",
        "gefs11",
        "gefs12",
        "gefs13",
        "gefs14",
        "gefs15",
        "gefs16",
        "gefs17",
        "gefs18",
        "gefs19",
        "gefs20",
    ]
    config_label = "base"
    subset_types = ["stat", "met", "methamsl", "cld", "cldhamsl"]
    # copy_subset(sub_types=subset_types, domains=[2], dates=dates, ens_members=ens_members, config_label=config_label,
    #             path_lasso_stage=path_lasso_stage, path_tutorial_stage=path_tutorial_stage)
    
    # Next, copy full set of domains 1, 2, 3, & 4 subset files for stat, met, cld, cldhamsl.
    # We only want a small number of these.
    dates = [
        "20190208",
    ]
    ens_members = [
        "eda03",
    ]
    config_label = "morr"
    domains = [1, 2, 3, 4]
    subset_types = ["stat", "met", "methamsl", "cld", "cldhamsl"]
    # copy_subset(sub_types=subset_types, domains=domains, dates=dates, ens_members=ens_members, config_label=config_label,
    #             path_lasso_stage=path_lasso_stage, path_tutorial_stage=path_tutorial_stage)

# end main()


#-----------------------------------------------------------------------
if __name__ == "__main__":
    main()

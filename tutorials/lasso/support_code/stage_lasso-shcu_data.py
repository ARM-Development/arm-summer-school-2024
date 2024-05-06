"""
This code stages LASSO-ShCu data files on Cumulus's wolf2 that are needed for the LASSO tutorial portion of the 2024 ARM Summer School.
It is assumed the LASSO-ShCu tar files are pre-copied into a single directory to draw from to build out an organized tree structure.

Author: William.Gustafson@pnnl.gov
Date: 6-May-2024
"""

from glob import glob
import os
import tarfile


#-----------------------------------------------------------------------
def stage_cogsdiagobsmod(tarfilename, path_stage):
    """
    Stage tar file of type sgplassocogsdiagobsmod*tar.
    This tar contain info for all sim IDs within the given case date and
    already has the case date in the tar file. So, it's untar path starts
    at the very top of the tree structure.

    Example: ./sgplassocogsdiagobsmodC1.m1.20190404.120000.tar
               0123456789012345678901234567890
                       987654321098765432109876543210987654321
    """

    # Untar the source tar into the destination folder...
    fh = tarfile.open(tarfilename, mode='r')
    fh.extractall(path=path_stage)
    fh.close()

# end stage_cogsdiagobsmod()


#-----------------------------------------------------------------------
def stage_confobsmod(tarfilename, path_stage):
    """
    Stage tar file of type sgplassoconfobsmod*tar.
    This tar does not contain the parent directory information, so we
    have to build it.

    Example: ./sgplassodiagconfobsmod4C1.m1.20190404.000000.tar
               0123456789012345678901234567890
                        987654321098765432109876543210987654321
    """

    # Determine path for untarring and create it if it does not exist...
    aa = os.path.basename(tarfilename)  # strip off path
    datestr = aa[-19:-11]  # date comes from the end of the filename
    sim_id = int( os.path.basename(aa)[22:(aa.index("C1.m1"))] )  # sim_id is the character(s) prior to C1.m1
    path_untar = f"{path_stage}/{datestr}/sim{sim_id:04d}"
    os.makedirs(path_untar, exist_ok=True)

    # Untar the source tar into the destination folder...
    fh = tarfile.open(tarfilename, mode='r')
    fh.extractall(path=path_untar)
    fh.close()
# end stage_confobsmod()


 #-----------------------------------------------------------------------
def stage_diagraw(tarfilename, path_stage):
    """
    Stage tar file of type sgplassodiagraw*.tar.
    This tar does not contain the parent directory information, so we
    have to build it.

    Example: ./sgplassodiagraw1C1.m1.20190506.000000.tar
               0123456789012345678901234567890
                 987654321098765432109876543210987654321
    """
    
    # Determine path for untarring and create it if it does not exist...
    aa = os.path.basename(tarfilename)  # strip off path
    datestr = aa[-19:-11]  # date comes from the end of the filename
    sim_id = int( os.path.basename(aa)[15:(aa.index("C1.m1"))] )  # sim_id is the character(s) prior to C1.m1
    path_untar = f"{path_stage}/{datestr}/sim{sim_id:04d}"
    os.makedirs(path_untar, exist_ok=True)

    # Untar the source tar into the destination folder...
    fh = tarfile.open(tarfilename, mode='r')
    fh.extractall(path=path_untar)
    fh.close()
# end stage_diagraw()


#-----------------------------------------------------------------------
def stage_highfreqobs(tarfilename, path_stage):
    """
    Stage tar file of type sgphighfreqobs*tar.
    This tar contain observation data organized by folder with each tar
    containing the obs for a single date. These get untarred into a
    high_res_obs folder inside the case date.

    Example: ./sgplassohighfreqobsC1.m1.20190404.120000.tar
               0123456789012345678901234567890
                    987654321098765432109876543210987654321
    """
    # Determine path for untarring and create it if it does not exist...
    aa = os.path.basename(tarfilename)  # strip off path
    datestr = aa[-19:-11]  # date comes from the end of the filename
    path_untar = f"{path_stage}/{datestr}/high_res_obs"
    os.makedirs(path_untar, exist_ok=True)

    # Untar the source tar into the destination folder...
    fh = tarfile.open(tarfilename, mode='r')
    fh.extractall(path=path_untar)
    fh.close()
# end stage_highfreqobs()
 


#-----------------------------------------------------------------------
def main():
    path_tars = "/gpfs/wolf2/arm/atm124/world-shared/arm-summer-school-2024/lasso_tutorial/ShCu/tars"
    path_stage = "/gpfs/wolf2/arm/atm124/world-shared/arm-summer-school-2024/lasso_tutorial/ShCu/test2"

    # Get the list of tar files to process and loop over them...
    tar_list = glob(f"{path_tars}/*.tar")
    for tarfilename in tar_list:
        # Parse the datastream type and call the appropriate subroutine to untar it...
        # File type options:
        #   sgplassocogsdiagobsmodC1.m1.20190404.120000.tar
        #   sgplassodiagconfobsmod4C1.m1.20190404.000000.tar
        #   sgplassodiagraw5C1.m1.20190404.000000.tar
        #   sgplassohighfreqobsC1.c1.20190404.000000.tar
        #   0         1         2         3
        #   0123456789012345678901234567890
        #           0123456789012345678901234567890
        aa = os.path.basename(tarfilename)
        if not aa[0:8] == "sgplasso":
            # not a tar we care about, so skip it
            continue
        # end if
        aa = aa[8:]  # strip off "sgplasso", should now start with the keys we are looking for

        # Call the appropriate staging routine for each tar type to 
        # account for the folder structure in each type...
        if aa[:14] == "diagconfobsmod":
            stage_confobsmod(tarfilename, path_stage)

        elif aa[:7] == "diagraw":
            stage_diagraw(tarfilename, path_stage)

        elif aa[:14] == "cogsdiagobsmod":
            stage_cogsdiagobsmod(tarfilename, path_stage)

        elif aa[:11] == "highfreqobs":
            stage_highfreqobs(tarfilename, path_stage)
        # end if            
# end main()


#-----------------------------------------------------------------------
if __name__ == "__main__":
    main()

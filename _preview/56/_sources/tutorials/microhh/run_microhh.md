Running MicroHH
-------

MicroHH is a computational fluid dynamics code made for Direct Numerical Simulation (DNS) and Large-Eddy Simulation of turbulent flows in the atmospheric boundary layer. The code is written in C++.

A tutorial and documentation is available at: https://microhh.readthedocs.io/en/latest/.

MicroHH is described in detail in [Van Heerwaarden et al. (2017)](http://www.geosci-model-dev-discuss.net/gmd-2017-41/#discussion).

Downloading the code
--------------------
General information to download the code from GitHub can be found here:
    https://github.com/microhh/microhh/blob/main/README.md

For this tutorial, we will use Thijs' fork, and in particular the `lagtraj` branch:
        git clone --recurse-submodules https://github.com/thijsheus/microhh.git

More details on how to compile and setup the code on your own can be found in the main README

Logging in to OSC
-----------------

To run this tutorial, we first log in on the Ohio Super Computer through:
    ondemand.osc.edu
and log in with the username that you got before the workshop.

From the side bar, select the *Ascend Desktop* to get in-browser access to the supercomputer.

Give the app a moment to start up, open it, and open a VNC window.

Quick Start to Running MicroHH
------------------------------

At the desktop, open a terminal and navigate to the summerschool folder:

    cd /fs/project/PFS0220/summerschool
make your own folder, and copy all relevant data to your own folder:
    
    cp template/* <yourname>/
and move to your own folder.

To submit a quick simulation to the supercomputer, you can submit a job to the queue:
    sbatch SGP.slurm


Changing the input parameters
-----------------------------
The input parameters are in `SGP.ini`. Feel free to browse through and look at what can be easily changed. More info on individual options is available on 
https://microhh.readthedocs.io/en/latest/


After the simulation is done, you can evaluate the results, for instance with the `analyze_microhh.ipynb` script.

Selecting particular ERA5 use cases (Advanced and Experimental):
---------------------
The eulerian_lagtraj.py code is based on the lagtraj Python package and pulls ERA5 data to drive the LES model. This is a bit too time consuming for the current tutorial, but the gist is as follows:

1. Open `config.yaml` to set the location, time, name, etc. Note that you can elect to use a Eulerian (fixed in space) setup, or a Lagrangian (moving along with the atmospheric flow) setup. A Lagrangian setup over land is not recommended.
1. Open `SGP.ini.base` to setup the case properties, such as domain size, grid points, etc. You can fill out `None` for anything that you want the system to decide
1. Run the python script: `python eulerian_lagtraj.py`
1. Initialize MicroHH following the instructions above.

    
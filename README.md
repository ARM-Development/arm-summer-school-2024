# ARM Summer School 2024

## ARM Summer School Focused on Open Science in the Department of Energy's Atmospheric Radiation Measurement (ARM) User Facility: Connecting State-of-the-Art Models with Diverse Field Campaign Observations


[![badge](https://img.shields.io/static/v1.svg?logo=Jupyter&label=ARM+JupyterHub&message=ACE+Environment&color=blue)](https://jupyterhub.arm.gov/hub/user-redirect/git-pull?repo=https%3A//github.com/ARM-Development/arm-ams-short-course-2024&urlpath=lab/tree/arm-ams-short-course-2024/notebooks&branch=main)
[![nightly-build](https://github.com/ARM-Development/arm-ams-short-course-2024/actions/workflows/nightly-build.yaml/badge.svg)](https://github.com/ARM-Development/arm-ams-short-course-2024/actions/workflows/nightly-build.yaml)
[![Binder](https://binder.projectpythia.org/badge_logo.svg)](https://binder.projectpythia.org/v2/gh/ARM-Development/arm-ams-short-course-2024/main?labpath=notebooks)

## Motivation

ARM Mobile Facilities (AMF) have traveled to locations all over the world, including South America for the Cloud, Aerosol, and Complex Terrain Interactions (CACTI) field campaign, as well as Norway for the Cold-Air Outbreaks in the Marine Boundary Layer Experiment (COMBLE). One of the key goals of these field deployments is to integrate measurements with a spectrum of model datasets, ranging from high-resolution large-eddy simulation to limited-domain nested weather and climate model datasets, furthering the understanding of Earth’s climate system. Within this tutorial, participants will gain a broad understanding of the ARM User Facility, the open data available to the community, the data workbench that allows data-proximate-computing, and science overviews of two ongoing model-observation intercomparison projects. This will be suitable for a broad audience of atmospheric scientists, bringing together both observations and simulations, as well as deep and shallow convection.

This summer school, aimed at a broad audience, will: 
1. Introduce participants to ARM’s observational facilities and data products and the community of atmospheric scientists that use and produce ARM data. 
2. Educate attendees on ARM’s measurement suite and data archive.
3. Educate attendees on ARM’s (and collaborators') model data.
4. Highlight the underlying science behind CACTI and COMBLE.
5. Demonstrate how to find and access ARM data.
6. Using open source tools, guide attendees in analyzing ARM’s open data in the Python programming language. 
7. Highlight several techniques to compare ARM observations and high-resolution model output. 


## Authors

[Max Grover](@mgrover1), [Scott Collis](https://github.com/scollis)

### Contributors

<a href="https://github.com/ProjectPythia/cookbook-template/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ARM-Development/arm-ams-short-course-2024" />
</a>

## Structure

To familiarize attendees with ARM, its measurements and data discovery systems.
1. To highlight the breadth of measurements and science possible through the AMF deployments for CACTI and COMBLE.
2. To demonstrate a series of analytical methods using open science cookbooks and ARM data, with a focus on robustly comparing observational data with high-resolution simulations. 
3. To provide an onramp to open science using ARM data and to remove barriers to using ARM data. 
4. To train attendees on the latest features of ARM tools and open HPC platforms.

### Lectures

### Small Group Projects

## Running the Notebooks

You can either run the notebook using [Binder](https://binder.projectpythia.org/) or on your local machine.

### Running on Jupyter

The simplest way to interact with a Jupyter Notebook is through the
[ARM Jupyter](https://jupyterhub.arm.gov), which enables the execution of a
[Jupyter Book](https://jupyterbook.org) on ARM infrastructure. The details of how this works are not
important for now. Navigate your mouse to
the top right corner of the book chapter you are viewing and click
on the rocket ship icon, (see figure below), and be sure to select
“launch Jupyterhub”. After a moment you should be presented with a
notebook that you can interact with. I.e. you’ll be able to execute
and even change the example programs. You’ll see that the code cells
have no output at first, until you execute them by pressing
{kbd}`Shift`\+{kbd}`Enter`. Complete details on how to interact with
a live Jupyter notebook are described in [Getting Started with
Jupyter](https://foundations.projectpythia.org/foundations/getting-started-jupyter.html).

### Running on Your Own Machine
If you are interested in running this material locally on your computer, you will need to follow this workflow:

1. Clone the `https://github.com/ARM-Development/arm-summer-school-2024` repository:

   ```bash
    git clone https://github.com/ARM-Development/arm-summer-school-2024
    ```  
1. Move into the `arm-summer-school-2024` directory
    ```bash
    cd arm-summer-school-2024
    ```  
1. Create and activate your conda environment from the `environment.yml` file
    ```bash
    conda env create -f environment.yml
    conda activate arm-summer-school-2024-dev
    ```  
1.  Move into the `notebooks` directory and start up Jupyterlab
    ```bash
    cd notebooks/
    jupyter lab
    ```

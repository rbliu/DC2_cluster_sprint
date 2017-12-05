# DC2_cluster_sprint

This repository is used to describe work done during the Argonne Sprint/Hack week (Dec 2017). We plan to run DM stack ([obs_file](https://github.com/rbliu/Memo-Linux/blob/master/how_to_run_obs_file.md)) on protoDC2 images to make shape measurements at pixel level.

*Contributor: Ian Dell'Antonio, Binyang Liu, Bhishan Poudel*

## Quick Start

- [Install DM Stack with v13.0 (or 12.0) version](https://pipelines.lsst.io/v/13-0/install/conda.html)

- [Clone and build obs_file](https://github.com/rbliu/Memo-Linux/blob/master/how_to_run_obs_file.md)

- To access the protoDC2 catalog, log in to nersc: https://jupyter.nersc.gov and follow this [tutorial notebook](https://github.com/LSSTDESC/gcr-catalogs/blob/master/examples/GCRCatalogs%20Demo.ipynb)



## TODO List:

- [x] Get some preliminary protoDC2 images. (Keep tracking this issue:https://github.com/LSSTDESC/DC2_Repo/issues/33)

- [ ] [Initial tests](https://github.com/rbliu/DC2_cluster_sprint/issues/1) with one single sensor to obtain feasible configurations.

- [ ] Tests with one single raft to check if the measurements in each sensor look reasonable.

- [ ] Run obs_file on more rafts.

- [ ] Plot mass map with shear measurements.

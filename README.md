# HMM-based-Selectivity-Estimation

This is the repository for my unsuccessful project on HMM-based selectivity estimation. The idea is to use HMM to model the selectivity of a query for predicates specifically '%x%y%z%' type predicates. The project performs well results for some type of queries but not for all. You can check the [report](/HMM-based-Selectivity-Estimation.pdf) for more details.

The repository contains also the DBLP author dataset and sampled versions of it that are used in my experiments.
You can analyze or develop the codes of my algorithm to improve it. Main code of the algorithm is under the double-hmm folder. Experiment files and dataset files are under the dblp-dataset folder.

The methodology can be improved in further studies by trying to find better optimization for the parameters of HMM model.
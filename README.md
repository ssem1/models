![image](https://user-images.githubusercontent.com/17502298/51855300-e6bfab00-22fa-11e9-9386-5b4be49bddea.png)

# malgo models

This repo is dedicated to the Machine Learning models that power the malgo toolset. Our current focus is implementing models for PoC and studying the various industry standards on usage. Eventually these models will be implemented and used for the build in-progress web application over in the main malgo repo. We also perform options modeling in this repo and plan on producing useful models for option pricing, profit modeling, etc.

Approved models by the core malgo team will be included in the API for subsequent rollouts to the malgo web application. Approved models will be implemented in the order they are approved.

## Getting Started

Recommend using [Anaconda](https://www.anaconda.com/distribution/). Also pip install numpy matplotlib scipy scikit-learn h5py tensorflow keras fbprophet should cover all needed libraries for use in this part of the repo. If you're playing with the models and find a missing dependency please open a PR.

For questions or discussions: [![Discord](https://user-images.githubusercontent.com/7288322/34471967-1df7808a-efbb-11e7-9088-ed0b04151291.png)](https://discord.gg/YzeEJ4)

### Prerequisites

Any additional dependencies are outlined within the model you're toying with, papers should always be made available in .pdf and .tex (no exceptions)

### Contributions

We love contributors and any models you build can be included via Pull Requests; review will occur ASAP

Over time, models will become out-of-date as no features are added to libraries and standard usage. Updates are encouraged. We are also heavily lacking on documentation outlining the functionality and performance of each model. This documentation would be great in the form of a short research paper or medium article. The goal is to separate papers and studies from models, but if a paper accompanies a model free to keep them together

Standard model output is a list of values. You can easily grab a column of output data from a dataframe using Pandas. This list will then be the input to API.py. 

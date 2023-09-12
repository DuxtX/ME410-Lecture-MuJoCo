## 1. Install Python (skip if you already have Python installed)
1. Download and install [Anaconda](https://www.anaconda.com/download) from their official website: 
	 - [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) also works for less disk space consumption;
	 - Install with all default settings;
## 2. Download MuJoCo package
1. Download the package from MuJoCo official website [https://github.com/google-deepmind/mujoco/releases](https://github.com/google-deepmind/mujoco/releases)
2. Unzip the package, you should be able to run the simulator GUI in './bin/simulate.exe'

## 3. Install MuJoCo Python bindings
1. Open the Anaconda Prompt from Start menu;
2. Create a new environment using the command below:
	`conda create --name mujoco python=3.9`
3. Activate the environment using the command below:
	`conda activate mujoco`
4. Install required libraries:

	Use the commands below to install all required libraries, run lines one by one:
	```
	conda install scipy
	conda install matplotlib
	pip install mujoco
	```
5. Now MuJoCo is ready for use.
6. Download the MuJoCo GUI package using the link: [https://github.com/google-deepmind/mujoco/releases](https://github.com/google-deepmind/mujoco/releases
7. Now MuJoCo is ready for use.

## Useful links:
1. MuJoCo official document: [https://mujoco.readthedocs.io/en/latest/overview.html](https://mujoco.readthedocs.io/en/latest/overview.html);
2. Anaconda installation document: [https://docs.anaconda.com/free/anaconda/install/index.html](https://docs.anaconda.com/free/anaconda/install/index.html)
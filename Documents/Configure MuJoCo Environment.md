## 1. Install Python (skip if you already have Python installed)
1. Install [Anaconda](https://www.anaconda.com/download) from their official website: 
	 - [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) also works for less disk consumption;
	 - Install with all default settings;
## 2. Install MuJoCo Environment
1. Open the Anaconda Prompt from Start menu;
2. Create a new environment using the command below:
	`conda create --name mujoco python=3.9`
3. Activate the environment using the command below:
	`conda activate mujoco`
4. Install required libraries:
	Use the commands below to install all required libraries, run lines one by one:
	`conda install scipy`
	`conda install matplotlib`
	`pip install mujoco`
5. Download the MuJoCo GUI package using the link: [https://github.com/google-deepmind/mujoco/releases](https://github.com/google-deepmind/mujoco/releases
6. Now MuJoCo is ready for use.


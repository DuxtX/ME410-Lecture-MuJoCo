## 1. Install Python (skip if you already have Python installed)
Download and install [Anaconda](https://www.anaconda.com/download) from their official website: 
- [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) also works for less disk space consumption;
- Install with all default settings;
## 2. Download MuJoCo package
1. Download the package from MuJoCo official website [https://github.com/google-deepmind/mujoco/releases](https://github.com/google-deepmind/mujoco/releases), select the correct version based on your operating system.

   For Windows, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-windows-x86_64.zip);
   
   For Mac OS, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-macos-universal2.dmg);
   
   For Linux, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-linux-aarch64.tar.gz).
2. Run the 'simulate' application in the package to start the simulator GUI:
   
   For Windows, unzip the package, the application is located in './bin/simulate.exe';

   For Mac OS, double-click the '.dmg' package, the application is located under the root folder.

## 3. Install MuJoCo Python bindings
1. Open the Anaconda Prompt from the Start menu;
2. Create a new environment using the command below:
	`conda create --name mujoco python=3.9`
3. Activate the environment using the command below:
	`conda activate mujoco`
4. Install required dependencies:

	Use the commands below to install all required libraries, and run lines one by one:
	```
	conda install scipy
	conda install matplotlib
	pip install mujoco
	```
5. Now MuJoCo is ready for use.

## Useful links:
1. MuJoCo official document: [https://mujoco.readthedocs.io/en/latest/overview.html](https://mujoco.readthedocs.io/en/latest/overview.html);
2. Anaconda installation document: [https://docs.anaconda.com/free/anaconda/install/index.html](https://docs.anaconda.com/free/anaconda/install/index.html)

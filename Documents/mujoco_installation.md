# MuJoCo Installation

## 1. Install Python (skip to Step 2.4 if you already have Python installed)
1. Download and install [Anaconda](https://www.anaconda.com/download) from their official website: 

   * [miniconda](https://docs.conda.io/projects/miniconda/en/latest/) also works with less disk space consumption;
   * Install with all default settings;
2. Initialize conda in terminal (you may skip this step if you are not familiar with the system terminal configuration)
   
   * Windows: 
  
     1. Open Anaconda Powershell Prompt from Start Menu;
     2. Run command:
		```
		conda init powershell
		```
     3. Close the prompt, open Windows Powershell, input `conda --version`, should return the version of the conda like: "conda 23.7.3";
   * MacOS:
  
     1. Open the zsh terminal and run commands below:
		```
		# Replace <PATH_TO_CONDA> with the path to your conda install
		source <PATH_TO_CONDA>/bin/activate
		conda init
		```
     2. Close the terminal and reopen, input `conda --version`, should return the version of the conda like: "conda 23.7.3";
     3. More details can be found at [Link](https://docs.anaconda.com/free/anaconda/install/mac-os/#:~:text=If%20you%20are%20on%20macOS,!%E2%80%9D)

<div class="page"/>

## 2. Install MuJoCo Python bindings
1. Open the Powershell in Windows, or terminal in Mac; Or use the Anaconda Prompt if you skipped the Step 1.2;
2. Create a new environment using the command:
	```
	conda create --name mujoco python=3.9
	```
3. Activate the environment using the command:
	```
	conda activate mujoco
	```
	**You should run this command to activate the environment every time when a new terminal is opened.**

	To deactivate the environment **(after use, not now)**, run command:
	```
	conda deactivate
	```

4. Install required dependencies:

	Use the commands below to install all required libraries, run lines one by one:
	```
	pip install scipy
	pip install matplotlib
	pip install mujoco
	```
5. Now MuJoCo is ready for use.

## 3. Download MuJoCo package
1. Download the package from MuJoCo official website [https://github.com/google-deepmind/mujoco/releases](https://github.com/google-deepmind/mujoco/releases), select the correct version based on your operating system.

   For Windows, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-windows-x86_64.zip);
   
   For Mac OS, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-macos-universal2.dmg);
   
   For Linux, download using [Link](https://github.com/google-deepmind/mujoco/releases/download/2.3.7/mujoco-2.3.7-linux-aarch64.tar.gz).

2. Run the 'simulate' application in the package to start the simulator GUI:
   
   For Windows, unzip the package, the application is located in './bin/simulate.exe';

   For Mac OS, double-click the '.dmg' package, the application is located under the root folder.

## Useful links:
1. MuJoCo official document: [https://mujoco.readthedocs.io/en/latest/overview.html](https://mujoco.readthedocs.io/en/latest/overview.html);
2. Anaconda installation document: [https://docs.anaconda.com/free/anaconda/install/index.html](https://docs.anaconda.com/free/anaconda/install/index.html)

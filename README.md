# Automated Testing with Python

Just a project with what I'm coding along while going through [a course about Automated Testing with Python](https://www.udemy.com/course/automated-software-testing-with-python/).

## Environment Setup

I'm using [Anaconda](https://www.anaconda.com) to manage my python packages. You can download it [here](https://www.anaconda.com/distribution/). Once you have it installed, you can run the following commands to setup your environment.

```bash
# Creates a conda environment with all required libraries
conda create -n automated-testing --file env.yml

# Activates the created environment
conda activate automated-testing

#Install packages not available in Conda
pip install Flask-JWT
```

## Interesting Stuff

### Windows Subsystem Linux (WSL)

[Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

```bash
# Starts SSH-agent and adds key to it.
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

### Anaconda

```bash
# Updates base conda
conda update -n base -c defaults conda

# Creates conda env for this project
conda create -n automated-testing --file env.yml

# Creates file with installed packages
# * The '--from-history' switch lists only packages installed by the user, so dependencies can be
# figured out automatically.
# * The 'grep' command is to remove the 'prefix' attribute from the yml.
conda env export -n automated-testing --from-history | grep -v "^prefix: " > env.yml

```

More at [managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

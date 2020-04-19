# Automated Testing with Python

For now, this is just a project to learn about automated testing with Python.

## Environment Setup

I'm using [Anaconda](https://www.anaconda.com) to manage my python packages. You can download it [here](https://www.anaconda.com/distribution/). Once you have it installed, you can run the following commands to setup your environment.

```bash
# Creates a conda environment with all required libraries
conda create -n automated-testing --file env.yml

# Activates the created environment
conda activate automated-testing
```

## Interesting Stuff

### Windows Subsystem Linux (WSL)

[Developing in WSL](https://code.visualstudio.com/docs/remote/wsl)

### Anaconda

```bash
# Updates base conda
conda update -n base -c defaults conda

# Creates conda env for this project
conda create -n automated-testing --file env.yml

# Creates file with installed packages
# * --from-history switch lists only packages installed by the user, so dependencies can be figured 
# out automatically.
# * the grep command is to remove the "prefix"
conda env export -n automated-testing --from-history | grep -v "^prefix: " > env.yml

```

More at [managing conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

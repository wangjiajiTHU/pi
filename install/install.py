import subprocess

# Create a new Conda environment named "pino"
# subprocess.run(["conda", "create", "-n", "pino", "-y"])

# Activate the "pino" environment
subprocess.run(["conda", "activate", "pino"])

# List of packages to install
packages = [
    "wandb",
    "tqdm",
    "scipy",
    "h5py",
    "numpy",
    "tensorflow==2.4.0",
]

# Install packages
for package in packages:
    subprocess.run(["conda", "install", "-y", package])

# Install PyTorch with GPU acceleration
subprocess.run(["conda", "install", "-y", "pytorch", "torchvision", "torchaudio", "cudatoolkit=10.2", "-c", "pytorch"])

# Install DeepXDE from PyPI
subprocess.run(["pip", "install", "DeepXDE"])

# Install the latest code from tensordiffeq's GitHub master branch
subprocess.run(["pip", "install", "git+https://github.com/tensordiffeq/tensordiffeq.git"])

# EpiblastOrientationMaps

Repository analyzing epiblast orientation maps supporting
- _"Boundary-guided cell alignment drives mouse epiblast maturation."_ by T. Ichikawa, P. C. Guruciaga, S. Hu, S. Plunder, M. Makino, M. Hamaji, A. Stokkermans, S. Yoshida, A. Erzberger, T. Hiiragi.
- _"Boundary geometry controls a topological defect transition that determines lumen nucleation in embryonic development"_ by P. C. Guruciaga, T. Ichikawa, S. Plunder, T. Hiiragi, A. Erzberger.

## System Requirements

### Software Dependencies
- Python 3.7 or higher
- Jupyter Notebook environment
- Python packages:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scipy
  - tqdm
  - more_itertools
  - statannotations
  - nbformat (for notebook imports)

### Operating Systems
- MacOS 18.5
- Windows 11
- Linux Mint

### Hardware Requirements
- Standard desktop computer with at least 4GB RAM

## Installation Guide

### Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/username/EpiblastOrientationMaps.git
   cd EpiblastOrientationMaps
   ```

2. Install required dependencies (with pip or conda):
   ```bash
   pip install numpy pandas matplotlib seaborn scipy tqdm more_itertools statannotations nbformat
   ```

### Typical runtime
Analysis of the orientation maps takes < 10 minutes on a standard desktop computer.

## Demo

### Running the Analysis
1. Open one of the analysis notebooks:
   - `wildtype_analysis.ipynb`: For analyzing wildtype data
   - `demo_analysis.ipynb`: For analyzing a demonstration dataset
   - `analysis_tools.ipynb`: Contains shared functions and utilities

2. Execute the cells in order by pressing Shift+Enter or by clicking the "Run" button in the Jupyter interface

3. The notebooks will generate visualizations and analysis results based on the epiblast orientation maps

### Example Usage
```python
# Run the analysis tools notebook to load common functions
%run demo_analysis.ipynb

# Load and process your data
# (See specific notebooks for detailed examples)
```

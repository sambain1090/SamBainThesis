Github repository for my thesis

## Python environment

Create and activate the Conda environment from the repository root:

```bash
conda env create -f environment.yml
conda activate thesis
```

Verify that Ultralytics is installed:

```bash
python -c "import ultralytics; print(ultralytics.__version__)"
```

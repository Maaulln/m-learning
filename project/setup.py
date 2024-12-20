from setuptools import setup, find_packages

setup(
    name="pump_predictor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.24.3",
        "pandas>=2.0.2",
        "scikit-learn>=1.2.2",
        "xgboost>=1.7.5",
        "matplotlib>=3.7.1",
        "seaborn>=0.12.2",
        "joblib>=1.2.0",
    ],
    python_requires=">=3.8",
)
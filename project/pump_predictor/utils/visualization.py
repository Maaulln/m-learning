import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from typing import Dict, List

def plot_feature_importance(importance_dict: Dict[str, float], title: str, feature_names: List[str] = None) -> None:
    """
    Plot feature importance scores
    
    Args:
    importance_dict (Dict[str, float]): Dictionary of feature importances
    title (str): Title of the plot
    feature_names (List[str], optional): Custom feature names to use instead of the keys in importance_dict
    """
    plt.figure(figsize=(10, 6))
    
    if feature_names:
        # Create a new dictionary with custom feature names
        importance_dict = dict(zip(feature_names, importance_dict.values()))
    
    importance_df = pd.DataFrame(
        importance_dict.items(),
        columns=['Feature', 'Importance']
    ).sort_values('Importance', ascending=True)
    
    sns.barplot(data=importance_df, y='Feature', x='Importance')
    plt.title(title)
    plt.tight_layout()
    plt.show()
    
def plot_confusion_matrix(y_true, y_pred, title: str) -> None:
    """Plot confusion matrix"""
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        pd.crosstab(y_true, y_pred, normalize='index'),
        annot=True,
        fmt='.2%',
        cmap='Blues'
    )
    plt.title(title)
    plt.tight_layout()
    plt.show()
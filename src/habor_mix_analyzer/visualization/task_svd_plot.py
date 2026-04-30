import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

def generate_task_svd_plot():
    df = pd.read_csv('data/processed/intermediate/task_imputed_matrix.csv')
    X_df = df.select_dtypes(include=[np.number])
    
    bad_cols = X_df.columns[(X_df.max() > 2) | (X_df.min() < -1)]
    good_cols = [c for c in X_df.columns if c not in bad_cols]
    X = X_df[good_cols].values
    
    variances = X.var(axis=0)
    mask = variances > 0
    X_filtered = X[:, mask]
    
    eps = 0.005
    X_smoothed = np.clip(X_filtered, eps, 1 - eps)
    X_logit = np.log(X_smoothed / (1 - X_smoothed))
    
    pca = PCA()
    pc_scores = pca.fit_transform(X_logit)
    
    plt.figure(figsize=(8, 6))
    
    is_model = df['agent'] == 'terminus-2'
    
    n_tasks = X_filtered.shape[1]

    plt.scatter(
        pc_scores[is_model, 0], pc_scores[is_model, 1],
        c='#1f77b4', label='Baseline (Terminus-2)', s=150, alpha=0.8, marker='o'
    )
    plt.scatter(
        pc_scores[~is_model, 0], pc_scores[~is_model, 1],
        c='#ff7f0e', label='Advanced Scaffold', s=150, alpha=0.8, marker='s'
    )

    for i in range(len(df)):
        if is_model.iloc[i]:
            model_name = df.iloc[i]['model']
            agent_idx = df[(df['model'] == model_name) & (df['agent'] != 'terminus-2')].index
            if len(agent_idx) > 0:
                j = agent_idx[0]
                plt.plot(
                    [pc_scores[i, 0], pc_scores[j, 0]],
                    [pc_scores[i, 1], pc_scores[j, 1]],
                    'k--', alpha=0.3
                )

    plt.title(f'Task-Level PCA ({n_tasks:,} tasks): PC1 vs PC2')
    plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% Variance) — General Capability')
    plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% Variance) — Agent Effect')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    out_dir = 'figs/appendix/quantitative'
    os.makedirs(out_dir, exist_ok=True)
    plt.savefig(f'{out_dir}/task_level_pca.png', dpi=300, bbox_inches='tight')
    print(f"Saved to {out_dir}/task_level_pca.png")

if __name__ == '__main__':
    generate_task_svd_plot()

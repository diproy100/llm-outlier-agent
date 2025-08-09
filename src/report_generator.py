import pandas as pd
import os

def save_report(df, output_path="data/outliers_with_explanations.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Report saved to: {output_path}")

def generate_summary(df):
    outlier_count = df['is_outlier'].sum()
    total_rows = len(df)
    summary = f"""
📊 Summary Report:
--------------------
Total Records       : {total_rows}
Outliers Detected   : {outlier_count}
Outlier Percentage  : {round((outlier_count / total_rows) * 100, 2)}%

Top 3 Outliers:
{df[df['is_outlier']].head(3)[['store_id', 'date', 'sales', 'llm_reason']].to_string(index=False)}
"""
    print(summary)

from data_loader import load_sales_data
from outlier_detector import detect_outliers
from llm_agent import explain_outliers
from report_generator import save_report, generate_summary

def run_pipeline():
    df = load_sales_data()
    df = detect_outliers(df)
    df = explain_outliers(df)
    save_report(df)
    generate_summary(df)

if __name__ == "__main__":
    run_pipeline()

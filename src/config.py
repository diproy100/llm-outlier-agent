# Global constants and paths

DATA_PATH = "data/store_sales_with_context.csv"
OUTPUT_PATH = "data/outliers_with_explanations.csv"

# Features used for model
FEATURES = ["sales", "inventory", "price"]


CONTEXT_COLUMNS = ["holiday", "promotion", "weather"]

# Outlier detection threshold
CONTAMINATION = 0.05

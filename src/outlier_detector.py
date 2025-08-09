from sklearn.ensemble import IsolationForest
from config import FEATURES, CONTAMINATION

def detect_outliers(df):
    model = IsolationForest(contamination=CONTAMINATION, random_state=42)
    df['outlier_score'] = model.fit_predict(df[FEATURES])
    df['is_outlier'] = df['outlier_score'] == -1
    return df

"""
Student Grade Prediction 
- Clean data exploration output
- Modular feature engineering
- Clear model implementation
"""

# ====================
# 1. INITIAL SETUP
# ====================
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load datasets
logs = pd.read_csv(r'C:\Users\yamar\OneDrive\Desktop\Hari Assignment\4070 dataset\logs.csv')
grades = pd.read_csv(r'C:\Users\yamar\OneDrive\Desktop\Hari Assignment\4070 dataset\scores.csv')

# ====================
# 2. DATA EXPLORATION
# ====================
def explore_data(logs_df, grades_df):
    """Analyze dataset characteristics and quality"""
    print("\n[DATA SHAPES]")
    print(f"Logs: {logs_df.shape} | Grades: {grades_df.shape}")
    
    print("\n[GRADE DISTRIBUTION]")
    print(grades_df['Grade'].value_counts(normalize=True).sort_index())
    
    print("\n[DATA QUALITY]")
    print("Missing Values:")
    print(f"Logs: {logs_df.isnull().sum().to_dict()}")
    print(f"Grades: {grades_df.isnull().sum().to_dict()}")

explore_data(logs, grades)

# ====================
# 3. DATA CLEANING
# ====================
def clean_ids(df, id_column='StudentId'):
    """Standardize student identifiers"""
    return (
        df
        .assign(**{id_column: lambda x: (
            x[id_column]
            .astype(str).str.strip()
            .str.replace(r'[^a-zA-Z0-9]', '', regex=True)
            .str.lower()
        )})
    )

logs = clean_ids(logs)
grades = clean_ids(grades)

# Convert datetime with validation
logs['Time'] = pd.to_datetime(
    logs['Time'], 
    format='%d/%m/%y, %H:%M',
    errors='coerce'
)

# ======================
# 4. FEATURE ENGINEERING
# ======================
def create_features(logs_df):
    """Generate predictive features from raw logs"""
    # Temporal features
    time_features = logs_df.assign(
        Week = lambda x: x.Time.dt.isocalendar().week,
        Hour = lambda x: x.Time.dt.hour
    )
    
    # Action type counts
    action_matrix = (
        time_features
        .groupby(['StudentId', 'Type'])
        .size()
        .unstack(fill_value=0)
        .add_prefix('Action_')
    )
    
    # Engagement metrics
    engagement_stats = (
        time_features
        .groupby('StudentId')
        .agg(
            Total_Actions=('Time', 'count'),
            Active_Weeks=('Week', 'nunique'),
            Peak_Hour=('Hour', lambda x: x.mode()[0])
        )
    )
    
    return pd.concat([action_matrix, engagement_stats], axis=1)

features = create_features(logs)

# ====================
# 5. DATA PREPARATION
# ====================
# Merge with grades and split data
model_data = (
    features
    .merge(grades, on='StudentId', how='inner')
    .dropna()
    .pipe(lambda df: (
        df.drop(columns=['StudentId', 'Grade']),
        df['Grade']
    ))
)

X_train, X_test, y_train, y_test = train_test_split(
    *model_data, 
    test_size=0.2, 
    stratify=model_data[1],  # Preserve grade distribution
    random_state=42
)

# ====================
# 6. MODEL PIPELINE
# ====================
def train_model(X_train, y_train):
    """Configure and train Random Forest classifier"""
    return RandomForestClassifier(
        n_estimators=150,
        max_depth=5,
        class_weight='balanced',
        random_state=42
    ).fit(X_train, y_train)

def evaluate_model(model, X_test, y_test):
    """Generate performance report"""
    predictions = model.predict(X_test)
    print("\n[MODEL PERFORMANCE]")
    print(classification_report(y_test, predictions))

# Execute pipeline
grade_model = train_model(X_train, y_train)
evaluate_model(grade_model, X_test, y_test)
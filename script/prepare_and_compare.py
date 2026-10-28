"""
Remote Work & Employee Wellbeing: data preparation and group comparisons.

Reads the original file from data/ (left unchanged), writes
data/cleaned_remote_work_wellbeing.csv for Power BI, and prints the
group comparisons and chi-square tests quoted in the README.

Run:  python script/prepare_and_compare.py
Needs: pandas, scipy
"""
from pathlib import Path
import pandas as pd
from scipy.stats import chi2_contingency

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "Impact_of_Remote_Work_on_Mental_Health_raw.csv"
CLEAN = ROOT / "data" / "cleaned_remote_work_wellbeing.csv"

# ---------- 1. Load and check ----------
df = pd.read_csv(RAW)
print("Rows, columns:", df.shape)
print("Duplicate rows:", df.duplicated().sum(), "| duplicate Employee_IDs:", df.Employee_ID.duplicated().sum())
print("Missing values:", df.isna().sum()[df.isna().sum() > 0].to_dict())

# ---------- 2. Clean ----------
# Blank values in these two fields are kept and labelled, not dropped.
df["Mental_Health_Condition"] = df["Mental_Health_Condition"].fillna("Not reported")
df["Physical_Activity"] = df["Physical_Activity"].fillna("Not reported")

# Ordinal satisfaction score for averages (plotting and ranking only)
df["Satisfaction_Score"] = df["Satisfaction_with_Remote_Work"].map(
    {"Unsatisfied": 1, "Neutral": 2, "Satisfied": 3})

# Derived bands for the dashboard
df["Age_Group"] = pd.cut(df.Age, [21, 29, 39, 49, 60], labels=["22-29", "30-39", "40-49", "50-60"]).astype(str)
df["Hours_Band"] = pd.cut(df.Hours_Worked_Per_Week, [19, 39, 49, 60], labels=["20-39", "40-49", "50-60"]).astype(str)
df["Experience_Band"] = pd.cut(df.Years_of_Experience, [0, 5, 10, 20, 35],
                              labels=["1-5", "6-10", "11-20", "21-35"]).astype(str)

assert df.Satisfaction_Score.notna().all()
assert not (df.Age_Group == "nan").any() and not (df.Hours_Band == "nan").any()
assert not (df.Experience_Band == "nan").any()
df.to_csv(CLEAN, index=False)
print("\nCleaned file written:", CLEAN.name, df.shape)

# ---------- 3. Descriptive comparisons ----------
def pct(a, b):
    return (pd.crosstab(df[a], df[b], normalize="index") * 100).round(1)

print("\nHeadline shares (%):")
for col in ["Work_Location", "Satisfaction_with_Remote_Work", "Stress_Level",
            "Productivity_Change", "Sleep_Quality", "Access_to_Mental_Health_Resources"]:
    print(f"  {col}:", df[col].value_counts(normalize=True).mul(100).round(1).to_dict())

print("\nWork location x satisfaction (%):\n", pct("Work_Location", "Satisfaction_with_Remote_Work").to_string())
print("\nWork location x stress (%):\n", pct("Work_Location", "Stress_Level").to_string())
print("\nWork location x productivity change (%):\n", pct("Work_Location", "Productivity_Change").to_string())
print("\nMean by work location:\n",
      df.groupby("Work_Location")[["Work_Life_Balance_Rating", "Social_Isolation_Rating",
                                   "Hours_Worked_Per_Week", "Satisfaction_Score"]].mean().round(2).to_string())
print("\nMean work-life balance by stress level:",
      df.groupby("Stress_Level").Work_Life_Balance_Rating.mean().round(2).to_dict())
print("\nCorrelation, hours worked vs work-life balance:",
      round(df.Hours_Worked_Per_Week.corr(df.Work_Life_Balance_Rating), 3))
print("\nSatisfied share (%) by company support score:",
      (df.assign(s=df.Satisfaction_with_Remote_Work.eq("Satisfied")).groupby("Company_Support_for_Remote_Work").s.mean() * 100).round(1).to_dict())

# ---------- 4. Chi-square tests of independence (exact tests run) ----------
print("\nChi-square tests of independence:")
tests = [("Work_Location", "Stress_Level"),
         ("Work_Location", "Satisfaction_with_Remote_Work"),
         ("Work_Location", "Productivity_Change"),
         ("Stress_Level", "Satisfaction_with_Remote_Work"),
         ("Access_to_Mental_Health_Resources", "Mental_Health_Condition")]
for a, b in tests:
    chi2, p, dof, _ = chi2_contingency(pd.crosstab(df[a], df[b]))
    print(f"  {a} x {b}: chi2={chi2:.2f}, dof={dof}, p={p:.4f}")

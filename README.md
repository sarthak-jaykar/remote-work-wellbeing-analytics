# Remote Work & Employee Wellbeing Analytics

### Work Location, Satisfaction, Stress and Work-Life Balance Dashboard

![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?logo=scipy&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0)
![Domain](https://img.shields.io/badge/Domain-HRM-success)
![Data Model](https://img.shields.io/badge/Data%20Model-Single%20Table-blue)

[![Dashboard Preview](screenshots/01_remote_work_overview.png)](screenshots/01_remote_work_overview.png)

*Select the image to view it at full size.*

---

## Project Overview

Organisations offering remote and hybrid work need to know whether work location is linked to satisfaction, stress, productivity, and work-life balance, and how large any differences are compared with normal variation within each group.

This project analyses 5,000 employee records to describe those patterns, test them with chi-square tests of independence, and present the results in a two-page Power BI dashboard. The aim is to show what the data supports, and what it does not.

The results can inform whether work location belongs in wellbeing and engagement planning, and which measures are worth collecting properly with a dedicated survey.

### Data Source

**Data Source:** Secondary data obtained from publicly available online sources for educational and analytical practice. The dataset was used for data preparation, analysis, dashboard development, and business insights.

---

## Key Metrics

| Employees | Remote Share | Satisfied with Remote Work | Average Hours per Week | Reporting a Mental-Health Condition |
| --- | --- | --- | --- | --- |
| **5,000** | **34.3%** (1,714) | **33.5%** | **39.6** | **76.1%** |

---

## Key Findings

All findings are descriptive. Each test is a chi-square test of independence at the 0.05 level. Five tests were run, so the threshold for significance after a Bonferroni correction is 0.01.

1. **Satisfaction differs by work location, but the difference is modest.** Satisfied share is 30.3% for remote, 34.2% for hybrid and 36.2% for onsite workers (p = 0.006). This still falls below the Bonferroni threshold.
2. **No significant association was detected between work location and stress (p = 0.75) or productivity change (p = 0.71).**
3. **No significant association was detected between stress level and satisfaction (p = 0.29).**
4. **No significant association was detected between access to mental-health resources and the recorded condition field (p = 0.37).**
5. **Hours worked and work-life balance are effectively unrelated** (correlation 0.001). Average hours vary only from 39.5 to 39.8 across work locations.
6. **Work-life balance barely changes across stress levels:** 3.03 (high), 3.00 (low), 2.92 (medium) on a 1 to 5 scale. No test was run on this comparison.
7. **Company support shows no consistent pattern.** Satisfied share ranges from 31.9% (support score 1) to 36.0% (score 5), without a steady trend. No test was run.

**What these findings do not show:** They do not show that remote work causes lower satisfaction, higher stress, or any other outcome. The associations are small, the data is cross-sectional and self-reported, and most categories are split almost evenly, so the dataset should be treated as illustrative.

---

## Business Problem and Objectives

Work location is a common hybrid-work question, but decisions about it need to rest on how large any differences are and whether they stand out from ordinary variation.

The project aims to:
1. Describe the workforce and its work arrangements.
2. Compare satisfaction, stress, productivity and sleep across work locations and other groups.
3. Test whether observed associations are larger than chance.
4. Present results in a dashboard that states clearly what the data does and does not show.

---

## Tools and Methodology

- **Python (pandas):** checked for missing values and duplicate rows, labelled blank values as "Not reported" rather than dropping them, added an ordinal satisfaction score and age, hours and experience bands.
- **SciPy:** five chi-square tests of independence.
- **Seaborn and Matplotlib:** exploratory analysis in a Jupyter notebook.
- **Power BI:** one data table, 11 DAX measures, two report pages with slicers, 100% stacked charts, a matrix and a column chart.

**Data notes**
- Mental_Health_Condition: 1,196 blank (24%), labelled "Not reported."
- Physical_Activity: 1,629 blank (33%), labelled "Not reported."
- Most categories sit near one third of employees each, which is unusual for survey data.

**Method notes**
- Chi-square tests cover only the five pairs listed above. Other comparisons are descriptive.
- Mental_Health_Condition is a recorded category, not a diagnosis.
- Productivity_Change is a three-level category, not a measured productivity value.

---

## Repository Structure

```text
remote-work-wellbeing-analytics/
├── README.md
├── data/
│   ├── Impact_of_Remote_Work_on_Mental_Health_raw.csv
│   └── cleaned_remote_work_wellbeing.csv
├── dashboard/
│   └── WFH-workforce-analytics.pbix
├── documentation/
│   └── measures.dax
├── script/
│   ├── prepare_and_compare.py
│   ├── remote-work-mental-health-eda.ipynb
│   └── theme.json
└── screenshots/
    ├── 01_remote_work_overview.png
    └── 02_wellbeing_worklife.png
```

---

## Dashboard

Two report pages, each with slicers and descriptive text boxes.

1. **[Remote Work & Workforce Overview](screenshots/01_remote_work_overview.png):** total employees, remote share, satisfied share and average hours; employees by work location; satisfaction and productivity change by work location; employees by industry. Slicers: age group, gender, job role.
2. **[Employee Wellbeing & Work-Life Balance](screenshots/02_wellbeing_worklife.png):** work-life balance by stress level; satisfied share by company support score; employees by sleep quality and stress level; recorded mental-health conditions. Slicers: location, industry, region.

Measures are in [`documentation/measures.dax`](documentation/measures.dax).

---

## How to Reproduce

**Data preparation and tests**

```bash
pip install pandas scipy
python script/prepare_and_compare.py
```

The script reads the raw file, writes `data/cleaned_remote_work_wellbeing.csv`, and prints the group comparisons and chi-square results.

**Notebook:** open `script/remote-work-mental-health-eda.ipynb` in Jupyter. The notebook reads the raw file from `data/`.

**Dashboard:** open `dashboard/WFH-workforce-analytics.pbix` in Power BI Desktop. If a file error appears, go to **Home → Transform data → Data source settings** and point the source to `data/cleaned_remote_work_wellbeing.csv`.

---

## Limitations

- **Secondary data with near-uniform categories.** Most categories sit at about one third each. Treat the findings as illustrative of the method.
- **Cross-sectional and self-reported.** There is no time dimension, so change over time cannot be assessed.
- **No causal design.** Work location was not randomly assigned. The associations are not evidence that remote work causes any outcome.
- **Non-significant does not mean no effect.** Tests not reaching significance mean no association was detected in this sample.
- **Small effects.** The one significant result has a small effect size.
- **Recorded, not diagnosed.** Mental_Health_Condition is a recorded category and has not been verified.
- **"Not reported" is included in the tests**, so the access-to-resources test runs across four categories of condition.

---

## Disclaimer

This is a portfolio project using secondary data. Results describe that dataset only. They are not clinical assessments, do not identify causes, and should not be read as evidence about any real organisation.

---

**Author:** [Sarthak Jaykar](https://www.linkedin.com/in/sarthak-jaykar/)

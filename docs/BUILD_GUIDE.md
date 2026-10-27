# Remote Work \& Wellbeing Dashboard: Build Guide

**Status:** Prepared, NOT yet built. There is no .pbix file for this project yet. Build it in Power BI Desktop with these steps, then check section 6.

## 1\. Data

* Source file: `data/cleaned\\\_remote\\\_work\\\_wellbeing.csv` (5,000 rows, 24 columns).
* Load: Home > Get data > Text/CSV, choose the file, then **Transform data**.
* Check data types: Age, Hours\_Worked\_Per\_Week, Number\_of\_Virtual\_Meetings, Years\_of\_Experience, Work\_Life\_Balance\_Rating, Social\_Isolation\_Rating, Company\_Support\_for\_Remote\_Work, Satisfaction\_Score as **Whole number**.
* Rename the table to `remote\\\_work\\\_cleaned` (this name is used in the DAX).
* Close \& Apply.

## 2\. Measures

Home > New measure, one per block in `dax/measures.dax`.

## 3\. Page structure

|#|Page|Business question|
|-|-|-|
|1|**Remote Work \& Workforce Overview**|How is the workforce split by work location, and how do satisfaction and productivity vary across locations?|
|2|**Employee Wellbeing \& Work-Life Balance**|How do stress, sleep, work-life balance and support relate across employees?|

### Text boxes (both pages)

* Page title: bold, 20 pt, navy `#1F2A44`, top-left.
* Subtitle: regular, 11 pt, grey `#5A6270`.
* Disclaimer (small, bottom of each page): `Self-reported and dataset-provided indicators. Observed patterns in a secondary-source dataset. Not a clinical assessment; does not show that remote work causes any outcome.`

## 4\. Page 1: Remote Work \& Workforce Overview

**Page title:** `Remote Work \\\& Workforce Overview`
**Subtitle:** `Work location, satisfaction and productivity across 5,000 employees.`
**Business question:** `How is the workforce split by work location, and how do satisfaction and productivity vary across locations?`

|Visual|Type|Fields|Title (exact text)|
|-|-|-|-|
|Card|Card|\[Total Employees]|Total Employees|
|Card|Card|\[Remote Share %]|Remote Share of Employees|
|Card|Card|\[Satisfied Share %]|Satisfied with Remote Work|
|Card|Card|\[Avg Hours per Week]|Average Hours per Week|
|Donut|Donut|Legend: Work\_Location, Values: Total Employees|Employees by Work Location|
|100% stacked bar|100% stacked bar|Axis: Work\_Location, Legend: Satisfaction\_with\_Remote\_Work, Values: Total Employees|Satisfaction with Remote Work by Work Location|
|100% stacked column|100% stacked column|Axis: Work\_Location, Legend: Productivity\_Change, Values: Total Employees|Productivity Change by Work Location|
|Bar|Bar|Axis: Industry, Values: Total Employees|Employees by Industry|

**Slicers:** Gender, Age\_Group, Job\_Role.

**Sorting:** Work\_Location in the order Remote, Hybrid, Onsite. Satisfaction in the order Unsatisfied, Neutral, Satisfied. Productivity in the order Decrease, No Change, Increase.

**Colours:** use one colour per satisfaction level (Unsatisfied soft red, Neutral grey, Satisfied green). Use the same three colours on page 2.

## 5\. Page 2: Employee Wellbeing \& Work-Life Balance

**Page title:** `Employee Wellbeing \\\& Work-Life Balance`
**Subtitle:** `Stress, sleep, work-life balance and company support. Patterns are descriptive.`
**Business question:** `How do stress, sleep and work-life balance vary across employees, and how do they relate to company support?`

|Visual|Type|Fields|Title (exact text)|
|-|-|-|-|
|Card|Card|\[Avg Work-Life Balance (1-5)]|Average Work-Life Balance (1 to 5)|
|Card|Card|\[High Stress Share %]|High Stress|
|Card|Card|\[Poor Sleep Share %]|Poor Sleep Quality|
|Card|Card|\[Access to Resources %]|Access to Mental Health Resources|
|Clustered column|Clustered column|Axis: Stress\_Level (order Low, Medium, High), Values: \[Avg Work-Life Balance (1-5)]|Work-Life Balance Rating by Stress Level|
|Column|Column|Axis: Company\_Support\_for\_Remote\_Work (1 to 5), Values: \[Satisfied Share %]|Satisfied Share by Company Support Score (1 to 5)|
|Matrix|Matrix|Rows: Sleep\_Quality, Columns: Stress\_Level, Values: Total Employees|Employees by Sleep Quality and Stress Level|
|Bar|Bar|Axis: Mental\_Health\_Condition, Values: Total Employees|Mental Health Condition Reported (not a diagnosis)|

**Slicers:** Work\_Location, Industry, Region.

**Note on the Mental Health visual:** keep the title and the disclaimer. Do not add interpretations (for example, linking a condition to a work pattern) to the visual.

## 6\. Verification

|Check|Expected|
|-|-|
|Total Employees|5,000|
|Remote Share|34.3% (1,714)|
|Satisfied Share|33.5%|
|High Stress Share|33.7%|
|Poor Sleep Share|33.7%|
|Access to Resources|48.9%|
|Avg Hours per Week|39.61|
|Avg Work-Life Balance|2.98|
|Productivity Increase|31.7%|
|Mental Condition Reported|76.1%|
|Work location x Satisfied (visual)|Remote 30.3%, Hybrid 34.2%, Onsite 36.2%|

If a number differs, check that the table is named `remote\\\_work\\\_cleaned` and that the data types are correct.

## 7\. Save and capture

Save as `remote\\\_work\\\_wellbeing\\\_dashboard.pbix` in `dashboard/`. Capture:

* `screenshots/01\\\_remote\\\_work\\\_overview.png`
* `screenshots/02\\\_wellbeing\\\_worklife.png`

## 8\. Change log (this step)

|Change|Reason|Status|
|-|-|-|
|Cleaned data: blanks in Mental\_Health\_Condition and Physical\_Activity labelled "Not reported"|Keep rows; make blanks explicit|Done (script and file)|
|Added Satisfaction\_Score, Age\_Group, Hours\_Band, Experience\_Band|Needed for averages and bands|Done (script and file)|
|Two-page dashboard specified with titles, disclaimers and measures|Dashboard requested|Specified. Needs building in Desktop.|




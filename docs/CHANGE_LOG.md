# Change Log: Remote Work & Employee Wellbeing Analytics

| # | File | Change | Reason |
|---|---|---|---|
| 1 | notebook | Removed the cell that overwrote `df` with a 5-row hand-typed sample | Plots that followed were drawn from invented data |
| 2 | notebook | Removed the two template cells ("replace with your data") and their heading | Leftover template code duplicating earlier plots |
| 3 | notebook | Changed the Kaggle data path to a relative file path | Path would not work outside Kaggle |
| 4 | notebook | Replaced the 3D satisfaction plot to use an ordered 1 to 3 scale | Plot failed on real data because satisfaction is text |
| 5 | notebook | Regenerated figures for the remaining plot cells on the real data | Figures in the original output were from the sample data |
| 6 | data/raw | Kept the original CSV unchanged | Preserve source |
| 7 | data/cleaned | Blanks labelled "Not reported" (2 columns); added Satisfaction_Score, Age_Group, Hours_Band, Experience_Band | Keep rows; enable averages and bands |
| 8 | scripts | Added `prepare_and_compare.py` for cleaning, comparisons, and five chi-square tests | Every number in the README can be reproduced |
| 9 | dax | Added measures for the dashboard | Dashboard build |
| 10 | docs | Added the build guide for the two-page dashboard | No .pbix file exists yet |
| 11 | README | Written from the project's verified results; claims limited to what was tested | Analytical integrity |

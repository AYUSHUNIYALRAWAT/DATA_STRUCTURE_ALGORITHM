# ABC Company Performance Dashboard

An Excel dashboard for comparing the performance of 10 companies across 10 industries. It brings together revenue, profit margin, employee count, customer satisfaction and annual growth in company and industry views.

## Project overview

The project includes the Excel dashboard, a CSV dataset exported from its company-level source table, metric summary sheets and a dashboard report with charts. It is designed for quick exploratory comparisons and to help identify companies or industries for further review. The workbook does not state a reporting period, so its figures should be treated as a snapshot rather than a time trend.

## Workbook contents

| Sheet | Purpose |
| --- | --- |
| `abc company report` | Main report dashboard with charts |
| `Sheet1` | Company-level source records; use this as the source of truth |
| `revenue` | Revenue by industry |
| `profit vs revenue` | Company revenue and profit margin comparison |
| `profit margin` | Profit margin by country |
| `employee` | Employee count by company |
| `customer statisfaction` | Customer satisfaction by company |
| `annual growth` | Annual growth by industry |
| `Sheet2` | Industry summary of employee count, satisfaction and revenue |

## Dataset

[`company_performance.csv`](company_performance.csv) is a portable CSV export of the 10 company-level records from the workbook’s `Sheet1` source tab. Use it for analysis in spreadsheet, database or programming tools. The workbook remains available for the dashboard and chart views.

## Data fields

The source table has one row per company and includes:

- Company ID, company name, industry and country
- Revenue in USD
- Employee count
- Year founded
- Profit margin (%)
- Customer satisfaction score
- Annual growth (%)

## Snapshot highlights

Based on the 10 records in the supplied workbook:

- **Total listed revenue:** $30.89 million
- **Total listed employees:** 5,975
- **Highest revenue:** AutoMotion Motors ($7.20 million)
- **Highest profit margin:** FinCore Banking (31%)
- **Highest customer satisfaction score:** HealthFirst Pharma (91)
- **Highest annual growth:** AutoMotion Motors (20%)

These are descriptive figures from the workbook and do not indicate a specific period or trend.

## Open the project

The workbook, `excel final dashboard.xlsx`, is included in this repository. Open it in Microsoft Excel or another spreadsheet application that supports Excel charts. Start with `abc company report` for the dashboard and use `Sheet1` to inspect the company-level records behind the summaries.

No scripts or additional software are required to view the workbook.

## Metric and data notes

- Revenue is recorded in USD. No currency conversion policy or source citation is provided in the workbook.
- Profit margin and annual growth are percentages. Do not add these percentages to create a portfolio total. A consolidated profit margin requires company profit and revenue amounts or a documented revenue-weighted calculation.
- Customer satisfaction is an undocumented score. Its scale, survey method and reporting period are not specified, so compare scores cautiously.
- The employee measure is not defined as average, year-end or full-time-equivalent headcount.
- The workbook contains no as-of date, reporting period, update cadence or refresh source.
- The `annual growth` summary omits Energy, although the company-level records list EcoEnergy Power with 13% annual growth.
- Some summary labels use “Sum of” for percentage and satisfaction measures. Adding rates or scores is not a meaningful aggregate; use company-level comparisons or document a suitable aggregation method.

## Suggested improvements

Before using the dashboard for recurring or external reporting, document the reporting period and source for each metric, define the customer satisfaction scale, correct the Energy omission, and review the aggregation rules for percentages and scores.

## License

No license is specified. Add a license if you intend to permit reuse of this project.

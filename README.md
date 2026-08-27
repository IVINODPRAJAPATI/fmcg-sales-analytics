# FMCG Sales Analytics Dashboard

## Overview
Analysis of ~190,000 daily FMCG sales transactions (2022–2024) across product categories, regions, sales channels, and promotions, to uncover demand drivers and build a predictive sales model.

**Dataset:** [FMCG Daily Sales Data (2022–2024)](https://www.kaggle.com/datasets/beatafaron/fmcg-daily-sales-data-to-2022-2024) — synthetic daily-level transactional data simulating FMCG sales, with product hierarchy (SKU → Brand → Segment → Category), sales channels (Retail/Discount/E-commerce), regions, pricing, promotions, and stock/delivery data.

## Data Cleaning
- No missing values found across any of the 14 original columns.
- No duplicate rows found.
- Removed 3 rows with negative values in `stock_available`, `delivered_qty`, or `units_sold` (0.0016% of data), treated as data entry noise.
- Converted `date` to datetime and engineered `month`, `quarter`, and `day_of_week` features.

## Key Findings (Exploratory Analysis)
1. **Yogurt is the dominant category**, accounting for ~1.57M total units sold — roughly double the next-closest category (Milk, ~783K) and over 12x the weakest category (Juice, ~124K).
2. **Promotions nearly double average sales** — average units sold rises from 17.4 (no promotion) to 34.1 (with promotion), a ~96% increase.
3. **Regional performance is nearly uniform** — average units sold ranges only from 19.86 to 19.96 across all three regions (PL-North, PL-South, PL-Central), suggesting demand is not region-driven.
4. **Sales show clear seasonality** — volume rises steadily from January (~222K units) to a peak in July (~395K units), then declines toward year-end.

## Predictive Modeling
Built and compared two models to predict `units_sold` using category, channel, region, pack type, price, promotion, delivery days, and time-based features (month, quarter, day of week).

| Model | RMSE | R² |
|---|---|---|
| Linear Regression | 9.89 | 0.283 |
| Decision Tree (max_depth=6) | 9.33 | 0.362 |

**Decision Tree outperformed Linear Regression** on both metrics, suggesting the relationship between features and sales is non-linear rather than purely additive.

### Feature Importance (Linear Regression coefficients)
`promotion_flag` was by far the strongest driver of predicted sales (+16.6), confirming the EDA finding above with model-level evidence. Category (particularly Yogurt, SnackBar, ReadyMeal vs. baseline Juice) was the next most influential group of features. Channel, region, and pack type had minimal effect (coefficients under 0.12), consistent with the near-uniform regional performance observed in EDA.

## Tools Used
Python, Pandas, NumPy, Scikit-learn (Linear Regression, Decision Tree Regressor), Jupyter Notebook

## Next Steps
- Build an interactive Streamlit/Plotly dashboard to visualize these trends
- Explore K-Means clustering to segment products or regions by sales pattern
- Investigate promotion effect further, controlling for category (to check whether the effect holds within each category, not just overall)

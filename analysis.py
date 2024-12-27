from scipy.stats import chi2_contingency
import pandas as pd

df = pd.read_csv('finish.csv', encoding='utf-8')

def chi_square_analysis(combined_df):
    # Create a contingency table for county and case type
    contingency_table = pd.crosstab(combined_df['oc_county'], combined_df['type'])

    # Perform the Chi-square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Prepare results for reporting
    chi_square_results = {
        "Chi2 Statistic": chi2,
        "P-Value": p,
        "Degrees of Freedom": dof,
        "Expected Frequencies": expected
    }

    # Print the results
    print("Chi-Square Test Results:")
    for key, value in chi_square_results.items():
        print(f"{key}: {value}")

    # Interpret the results
    alpha = 0.05  # Significance level
    if p < alpha:
        print("The relationship between county and case type is statistically significant.")
    else:
        print("The relationship between county and case type is not statistically significant.")

chi_square_analysis(df) 


# 卡方統計量 (Chi2 Statistic): 6303.75
# P 值 (P-Value): 0.0
# 自由度 (Degrees of Freedom): 147

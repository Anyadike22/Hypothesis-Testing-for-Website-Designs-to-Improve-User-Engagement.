# -*- coding: utf-8 -*-
"""Hypothesis Testing .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kJ7O82neai_gdXlLEDMRoX3plqfyy3zT
"""

import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("website_ab_test.csv")

print(df.head())

# dataset summary
summary = {
    'Number of Records': df.shape[0],
    'Number of Columns': df.shape[1],
    'Missing Values': df.isnull().sum(),
    'Numerical Columns Summary': df.describe()
}

summary

# Group by 'Theme' and calculate mean for numeric columns
theme_performance = df.groupby('Theme').mean(numeric_only=True)

# Sort by conversion rate
theme_performance_sorted = theme_performance.sort_values(by='Conversion Rate', ascending=False)

print(theme_performance_sorted)



"""# The Comparison
The comparison between the Light Theme and Dark Theme on average performance metrics reveals the following insights:

## Click Through Rate (CTR):

The Dark Theme has a slightly higher average CTR (0.2645) compared to the Light Theme (0.2471).

##Conversion Rate:
The Light Theme leads with a marginally higher average Conversion Rate (0.2555) compared to the Dark Theme (0.2513).

## Bounce Rate:
The Bounce Rate is slightly higher for the Dark Theme (0.5121) than for the Light Theme (0.4990).

## Scroll Depth:

Users on the Light Theme scroll slightly further on average (50.74%) compared to those on the Dark Theme (49.93%).

## Age:
The average age of users is similar across themes, with the Light Theme at approximately 41.73 years and the Dark Theme at 41.33 years.
Session Duration: The average session duration is slightly longer for users on the Light Theme (930.83 seconds) than for those on the Dark Theme (919.48 seconds).

From these insights, it appears that the Light Theme slightly outperforms the Dark Theme in terms of Conversion Rate, Bounce Rate, Scroll Depth, and Session Duration, while the Dark Theme leads in Click Through Rate. However, the differences are relatively minor across all metrics.
"""



"""## Getting Started with Hypothesis Testing

We’ll use a significance level (alpha) of 0.05 for our hypothesis testing. It means we’ll consider a result statistically significant if the p-value from our test is less than 0.05.

Let’s start with hypothesis testing based on the Conversion Rate between the Light Theme and Dark Theme. Our hypotheses are as follows:

Null Hypothesis (H0​): There is no difference in Conversion Rates between the Light Theme and Dark Theme.
Alternative Hypothesis (Ha​): There is a difference in Conversion Rates between the Light Theme and Dark Theme.
We’ll use a two-sample t-test to compare the means of the two independent samples. Let’s proceed with the test:
"""

# extracting conversion rates for both themes
conversion_rates_light = df[df['Theme'] == 'Light Theme']['Conversion Rate']
conversion_rates_dark = df[df['Theme'] == 'Dark Theme']['Conversion Rate']

# performing a two-sample t-test
t_stat, p_value = ttest_ind(conversion_rates_light, conversion_rates_dark, equal_var=False)

t_stat, p_value



"""# The result
The result  of the two-sample t-test gives a p-value of approximately 0.635. Since this p-value is much greater than our significance level of 0.05, we do not have enough evidence to reject the null hypothesis. Therefore, we conclude that there is no statistically significant difference in Conversion Rates between the Light Theme and Dark Theme based on the data provided.

# Hypothesis testing based on the Click Through Rate (CTR)

Now, let’s conduct hypothesis testing based on the Click Through Rate (CTR) to see if there’s a statistically significant difference between the Light Theme and Dark Theme regarding how often users click through. Our hypotheses remain structured similarly:

Null Hypothesis (H0​): There is no difference in Click Through Rates between the Light Theme and Dark Theme.
Alternative Hypothesis (Ha​): There is a difference in Click Rates between the Light Theme and Dark Theme.
We’ll perform a two-sample t-test on the CTR for both themes. Let’s proceed with the calculation:
"""

# extracting click through rates for both themes
ctr_light = df[df['Theme'] == 'Light Theme']['Click Through Rate']
ctr_dark = df[df['Theme'] == 'Dark Theme']['Click Through Rate']

# performing a two-sample t-test
t_stat_ctr, p_value_ctr = ttest_ind(ctr_light, ctr_dark, equal_var=False)

t_stat_ctr, p_value_ctr

"""# The Result

The two-sample t-test for the Click Through Rate (CTR) between the Light Theme and Dark Theme yields a p-value of approximately 0.048. This p-value is slightly below our significance level of 0.05, indicating that there is a statistically significant difference in Click Through Rates between the Light Theme and Dark Theme, with the Dark Theme likely having a higher CTR given the direction of the test statistic.
"""



"""#Hypothesis Testing based on Bounce rate and Scroll depth


Now, let’s perform Now, let’s perform Hypothesis Testing based on two other metrics: bounce rate and scroll depth, which are important metrics for analyzing the performance of a theme or a design on a website. I’ll first perform these statistical tests and then create a table to show the report of all the tests we have done:, which are important metrics for analyzing the performance of a theme or a design on a website. I’ll first perform these statistical tests and then create a table to show the report of all the tests we have done:
"""

# extracting bounce rates for both themes
bounce_rates_light = df[df['Theme'] == 'Light Theme']['Bounce Rate']
bounce_rates_dark = df[df['Theme'] == 'Dark Theme']['Bounce Rate']

# performing a two-sample t-test for bounce rate
t_stat_bounce, p_value_bounce = ttest_ind(bounce_rates_light, bounce_rates_dark, equal_var=False)

# extracting scroll depths for both themes
scroll_depth_light = df[df['Theme'] == 'Light Theme']['Scroll_Depth']
scroll_depth_dark = df[df['Theme'] == 'Dark Theme']['Scroll_Depth']

# performing a two-sample t-test for scroll depth
t_stat_scroll, p_value_scroll = ttest_ind(scroll_depth_light, scroll_depth_dark, equal_var=False)

# creating a table for comparison
comparison_table = pd.DataFrame({
    'Metric': ['Click Through Rate', 'Conversion Rate', 'Bounce Rate', 'Scroll Depth'],
    'T-Statistic': [t_stat_ctr, t_stat, t_stat_bounce, t_stat_scroll],
    'P-Value': [p_value_ctr, p_value, p_value_bounce, p_value_scroll]
})

comparison_table

"""# Result Insights

## Click Through Rate:

The test reveals a statistically significant difference, with the Dark Theme likely performing better (P-Value = 0.048).

## Conversion Rate:
No statistically significant difference was found (P-Value = 0.635).

## Bounce Rate:
There’s no statistically significant difference in Bounce Rates between the themes (P-Value = 0.230).

## Scroll Depth:

Similarly, no statistically significant difference is observed in Scroll Depths (P-Value = 0.450).
"""



"""# Conclusion

In conclusion , while the two themes perform similarly across most metrics, the Dark Theme has a slight edge in terms of engaging users to click through. For other key performance indicators like Conversion Rate, Bounce Rate, and Scroll Depth, the choice between a Light Theme and a Dark Theme does not significantly affect user behaviour according to the data provided.
"""
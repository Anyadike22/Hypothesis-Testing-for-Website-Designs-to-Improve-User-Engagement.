# Hypothesis-Testing-for-Website-Designs-to-Improve-User-Engagement.

# Problem Statement 
An online bookstore is looking to optimize its website design to improve user engagement and ultimately increase book purchases. The website currently offers two themes for its users: “Light Theme” and “Dark Theme.” The bookstore’s data science team wants to conduct an A/B testing experiment (hypothesis testing ) to determine which theme leads to better user engagement and higher conversion rates for book purchases.

The data collected by the bookstore contains user interactions and engagement metrics for both the Light Theme and Dark Theme. The dataset includes the following key features:

#### Theme: dark or light
#### Click Through Rate: The proportion of the users who click on links or buttons on the website.
#### Conversion Rate: The percentage of users who signed up on the platform after visiting for the first time.
#### Bounce Rate: The percentage of users who leave the website without further interaction after visiting a single page.
#### Scroll Depth: The depth to which users scroll through the website pages.
#### Age: The age of the user.
#### Location: The location of the user.
#### Session Duration: The duration of the user’s session on the website.
#### Purchases: Whether the user purchased the book (Yes/No).
#### Added_to_Cart: Whether the user added books to the cart (Yes/No).

The task/goal is to identify which theme, Light Theme or Dark Theme, yields better user engagement, purchases and conversion rates. You need to determine if there is a statistically significant difference in the key metrics between the two themes.

# Hypothesis Testing: The Process 
So, Hypothesis Testing is a fundamental process in data science for making data-driven decisions and inferences about populations based on sample data. Below is the process we can follow for the task of Hypothesis Testing:

Hypothesis Testing: Process We Can Follow
So, Hypothesis Testing is a fundamental process in data science for making data-driven decisions and inferences about populations based on sample data. Below is the process we can follow for the task of Hypothesis Testing:

Hypothesis Testing: Process We Can Follow
So, Hypothesis Testing is a fundamental process in data science for making data-driven decisions and inferences about populations based on sample data. Below is the process we can follow for the task of Hypothesis Testing:

#### 1.Gather the necessary data required for the hypothesis test.
#### 2. Define Null (H0) and Alternative Hypothesis (H1 or Ha).
#### 3.Choose the Significance Level (α), which is the probability of rejecting the null hypothesis when it is true.
#### 4.Select the appropriate statistical tests. Examples include t-tests for comparing means, chi-square tests for categorical data, and ANOVA for comparing means across more than two groups.
#### 5.Perform the chosen statistical test on your data.
#### 6.Determine the p-value and interpret the results of your statistical tests.Gather the necessary data required for the hypothesis test.

# Results of Hypothesis Testing for the Click Through Rate (CTR) between the Light Theme and Dark Theme

The two-sample t-test for the Click Through Rate (CTR) between the Light Theme and Dark Theme yields a p-value of approximately 0.048. This p-value is slightly below our significance level of 0.05, indicating that there is a statistically significant difference in Click Through Rates between the Light Theme and Dark Theme, with the Dark Theme likely having a higher CTR given the direction of the test statistic.

# Result of Hypothesis Testing for Bounce rate and Scroll depth

## Bounce Rate:
There’s no statistically significant difference in Bounce Rates between the themes (P-Value = 0.230).

## Scroll Depth:
Similarly, no statistically significant difference is observed in Scroll Depths (P-Value = 0.450).

# Conclusion 
In conclusion , while the two themes perform similarly across most metrics, the Dark Theme has a slight edge in terms of engaging users to click through. For other key performance indicators like Conversion Rate, Bounce Rate, and Scroll Depth, the choice between a Light Theme and a Dark Theme does not significantly affect user behaviour according to the data provided.



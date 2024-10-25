import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
import max_iptm_LIS_validation

#Initiating the font sizes for the subsequent plt plots
plt.rcParams.update({'font.size': 10})

#Reading in the the results for the validation data.
data = pd.read_csv("validation_custom_results.csv")

max_ipTM = max_iptm_LIS_validation.get_max(data, "ipTM")
max_LIS = max_iptm_LIS_validation.get_max(data, "LIS")
max_LIA = max_iptm_LIS_validation.get_max(data, "LIA")


#T-test ipTM
def t_test(data: pd.DataFrame, metric: str):
    negative = data[data["Label"] == "Negative"]
    positive = data[data["Label"] == "Positive"]

    metric_negative = negative[metric]
    metric_positive = positive[metric] 

    t_stat,p_value = stats.ttest_ind(metric_negative, metric_positive)

    return p_value

ipTM_p_value = t_test(max_ipTM, "ipTM")
print('ipTM p-value: {:0.3e}'.format(ipTM_p_value))
LIS_p_value = t_test(max_LIS, "LIS")
print('LIS p-value: {:0.3e}'.format(LIS_p_value))
LIA_p_value = t_test(max_LIA, "LIA")
print('LIA p-value: {:0.3e}'.format(LIA_p_value))

# Initiating a box plot with binary labels on the x axis and ipTM values on the y axis.
sns.swarmplot(x='Label', y='ipTM', data=max_ipTM, color="black")
sns.boxplot(x='Label', y='ipTM', data=max_ipTM)

# Add labels and title
plt.xlabel('Peptidase-inhibitor interaction')
plt.ylabel('ipTM')
plt.title('Distribution of max ipTM from validation data set')

#Display the plot
plt.show()

# Initiating a box plot with binary labels on the x axis and LIS values on the y axis.
sns.swarmplot(x='Label', y='LIS', data=max_LIS, color="black")
sns.boxplot(x='Label', y='LIS', data=max_LIS)

# Add labels and title
plt.xlabel('Peptidase-inhibitor interaction')
plt.ylabel('LIS')
plt.title('Distribution of max LIS from validation data set')

#Display the plot
plt.show()

# Initiating a box plot with binary labels on the x axis and LIA values on the y axis.
sns.swarmplot(x='Label', y='LIA', data=max_LIA, color="black")
sns.boxplot(x='Label', y='LIA', data=max_LIA)

# Add labels and title
plt.xlabel('Peptidase-inhibitor interaction')
plt.ylabel('LIA')
plt.title('Distribution of max LIA from validation data set')

#Display the plot
plt.show()
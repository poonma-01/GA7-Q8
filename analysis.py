# analysis.py
# Email: 23f2003677@ds.study.iitm.ac.in

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Quarterly retention data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "RetentionRate": [69.27, 67.79, 73.97, 72.77],
}
df = pd.DataFrame(data)

# Industry target
industry_target = 85
average = df["RetentionRate"].mean()

print("Verification email: 23f2003677@ds.study.iitm.ac.in")
print("Average retention rate:", round(average, 2))

# Visualization
plt.figure(figsize=(7,5))
sns.lineplot(data=df, x="Quarter", y="RetentionRate", marker="o", label="Company")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (85)")
plt.title("Customer Retention Rate vs Industry Target (2024)")
plt.ylabel("Retention Rate (%)")
plt.ylim(60,90)
plt.legend()
plt.tight_layout()
plt.savefig("retention_trend.png", dpi=150)
plt.show()

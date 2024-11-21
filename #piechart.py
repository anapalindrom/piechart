#piechart
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'study_sessions.csv' 
df = pd.read_csv(file_path)

df["Duration"] = pd.to_timedelta(df["Duration"])

total_duration_per_subject = df.groupby("Subject")["Duration"].sum()
total_duration_per_subject_in_hours = total_duration_per_subject.dt.total_seconds() / 3600

plt.figure(figsize=(8, 8))

colors = plt.cm.Set3.colors 

plt.pie(total_duration_per_subject_in_hours, 
        labels=total_duration_per_subject_in_hours.index, 
        autopct='%1.1f%%',
        startangle=140,  
        colors=colors[:len(total_duration_per_subject_in_hours)],  
        wedgeprops={'edgecolor': 'black'})  

plt.title("Total Study Duration per Subject", fontsize=14)

plt.legend(total_duration_per_subject_in_hours.index, 
           title="Subjects", 
           loc="lower right", 
           fontsize=10)

plt.tight_layout()
plt.show()

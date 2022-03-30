import pandas as pd
import plotly.express as px

df = pd.read_csv("studentData.csv")
attempt_mean = df.groupby(['student_id'], 0, None, False).mean()
print(attempt_mean)
fig = px.scatter(attempt_mean, x="student_id", y="attempt", color="attempt")
fig.show()

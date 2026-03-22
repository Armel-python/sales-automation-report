import pandas as pd
data=pd.read_csv("sales_report.csv")
print(data)
total_sales=data["Sales"].sum()
average_sales=data["Sales"].mean()
max_sales=data["Sales"].max()
print("Total sales:",total_sales)
print("Average sales:",average_sales)
print("Best sales:",max_sales)
summary= pd.DataFrame({"Metric":["Total sales:","Average sales:","Best sales:"],"Values":[total_sales,average_sales,max_sales]})
summary.to_csv("summary_report.csv",index=False)
print("summary report created")
import matplotlib.pyplot as plt 
colors=[]
for sale in data["Sales"]:
    if sale>average_sales:
        colors.append("red")
    else:
        colors.append("blue")
plt.bar(data["Names"], data["Sales"],color=colors)
plt.title("Sales Report")
plt.xlabel("Names")
plt.ylabel("Sales")
plt.savefig("sales_chart.png")
plt.show
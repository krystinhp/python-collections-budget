from .import Expense
import collections
import matplotlib.pyplot as plt

#Read in the spending data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

#Create a list of the Spending Data
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

#Count Categoies with a Counter Collection
spending_counter = collections.Counter(spending_categories)
print(spending_counter)

#Get the Top 5 Collections
top5 = spending_counter.most_common(5)

#Convert the Dictonary to 2 List
categories, count = zip(*top5) 

#Plot the Top5 Most Common Categories
fig, ax = plt.subplots()

#Create the bar chart
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")

#Display the graph
plt.show()
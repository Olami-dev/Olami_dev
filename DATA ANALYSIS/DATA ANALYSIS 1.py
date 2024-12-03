import matplotlib.pyplot as plt

categories = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
variables = [0.17, 0.3, 0.085, 0.19, 0.3]

# Create the horizontal bar chart
plt.barh(categories, variables, color='purple')

# Add title and labels
plt.title('Bar Chart')
plt.xlabel('Proportion of Total')
plt.ylabel('Categories')

# Display the plot
plt.show()

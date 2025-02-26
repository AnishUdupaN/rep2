import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D



class graphs:
    def lineplot(self):
        x = np.linspace(0, 10, 100)  # Generating 100 points between 0 and 10
        y = np.sin(x)  # Sine function
        plt.plot(x, y, label="Sine Wave")  # Plot sine wave
        plt.xlabel("X-axis")  # Label for x-axis
        plt.ylabel("Y-axis")  # Label for y-axis
        plt.title("Line Plot")  # Title of the plot
        plt.legend()  # Display legend
        plt.show()  # Show the plot

    def scatterplot(self):
        x = np.random.rand(50)
        y = np.random.rand(50)
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Scatter Plot")
        plt.show()
    
    def barchart(self):
        categories = ['A', 'B', 'C', 'D']
        values = [10, 20, 15, 25]
        plt.bar(categories, values, color=['blue', 'green', 'red', 'purple'])
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.title("Bar Chart")
        plt.show()
    
    def horizontalbarchart(self):
        categories = ['A', 'B', 'C', 'D']
        values = [10, 20, 15, 25]
        plt.barh(categories, values, color='orange')
        plt.xlabel("Values")
        plt.ylabel("Categories")
        plt.title("Horizontal Bar Chart")
        plt.show()
    
    def histogram(self):
        data = np.random.randn(1000)
        plt.hist(data, bins=30, color='green', edgecolor='black')
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        plt.title("Histogram")
        plt.show()
    
    def sineplot(self):
        x = np.linspace(0, 10, 100)  
        y = np.sin(x)  
        plt.plot(x, y, label="Sine Wave")  
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Line Plot")
        plt.legend()
        plt.show()

    def scatterplot(self):
        x = np.random.rand(50)
        y = np.random.rand(50)
        plt.scatter(x, y, color='red', marker='o')
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.title("Scatter Plot")
        plt.show()
    
    def pairplot(self):
        data_dict = {
            "total_bill": np.random.uniform(5, 50, 100),
            "tip": np.random.uniform(1, 10, 100),
            "sex": np.random.choice(["Male", "Female"], 100),
            "smoker": np.random.choice(["Yes", "No"], 100),
            "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
            "time": np.random.choice(["Lunch", "Dinner"], 100),
            "size": np.random.randint(1, 6, 100)
            }
        data_df = pd.DataFrame(data_dict)
        sys.pairplot(data_df, hue="sex")
        plt.title("Pair Plot")
        plt.show()
    
import matplotlib.pyplot as plt
import os

def create_visualization():
    # Sample data
    cities = ['Delhi', 'Mumbai', 'Chennai']
    temperatures = [30, 32, 28]

    plt.bar(cities, temperatures)
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather Data Visualization')
    
    # Save to a file
    image_path = os.path.join('static', 'weather_chart.png')
    plt.savefig(image_path)
    plt.close()  # Close the figure to free memory
    return image_path

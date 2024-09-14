import numpy as np  
import matplotlib.pyplot as plt

# Simulate a continuous data stream
def data_stream_simulation(n=2000):
    t = np.linspace(0, 10, n)    # Generate 'n' time points between 0 and 10 (creates a time axis for the data).
    
    # pattern to represent regular changes, plus random noise added on top.
    data = np.sin(t) + np.random.normal(0, 0.5, n) 
    
    # Choose random points in the data to be anomalies (about 5% of the data points).
    anomaly_indices = np.random.choice(np.arange(n), size=int(0.05 * n), replace=False)
    
    # Add big spikes to the selected anomaly points (simulating anomalies).
    data[anomaly_indices] += np.random.normal(10, 3, len(anomaly_indices))
    
    return data  # Return the simulated data stream with normal and anomalous points.

# Detect anomalies using the Z-Score method
def detect_anomalies(data, threshold=3):
    anomalies = []  # Initialize an empty list to store indices of detected anomalies.
    
    mean = np.mean(data)   # Calculate the average (mean) of the entire data set.
    print(mean)
    std = np.std(data)     # Calculate the standard deviation (how spread out the data is).
    
    # Loop through each point in the data stream.
    for i, point in enumerate(data):
        z_score = (point - mean) / std  # Calculate the Z-Score for each data point (distance from the mean).
        
        # If the Z-Score is greater than the threshold (3), consider it an anomaly.
        if abs(z_score) > threshold:
            anomalies.append(i)  # Store the index of the anomaly.
    
    return anomalies  # Return the list of anomaly indices.

# Visualize the data stream and anomalies
def visualize_stream(data, anomalies):
    plt.figure(figsize=(10, 6))    # Create a plot figure with a size of 10x6 inches.
    
    plt.plot(data, label='Data Stream')   # Plot the data stream (normal and anomaly points).
    
    # Highlight the anomalies by plotting them as red dots on the graph.
    plt.scatter(anomalies, data[anomalies], color='red', label='Anomalies')
    
    plt.legend()  # Add a legend to explain the data stream and anomalies.
    plt.show()    # Display the graph.

# Main Function to Run Simulation and Anomaly Detection
data = data_stream_simulation()  # Simulate a data stream.
anomalies = detect_anomalies(data)  # Detect anomalies in the data stream.
visualize_stream(data, anomalies)  # Visualize the data and detected anomalies.

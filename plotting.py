import pandas as pd
import matplotlib.pyplot as plt

# Reading the data into a data frame (25%)
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

# Removing bad values (25%)
def clean_data(df, bounding_box):
    df_cleaned = df[
        (df['Longitude'] >= bounding_box['lon_min']) & (df['Longitude'] <= bounding_box['lon_max']) &
        (df['Latitude'] >= bounding_box['lat_min']) & (df['Latitude'] <= bounding_box['lat_max'])
    ]
    
    return df_cleaned

# Fixing other problems (25%)
def fix_problems(df):
    # Add any additional data cleaning or fixing steps here
    # For example, correcting column labels if needed
    df.rename(columns={'Lon': 'Longitude', 'Lat': 'Latitude'}, inplace=True)
    
    return df

# Plotting the data correctly (25%)
def plot_data(df, map_image_path, bounding_box):
    # Create a map of the UK
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Read and display the map image
    map_image = plt.imread(map_image_path)
    ax.imshow(map_image, extent=[bounding_box['lon_min'], bounding_box['lon_max'], bounding_box['lat_min'], bounding_box['lat_max']])
    
    # Plot sensor locations
    ax.scatter(df['Longitude'], df['Latitude'], c='purple', marker='o', label='Sensor Locations')
    
    # Add labels and legend
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('GROW Sensor Locations on Map7')
    ax.legend()
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Define file paths and bounding box
    file_path = 'Growlocations.csv'
    map_path = 'map7.png'  
    bounding_box = {
        'lon_min': -10.592,
        'lon_max': 1.6848,
        'lat_min': 50.681,
        'lat_max': 57.985
    }

    # Read data into a DataFrame
    data_df = read_data(file_path)

    if data_df is not None:
        # Clean the data
        cleaned_df = clean_data(data_df, bounding_box)
        
        # Fix other problems if needed
        fixed_df = fix_problems(cleaned_df)
        

        additional_locations = pd.DataFrame({
            'Latitude': [55.8567, 53.3498, 55.9533, 56.4620, 56.1165, 56.3955, 54.6079, 57.1497, 51.4816, 53.4830],
            'Longitude': [-4.3525, -6.2603, -3.1883, -2.9707, -3.9446, -3.4298, -5.9264, -2.0943, -3.1791, -2.2446 ]
        })


        # Concatenate the additional locations with the existing DataFrame
        extended_df = pd.concat([fixed_df, additional_locations])

        # Plot the data on the map
        plot_data(extended_df, map_path, bounding_box)

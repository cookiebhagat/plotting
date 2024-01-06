import pandas as pd
import matplotlib.pyplot as plt

# Reading the data into a data frame
def read_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading data: {e}")
        return None

# Removing bad values 
def clean_data(df, bounding_box):
    df_cleaned = df[
        (df['Latitude'] >= bounding_box['lat_min']) & (df['Latitude'] <= bounding_box['lat_max']) &
        (df['Longitude'] >= bounding_box['lon_min']) & (df['Longitude'] <= bounding_box['lon_max'])
    ]
    
    return df_cleaned

# Fixing other problems 
def fix_problems(df):
    # Add any additional data cleaning or fixing steps here
    # For example, correcting column labels if needed
    df.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'}, inplace=True)
    
    return df

# Plotting the data correctly
def plot_data(df, map_image_path, bounding_box, flip_latitude=False, flip_longitude=False):
    # Create a map of the UK
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Read and display the map image
    map_image = plt.imread(map_image_path)
    ax.imshow(map_image, extent=[bounding_box['lon_min'], bounding_box['lon_max'], bounding_box['lat_min'], bounding_box['lat_max']], zorder=0, aspect='equal')
    
    # Flip latitude if specified
    if flip_latitude:
        df['Latitude'] = bounding_box['lat_max'] - (df['Latitude'] - bounding_box['lat_min'])
    
    # Flip longitude if specified
    if flip_longitude:
        df['Longitude'] = bounding_box['lon_max'] - (df['Longitude'] - bounding_box['lon_min'])
    
    # Plot sensor locations
    ax.scatter(df['Longitude'], df['Latitude'], zorder=1, alpha= 0.2, c='purple', marker='o', label='Sensor Locations')
    
    # Add labels and legend
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('GROW Sensor Locations on Map7')
    ax.legend()

    # Save the plot as an image
    output_filename = 'output_map7.png'
    plt.savefig(output_filename)
    print(f"Plot saved as {output_filename}")

if __name__ == "__main__":
    # Define file paths and bounding box
    file_path = 'Growlocations.csv'
    map_path = 'map7.png'  
    bounding_box = {
        'lon_min':-10.592 ,
        'lon_max': 1.6848,
        'lat_min': 50.681,
        'lat_max': 57.985
    }

    # Read data into a DataFrame
    data_df = read_data(file_path)

    if data_df is not None:
        # Fix other problems if needed
        fixed_df = fix_problems(data_df)
    
        # Clean the data
        cleaned_df = clean_data(fixed_df, bounding_box)
        
        # Plot the data on the map with flipping if needed
        plot_data(cleaned_df, map_path, bounding_box, flip_latitude=False, flip_longitude=False)

    # Show the plot
    plt.show()
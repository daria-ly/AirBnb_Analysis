# src/plotting.py
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Improve overall aesthetics with Seaborn
sns.set_theme(style="whitegrid")  # Use a clean and modern style
sns.set_palette("pastel")  # Choose a soft and friendly color palette

class CityNotFoundException(Exception):
    """Exception raised when a respective city is not found."""
    def __init__(self, message="Respective city not found"):
        self.message = message
        super().__init__(self.message)

def plot_room_type_distribution(data_frames, location):

    room_type_order = ['Entire home/apt', 'Private room', 'Shared room', 'Hotel room']

    if location == 'Albany':
        data = data_frames[0]
    elif location == 'Athens':
        data = data_frames[1]
    elif location == 'Amsterdam':
        data = data_frames[2]
    elif location == 'Antwerp':
        data = data_frames[3]
    elif location == 'Bangkok':
        data = data_frames[4]
    else:
        raise CityNotFoundException(f"{location} not found")

    plt.figure(figsize=(5, 3))
    ax = sns.countplot(x='room_type', data=data, order=room_type_order)
    plt.title(f'Distribution of Listings by Room Type in {location}', fontsize=14)
    plt.xlabel('Room Type', fontsize=7)
    plt.ylabel('Number of Listings', fontsize=7)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # Removing the coordinate display from the bottom right of the figure
    ax.format_coord = lambda x, y: ''

    # Specify the filename for saving the plot and save it
    filename = f"{location}_room_type_distribution.png"
    plt.savefig(filename, bbox_inches='tight', dpi=300)  # Save with high resolution and tight bounding box
    plt.close()


def plot_license_distribution(data_frames, location):

    if location == 'Albany':
        data = data_frames[0]
    elif location == 'Athens':
        data = data_frames[1]
    elif location == 'Amsterdam':
        data = data_frames[2]
    elif location == 'Antwerp':
        data = data_frames[3]
    elif location == 'Bangkok':
        data = data_frames[4]
    else:
        raise CityNotFoundException(f"{location} not found")

    if 'license' in data.columns and data['license'].isnull().all():
        # Case where the 'license' column exists and all values are NaN
        data['license_category'] = "No license"
    else:
        # Normal case where 'license' data is present or the column is missing
        data['license_category'] = data['license'].apply(lambda x: "No license" if pd.isnull(x) else ("No licensing required" if x == "No licensing required" else "Required"))

    # Convert license_category to a DataFrame if it's a single value
    if isinstance(data['license_category'], str):
        data = pd.DataFrame({"license_category": [data['license_category']] * len(data)})

    # Calculate the counts for each category
    license_counts = data['license_category'].value_counts(normalize=True) * 100

    # Plotting
    plt.figure(figsize=(4,3))
    patches, texts, autotexts = plt.pie(license_counts, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    for text in autotexts:
        text.set_color('black')  # Ensure the percentage texts are easily readable

    plt.title(f'License Distribution in {location}', fontsize=8)

    # Removing the coordinate display is not applicable to pie charts as they don't show cursor coordinates

    # Create the legend manually with color patches
    plt.legend(patches, license_counts.index, loc='lower center', bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=7)

    # Specify the filename for saving the plot and save it
    filename = f"{location}_license_distribution.png"
    plt.savefig(filename, bbox_inches='tight', dpi=300)  # Save with high resolution and tight bounding box
    plt.close()


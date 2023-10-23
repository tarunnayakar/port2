import os

def bulk_rename_images(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)
    
    # Filter out only image files (you can adjust the extensions as needed)
    image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Sort the image files for consistent numbering
    image_files.sort()
    
    # Counter for numbering
    counter = 1
    
    for image_file in image_files:
        old_path = os.path.join(directory, image_file)
        new_path = os.path.join(directory, f"{counter}.jpg")  # Adjust the extension if needed
        
        os.rename(old_path, new_path)
        print(f"Renamed {image_file} to {counter}.jpg")
        
        counter += 1

# Specify the directory where your images are located
directory = "C:/Users/R. TARUN NAYAKA/Pictures/tarun records/cert2"

# Call the function to perform the renaming the given files in numeric order
bulk_rename_images(directory)

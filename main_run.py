import difflib
import pandas as pd

def read_csv_file(file_path):
    """Reads a CSV file and returns a list of dictionaries containing first name, last name, and netID."""
    with open(file_path, 'r') as f:
        data = []
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(',')
                if len(parts) == 3:
                    first_name = parts[0].strip()
                    last_name = parts[1].strip()
                    net_id = parts[2].strip()
                    data.append({
                        "first_name": first_name,
                        "last_name": last_name,
                        "net_id": net_id
                    })
        return data

def read_text_file(file_path):
    """Reads a text file and returns the content as a single string."""
    with open(file_path, 'r') as f:
        return f.read()

def is_present_with_tolerance(attribute, text_content, tolerance=0.8):
    """
    Checks if an attribute is present in the text content with a similarity above the tolerance threshold.

    Args:
        attribute (str): The attribute to search for.
        text_content (str): The content of the second file.
        tolerance (float): Similarity threshold (0-1).

    Returns:
        bool: True if a match is found, False otherwise.
    """
    # Normalize the attribute and text content for comparison
    attribute = attribute.strip().lower()
    text_content = text_content.lower()

    # Split text content into words or segments to check similarity
    for segment in text_content.split():
        similarity = difflib.SequenceMatcher(None, attribute, segment).ratio()
        print(f"Comparing '{attribute}' with '{segment}': Similarity = {similarity}")  # Debugging
        if similarity >= tolerance:
            print(f"Match found: '{attribute}' matches '{segment}' with similarity {similarity}")
            return True

    print(f"No match found for '{attribute}'")
    return False




def build_comparison_table(csv_data, text_content, tolerance=0.8):
    """
    Builds a comparison table indicating the presence of each attribute in the text content
    and identifies rows where all three attributes are missing.

    Args:
        csv_data (list of dict): List of dictionaries from the CSV file.
        text_content (str): The content of the second file.
        tolerance (float): Similarity threshold (0-1).

    Returns:
        pd.DataFrame: Full comparison table and another DataFrame of rows where all three are missing.
    """
    comparison_results = []
    for row in csv_data:
        first_name = row["first_name"]
        last_name = row["last_name"]
        net_id = row["net_id"]

        # Check presence with tolerance
        first_name_present = is_present_with_tolerance(first_name, text_content, tolerance)
        last_name_present = is_present_with_tolerance(last_name, text_content, tolerance)
        net_id_present = is_present_with_tolerance(net_id, text_content, tolerance)

        # Append results
        comparison_results.append({
            "First Name": first_name,
            "Last Name": last_name,
            "NetID": net_id,
            "First Name Present": first_name_present,
            "Last Name Present": last_name_present,
            "NetID Present": net_id_present
        })

    # Create DataFrame from results
    comparison_df = pd.DataFrame(comparison_results)

    # Filter rows where all three columns are False
    
    missing_all_df = comparison_df[
        (comparison_df["First Name Present"] == False) &
        (comparison_df["Last Name Present"] == False) &
        (comparison_df["NetID Present"] == False)
    ][["First Name", "Last Name", "NetID"]]

    # Filter rows where two or more attributes are False
    missing_two_or_more_df = comparison_df[
        (~comparison_df["First Name Present"] & ~comparison_df["Last Name Present"]) |
        (~comparison_df["First Name Present"] & ~comparison_df["NetID Present"]) |
        (~comparison_df["Last Name Present"] & ~comparison_df["NetID Present"])
    ][["First Name", "Last Name", "NetID"]]

    return comparison_df, missing_two_or_more_df

    #return comparison_df, missing_all_df



def main():
    # File paths
    file1 = "data.csv"  # CSV file with first name, last name, and netID
    file2 = "data/nov25.txt"  # Random text file to search

    # Read the files
    csv_data = read_csv_file(file1)
    text_content = read_text_file(file2)

    # Build comparison table
    comparison_table, missing_all_table = build_comparison_table(csv_data, text_content, tolerance=0.8)

    # Output the results
    print("Comparison Table:")
    print(comparison_table)

    print("\nRows with 2/3 attributes missing:")
    print(missing_all_table)

    # Optionally save the tables to CSV files
    comparison_table.to_csv("comparison_results.csv", index=False)
    missing_all_table.to_csv("missing_all_results.csv", index=False)


if __name__ == "__main__":
    main()

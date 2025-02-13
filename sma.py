import pandas as pd

def calculate_sma(input_file, output_file, sma_period=10):
    # Load the CSV file
    df = pd.read_csv(input_file)
    
    # Define the columns for which SMA needs to be calculated
    sma_columns = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    
    # Compute the 10-day SMA for each relevant column
    for col in sma_columns:
        print(col)
        print(df)
        df[f"SMA({col}) {sma_period}D"] = df[col].rolling(window=sma_period).mean()
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Updated file saved as: {output_file}")

# Example usage
input_csv = "RELIANCE.csv"  # Replace with your actual file path
output_csv = "RELIANCE_with_SMA.csv"
calculate_sma(input_csv, output_csv)
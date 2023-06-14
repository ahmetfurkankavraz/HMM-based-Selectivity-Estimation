def calculate_relative_error(hmm_output_file, output_file):
    with open(hmm_output_file, "r") as hmm_file, open(output_file, "r") as output_file:
        hmm_values = hmm_file.readlines()
        output_values = output_file.readlines()
        
        if len(hmm_values) != len(output_values):
            raise ValueError("The number of rows in the files does not match.")
        
        relative_errors = []
        
        for hmm_val, output_val in zip(hmm_values, output_values):
            hmm_val = float(hmm_val.strip())
            output_val = float(output_val.strip())
            
            if output_val == 0:
                continue
            relative_error = abs(hmm_val - output_val) / output_val
            relative_errors.append(relative_error)
        
        return relative_errors

# Example usage
hmm_output_file = "hmm_output.txt"
output_file = "output.txt"
relative_errors = calculate_relative_error(hmm_output_file, output_file)

avg_relative_error = sum(relative_errors) / len(relative_errors)
for error in relative_errors:
    print(error)

print (f"Average relative error: %{avg_relative_error*100}")

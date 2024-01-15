file_path = './diabetesdataset.csv'
data = pd.read_csv(file_path)
sample_before = data['Glucose(before Lunch)']
sample_after = data['Glucose(after Lunch)']

related_data = list(zip(sample_before, sample_after))

sample_size = 8

random_samples = random.sample(related_data, sample_size)

print("Random samples:",random_samples)

# Calculate the differences
differences = [after - before for before, after in random_samples]
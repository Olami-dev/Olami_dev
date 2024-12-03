import pandas as pd
import matplotlib.pyplot as plt

# Sample data
Sampledata = {
    'With Music': [304, 257, 174, 214, 69,
                   317, 387, 47, 157, 0,
                   332, 308, 317, 286, 236,
                   299, 206, 278, 188, 43,
                   0, 0, 0, 0, 0],
    'Without Music': [292, 270, 47, 288, 324,
                      292, 364, 316, 287, 75,
                      282, 149, 274, 319, 213,
                      3, 324, 2, 128, 219,
                      94, 164, 0, 0, 0]
}

df = pd.DataFrame(Sampledata)

# Create Histograms
plt.figure(figsize=(12, 7))

# Histogram for With Music
plt.subplot(1, 2, 1)
plt.hist(df['With Music'], bins=10, color='red', alpha=0.7, edgecolor='black')
plt.title('Histogram of Plant Growth With Music')
plt.xlabel('Growth (mm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

# Histogram for Without Music
plt.subplot(1, 2, 2)
plt.hist(df['Without Music'], bins=10, color='red', alpha=0.7, edgecolor='black')
plt.title('Histogram of Plant Growth Without Music')
plt.xlabel('Growth (mm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)

plt.tight_layout()
plt.show()

# Create Dot Plots
plt.figure(figsize=(10, 5))

# Dot plot for With Music
plt.subplot(1, 2, 1)
plt.scatter(df['With Music'], [0] * len(df['With Music']), color='red', alpha=0.6)
plt.title('Dot Plot of Plant Growth With Music')
plt.yticks([])
plt.xlabel('Growth (mm)')
plt.axhline(0, color='black', lw=0.5)

# Dot plot for No Music
plt.subplot(1, 2, 2)
plt.scatter(df['Without Music'], [0] * len(df['Without Music']), color='orange', alpha=0.6)
plt.title('Dot Plot of Plant Growth Without Music')
plt.yticks([])
plt.xlabel('Growth (mm)')
plt.axhline(0, color='black', lw=0.5)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt

def plot_bar(data, title, xlabel, ylabel):
    if not data:
        print("No data to visualize")
        return

    plt.figure()
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

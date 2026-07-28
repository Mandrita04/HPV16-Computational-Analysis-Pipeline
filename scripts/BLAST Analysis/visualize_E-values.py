#Visualize E-values of top BLAST hits using a scatter plot
import matplotlib.pyplot as plt

hits = ["Hit1", "Hit2", "Hit3", "Hit4"]

evalues = [1e-50, 1e-40, 1e-25, 1e-10]

plt.scatter(hits, evalues)#hits on the x-axis and E-values on the y-axis

plt.yscale("log")#Changes the vertical Y-axis from a normal linear scale to a logarithmic (base-10) scale

plt.xlabel("Hits")
plt.ylabel("E-value (log scale)")
plt.title("BLAST E-values")

plt.show()
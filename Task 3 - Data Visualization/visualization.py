import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("books.csv")

df.info()
print(df.isnull().sum())

rating_counts = df["Rating"].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(rating_counts.index, rating_counts.values)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating (Stars)")
plt.ylabel("Number of Books")
plt.xticks([1, 2, 3, 4, 5])
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("rating_distribution.png", dpi=300)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=20, edgecolor="black")

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("price_distribution.png", dpi=300)
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df["Rating"], df["Price"], alpha=0.6)

plt.title("Book Price vs Rating")
plt.xlabel("Rating (Stars)")
plt.ylabel("Price (£)")
plt.xticks([1, 2, 3, 4, 5])
plt.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("price_vs_rating.png", dpi=300)
plt.show()


fig, axes = plt.subplots(2, 2, figsize=(14, 10))

rating_counts = df["Rating"].value_counts().sort_index()
axes[0, 0].bar(rating_counts.index, rating_counts.values)
axes[0, 0].set_title("Distribution of Book Ratings")
axes[0, 0].set_xlabel("Rating (Stars)")
axes[0, 0].set_ylabel("Number of Books")
axes[0, 0].set_xticks([1, 2, 3, 4, 5])

axes[0, 1].hist(df["Price"], bins=20, edgecolor="black")
axes[0, 1].set_title("Distribution of Book Prices")
axes[0, 1].set_xlabel("Price (£)")
axes[0, 1].set_ylabel("Number of Books")

axes[1, 0].scatter(df["Rating"], df["Price"], alpha=0.6)
axes[1, 0].set_title("Book Price vs Rating")
axes[1, 0].set_xlabel("Rating (Stars)")
axes[1, 0].set_ylabel("Price (£)")
axes[1, 0].set_xticks([1, 2, 3, 4, 5])


axes[1, 1].axis("off")
metrics_text = (
    f"Total Books: {len(df)}\n"
    f"Average Price: £{df['Price'].mean():.2f}\n"
    f"Average Rating: {df['Rating'].mean():.2f} / 5"
)
axes[1, 1].text(
    0.1, 0.6, metrics_text,
    fontsize=16, va="center"
)
axes[1, 1].set_title("Key Metrics")

fig.suptitle("Books Data Visualization Dashboard", fontsize=18)
fig.tight_layout(rect=[0, 0, 1, 0.96])

fig.savefig("books_dashboard.png", dpi=300)
plt.show()


print("\n" + "=" * 40)
print("BOOKS DATA VISUALIZATION - KEY INSIGHTS")
print("=" * 40)

print(f"Total books: {len(df)}")
print(f"Average price: £{df['Price'].mean():.2f}")
print(f"Minimum price: £{df['Price'].min():.2f}")
print(f"Maximum price: £{df['Price'].max():.2f}")
print(f"Average rating: {df['Rating'].mean():.2f} / 5")

print("\nBooks by rating:")
print(df["Rating"].value_counts().sort_index())

print("\nAverage price by rating:")
print(df.groupby("Rating")["Price"].mean().round(2))

correlation = df["Price"].corr(df["Rating"])
print(f"\nPrice-rating correlation: {correlation:.3f}")





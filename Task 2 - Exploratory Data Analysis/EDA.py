import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("books.csv")


print("Rows and columns:", df.shape)
print("\n--- Dataset Information ---")
df.info()

print(df.isnull().sum())
print(df.duplicated().sum())
print(df.describe())

print(df["Rating"].value_counts().sort_index())
print("Average book price:", df["Price"].mean())
print("Minimum book price:", df["Price"].min())
print("Maximum book price:", df["Price"].max())


rating_counts = df["Rating"].value_counts().sort_index()
rating_counts.plot(kind="bar")

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig("rating_distribution.png", dpi=300)
plt.show()

plt.figure()

df["Price"].plot(kind="hist", bins=10)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("price_distribution.png", dpi=300)
plt.show()

print("\n--- Key Insights ---")

print("Total number of books:", len(df))

print(f"Average book price: £{df['Price'].mean():.2f}")

print(f"Lowest book price: £{df['Price'].min():.2f}")

print(f"Highest book price: £{df['Price'].max():.2f}")

print(f"Average book rating: {df['Rating'].mean():.2f} out of 5")

most_common_rating = df["Rating"].mode()[0]

rating_count = df["Rating"].value_counts()[most_common_rating]

print(f"Most common rating: {most_common_rating} stars "f"({rating_count} books)")



print("\n--- Book Availability Analysis ---")

print(df["Availability"].value_counts())


print("\n--- Cheapest and Most Expensive Books ---")

cheapest_book = df.loc[df["Price"].idxmin()]

most_expensive_book = df.loc[df["Price"].idxmax()]

print(
    f"Cheapest book: {cheapest_book['Title']} "
    f"(£{cheapest_book['Price']:.2f})"
)

print(
    f"Most expensive book: {most_expensive_book['Title']} "
    f"(£{most_expensive_book['Price']:.2f})"
)

print("\n--- Average Price by Rating ---")

average_price_by_rating = df.groupby("Rating")["Price"].mean().sort_index()

print(average_price_by_rating.round(2))

print("\n--- Price and Rating Correlation ---")

correlation = df["Price"].corr(df["Rating"])

print(f"Correlation: {correlation:.3f}")


print("Interpretation: Price and rating have almost no linear relationship.")

plt.figure()

plt.scatter(df["Rating"], df["Price"])

plt.title("Book Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.tight_layout()
plt.savefig("price_vs_rating.png", dpi=300)
plt.show()
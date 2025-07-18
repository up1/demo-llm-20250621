import lancedb

def list(query):
    # Connect to the LanceDB database
    db = lancedb.connect("./lancedb/foods")
    table = db.open_table("food_recommendations")
    print(f"Table: {table.name}")

    # List data from the table
    results = table.search(query).select(['vector']).limit(5).to_pandas()
    print("Search Results:")
    print(results)

if __name__ == "__main__":
    query = "piza"
    print(f"Query: {query}")
    list(query)
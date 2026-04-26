from reader import Reader

# def main():
reader = Reader(
    database_path=r"C:\Users\Truc\Documents\VS CODE\delivery-time-prediction\database\amazon_delivery.csv"
)
print(reader.get_index())
print("hello delivery time prediction")
# if __name__ == "main":
#   main()

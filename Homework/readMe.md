# 1. Customers in Germany, UK, USA

    SELECT CustomerName,City FROM Customers
    where Country = "Germany";



# 2. Products category 1, category 2

    SELECT 	ProductName, CategoryID FROM Products
    where CategoryID = 1;

# 3. Customers in London
    SELECT CustomerName, City FROM Customers
    where City = "London";
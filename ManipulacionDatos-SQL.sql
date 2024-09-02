"Prueba 4:"


select order_id from OrdenesVentas where amount_total > 1000;


"Prueba 5:"


SELECT D2.EmployeeID, D2.FirstName, D2.LastName, OD.OrderID, D1.ProductName, D1.CategoryName 
FROM (OrderDetails OD
	INNER JOIN (SELECT C.CategoryID, C.CategoryName, P.ProductName, p.ProductID  
    			FROM Categories C, Products P  
                WHERE C.CategoryName="Beverages") AS D1
    ON OD.ProductID = D1.ProductID)
    INNER JOIN (SELECT E.EmployeeID, E.FirstName, E.LastName, O.OrderID
				FROM Orders O, Employees E  
				WHERE O.EmployeeID=E.EmployeeID) AS D2
    ON OD.OrderID=D2.OrderID
    ORDER BY D2.EmployeeID;
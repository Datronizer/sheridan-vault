In the pptx provided with the Custohave to mer Order snipped table, you have to format your stuff as so:
(double subscript means underlined)

```
Customer Order

0NF     // un-normalized rule (lists only columns)
ORDER(orderNum, orderDate, customerNum, customerName, customerCity, customerStreet, customerProv, customerZip, [prodNo, prodDesc, qty, price])     // square brackets indicate repeating rules.

1NF     // split repeated group into different table (could be intermediary)
ORDER(__orderNum__, orderDate, customerNum, customerName, customerCity, customerStreet, customerProv, customerZip)
Order-Product(__orderNum__, __prodNo__, prodDesc, qty, price)  //include PK from main table.

2NF     // keep splitting main tables
ORDER(__orderNum__, orderDate, customerNum, customerName, customerCity, customerStreet, customerProv, customerZip)
Order-Product(__orderNum__, __prodNo, qty, price)    
Product(__prodNo__, prodDesc)    //split into new table

3NF     // remove transitive dependencies
// if we know customer number, we can probably tell who they are, so we make new table
ORDER(__orderNum__, orderDate, **customerNum**)
Order-Product(__orderNum__, __prodNo, qty, price)    
Product(__prodNo__, prodDesc)    //split into new table
Customer(customerNum, customerName, customerCity, customerStreet, customerProv, customerZip)
```
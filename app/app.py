
from click import option
import mysql.connector 
import streamlit as st


mydb=mysql.connector.connect(          
    host="localhost",
    user="root",
    password="...",
    database="..."
)

mycursor = mydb.cursor()          
print("Connnection Established")






# Create Streamlit app

def main(): 
    st.title(":gray[Database Management Panel] ")
    
    st.logo(image="C:/Users/Utku/Desktop/Gemini_Generated.png", size="large")
    
    table_options=st.sidebar.selectbox("Select an table",("Categories","Product","Inventory","Supplier"))
    operations=st.sidebar.selectbox(f" Select operation for {table_options} ",("Create","Read","Update","Delete"))


    if table_options=="Product":
        Handle_Product(operations)
    elif table_options=="Categories":
        Handle_Categories(operations)
    elif table_options=="Supplier":
        Handle_Supplier(operations)
    elif table_options=="Inventory":
        Handle_Inventory(operations)



# Categories processes

def Handle_Categories(operations):
    st.subheader(f"Category table {operations} operation", divider="gray") 
    
    if operations=="Create":
        Category_name=st.text_input("Category_name")
        Description=st.text_input("Description")
        
        if st.button("Create"): 
            sql= "INSERT INTO Categories(Category_name, Description) values(%s,%s)"
            val= (Category_name,Description)
            mycursor.execute(sql,val)
            mydb.commit() 
            st.success("Record created successfully")

    elif operations=="Read":
        st.text("Categories are listed")
        mycursor.execute("select Categories.Category_name, Categories.Description from categories;")
        result=mycursor.fetchall()
        for row in result:
            st.warning(row) 

    elif operations=="Update":
        mycursor.execute("Select Category_name from Categories;")
        Category=[row[0] for row in mycursor.fetchall()]
        Selected_category=st.selectbox("The category you want to update",Category)

        Category_name=st.text_input("New Category_name")
        Description=st.text_input("New Description")

        if st.button("Update"):
            sql="Update Categories Set Category_name=%s, Description=%s where Category_name=%s"
            val=(Category_name, Description, Selected_category)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully updated")


    elif operations=="Delete":
        mycursor.execute("Select Category_name from Categories;")
        Category=[row[0] for row in mycursor.fetchall()]
        Selected_category=st.selectbox("The category you want to delete",Category)

        if st.button("Delete"):
            sql="Delete from Categories where Category_name=%s"
            val=(Selected_category,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully deleted")


# Product processes

def Handle_Product(operations):
    st.subheader(f"Product table {operations} operation", divider="gray")
    
    if operations=="Create":   
        Product_name=st.text_input("Product_name")

        mycursor.execute("Select Supplier.Company_name, Product.Supplier_id from Product " \
        "JOIN Supplier on Product.Supplier_id=Supplier.Supplier_id;")
        supplier_data=mycursor.fetchall()
        supplier_dict = {name: id for name, id in supplier_data}                
        Selected_Supplier_name=st.selectbox("Company name (Supplier_id)",list(supplier_dict.keys()))     
        Selected_Supplier_id = supplier_dict[Selected_Supplier_name]
        
        mycursor.execute("Select Categories.Category_name, Categories.Category_id from Categories;")
        Category_data=mycursor.fetchall()
        category_dict = {name: id for name, id in Category_data}
        Selected_Category_name=st.selectbox("Category name (Category_id)", list(category_dict.keys()))
        Selected_Category_id=category_dict[Selected_Category_name]

        Unit_price=st.number_input("Unit_price")
        Unit=st.text_input("Unit")
        Discounted=st.radio("Discounted",("Yes","No"))

        if st.button("Create"):
            sql="INSERT INTO Product(Product_name, Supplier_id, Category_id, Unit_price, Unit, Discounted) VALUES(%s,%s,%s,%s,%s,%s)"  
            val=(Product_name,Selected_Supplier_id,Selected_Category_id,Unit_price,Unit,Discounted)
            mycursor.execute(sql,val)     
            mydb.commit()
            st.success("Record created successfully")  


    elif operations=="Read":
        st.text("Product are listed")
        mycursor.execute("Select*from Product")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)


    elif operations=="Update":

        mycursor.execute("Select Product_name from Product;")
        Product=[row[0] for row in mycursor.fetchall()]
        Selected_Product=st.selectbox("Names of Products",Product) 

        Product_name=st.text_input("New Product name")

        mycursor.execute("Select Supplier.Company_name, Supplier.Supplier_id from Supplier;")
        supplier_data=mycursor.fetchall()
        supplier_dict= {name: id for name, id in supplier_data}  
        Selected_Company_name=st.selectbox("Select a Supplier", list(supplier_dict.keys()))
        Selected_Supplier_id=supplier_dict[Selected_Company_name]

        mycursor.execute("Select Categories.Category_name, Categories.Category_id from Categories;")
        category_data=mycursor.fetchall()
        category_dict={name: id for name, id in category_data}
        Selected_Category_name=st.selectbox("Select a Category", list(category_dict.keys()))
        Selected_Category_id=category_dict[Selected_Category_name]

        Unit_price=st.number_input("New Unit_price")
        Unit=st.text_input("New Unit")
        Discounted=st.radio("New Discounted",("Yes","No"))
        
        if st.button("Update"):
            sql="Update Product Set Product_name=%s, Supplier_id=%s, Category_id=%s, Unit_price=%s, Unit=%s, Discounted=%s where Product_name=%s"
            val=(Product_name,Selected_Supplier_id,Selected_Category_id,Unit_price,Unit,Discounted,Selected_Product)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully updated")


    elif operations=="Delete":

        mycursor.execute("Select Product_name from Product;")
        Product=[row[0] for row in mycursor.fetchall()]
        Selected_Product=st.selectbox("The product you want to delete",Product)

        if st.button("Delete"):
            sql="Delete from Product where Product_name=%s"
            val=(Selected_Product,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully deleted")


# Inventory processes

def Handle_Inventory(operations):
    st.subheader(f"Inventory table {operations} operation", divider="gray")

    if operations=="Create":

        mycursor.execute("SELECT Product_id, Product_name FROM Product")
        Product_data = mycursor.fetchall()
        Product_dict = {name: id for id, name in Product_data}
        Selected_Product_name = st.selectbox("Select a Product", list(Product_dict.keys()))  
        Selected_Product_id = Product_dict[Selected_Product_name]
        

        mycursor.execute("SELECT DISTINCT Wherehouse FROM Inventory Where Product_id = %s;", (Selected_Product_id,))
        Wherehouse_list=[row[0] for row in mycursor.fetchall()] 
        if not Wherehouse_list:
            st.warning("There is no designated warehouse for this product.")
        else:
            selected_wherehouse = st.selectbox("Warehouses where this product is located", Wherehouse_list)
        
        
        Quantity=st.text_input("Quantity")

        if st.button("Create"):
            sql = "UPDATE Inventory SET Quantity = Quantity + %s WHERE Wherehouse = %s and Product_id = %s;"
            val=(Quantity,selected_wherehouse,Selected_Product_id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record created successfully")


    elif operations=="Read":
        st.text("Inventory is listed")
        mycursor.execute("SELECT Product.Product_name, Inventory.Wherehouse, Inventory.Quantity \
            from Inventory JOIN Product on Inventory.Product_id = Product.Product_id;")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)
        
    elif operations=="Update":

        mycursor.execute("SELECT Product_id, Product_name FROM Product")
        Product_data = mycursor.fetchall()
        Product_dict = {name: id for id, name in Product_data}
        Selected_Product_name = st.selectbox("The product you want to update", list(Product_dict.keys()))  
        Selected_Product_id = Product_dict[Selected_Product_name]

        mycursor.execute("SELECT Product_id, Product_name FROM Product")
        Inventory_data = mycursor.fetchall()
        Inventory_dict = {name: id for id, name in Inventory_data}
        Selected_Inventory_name = st.selectbox("The product to be updated with the selected product", list(Inventory_dict.keys()))  
        Selected_Inventory_id = Inventory_dict[Selected_Inventory_name]

        Wherehouse=st.selectbox("New Wherehouse",("Gimat depo","Gölbaşı depo","Batıkent depo","Macunkööy depo"))
        Quantity=st.text_input("New Quantiy")

        if st.button("Update"):
            sql="Update Inventory set Product_id=%s,Wherehouse=%s,Quantity=%s where Product_id=%s"
            val=(Selected_Inventory_id,Wherehouse,Quantity,Selected_Product_id)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Update successful")

    elif operations=="Delete":

        mycursor.execute("Select*from Inventory;")
        Inventory=[row[0] for row in mycursor.fetchall()]
        Selected_Inventory = st.selectbox("Products to be removed from the warehouse",Inventory)

        if st.button("Delete"):
            sql="Delete from Inventory where Inventory_id=%s"
            val=(Selected_Inventory,)
            mycursor.execute(sql,val)   
            mydb.commit()
            st.success("Successfully deleted")


# Supplier processes

def Handle_Supplier(operations):
    st.subheader(f"Supplier table {operations} operation", divider="gray")
    
    if operations=="Create":
        Company_name=st.text_input("Company_name")
        Contact_name=st.text_input("Contact_name")
        Email=st.text_input("Email")
        Phone=st.text_input("Phone")
        Address=st.text_input("Address")
        City=st.text_input("City")
        Country=st.text_input("Country")

        if st.button("Create"):
            sql="INSERT INTO Supplier(Company_name, Contact_name, Email, Phone, Address, City, Country) values(%s,%s,%s,%s,%s,%s,%s)"
            val=(Company_name,Contact_name,Email,Phone,Address,City,Country)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record created successfully")

    elif operations=="Read":
        st.text("Suppliers are listed")
        mycursor.execute("Select*from Supplier;")
        result=mycursor.fetchall()
        for row in result:
            st.warning(row)

    elif operations=="Update":
        mycursor.execute("Select Company_name from Supplier")
        Companies = [row[0] for row in mycursor.fetchall()]
        Selected_name=st.selectbox("The company you want to update",Companies)

        Company_name=st.text_input("New Company_name")
        Contact_name=st.text_input("New Contact_name")
        Email=st.text_input("New Email")
        Phone=st.text_input("New Phone")
        Address=st.text_input("New Address")
        City=st.text_input("New City")
        Country=st.text_input("New Country")
        if st.button("Update"):
            sql="Update Supplier set Company_name=%s,Contact_name=%s,Email=%s,Phone=%s,Address=%s,City=%s,Country=%s where Company_name=%s"
            val=(Company_name,Contact_name,Email,Phone,Address,City,Country,Selected_name)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully updated")

    elif operations=="Delete":
        mycursor.execute("Select Company_name from Supplier;")
        Companies=[row[0] for row in mycursor.fetchall()]
        Selected_name=st.selectbox("The company you want to delete",Companies)

        if st.button("Delete"):
            sql="Delete from supplier where Company_name=%s;"
            val=(Selected_name,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Successfully deleted") 




if __name__=="__main__":  
    main()











######### Streamlit running
# stremlit run C:/Users/...

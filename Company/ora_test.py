import cx_Oracle



connection = cx_Oracle.connect(user="admin", password="Krishna12345", dsn="db202112131853_low")

cursor = connection.cursor()

# Create a table

cursor.execute("""begin
                     execute immediate 'drop table pytab';
                     exception when others then if sqlcode <> -942 then raise; end if;
                  end;""")
cursor.execute("create table pytab (id number, data varchar2(20),name  varchar2(20))")

# Insert some rows

rows = [ (1, "First",'Anand' ),
         (2, "Second",'Bala' ),
         (3, "Third" ,'Chari'),
         (4, "Fourth" ,'Thiru'),
         (5, "Fifth" , 'Pope'),
         (6, "Sixth" ,'Hari'),
         (7, "Seventh" ,'Otto') ]

cursor.executemany("insert into pytab(id, data,name) values (:1, :2,:3)", rows)
cursor.execute("insert into REG(NAME) values ('u8ig_hrf')")
connection.commit()  # uncomment to make data persistent

# Now query the rows back

for row in cursor.execute('select * from pytab'):
    print(row,row[0],row[2])
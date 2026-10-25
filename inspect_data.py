import csv
with open("soilph.csv", encoding="utf-8-sig") as f:
    reader= csv.DictReader(f)
    rows = list(reader)
    print("number of rows:", len(rows))
    print("column:", list(rows[0].keys()))
    values=[]
    for row in rows:
        value=float(row["pH (H2O)"])
        values.append (values)
        print("smallest:", min(values))
        print("largest",max(values))
        print("count:", len(values))
    values = []
    for row in rows:
        raw =row["pH (H2O)"].strip()
        if raw =="":
            continue
        values.append(float(raw))
    print("smallest:", min(values))
    print("largest:", max(values))
    print("count:", len(values))
def inspect_column(filename, column) :
    with open(filename, encoding="utf-8-sig") as f:
        rows =list(csv.DictReader(f))
        values =[]
        for row in rows:
            raw = row[column].strip()
            if raw =="":
                continue
            values.append(float(raw))
            return {
                "smallest": min(values),
                "largest": max(values),
                "count": len(values),
            }
        result =inspect_column("soilph.csv","pH (H2O)")
        print(result)
        
ph_result= inspect_column ("soilph.csv", "pH (H2O)")
x_result= inspect_column ("soilph.csv","X_Coord")
print ("ph:", ph_result)
print ("coordinate:", x_result)
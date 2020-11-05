def Write_Patients_DataBase(Pateints_DataBase):
    myfile = open("schoolstu.csv", "a")
    myfile.write(
        "\n" + "," + Pateints_DataBase[0] + "," + Pateints_DataBase[1] + "," + Pateints_DataBase[2]
        + "," + Pateints_DataBase[3] + "," + Pateints_DataBase[4] + "," + Pateints_DataBase[5]
        + "," + Pateints_DataBase[6] + "," + Pateints_DataBase[7] + "," + Pateints_DataBase[8]
        + "," + Pateints_DataBase[9] + "," + Pateints_DataBase[10] + "\n")
    myfile.close()

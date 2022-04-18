from openpyxl import load_workbook
import xlrd
from datetime import date
from datetime import datetime
import time
import serial
import argparse
 
#load excel file
ids_file = "csv/registered_ids.xlsx"
ids_wb = xlrd.open_workbook(ids_file)
ids_sheet = ids_wb.sheet_by_index(0)

parser = argparse.ArgumentParser()
parser.add_argument("--port")
args = parser.parse_args()
print(args.port)
ser = serial.Serial(args.port, '9600')
isIdFound = False
timer = time.time()

try:
    while True:
        if (time.time() - timer) > 5:
            isIdFound = False

        message = ""
        if not isIdFound:
            ser.flushInput()
            ser.flushOutput()
            message = ser.readline().decode("utf-8")
            id_attendee = message.rstrip().lstrip()
            name_attendee = ""
            role_attendee = ""
            ac_number_attendee = ""

            i=0
            while True:
                try:
                    identifier = str(ids_sheet.cell_value(i, 0))
                    name = str(ids_sheet.cell_value(i, 1))
                    role = str(ids_sheet.cell_value(i, 2))
                    ac_number = str(ids_sheet.cell_value(i, 3))
                    if(identifier == id_attendee):
                        name_attendee = name
                        role_attendee = role
                        ac_number_attendee = ac_number
                        isIdFound = True
                        print(name+"  "+role+"  "+ac_number)
                        break
                except IndexError:
                    print('Not registered')
                    break
                i=i+1

            if isIdFound:
                j=0
                while True:
                    attendace_file  = "csv/attendace_report.xlsx"
                    attendace_wb = load_workbook(filename=attendace_file)
                    attendace_sheet = attendace_wb.active
                    attendace_read_wb = xlrd.open_workbook(attendace_file)
                    attendace_read_sheet = attendace_read_wb.sheet_by_index(0)
                    try:
                        Date = str(attendace_read_sheet.cell_value(j, 0))
                    except IndexError:
                        j=j+1
                        attendace_sheet["A"+str(j)] = date.today()
                        attendace_sheet["B"+str(j)] = datetime.now().strftime("%H:%M:%S")
                        attendace_sheet["C"+str(j)] = name_attendee
                        attendace_sheet["D"+str(j)] = role_attendee
                        attendace_sheet["E"+str(j)] = ac_number_attendee
                        try:
                            attendace_wb.save(filename=attendace_file)
                        except IOError:
                            print(attendace_file+" is open, please close file & try again!")
                        
                        timer = time.time()
                        break
                    j=j+1

except KeyboardInterrupt:
    pass
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Attendencedata

from datetime import date


# Create your views here.


def index(request):
    
    attendence = Attendencedata.objects.all()
    
    context = {
        'attendence': attendence,
    }
    return render(request, 'index.html',context)

li_start=[]
def start_date(request,pk):
    # Attendencedata.objects.create(date=date.today())
    start_time = get_object_or_404(Attendencedata, pk=pk)
    start_time.start =date.today()
    li_start.append(start_time)
    start_time.save()
    print(li_start)
    return HttpResponse('in start button',start_time)

li_end=[]
def end_date(request,pk):
    end_time = get_object_or_404(Attendencedata, pk=pk)
    end_time.end =date.today()
    li_end.append(end_time)
    end_time.save()
    print(li_end)

    return HttpResponse('in end button')



# from datetime import datetime, timedelta
# import json


# class AttendanceTracker:
#     li = []

#     def __init__(self):
#         self.attendance_records = []
#         self.attendance_date = None
#         self.data_all = []
#         self.detail_json = []

#     def take_date(self):
#         date_str = input("Enter date (YYYY-MM-DD): ")
#         try:
#             # self.attendance_date = datetime.strptime(date_str, "%Y-%m-%d").date()
#             self.attendance_date = date_str
#         except ValueError:
#             print("Please enter the date in the format YYYY-MM-DD.")

#     def take_attendance(self):
#         while True:
#             in_time_str = input("Enter entry time (HH:MM) or 'no' to stop: ")
#             if in_time_str.lower() == 'no':
#                 break

#             out_time_str = input("Enter exit time (HH:MM): ")
#             try:
#                 entry_time = datetime.strptime(in_time_str, "%H:%M")
#                 exit_time = datetime.strptime(out_time_str, "%H:%M")
#             except ValueError:
#                 print("Please enter time in format HH:MM.")
#                 continue

#             self.attendance_records.append((entry_time, exit_time))

#     def calculate_working_hours(self):
#         total_working_hours = timedelta()
#         total_breaks = timedelta()

#         for i in range(len(self.attendance_records)):
#             entry_time, exit_time = self.attendance_records[i]

#             if i < len(self.attendance_records) - 1:
#                 next_entry_time, _ = self.attendance_records[i + 1]
#                 break_duration = next_entry_time - exit_time
#                 # Ensure positive break time
#                 total_breaks += max(break_duration, timedelta())

#             work_duration = exit_time - entry_time
#             total_working_hours += work_duration

#         return total_working_hours, total_breaks

#     def show_attendance_data(self):
#         # print(f"Attendance Data for {self.attendance_date}:")

#         for entry_time, exit_time in self.attendance_records:
#             # add for json
#             self.data_all.append({
#                 'enter_time': entry_time.strftime('%H:%M'),
#                 'exit_time': exit_time.strftime('%H:%M'),
#             })

#             # print(f"Entry: {entry_time.strftime('%H:%M')} - Exit: {exit_time.strftime('%H:%M')}")

#     def show_summary(self):

#         total_work_hours, total_breaks = self.calculate_working_hours()
#         total_working_and_breaks = total_work_hours + total_breaks

#         #  add in json

#         self.detail_json.append({
#             'Date': str(self.attendance_date),
#             'Total working hours': str(total_work_hours),
#             'Total breaks': str(total_breaks),
#             'Total working + breaks': str(total_working_and_breaks)

#         })

#     # function to add to JSON
#     def write_json(self, new_data, filename='data.json'):
#         with open(filename, 'r+') as file:
#           # First we load existing data into a dict.
#             file_data = json.load(file)
#         # Join new_data with file_data inside emp_details
#             file_data["emp_details"].append(new_data[0])
#         # Sets file's current position at offset.
#             file.seek(0)
#         # convert back to json.
#             json.dump(file_data, file, indent=4)
#             print("added")


# # Example usage
# attendance = AttendanceTracker()
# attendance.take_date()
# attendance.take_attendance()
# attendance.show_attendance_data()
# attendance.show_summary()
# attendance.write_json(attendance.detail_json)
# print(AttendanceTracker.li)

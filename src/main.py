import datetime

def main(num_people, shifts):
  """
  מקבל כמות אנשים ושמירות עם זמן התחלה וזמן סוף, מחלק את האנשים באופן שווה
  ומכניס את השמירות ללוח שנה.

  Args:
    num_people: מספר האנשים.
    shifts: רשימה של מילונים, כאשר כל מילון מכיל את מפתחות "start_time" ו-"end_time"
           המייצגים את זמן התחלה וסוף השמירה בהתאמה.

  Returns:
    לוח שנה עם השמירות המחולקות.
  """

  calendar = {}

  for shift in shifts:
    start_time = datetime.datetime.strptime(shift["start_time"], "%Y-%m-%d %H:%M")
    end_time = datetime.datetime.strptime(shift["end_time"], "%Y-%m-%d %H:%M")
    duration = (end_time - start_time).seconds / 3600
    shift_slot = duration / num_people

    for i in range(num_people):
      slot_start_time = start_time + datetime.timedelta(hours=i * shift_slot)
      slot_end_time = slot_start_time + datetime.timedelta(hours=shift_slot)

      calendar[f"שמירה {i+1}"] = {
        "start_time": slot_start_time.strftime("%Y-%m-%d %H:%M"),
        "end_time": slot_end_time.strftime("%Y-%m-%d %H:%M"),
      }

  return calendar

# דוגמה לשימוש
num_people = 4
shifts = [
  {"start_time": "2024-05-12 10:00", "end_time": "2024-05-14 14:40"},
]

calendar = main(num_people, shifts)
print(calendar)

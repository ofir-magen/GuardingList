import datetime

def main(num_people, shifts):
  calendar = {}

  for shift in shifts:
    start_time = datetime.datetime.strptime(shift["start_time"], "%Y-%m-%d %H:%M")
    end_time = datetime.datetime.strptime(shift["end_time"], "%Y-%m-%d %H:%M")
    duration = (end_time - start_time).seconds / 3600
    shift_slot = duration / len(num_people)
    print("split the shift to: ",shift_slot ," H")

    i=0
    for person in num_people:
      slot_start_time = start_time + datetime.timedelta(hours=i * shift_slot)
      slot_end_time = slot_start_time + datetime.timedelta(hours=shift_slot)
      i=i+1

      calendar[f"Gard {person}"] = {
        "start_time": slot_start_time.strftime("%Y-%m-%d %H:%M"),
        "end_time": slot_end_time.strftime("%Y-%m-%d %H:%M"),
      }

  return calendar


if __name__ == '__main__':
  num_people = ["ofir", "D.P", "golik", "nadev"]
  shifts = [
    {"start_time": "2024-05-12 10:00", "end_time": "2024-05-14 14:40"},
  ]

  calendar = main(num_people, shifts)
  print(calendar)

from . import jalali
from django.utils import timezone


def jalali_converter(time):
    time = timezone.localtime(time)
    jmonth = ["فروردین",
           "اردیبهشت",
           "خرداد",
           "تیر",
           "مرداد",
           "شهریور",
           "مهر",
           "آبان",
           "آذر",
           "دی",
           "بهمن",
           "اسفند"]

    timeToStr = "{},{},{}".format(time.year, time.month, time.day)
    timeToTuple = jalali.Gregorian(timeToStr).persian_tuple()
    timeToList = list(timeToTuple)

    for index, month in enumerate(jmonth):
        if timeToList[1] == index + 1:
            timeToList[1] = month
            break

    output = "{} {} {}, ساعت {}:{}".format(
        timeToList[2],
        timeToList[1],
        timeToList[0],
        time.hour,
        time.minute,
    )
    return output

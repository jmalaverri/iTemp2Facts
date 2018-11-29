import re
import datetime
#import fileinput

# Parse a string date from Yago into a YYYY-MM-DD format.
def parse_date(dt):
    m = re.search('\d{0,4}\-(\d|#){0,2}-(\d|#){0,2}', dt)
    try:
        if m is None:
            #date = "0"
            return "0"

        date = m.group(0)
        if date.find("#") > -1:
            date = date.replace("#", "").strip('-')

        return date
    except ValueError:
        pass


def strtodate(string):
    for fmt in ["%Y-%m-%d", "%Y-%m", "%Y"]:
        try:
            return datetime.datetime.strptime(string, fmt).date()
        except ValueError:
            continue


# def rename_predicate(file_name):
#     print(file_name)
#     with fileinput.FileInput("outputs/"+file_name+".txt", inplace=True, backup='.bak') as file:
#         for line in file:
#             print(line.replace("wasCreatedOnDate", "validOnDate"), end='')


def converttostr(o):
    if isinstance(o, datetime.date):
        return o.__str__()
    elif o is None:
        return '-'
    else:
        return o
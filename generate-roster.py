import numpy as np
import csv
import os
import random
import datetime as dt

from Marshal import Marshal

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
authorisedMarshalsFile = 'authorised-marshals.csv'

ActiveMarshals = np.genfromtxt(
    os.path.join(__location__, authorisedMarshalsFile),
    delimiter=',',
    dtype='U20',
    skip_header=True
)

usedMarshals = []
marshals = []


def get_marshal():
    try:
        marshal = random.choice(marshals)
        if marshal.is_marshal():
            if marshal not in usedMarshals:
                return marshal
            elif marshal in usedMarshals:
                if usedMarshals.count(marshal) < 2:
                    return marshal
                elif usedMarshals.count(marshal) >= 2:
                    return get_marshal()
        elif not marshal.is_marshal():
            return get_marshal()
    except RecursionError:
        return Marshal("", False, False, False)


def get_head_marshal():
    try:
        marshal = random.choice(marshals)
        if marshal.is_headmarshal():
            if marshal not in usedMarshals:
                return marshal
            elif marshal in usedMarshals:
                if usedMarshals.count(marshal) < 2:
                    return marshal
                elif usedMarshals.count(marshal) >= 2:
                    return get_head_marshal()
        elif not marshal.is_headmarshal():
            return get_head_marshal()
    except RecursionError:
        return Marshal("", False, False, False)


def get_grey_leader():
    try:
        marshal = random.choice(marshals)
        if marshal.is_greyleader():
            if marshal not in usedMarshals:
                return marshal
            elif marshal in usedMarshals:
                if usedMarshals.count(marshal) < 2:
                    return marshal
                elif usedMarshals.count(marshal) >= 2:
                    return get_grey_leader()
        elif not marshal.is_greyleader():
            return get_grey_leader()
    except RecursionError:
        return Marshal("", False, False, False)


def next_weekday(d, weekday):
    date = d
    while date.weekday() != weekday:
        date += dt.timedelta(1)
    return date


# Process CSV
for marshalRow in ActiveMarshals:
    name = marshalRow[3]

    HeadMarshal = False
    RegularMarshal = False
    GreyLeader = False

    if marshalRow[0] != "":
        RegularMarshal = (False, True)[bool(len(marshalRow[0]) > 0)]

    if marshalRow[1] != "":
        HeadMarshal = (False, True)[bool(len(marshalRow[1]) > 0)]

    if marshalRow[2] != "":
        GreyLeader = (False, True)[bool(len(marshalRow[2]) > 0)]

    marshals.append(Marshal(name, HeadMarshal, RegularMarshal, GreyLeader))

roster = []

# Logic = 2 months (8 weeks), require GL, HM and 2 M's
#         no one person should have more than two rostered
#         positions in two months
#

todaysDate = next_weekday(dt.datetime.now(), 3)
for idx in range(8):
    weekDate = todaysDate + dt.timedelta(weeks=idx)
    weekDate = weekDate.strftime("%Y-%m-%d")

    week = idx + 1

    if week % 3 == 0:
        eventType = "Arena"
    else:
        eventType = "Chronicles"

    GreyLeader = get_grey_leader()
    HeadMarshal = get_head_marshal()
    MarshalOne = get_marshal()
    MarshalTwo = get_marshal()
    MarshalThree = get_marshal()

    if HeadMarshal == GreyLeader:
        HeadMarshal = get_head_marshal()

    if MarshalOne == HeadMarshal or MarshalOne == GreyLeader:
        MarshalOne = get_marshal()

    if MarshalTwo == HeadMarshal or MarshalTwo == GreyLeader or MarshalTwo == MarshalOne:
        MarshalTwo = get_marshal()

    if MarshalThree == HeadMarshal or MarshalThree == GreyLeader or MarshalThree == MarshalOne or MarshalThree == MarshalTwo:
        MarshalThree = get_marshal()

    thisWeeksRoster = [weekDate, eventType, HeadMarshal.get_name(), MarshalOne.get_name(), MarshalTwo.get_name(), MarshalThree.get_name(), GreyLeader.get_name()]

    usedMarshals.extend((GreyLeader, HeadMarshal, MarshalOne, MarshalTwo, MarshalThree))

    roster.append(thisWeeksRoster)

with open("roster.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(roster)

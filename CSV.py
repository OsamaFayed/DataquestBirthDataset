def read_csv(input_file):
    f = open(input_file, "r",)
    data = f.read()
    string_list = data.split("\n")
    final_list = []
    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(value)
        final_list.append(int_fields)
    return final_list


def month_births(mb_list):
    births_per_month = {}
    for lst in mb_list:
        month = int(lst[1])
        births = int(lst[4])
        if month in births_per_month:
            births_per_month[month] += births
        else:
            births_per_month[month] = births
    return births_per_month


def dow_births(list_of_lists):
    day_of_week = {}
    for day_lst in list_of_lists:
        day_of = int(day_lst[3])
        births = int(day_lst[4])
        if day_of in day_of_week:
            day_of_week[day_of] += births
        else:
            day_of_week[day_of] = births

    return day_of_week


def calc_counts(data, column):
    number_births_yearly = {}
    number_births_monthly = {}
    number_births_day_per_month = {}
    number_births_day_per_week = {}
    for col in data:
        year = int(col[0])
        month = int(col[1])
        day_per_month = int(col[2])
        day_per_week = int(col[3])
        births = int(col[4])
        if column == "year":
            if year in number_births_yearly:
                number_births_yearly[year] += births
            else:
                number_births_yearly[year] = births
        if column == "month":
            if month in number_births_monthly:
                number_births_monthly[month] += births
            else:
                number_births_monthly[month] = births
        if column == "day_per_month":
            if day_per_month in number_births_monthly:
                number_births_monthly[day_per_month] += births
            else:
                number_births_day_per_month[day_per_month] = births
        if column == "day_per_week":
            if day_per_week in number_births_day_per_week:
                number_births_day_per_week[day_per_week] += births
            else:
                number_births_day_per_week[day_per_week] = births

    if column == "year":
        return number_births_yearly
    if column == "month":
        return number_births_monthly
    if column == "day_per_month":
        return number_births_day_per_month
    if column == "day_per_week":
        return number_births_day_per_week


def get_min_max(dic):
    min_years_sorted = min(zip(dic.values(), dic.keys()))
    max_years_sorted = max(zip(dic.values(), dic.keys()))
    return 'min: ', min_years_sorted, 'max: ', max_years_sorted


def get_dif(number_births_yearly, from_value, to_value):
    if from_value in number_births_yearly:
        diff = abs(number_births_yearly[from_value] - number_births_yearly[to_value])
    else:
        return from_value, 'Not Found'
    return diff


cdc_list = read_csv("D:\Projects\Python dataQuest\CSV Repo\-births_1994-2000.csv")
cdc_month_births1 = month_births(cdc_list[1:len(cdc_list)])
cdc_day_births = dow_births(cdc_list[1:len(cdc_list)])
cdc_year_births = calc_counts(cdc_list[1:len(cdc_list)], column='year')
cdc_month_births = calc_counts(cdc_list[1:len(cdc_list)], column="month")
cdc_dom_births = calc_counts(cdc_list[1:len(cdc_list)], column="day_per_month")
cdc_dow_births = calc_counts(cdc_list[1:len(cdc_list)], column="day_per_week")

dif = get_dif(cdc_year_births, 1994, 2002)

minMax = get_min_max(cdc_year_births)
print(minMax)
print(cdc_year_births)
print(cdc_dom_births)
print(cdc_dow_births)
print(cdc_month_births)
print(dif)

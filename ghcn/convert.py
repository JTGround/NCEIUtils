from ghcn.types.records import ElementDailyRecord


def convert_monthly_to_daily_record(monthly_records):
    daily_records_list = []
    for record in monthly_records:
        for daily_values in record.daily_values:
            daily_record = ElementDailyRecord(record.station_id, record.year, record.month, daily_values.date,
                                              record.element,
                                              daily_values.val, daily_values.m_flag, daily_values.q_flag,
                                              daily_values.s_flag)
            daily_records_list.append(daily_record)
    return daily_records_list

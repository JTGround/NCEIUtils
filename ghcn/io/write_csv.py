import os
from ghcn.types.records import DailyValue, ElementMonthlyRecord


def write_dly_csv(daily_records, target_path, append_if_null=True):
    # write flattened to csv
    file_append = open(target_path, 'a')
    try:
        for record in daily_records:
            if record.val is not None or append_if_null is True:
                line = [record.station_id, str(record.year), str(record.month), str(record.date), str(record.element),
                        str(record.val), str(record.m_flag), str(record.q_flag), str(record.s_flag)]
                line_string = ",".join(line) + "\n"
                file_append.write(line_string)
    finally:
        file_append.close()


def convert_dly_to_csv(source_path, target_path, delete_source=False):
    records = []

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return records

    # read from dly
    file = open(source_path, 'r')
    try:
        for line in file:
            station_id = line[0:11]
            year = int(line[11:15])
            month = int(line[15:17])
            element = line[17:21]

            values = []
            for day in range(0, 31):
                base = 21 + (day * 8)
                val = line[base: base + 5].strip()
                if val == -9999:
                    val = None
                m_flag = line[base + 5: base + 6].strip()
                q_flag = line[base + 6: base + 7].strip()
                s_flag = line[base + 7: base + 8].strip()
                daily_value = DailyValue(val, m_flag, q_flag, s_flag)
                values.append(daily_value)
            daily_record = ElementMonthlyRecord(station_id, year, month, element, values)
            records.append(daily_record)
    finally:
        file.close()

    # write flattened to csv
    file_append = open(target_path, 'a')
    try:
        for record in records:
            for element in record.daily_values:
                line = [record.station_id, str(record.year), str(record.month), str(record.element),
                        element.val, element.m_flag, element.q_flag, element.s_flag]
                line_string = ",".join(line) + "\n"
                file_append.write(line_string)
    finally:
        file_append.close()

    # delete the source file, if required
    if delete_source:
        if os.path.exists(source_path):
            try:
                os.remove(source_path)
            except IOError:
                print("Unable to delete file: path=" + source_path)
        else:
            print("File (path=" + source_path + ") does not exist.")

    return records


def convert_countries_csv(source_path, target_path, delete_source=False):

    if not os.path.exists(source_path):
        print('File (path=' + source_path + ') does not exist.')
        return

    try:
        file = open(source_path, 'r')
        file_append = open(target_path, 'a')

        for line in file:
            csv_line1 = line[:2] + ',' + line[3:]
            file_append.write(csv_line1)
    except IOError:
        print("Unable to convert file: path=" + source_path)
    finally:
        file.close()
        file_append.close()

    # delete the source file, if required
    if delete_source:
        if os.path.exists(source_path):
            try:
                os.remove(source_path)
            except IOError:
                print("Unable to delete file: path=" + source_path)
        else:
            print("File (path=" + source_path + ") does not exist.")
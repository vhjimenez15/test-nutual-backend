from datetime import datetime


def helper_create_avm(data):
    if data.get('valuation_date'):
        date_str = data.get('valuation_date')
        date_format = '%d/%m/%Y'
        data['valuation_date'] = datetime.strptime(date_str, date_format)
    return data


def helper_update_avm(data):
    if data.get('valuation_date'):
        date_str = data.get('valuation_date')
        date_format = '%d/%m/%Y'
        data['valuation_date'] = datetime.strptime(date_str, date_format)
    return data

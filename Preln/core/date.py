import logging
import re

def __dow(day, month, year):
    week = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    year = int(year)
    month = int(month)
    day = int(day)

    
    if month % 2 == 0:
        if 1 <= month < 7:
            if month == 2:
                if day < 1 or day > 28: return 0
            else:
                if day < 1 or day > 30: return 0
        if 7 < month <= 12:
            if day < 1 or day > 31: return 0
    else:
        if 1 <= month < 7:
            if day < 1 or day > 31: return 0
        if month == 7:
            if day < 1 or day > 31: return 0
        if 7 < month <= 12:
            if day < 1 or day > 30: return 0
    
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3: year-= 1
    
    return week[round((year + year/4 - year/100 + year/400 + t[month-1] + day) % 7)]


def date(text, type, debug):
    """
    Method for format dates or eliminate it.
    
    :param text: The text to be preprocessed
    :type: str
    
    :param type: Type of date (eliminate or format)
    :type: str
    
    :param debug: Apply debugging
    :type: bool
    """
    
    if debug: logging.basicConfig(level=logging.DEBUG, format='%(asctime)s | %(levelname)8s | %(message)s')
    
    
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    
    date_format = ''
    date_format_ = ''
    day = ''
    month = ''
    
    if re.findall(r'((\d{1,2}/\d{1,2}/\d{4})|(\d{1,2}\-\d{1,2}\-\d{4}))', text):
        date_format = re.search(r'((\d{1,2}/\d{1,2}/\d{4})|(\d{1,2}\-\d{1,2}\-\d{4}))', text)
        date_format = date_format.group(1)
        date_format_ = date_format.replace('-', '/')
        dmy = date_format_.split('/')
        
        try:
            day = __dow(dmy[0], dmy[1], dmy[2])
            if day == 0: raise IndexError
            
            month = months[int(dmy[1]) - 1]
            
            if type == 'complete':
                text = text.replace(date_format, f'{day} {dmy[0]} de {month} de {dmy[2]}')
            if type == 'eliminate':
                text = text.replace(date_format, '')
            if type == 'month':
                text = text.replace(date_format, f'{month}')
            if type == 'month_year':
                text = text.replace(date_format, f'{month} de {dmy[2]}')
                
            if type == 'eliminate':
                logging.debug('-- Date eliminated!')
            else:
                logging.debug('-- Date formated!')
        except IndexError:
            print(f'ERROR: Date out of range: {dmy}')
            
    else:
        logging.debug('-- the text doesnt has any valid date format!')


    return text


if __name__ == '__main__':
    date()
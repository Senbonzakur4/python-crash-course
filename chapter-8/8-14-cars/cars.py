# 8.14 Cars

def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car = make_car('Honda', 'Civic', color='Blue', year=2026, type='Sedan')

print(f"\n{car}\n")
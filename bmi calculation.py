# to identify obesity using bmi
height_ft = input('enter your height (ft): ')
height_in = input('enter your height (in): ')
weight_lb = input('enter your weight in pound: ')
weight_kg = float(weight_lb) / 2.204
height_meter = (int(height_ft) * 12 + int(height_in)) * 2.54 / 100
bmi = weight_kg / height_meter ** 2
print('your bmi is:', bmi)
if bmi >= 35:
    print('you are severe obesity')
elif bmi >= 27 and bmi < 35:
    print('you are medium obesity')
elif bmi >= 24 and bmi < 27:
    print('you are light obesity')
elif bmi >=18.5 and bmi < 24:
    print('you are normal')
else: 
    print('you are too light')
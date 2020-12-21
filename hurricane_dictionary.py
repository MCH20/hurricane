# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


# write your update damages function here:

def update_damages(damage_list):
    updated_damages = []
    for amount in damage_list:
        if amount == 'Damages not recorded':
            updated_damages.append(amount)
        elif 'M' in amount:
            update = amount.replace('M', "")
            update = float(update) * 1000000
            updated_damages.append(update)
        elif 'B' in amount:
            update = amount.replace('B', "")
            update = float(update) * 1000000000
            updated_damages.append(update)
    return updated_damages

updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:

def hurricane_dictionary(names):
    hurricane_values = []
    for n in range(len(names)):
        value = {'Name':names[n] , 'Months':months[n] , 'Year':years[n] , "Max Sustained Winds":max_sustained_winds[n] , 'Areas Affected':areas_affected[n] , 'Damages' :updated_damages[n] , 'Deaths':deaths[n]}
        hurricane_values.append(value)
    zipped_hurricanes = zip(names, hurricane_values)
    name_dictionary = {key:value for key, value in zipped_hurricanes}
    return name_dictionary

hurricane_dictionary = hurricane_dictionary(names)
print(hurricane_dictionary)



# write your construct hurricane by year dictionary function here:

def convert_to_year(hurricane_dictionary):
    year_dictionary = {}
    previous_cane = []
    for hurricane, values in hurricane_dictionary.items():
        current_cane = values
        current_year = values.get('Year')
        if current_year not in year_dictionary:
            year_dictionary[current_year] = [current_cane]
            previous_cane = current_cane
        elif current_year in year_dictionary:
            year_dictionary.update({current_year: [previous_cane, current_cane]})
    print(year_dictionary)

convert_to_year(hurricane_dictionary)



# write your count affected areas function here:

def times_affected(hurricane_dictionary):
    areas_dictionary = {}
    for hurricane, values in hurricane_dictionary.items():
        areas_affected = values.get('Areas Affected')
        for area in areas_affected:
            if area not in areas_dictionary:
                areas_dictionary[area] = 1
            elif area in areas_dictionary:
                count = areas_dictionary.get(area)
                count += 1
                areas_dictionary[area] = count
    return areas_dictionary

areas_dictionary = times_affected(hurricane_dictionary)

times_affected(hurricane_dictionary)

# write your find most affected area function here:

def most_affected(areas_dictionary):
    max_area = ''
    max_count = 0
    for area, count in areas_dictionary.items():
        if count > max_count:
            max_count = count
            max_area = area
    print(max_area + ": " + str(max_count))

most_affected(areas_dictionary)

# write your greatest number of deaths function here:

def most_deaths(hurricane_dictionary):
    max_deaths_hurricane = ''
    max_deaths_count = 0
    for hurricane, value in hurricane_dictionary.items():
        deaths = value.get('Deaths')
        if deaths > max_deaths_count:
            max_deaths_count = deaths
            max_deaths_hurricane = hurricane
    print(max_deaths_hurricane + " caused " + str(max_deaths_count) + " deaths.")

most_deaths(hurricane_dictionary)

# write your catgeorize by mortality function here:

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def categorize_by_mortality(hurricane_dictioanry):
    mortality_dictionary = {1:[] , 2:[] , 3:[] , 4:[] , 5:[]}
    for hurricane, value in hurricane_dictionary.items():
        deaths = value.get('Deaths')
        if deaths > mortality_scale.get(4):
            mortality_dictionary[5].append(value)
        for n in range(4,0,-1):
            if mortality_scale.get(n-1) < deaths <= mortality_scale.get(n):
                mortality_dictionary[n].append(value)
    return mortality_dictionary

mortality_dictionary = categorize_by_mortality(hurricane_dictionary)
print(mortality_dictionary)

# write your greatest damage function here:

def greatest_damage(hurricane_dictionary):
    max_damage_hurricane = ''
    max_damage = 0
    for hurricane, value in hurricane_dictionary.items():
        damage = value.get('Damages')
        if 'Damages not recorded' not in str(damage):
            if damage > max_damage:
                max_damage = damage
                max_damage_hurricane = hurricane
    max_damage_adjusted = max_damage/1000000000
    print(max_damage_hurricane + " caused the most damage: " + str(max_damage_adjusted) + "B dollars")

greatest_damage(hurricane_dictionary)



# write your catgeorize by damage function here:

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def categorize_by_damage(hurricane_dictioanry):
     hurricane_by_damage = {0:[] , 1:[] , 2:[] , 3: [] , 4:[] , 5:[]}
    for hurricane,value in hurricane_dictioanry.items():
        damages = value.get('Damages')
        if 'Damages not recorded' in str(damages):
            hurricane_by_damage[0].append(value)
        elif damages > damage_scale.get(4):
            hurricane_by_damage[5].append(value)
        else:
            for n in range(4,0,-1):
                if damage_scale.get(n-1)< damages <= damage_scale.get(n):
                    hurricane_by_damage[n].append(value)
    return hurricane_by_damage

damage_dictionary = categorize_by_damage(hurricane_dictionary)